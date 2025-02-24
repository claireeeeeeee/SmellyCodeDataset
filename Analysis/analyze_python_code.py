"""
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
"""

import os
import re
import ast
import hashlib
from collections import defaultdict

# Define Code Smell Rules (All 22 rules included)
CLASS_SMELL_RULES = [
    {"id": 1, "category": "Bloaters", "name": "Large Class", "condition": lambda c: c['LOC'] > 200 or c['Methods'] > 15 or c['Cyclomatic Complexity'] > 30},
    {"id": 2, "category": "Bloaters", "name": "Too Many Attributes", "condition": lambda c: c['Attributes'] > 10},
    {"id": 3, "category": "Bloaters", "name": "Lazy Class", "condition": lambda c: c['Attributes'] < 2},
    {"id": 4, "category": "Bloaters", "name": "God Object", "condition": lambda c: c['Responsibilities'] > 5},
    {"id": 15, "category": "Object-Orientation Abusers", "name": "Temporary Field", "condition": lambda c: c['Temporary Fields'] > 0},
    {"id": 16, "category": "Object-Orientation Abusers", "name": "Refused Bequest", "condition": lambda c: c['Unused Methods'] > 0},
    {"id": 17, "category": "Object-Orientation Abusers", "name": "Speculative Generality", "condition": lambda c: c['Unnecessary Abstractions'] > 0},
    {"id": 18, "category": "Change Preventers", "name": "Divergent Change", "condition": lambda c: c['Change Reasons'] > 1},
    {"id": 19, "category": "Change Preventers", "name": "Shotgun Surgery", "condition": lambda c: c['Affected Files'] > 5},
    {"id": 20, "category": "Change Preventers", "name": "Parallel Inheritance Hierarchies", "condition": lambda c: c['Parallel Hierarchies'] > 0},
    {"id": 21, "category": "Dispensables", "name": "Data Class", "condition": lambda c: c['Methods'] == 0},
    {"id": 22, "category": "Dispensables", "name": "Dead Code", "condition": lambda c: c['Unused Code'] > 0},
]

METHOD_SMELL_RULES = [
    {"id": 5, "category": "Bloaters", "name": "Long Method", "condition": lambda m: m['LOC'] > 20},
    {"id": 6, "category": "Bloaters", "name": "High Complexity", "condition": lambda m: m['Cyclomatic Complexity'] > 10},
    {"id": 7, "category": "Bloaters", "name": "Method Duplication", "condition": lambda m: m['Duplicated']},
    {"id": 8, "category": "Bloaters", "name": "Primitive Obsession", "condition": lambda m: m['Parameters'] > 2},
    {"id": 9, "category": "Couplers", "name": "Feature Envy", "condition": lambda m: m['Foreign Calls'] > 3},
    {"id": 10, "category": "Couplers", "name": "Inappropriate Intimacy", "condition": lambda m: m['Private Accesses'] > 2},
    {"id": 11, "category": "Couplers", "name": "Message Chains", "condition": lambda m: m['Method Chaining Depth'] > 2},
    {"id": 12, "category": "Couplers", "name": "Middle Man", "condition": lambda m: m['Delegation Percentage'] > 50},
    {"id": 13, "category": "Dispensables", "name": "Unnecessary Comments", "condition": lambda m: m['Comments'] > 3},
    {"id": 14, "category": "Object-Orientation Abusers", "name": "Switch Statements", "condition": lambda m: m['Switch Statements'] > 2},
]

# Extract Python class & method details
def analyze_python_code(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        code = file.read()
    
    tree = ast.parse(code)
    classes = defaultdict(lambda: {"LOC": 0, "Methods": 0, "Attributes": 0, "Cyclomatic Complexity": 0, "Unused Methods": 0, "Temporary Fields": 0, "Responsibilities": 0})
    methods = defaultdict(lambda: {"LOC": 0, "Cyclomatic Complexity": 0, "Parameters": 0, "Foreign Calls": 0, "Private Accesses": 0, "Method Chaining Depth": 0, "Delegation Percentage": 0, "Comments": 0, "Switch Statements": 0, "Duplicated": False})

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            classes[class_name]["LOC"] = len(code.split("\n"))
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    classes[class_name]["Methods"] += 1
                    methods[(class_name, method_name)]["LOC"] = len(ast.get_source_segment(code, item).split("\n"))
                    methods[(class_name, method_name)]["Parameters"] = len(item.args.args)
                    methods[(class_name, method_name)]["Cyclomatic Complexity"] = sum(isinstance(n, (ast.If, ast.For, ast.While)) for n in ast.walk(item))
        elif isinstance(node, ast.Assign):
            class_name = node.scopes[0].name if hasattr(node, "scopes") else "Unknown"
            classes[class_name]["Attributes"] += 1

    return classes, methods

# Compare method similarity (Duplicate Code Detection)
def check_duplicate_methods(methods):
    hashes = {}
    for (cls, method), data in methods.items():
        method_body = f"{cls}::{method}::{data['LOC']}"
        hash_value = hashlib.md5(method_body.encode()).hexdigest()
        if hash_value in hashes:
            methods[(cls, method)]["Duplicated"] = True
            methods[(hashes[hash_value], method)]["Duplicated"] = True
        else:
            hashes[hash_value] = cls

# Run Code Smell Analysis
def detect_code_smells(classes, methods):
    detected_smells = []
    
    # Apply class-level rules
    for class_name, class_data in classes.items():
        for rule in CLASS_SMELL_RULES:
            if rule["condition"](class_data):
                detected_smells.append((class_name, "-", rule["id"], rule["category"], rule["name"]))

    # Apply method-level rules
    for (class_name, method_name), method_data in methods.items():
        for rule in METHOD_SMELL_RULES:
            if rule["condition"](method_data):
                detected_smells.append((class_name, method_name, rule["id"], rule["category"], rule["name"]))

    return detected_smells

# Generate Markdown Report
def generate_report(detected_smells, output_path="CodeSmellsReport.md"):
    with open(output_path, "w", encoding="utf-8") as report:
        report.write("| Language | Class | Method | Code Smell # | Category | Code Smell |\n")
        report.write("|----------|-------|--------|--------------|------------|------------|\n")
        for class_name, method_name, smell_id, category, name in detected_smells:
            report.write(f"| Python | {class_name} | {method_name} | {smell_id} | {category} | {name} |\n")
    print(f"✅ Code Smell Report Generated: {output_path}")

# Main Function
def main(filepath):
    if not os.path.exists(filepath):
        print("❌ Error: File not found.")
        return

    # Step 1: Extract Code Metrics
    print("🔍 Analyzing Python code...")
    classes, methods = analyze_python_code(filepath)

    # Step 2: Detect Duplicate Code
    check_duplicate_methods(methods)

    # Step 3: Apply Code Smell Detection
    print("🚨 Detecting code smells...")
    detected_smells = detect_code_smells(classes, methods)

    # Step 4: Generate Report
    generate_report(detected_smells)

if __name__ == "__main__":
    main("Pizza.py")