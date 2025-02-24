"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def generate_category_language_visuals(csv_path):
    """
    Reads category-language-level comparison results from CSV and generates heatmaps and radar charts.
    """

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Ensure numeric values and handle missing data
    df["Precision"] = pd.to_numeric(df["Precision"], errors="coerce")
    df["Recall"] = pd.to_numeric(df["Recall"], errors="coerce")
    df["F1-score"] = pd.to_numeric(df["F1-score"], errors="coerce")
    df.fillna(0, inplace=True)  # Replace NaN values with 0

    # **Separate Data for Each Model**
    df_gpt4 = df[df["Model"] == "GPT-4"].groupby(["Category", "Language"], as_index=False).mean()
    df_deepseek = df[df["Model"] == "DeepSeek"].groupby(["Category", "Language"], as_index=False).mean()

    # Pivot Data for Heatmaps
    precision_gpt4 = df_gpt4.pivot(index="Category", columns="Language", values="Precision")
    precision_deepseek = df_deepseek.pivot(index="Category", columns="Language", values="Precision")
    precision_diff = precision_gpt4 - precision_deepseek  # Precision Difference

    recall_gpt4 = df_gpt4.pivot(index="Category", columns="Language", values="Recall")
    recall_deepseek = df_deepseek.pivot(index="Category", columns="Language", values="Recall")
    recall_diff = recall_gpt4 - recall_deepseek  # Recall Difference

    f1_gpt4 = df_gpt4.pivot(index="Category", columns="Language", values="F1-score")
    f1_deepseek = df_deepseek.pivot(index="Category", columns="Language", values="F1-score")
    f1_diff = f1_gpt4 - f1_deepseek  # F1-score Difference

    # 📊 **1. Precision Difference Heatmap (GPT-4 - DeepSeek)**
    plt.figure(figsize=(10, 6))
    sns.heatmap(precision_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("Precision Difference (GPT-4 - DeepSeek) by Category & Language")
    plt.xlabel("Language")
    plt.ylabel("Category")
    plt.xticks(rotation=45)
    plt.savefig("Category_Language_Precision_Diff_Heatmap.png")
    print("📊 Saved: Category_Language_Precision_Diff_Heatmap.png")

    # 📊 **2. Recall Difference Heatmap (GPT-4 - DeepSeek)**
    plt.figure(figsize=(10, 6))
    sns.heatmap(recall_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("Recall Difference (GPT-4 - DeepSeek) by Category & Language")
    plt.xlabel("Language")
    plt.ylabel("Category")
    plt.xticks(rotation=45)
    plt.savefig("Category_Language_Recall_Diff_Heatmap.png")
    print("📊 Saved: Category_Language_Recall_Diff_Heatmap.png")

    # 📊 **3. F1-score Difference Heatmap (GPT-4 - DeepSeek)**
    plt.figure(figsize=(10, 6))
    sns.heatmap(f1_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("F1-score Difference (GPT-4 - DeepSeek) by Category & Language")
    plt.xlabel("Language")
    plt.ylabel("Category")
    plt.xticks(rotation=45)
    plt.savefig("Category_Language_F1_Diff_Heatmap.png")
    print("📊 Saved: Category_Language_F1_Diff_Heatmap.png")

    # 📊 **4. Radar Chart - Performance Metrics by Category & Language**
    categories = df["Category"].unique()

    for lang in df["Language"].unique():
        df_lang = df[df["Language"] == lang]
        
        precision_gpt4 = df_lang[df_lang["Model"] == "GPT-4"]["Precision"].tolist()
        recall_gpt4 = df_lang[df_lang["Model"] == "GPT-4"]["Recall"].tolist()
        f1_gpt4 = df_lang[df_lang["Model"] == "GPT-4"]["F1-score"].tolist()

        precision_deepseek = df_lang[df_lang["Model"] == "DeepSeek"]["Precision"].tolist()
        recall_deepseek = df_lang[df_lang["Model"] == "DeepSeek"]["Recall"].tolist()
        f1_deepseek = df_lang[df_lang["Model"] == "DeepSeek"]["F1-score"].tolist()

        categories_list = list(categories)
        
        # Close the radar chart
        precision_gpt4 += precision_gpt4[:1]
        recall_gpt4 += recall_gpt4[:1]
        f1_gpt4 += f1_gpt4[:1]

        precision_deepseek += precision_deepseek[:1]
        recall_deepseek += recall_deepseek[:1]
        f1_deepseek += f1_deepseek[:1]

        angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
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
        ax.set_xticklabels(categories, fontsize=10, rotation=45)
        plt.title(f"Radar Chart - Precision, Recall, F1-score for {lang}")
        plt.legend(loc="upper right")
        plt.savefig(f"Category_Language_Radar_Chart_{lang}.png")
        print(f"📊 Saved: Category_Language_Radar_Chart_{lang}.png")

    print("✅ All category-language visualizations generated successfully!")

# Run the function with the given CSV file
generate_category_language_visuals("Category_Language_Level_Comparison.csv")
