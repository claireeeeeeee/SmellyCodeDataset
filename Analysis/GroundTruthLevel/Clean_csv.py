"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import pandas as pd
import sys
import os

def clean_and_normalize(csv_filename):
    """
    Cleans and normalizes a given CSV file:
    - Standardizes column names
    - Removes incorrect 'Code Smell #' values
    - Ensures numerical consistency
    - Creates a unique identifier for comparisons
    - Saves the cleaned file in the same directory with 'Cleaned_' prefix
    """

    # Check if file exists
    if not os.path.exists(csv_filename):
        print(f"Error: File '{csv_filename}' not found.")
        return

    # Load CSV file
    df = pd.read_csv(csv_filename)

    # Standardize column names
    df.columns = df.columns.str.strip()

    # Ensure 'Code Smell #' is an integer and remove incorrect entries
    if "Code Smell #" in df.columns:
        df = df[df["Code Smell #"] != "Code Smell #"]  # Remove erroneous row if exists
        df["Code Smell #"] = pd.to_numeric(df["Code Smell #"], errors='coerce')  # Convert to numeric, handle errors
        df = df.dropna(subset=["Code Smell #"])  # Drop rows where conversion failed
        df["Code Smell #"] = df["Code Smell #"].astype(int)  # Convert to integer

    # Ensure 'Method' column is string (avoiding NaN mismatches)
    if "Method" in df.columns:
        df["Method"] = df["Method"].fillna("").astype(str)

    # Create a unique identifier for each entry
    df["Identifier"] = df["Language"] + "_" + df["Class"] + "_" + df["Method"] + "_" + df["Code Smell"]

    # Generate new filename
    dir_name, filename = os.path.split(csv_filename)
    cleaned_filename = os.path.join(dir_name, "Cleaned_" + filename)

    # Save the cleaned file in the same directory
    df.to_csv(cleaned_filename, index=False)
    print(f"✅ Cleaned file saved: {cleaned_filename}")

# Check if user provided a filename
if len(sys.argv) < 2:
    print("Usage: python clean_csv.py <csv_filename>")
    sys.exit(1)

# Get filename from command line argument
csv_filename = sys.argv[1]

# Run cleaning function
clean_and_normalize(csv_filename)
