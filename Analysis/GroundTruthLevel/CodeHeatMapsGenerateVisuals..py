"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from GroundTruthSize.md
file_path = "GroundTruthSize.md"

data = []
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines[2:]:  # Skip header lines
        parts = line.strip().split("|")
        if len(parts) >= 6:
            data.append({
                "Programming Language": parts[1].strip(),
                "Class Name": parts[2].strip(),
                "Lines of Code": int(parts[3].strip()),
                "Number of Methods": int(parts[4].strip()),
                "Number of Attributes": int(parts[5].strip()),
                "Number of Code Smells": int(parts[6].strip())
            })

# Convert to DataFrame
df = pd.DataFrame(data)

# Set figure style
plt.style.use("ggplot")

# Function to generate and save heatmaps
def generate_heatmap(metric, title, cmap, filename):
    plt.figure(figsize=(12, 8))
    pivot_table = df.pivot("Class Name", "Programming Language", metric)
    sns.heatmap(pivot_table, annot=True, cmap=cmap, linewidths=0.5, fmt="d")
    plt.title(title)
    plt.xlabel("Programming Language")
    plt.ylabel("Class Name")
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()

# Generate and save 4 Heatmaps
generate_heatmap("Lines of Code", "Heatmap of Lines of Code Across Classes and Languages", "Blues", "LOCHeatMap.png")
generate_heatmap("Number of Methods", "Heatmap of Number of Methods Across Classes and Languages", "Greens", "MethodsNoHeatMap.png")
generate_heatmap("Number of Attributes", "Heatmap of Number of Attributes Across Classes and Languages", "Oranges", "AttributesNoHeatMap.png")
generate_heatmap("Number of Code Smells", "Heatmap of Code Smells Across Classes and Languages", "Reds", "CodeSmellsNoHeatMap.png")
