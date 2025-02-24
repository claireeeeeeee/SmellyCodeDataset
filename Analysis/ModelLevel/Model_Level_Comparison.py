"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import sys
import os

def compute_metrics(tp, fp, fn):
    """
    Computes Precision, Recall, and F1-score.
    """
    precision = len(tp) / (len(tp) + len(fp)) if (len(tp) + len(fp)) > 0 else 0
    recall = len(tp) / (len(tp) + len(fn)) if (len(tp) + len(fn)) > 0 else 0
    f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    return precision, recall, f1

def compare_models(ground_truth_path, gpt4_path, deepseek_path):
    """
    Compares GPT-4 and DeepSeek code smell detection with ground truth.
    Generates overall model-level performance metrics.
    """

    # Load cleaned CSV files
    df_ground_truth = pd.read_csv(ground_truth_path)
    df_gpt4 = pd.read_csv(gpt4_path)
    df_deepseek = pd.read_csv(deepseek_path)

    # Ensure identifier column exists
    if "Identifier" not in df_ground_truth.columns or "Identifier" not in df_gpt4.columns or "Identifier" not in df_deepseek.columns:
        print("❌ Error: 'Identifier' column missing in one of the CSV files. Ensure you have cleaned the files first.")
        return

    # Identify matches and mismatches
    tp_gpt4 = df_ground_truth[df_ground_truth["Identifier"].isin(df_gpt4["Identifier"])]
    fp_gpt4 = df_gpt4[~df_gpt4["Identifier"].isin(df_ground_truth["Identifier"])]
    fn_gpt4 = df_ground_truth[~df_ground_truth["Identifier"].isin(df_gpt4["Identifier"])]

    tp_deepseek = df_ground_truth[df_ground_truth["Identifier"].isin(df_deepseek["Identifier"])]
    fp_deepseek = df_deepseek[~df_deepseek["Identifier"].isin(df_ground_truth["Identifier"])]
    fn_deepseek = df_ground_truth[~df_ground_truth["Identifier"].isin(df_deepseek["Identifier"])]

    # Compute overall performance metrics
    precision_gpt4, recall_gpt4, f1_gpt4 = compute_metrics(tp_gpt4, fp_gpt4, fn_gpt4)
    precision_deepseek, recall_deepseek, f1_deepseek = compute_metrics(tp_deepseek, fp_deepseek, fn_deepseek)

    # Create results DataFrame
    comparison_results = pd.DataFrame({
        "Model": ["GPT-4", "DeepSeek"],
        "True Positives (TP)": [len(tp_gpt4), len(tp_deepseek)],
        "False Positives (FP)": [len(fp_gpt4), len(fp_deepseek)],
        "False Negatives (FN)": [len(fn_gpt4), len(fn_deepseek)],
        "Precision": [precision_gpt4, precision_deepseek],
        "Recall": [recall_gpt4, recall_deepseek],
        "F1-score": [f1_gpt4, f1_deepseek]
    })

    # Save the comparison report in CSV
    csv_output_path = "Model_Level_Comparison.csv"
    comparison_results.to_csv(csv_output_path, index=False)

    # Print Summary
    print("\n✅ Comparison Completed:")
    print(comparison_results.to_string(index=False))
    print(f"\n📄 Results saved to: {csv_output_path}")

# Check if correct arguments are provided
if len(sys.argv) < 4:
    print("Usage: python compare_models.py <ground_truth.csv> <gpt4_predictions.csv> <deepseek_predictions.csv>")
    sys.exit(1)

# Get file paths from command-line arguments
ground_truth_path = sys.argv[1]
gpt4_path = sys.argv[2]
deepseek_path = sys.argv[3]

# Run comparison
compare_models(ground_truth_path, gpt4_path, deepseek_path)
