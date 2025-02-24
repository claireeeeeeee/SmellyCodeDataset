"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_visualizations(csv_path):
    """
    Reads model comparison results from CSV and generates multiple visualizations.
    """

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Define colors for charts
    colors = ['blue', 'green']

    # 📊 **1. Bar Chart - True Positives, False Positives, False Negatives**
    fig, ax = plt.subplots(figsize=(8, 6))
    df.set_index("Model")[["True Positives (TP)", "False Positives (FP)", "False Negatives (FN)"]].plot(kind="bar", ax=ax, color=['green', 'red', 'orange'])
    plt.title("True Positives, False Positives, False Negatives by Model")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.legend(loc="upper right")
    plt.savefig("Model_Level_TP_FP_FN_BarChart.png")
    print("📊 Saved: Model_Level_TP_FP_FN_BarChart.png")

    # 📊 **2. Bar Chart - Precision, Recall, F1-score**
    fig, ax = plt.subplots(figsize=(8, 6))
    df.set_index("Model")[["Precision", "Recall", "F1-score"]].plot(kind="bar", ax=ax, color=['blue', 'purple', 'black'])
    plt.title("Precision, Recall, and F1-score by Model")
    plt.ylabel("Score")
    plt.xticks(rotation=0)
    plt.ylim(0, 1)
    plt.legend(loc="upper right")
    plt.savefig("Model_Level_Precision_Recall_F1_BarChart.png")
    print("📊 Saved: Model_Level_Precision_Recall_F1_BarChart.png")

    # 📊 **3. Stacked Bar Chart - TP, FP, FN Breakdown**
    fig, ax = plt.subplots(figsize=(8, 6))
    df.set_index("Model")[["True Positives (TP)", "False Positives (FP)", "False Negatives (FN)"]].plot(kind="bar", stacked=True, ax=ax, color=['green', 'red', 'orange'])
    plt.title("Model_Level_Stacked TP, FP, FN by Model")
    plt.ylabel("Count")
    plt.xticks(rotation=0)
    plt.savefig("Model_Level_Stacked_TP_FP_FN.png")
    print("📊 Saved: Model_Level_Stacked_TP_FP_FN.png")

    # 📊 **4. Radar Chart - Overall Model Performance**
    categories = ["Precision", "Recall", "F1-score"]
    values_gpt4 = df[df["Model"] == "GPT-4"][categories].values.flatten().tolist()
    values_deepseek = df[df["Model"] == "DeepSeek"][categories].values.flatten().tolist()

    # Close the radar chart
    values_gpt4 += values_gpt4[:1]
    values_deepseek += values_deepseek[:1]

    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # Repeat first value to close chart

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values_gpt4, color='blue', alpha=0.4, label="GPT-4")
    ax.fill(angles, values_deepseek, color='red', alpha=0.4, label="DeepSeek")
    ax.plot(angles, values_gpt4, color='blue', linewidth=2)
    ax.plot(angles, values_deepseek, color='red', linewidth=2)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    plt.title("Radar Chart - Model Performance")
    plt.legend(loc="upper right")
    plt.savefig("Model_Level_Radar_Chart_Performance.png")
    print("📊 Saved: Model_Level_Radar_Chart_Performance.png")

    print("✅ All visualizations generated successfully!")

# Run the function with the given CSV file
generate_visualizations("Model_Level_Comparison.csv")
