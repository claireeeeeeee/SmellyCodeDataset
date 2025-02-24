<!-- 
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
 --->


# Smelly Code Dataset for LLM-Based Code Analysis

## Overview

This repository contains a collection of **intentionally smelly code** in multiple programming languages (**Java, Python, JavaScript, and C++**). The dataset is used to **test and evaluate the capabilities of Large Language Models (LLMs)** in detecting and refactoring common code smells.

Code smells included in this dataset belong to the following categories:
- **Bloaters** (Large Classes, Long Methods, Primitive Obsession)
- **Couplers** (Feature Envy, Inappropriate Intimacy)
- **Change Preventers** (Divergent Change, Shotgun Surgery)
- **Dispensables** (Duplicate Code, Lazy Class, Data Class)
- **Object-Oriented Abusers** (Refused Bequest, Alternative Classes with Different Interfaces)

## Purpose

The primary goal of this dataset is to **assess how well LLMs like GPT-4, Code Llama, and other AI models** can:
- Detect various types of code smells.
- Suggest effective refactoring strategies.
- Improve code maintainability based on automated analysis.

## Project Structure

