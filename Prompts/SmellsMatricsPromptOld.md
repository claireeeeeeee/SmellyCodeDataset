<!-- 
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
 --->


# Comprehensive Code Quality Analysis and Code Smell Detection

---

## **Input:**
1. A codebase in any programming language.
2. The following matrix for detecting code smells:

```markdown
| **Code Smell**              | **Metric**                                   | **Threshold**             | **Action**                                                                                   |
|------------------------------|----------------------------------------------|---------------------------|---------------------------------------------------------------------------------------------|
| Large Class                 | Lines of Code                                | > 200                     | Refactor by breaking the class into smaller, focused sections while keeping related logic together. |
| Too Many Methods            | Number of Methods                            | > 15                      | Simplify responsibilities, merge redundant logic, or split into cohesive helper methods.    |
| Too Many Attributes         | Number of Attributes                         | > 10                      | Group related attributes or reduce unnecessary state management.                            |
| Long Method                 | Lines of Code in a Method                    | > 20                      | Split the method into smaller, focused methods.                                             |
| High Complexity             | Cyclomatic Complexity in a Class/Method      | > 10 (method) / > 30 (class) | Simplify logic by breaking down conditions or refactoring into helper functions.            |
| Method Matching             | Percentage of Code Similarity with Another Method | > 80%                    | Consolidate similar methods into one reusable method.                                       |
| Frequent Primitive Patterns | Repeated Patterns of Primitive Data Types    | > 2 sequences             | Encapsulate common patterns into reusable data structures or objects.                      |
| Frequent Variable Patterns  | Repeated Patterns of Variables Used Together | > 2 sequences             | Encapsulate into higher-level abstractions.                                                 |
| Feature Envy                | Number of Foreign Method Calls               | > 3                       | Move the method to the interacting class to reduce coupling.                                |
| Inappropriate Intimacy      | Private/Protected Members Accessed           | > 2                       | Reorganize relationships between classes or merge classes as needed.                        |
| Message Chains              | Method Calls Chained in One Statement        | > 2 levels                | Introduce intermediary methods or use a Facade to simplify chains.                          |
| Middle Man                  | Delegated Methods                            | > 50%                     | Remove unnecessary delegation by calling methods directly from the client.                  |
| Lazy Class                  | Number of Attributes                         | < 2                       | Merge with a related class or remove if it serves no distinct purpose.                      |
| Shotgun Surgery             | Classes Affected by a Single Change          | > 3                       | Reduce dependencies, centralize logic.                                                      |
| Divergent Change            | Different Functionalities Modified Together  | > 3                       | Split class into separate cohesive components.                                              |
| Parallel Inheritance        | Parallel Classes Required                    | > 2 hierarchies           | Reduce dependency between hierarchies, redesign relationships.                              |
| Control Coupling            | Direct Dependencies Between Classes          | > 3                       | Use dependency injection or introduce an interface.                                        |
| Refused Bequest             | Unused Inherited Methods                     | > 50%                     | Remove inheritance, use composition instead.                                               |
| God Object                  | Responsibilities in a Single Class          | > 5                       | Split the class based on single responsibility principle.                                   |
| Unnecessary Comments        | Number of Comments Per Method                | > 3                       | Refactor the code to be self-explanatory.                                                  |
```

---

## **Instructions:**
1. **Extract Metrics**:
   - Parse the provided code to calculate the following metrics:
     - **Classes**:
       - Lines of Code, Number of Methods, Number of Attributes, Cyclomatic Complexity (sum of all methods' complexity in the class divided by the number of methods).
     - **Methods**:
       - Lines of Code, Number of Parameters, Cyclomatic Complexity.
       - Percentage of code similarity with other methods.
       - Count of:
         - Foreign Method Calls (calls to methods in other classes).
         - Private/Protected Member Access.
         - Method Chaining (number of chained calls in one statement).
         - Delegation Percentage (percentage of logic delegated to other classes).

2. **Generate a Markdown Code Smells Table**:
   - Compare metrics against thresholds to identify code smells.
   - Include the following columns:
     - **Code Smell Name**
     - **Location (Class/Method)**
     - **Metric**
     - **Detected Value**
     - **Recommendation**

3. **Refactor Code**:
   - we already have five classes (Customer, Pizza, Drink, Cashier, Shop), so do not create or a new class with these name as they exit, and you are given only one of them to refactor.
   - Apply the recommended actions from the Code Smells Table.
   - Refactor the code to fix the identified code smells, prioritizing modifications within the existing entities (e.g., classes, methods, functions).
   - Avoid creating new entities unless required for distinct responsibilities not covered by the existing ones.
   - Ensure the refactored code is clean, follows the language's best practices, and retains the original functionality and logic.
   - Refactor the code by splitting classes, simplifying methods, and encapsulating logic where necessary.

4. **Generate Output**:
   - **Code Smells Table**:
     - The Markdown table summarizing the analysis (e.g., `CodeSmellsReport.md`).
     - Format as a standalone Markdown table listing all identified code smells.
     - Provide the refactored code after addressing the detected smells.
     - The complete refactored code in the same language as the input file (e.g., `RefactoredCode.java`, `RefactoredCode.js`, `RefactoredCode.py`, `RefactoredCode.cpp`).

---

## **Output Example:**

### Code Smells Table
The `CodeSmellsReport.md` file will include:
```markdown
# Detected Code Smells

| Code Smell         | Location               | Metric                       | Detected Value          | Recommendation                                            |
|--------------------|-----------------------|-----------------------------|-------------------------|----------------------------------------------------------|
| Large Class        | Cashier               | Number of Methods > 15      | 28                      | Split into smaller, focused classes.                    |
| Primitive Obsession| order_with_details    | Number of Parameters > 2     | 6                       | Encapsulate into an `OrderDetails` class.               |
```

