"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_language_visuals(csv_path):
    """
    Reads language-level comparison results from CSV and generates bar charts and radar charts.
    """

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Ensure numeric values and handle missing data
    df["Precision"] = pd.to_numeric(df["Precision"], errors="coerce")
    df["Recall"] = pd.to_numeric(df["Recall"], errors="coerce")
    df["F1-score"] = pd.to_numeric(df["F1-score"], errors="coerce")
    df.fillna(0, inplace=True)  # Replace NaN values with 0

    # 📊 **1. Bar Chart - True Positives, False Positives, False Negatives by Language**
    fig, ax = plt.subplots(figsize=(10, 6))
    df.pivot(index="Language", columns="Model", values="True Positives (TP)").plot(kind="bar", ax=ax, color=['green', 'lightgreen'])
    df.pivot(index="Language", columns="Model", values="False Positives (FP)").plot(kind="bar", ax=ax, color=['red', 'pink'], alpha=0.6)
    df.pivot(index="Language", columns="Model", values="False Negatives (FN)").plot(kind="bar", ax=ax, color=['orange', 'yellow'], alpha=0.6)
    plt.title("True Positives, False Positives, False Negatives by Language")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.legend(["GPT-4 TP", "DeepSeek TP", "GPT-4 FP", "DeepSeek FP", "GPT-4 FN", "DeepSeek FN"], loc="upper right")
    plt.savefig("Model_Language_TP_FP_FN_BarChart.png")
    print("📊 Saved: Model_Language_TP_FP_FN_BarChart.png")

    # 📊 **2. Bar Chart - Precision, Recall, F1-score by Language**
    fig, ax = plt.subplots(figsize=(10, 6))
    df.pivot(index="Language", columns="Model", values="Precision").plot(kind="bar", ax=ax, color=['blue', 'lightblue'])
    df.pivot(index="Language", columns="Model", values="Recall").plot(kind="bar", ax=ax, color=['purple', 'pink'], alpha=0.6)
    df.pivot(index="Language", columns="Model", values="F1-score").plot(kind="bar", ax=ax, color=['black', 'gray'], alpha=0.6)
    plt.title("Precision, Recall, and F1-score by Language")
    plt.ylabel("Score")
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    plt.legend(["GPT-4 Precision", "DeepSeek Precision", "GPT-4 Recall", "DeepSeek Recall", "GPT-4 F1-score", "DeepSeek F1-score"], loc="upper right")
    plt.savefig("Model_Language_Precision_Recall_F1_BarChart.png")
    print("📊 Saved: Model_Language_Precision_Recall_F1_BarChart.png")

    # 📊 **3. Stacked Bar Chart - TP, FP, FN Breakdown by Language**
    fig, ax = plt.subplots(figsize=(10, 6))
    df.set_index(["Language", "Model"])[["True Positives (TP)", "False Positives (FP)", "False Negatives (FN)"]].unstack().plot(kind="bar", stacked=True, ax=ax, color=['green', 'red', 'orange'])
    plt.title("Stacked TP, FP, FN by Language")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.savefig("Model_Language_Stacked_TP_FP_FN.png")
    print("📊 Saved: Model_Language_Stacked_TP_FP_FN.png")

    # 📊 **4. Radar Chart - Performance Metrics by Language**
    languages = df["Language"].unique()

    precision_gpt4 = df[df["Model"] == "GPT-4"]["Precision"].tolist()
    recall_gpt4 = df[df["Model"] == "GPT-4"]["Recall"].tolist()
    f1_gpt4 = df[df["Model"] == "GPT-4"]["F1-score"].tolist()

    precision_deepseek = df[df["Model"] == "DeepSeek"]["Precision"].tolist()
    recall_deepseek = df[df["Model"] == "DeepSeek"]["Recall"].tolist()
    f1_deepseek = df[df["Model"] == "DeepSeek"]["F1-score"].tolist()

    languages = list(languages)

    # Close the radar chart
    precision_gpt4 += precision_gpt4[:1]
    recall_gpt4 += recall_gpt4[:1]
    f1_gpt4 += f1_gpt4[:1]

    precision_deepseek += precision_deepseek[:1]
    recall_deepseek += recall_deepseek[:1]
    f1_deepseek += f1_deepseek[:1]

    angles = np.linspace(0, 2 * np.pi, len(languages), endpoint=False).tolist()
    angles += angles[:1]  # Repeat first value to close chart

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Plot GPT-4
    ax.fill(angles, precision_gpt4, color='blue', alpha=0.2, label="GPT-4 Precision")
    ax.fill(angles, recall_gpt4, color='green', alpha=0.2, label="GPT-4 Recall")
    ax.fill(angles, f1_gpt4, color='black', alpha=0.2, label="GPT-4 F1-score")

    # Plot DeepSeek
    ax.fill(angles, precision_deepseek, color='red', alpha=0.2, label="DeepSeek Precision")
    ax.fill(angles, recall_deepseek, color='purple', alpha=0.2, label="DeepSeek Recall")
    ax.fill(angles, f1_deepseek, color='gray', alpha=0.2, label="DeepSeek F1-score")

    ax.plot(angles, precision_gpt4, color='blue', linewidth=2)
    ax.plot(angles, recall_gpt4, color='green', linewidth=2)
    ax.plot(angles, f1_gpt4, color='black', linewidth=2)

    ax.plot(angles, precision_deepseek, color='red', linewidth=2)
    ax.plot(angles, recall_deepseek, color='purple', linewidth=2)
    ax.plot(angles, f1_deepseek, color='gray', linewidth=2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(languages, fontsize=10, rotation=45)
    plt.title("Radar Chart - Precision, Recall, F1-score by Language")
    plt.legend(loc="upper right")
    plt.savefig("Model_Language_Radar_Chart.png")
    print("📊 Saved: Model_Language_Radar_Chart.png")

    print("✅ All language-level visualizations generated successfully!")

# Run the function with the given CSV file
generate_language_visuals("Model_Language_Level_Comparison.csv")
