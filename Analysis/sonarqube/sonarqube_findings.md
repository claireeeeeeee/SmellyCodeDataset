# SonarQube Findings Mapped to Code Smell Categories


**Python package**  
shop.py

| SonarQube Finding                                               | Mapped Code Smell Category | Explanation |
|-----------------------------------------------------------------|--------------------------|-------------|
| **Bug: All branches in conditional structure are the same (1)** | **Dispensables → Duplicate Code** | Redundant conditional structure leads to unnecessary duplication |
| **Empty methods (2)**                                           | **Dispensables → Lazy Class** | Unused methods that do not contribute to functionality |
| **Duplicate string literals (2)**                               | **Bloaters → Primitive Obsession** | Hardcoded values should be replaced with structured objects/constants |


pizza.py

| SonarQube Finding     | Mapped Code Smell Category | Explanation |
|-----------------------|--------------------------|-------------|
| **Functions and methods should not be empty (3)** | **Dispensables → Lazy Class** | Unused methods that do not contribute to functionality |


drink.py : sonarqube found 0 issues

customer.py

| SonarQube Finding                 | Mapped Code Smell Category | Explanation |
|-----------------------------------|--------------------------|-------------|
| **Empty methods (3)**             | **Dispensables → Lazy Class** | Unused methods that do not contribute to functionality |
| **Duplicate string literals (2)** | **Bloaters → Primitive Obsession** | Hardcoded values should be replaced with structured objects/constants |


chef.py

| SonarQube Finding                 | Mapped Code Smell Category | Explanation |
|-----------------------------------|--------------------------|-------------|
| **Bug: All branches in conditional structure are the same (1)** | **Dispensables → Duplicate Code** | Redundant conditional structure leads to unnecessary duplication |
 | **Function arguments should match parameters (1)** | **Change Preventers → Divergent Change** | Mismatched arguments can cause a TypeError, indicating a bug that needs fixing |
| **Empty methods (3)**             | **Dispensables → Lazy Class** | Unused methods that do not contribute to functionality |


cashier.py

| SonarQube Finding                 | Mapped Code Smell Category | Explanation |
|-----------------------------------|--------------------------|-------------|
| **Bug: All branches in conditional structure are the same (1)** | **Dispensables → Duplicate Code** | Redundant conditional structure leads to unnecessary duplication |
| **Empty methods (3)**             | **Dispensables → Lazy Class** | Unused methods that do not contribute to functionality |

