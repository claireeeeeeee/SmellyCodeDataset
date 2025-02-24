"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_type_language_visuals(csv_path):
    """
    Reads type-language-level comparison results from CSV and generates model-specific heatmaps for better comparison.
    """

    # Load CSV file
    df = pd.read_csv(csv_path)

    # Ensure numeric values and handle missing data
    df["Precision"] = pd.to_numeric(df["Precision"], errors="coerce")
    df["Recall"] = pd.to_numeric(df["Recall"], errors="coerce")
    df["F1-score"] = pd.to_numeric(df["F1-score"], errors="coerce")
    df.fillna(0, inplace=True)  # Replace NaN values with 0

    # **Separate Data for Each Model**
    df_gpt4 = df[df["Model"] == "GPT-4"].groupby(["Code Smell", "Language"], as_index=False).mean()
    df_deepseek = df[df["Model"] == "DeepSeek"].groupby(["Code Smell", "Language"], as_index=False).mean()

    # Pivot Data for Heatmaps
    precision_gpt4 = df_gpt4.pivot(index="Code Smell", columns="Language", values="Precision")
    precision_deepseek = df_deepseek.pivot(index="Code Smell", columns="Language", values="Precision")
    precision_diff = precision_gpt4 - precision_deepseek  # Precision Difference

    recall_gpt4 = df_gpt4.pivot(index="Code Smell", columns="Language", values="Recall")
    recall_deepseek = df_deepseek.pivot(index="Code Smell", columns="Language", values="Recall")
    recall_diff = recall_gpt4 - recall_deepseek  # Recall Difference

    f1_gpt4 = df_gpt4.pivot(index="Code Smell", columns="Language", values="F1-score")
    f1_deepseek = df_deepseek.pivot(index="Code Smell", columns="Language", values="F1-score")
    f1_diff = f1_gpt4 - f1_deepseek  # F1-score Difference

    # 📊 **1. Heatmap for GPT-4 Precision**
    plt.figure(figsize=(14, 7))
    sns.heatmap(precision_gpt4, annot=True, cmap="Blues", linewidths=0.5, fmt=".2f")
    plt.title("GPT-4 Precision by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Precision_Heatmap_GPT4.png")
    print("📊 Saved: Type_Language_Precision_Heatmap_GPT4.png")

    # 📊 **2. Heatmap for DeepSeek Precision**
    plt.figure(figsize=(14, 7))
    sns.heatmap(precision_deepseek, annot=True, cmap="Blues", linewidths=0.5, fmt=".2f")
    plt.title("DeepSeek Precision by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Precision_Heatmap_DeepSeek.png")
    print("📊 Saved: Type_Language_Precision_Heatmap_DeepSeek.png")

    # 📊 **3. Precision Comparison (GPT-4 - DeepSeek)**
    plt.figure(figsize=(14, 7))
    sns.heatmap(precision_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("Precision Difference (GPT-4 - DeepSeek) by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Precision_Diff_Heatmap.png")
    print("📊 Saved: Type_Language_Precision_Diff_Heatmap.png")

    # 📊 **4. Heatmap for GPT-4 Recall**
    plt.figure(figsize=(10, 6))
    sns.heatmap(recall_gpt4, annot=True, cmap="Greens", linewidths=0.5, fmt=".2f")
    plt.title("GPT-4 Recall by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Recall_Heatmap_GPT4.png")
    print("📊 Saved: Type_Language_Recall_Heatmap_GPT4.png")

    # 📊 **5. Heatmap for DeepSeek Recall**
    plt.figure(figsize=(10, 6))
    sns.heatmap(recall_deepseek, annot=True, cmap="Greens", linewidths=0.5, fmt=".2f")
    plt.title("DeepSeek Recall by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Recall_Heatmap_DeepSeek.png")
    print("📊 Saved: Type_Language_Recall_Heatmap_DeepSeek.png")

    # 📊 **6. Recall Comparison (GPT-4 - DeepSeek)**
    plt.figure(figsize=(10, 6))
    sns.heatmap(recall_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("Recall Difference (GPT-4 - DeepSeek) by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_Recall_Diff_Heatmap.png")
    print("📊 Saved: Type_Language_Recall_Diff_Heatmap.png")

    # 📊 **7. Heatmap for F1-score GPT-4**
    plt.figure(figsize=(10, 6))
    sns.heatmap(f1_gpt4, annot=True, cmap="Oranges", linewidths=0.5, fmt=".2f")
    plt.title("GPT-4 F1-score by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_F1_Heatmap_GPT4.png")
    print("📊 Saved: Type_Language_F1_Heatmap_GPT4.png")

    # 📊 **8. Heatmap for F1-score DeepSeek**
    plt.figure(figsize=(10, 6))
    sns.heatmap(f1_deepseek, annot=True, cmap="Oranges", linewidths=0.5, fmt=".2f")
    plt.title("DeepSeek F1-score by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_F1_Heatmap_DeepSeek.png")
    print("📊 Saved: Type_Language_F1_Heatmap_DeepSeek.png")

    # 📊 **9. F1-Score Comparison (GPT-4 - DeepSeek)**
    plt.figure(figsize=(10, 6))
    sns.heatmap(f1_diff, annot=True, cmap="coolwarm", linewidths=0.5, fmt=".2f", center=0)
    plt.title("F1-score Difference (GPT-4 - DeepSeek) by Code Smell & Language")
    plt.xlabel("Language")
    plt.ylabel("Code Smell")
    plt.xticks(rotation=45)
    plt.savefig("Type_Language_F1_Diff_Heatmap.png")
    print("📊 Saved: Type_Language_F1_Diff_Heatmap.png")

    print("✅ All type-language visualizations generated successfully!")

# Run the function with the given CSV file
generate_type_language_visuals("Type_Language_Level_Comparison.csv")
