# **Comprehensive Code Quality Analysis and Code Smell Detection Rules**

## **Input:**
- A codebase in any programming language.
- The provided class to refactor is one of the following: `Customer`, `Pizza`, `Drink`, `Cashier`, or `Shop`. **No new class with these names should be created**.
- The analysis should detect and **fix** code smells based on the predefined **Code Smells Table**.

---

## **Rules**

### **Step 1: Extract Metrics (Parameter Analysis)**

#### **Class-Level Rules**

1. **Class LOC Rule**  
   - **Action:** Count the total number of lines in the class.

2. **Class Method Count Rule**  
   - **Action:** Count the total number of methods in the class.

3. **Class Attribute Count Rule**  
   - **Action:** Count the total number of attributes (fields) in the class.

4. **Class Cyclomatic Complexity Rule**  
   - **Action:** Compute the average cyclomatic complexity of methods in the class.

#### **Method-Level Rules**

5. **Method LOC Rule**  
   - **Action:** Count the total number of lines in the method.

6. **Method Parameter Count Rule**  
   - **Action:** Count the number of parameters the method accepts.

7. **Method Cyclomatic Complexity Rule**  
   - **Action:** Count the number of decision points (if, for, while, switch, etc.).

8. **Method Code Similarity Rule**  
   - **Action:** Compute the percentage of duplicated code in different methods.

9. **Method Foreign Calls Rule**  
   - **Action:** Count the number of calls to methods in other classes.

10. **Method Private/Protected Access Rule**  
   - **Action:** Count the number of accesses to private or protected members.

11. **Method Chaining Depth Rule**  
   - **Action:** Count the number of chained method calls in a single statement.

12. **Method Delegation Percentage Rule**  
   - **Action:** Compute the percentage of logic delegated to other classes.

---

### **Step 2: Apply Code Smell Detection and Refactoring Rules**

#### **Class-Level Code Smell Rules**

13. **Large Class Rule**  
   - **Condition:**  
     - `LOC > 200` OR  
     - `Number of Methods > 15` OR  
     - `Cyclomatic Complexity > 30`  
   - **Action:**  
     - **Refactor the class by splitting large methods** into smaller ones, avoiding unnecessary complexity.
     - **Do NOT create a new class with existing names (`Customer, Pizza, Drink, Cashier, Shop`)**. Instead, optimize within the current class.

14. **Too Many Attributes Rule**  
   - **Condition:**  
     - `Number of Attributes > 10`  
   - **Action:**  
     - Group related attributes into structured objects if applicable.
     - Avoid unnecessary attributes and **ensure proper encapsulation**.

15. **Lazy Class Rule**  
   - **Condition:**  
     - `Number of Attributes < 2`  
   - **Action:**  
     - Merge with a related class **only if necessary** while maintaining clarity.

16. **God Object Rule**  
   - **Condition:**  
     - `Responsibilities (Distinct Functional Areas) > 5`  
   - **Action:**  
     - **Reorganize logic** to make responsibilities clearer **without creating a new class unless absolutely necessary**.

#### **Method-Level Code Smell Rules**

17. **Long Method Rule**  
   - **Condition:**  
     - `LOC > 20`  
   - **Action:**  
     - Split large methods into smaller, reusable helper methods.

18. **High Complexity Method Rule**  
   - **Condition:**  
     - `Cyclomatic Complexity > 10`  
   - **Action:**  
     - Reduce nested conditions and improve method clarity.

19. **Method Duplication Rule**  
   - **Condition:**  
     - `Code Similarity with Another Method > 80%`  
   - **Action:**  
     - Consolidate duplicate logic into reusable methods.

20. **Primitive Obsession Rule**  
   - **Condition:**  
     - `Number of Parameters > 2` (especially primitive types)  
   - **Action:**  
     - Encapsulate parameters into structured objects **within the same class**.

21. **Feature Envy Rule**  
   - **Condition:**  
     - `Foreign Method Calls > 3`  
   - **Action:**  
     - Move the method closer to where the data is primarily used.

22. **Inappropriate Intimacy Rule**  
   - **Condition:**  
     - `Private/Protected Member Access > 2`  
   - **Action:**  
     - Improve encapsulation and reduce direct access to internal members.

23. **Message Chains Rule**  
   - **Condition:**  
     - `Method Chaining Depth > 2`  
   - **Action:**  
     - Introduce intermediary methods.

24. **Middle Man Rule**  
   - **Condition:**  
     - `Delegation Percentage > 50%`  
   - **Action:**  
     - Remove unnecessary delegation.

25. **Unnecessary Comments Rule**  
   - **Condition:**  
     - `Number of Comments > 3`  
   - **Action:**  
     - Make the code self-explanatory with better naming.

---

### **Step 3: Refactoring Process and Output Rules**

26. **Code Smell Report Rule**  
   - **Condition:**  
     - If any of the above code smells are detected.  
   - **Action:**  
     - Generate a structured Markdown table (`CodeSmellsReport.md`) summarizing the detected code smells.

27. **Refactored Code Rule**

   - **Condition:**  
     - If code smells are detected and refactoring is required.  
     - **The provided class may depend on existing classes that are not given** (e.g., `Customer` might already exist elsewhere in the project).  

   - **Action:**  
     - Generate a **refactored version of the given class**, ensuring:  
       - **No new class is created with existing names (`Customer, Pizza, Drink, Cashier, Shop`)**.  
       - **If a related class (e.g., `Customer`) logically exists but is not provided, assume its presence and use it instead of recreating attributes.**  
       - The class is optimized by **splitting methods, simplifying logic, and encapsulating where necessary**.  
       - Code follows best practices for maintainability, readability, and performance.  
       - **Preserve the expected behavior of the system** and ensure compatibility with related classes.  
       - **Save the refactored class as** `Refactored_<ClassName>.ext` (e.g., `Refactored_Customer.java`).

28. **Preserve Original Functionality Rule**  
   - **Condition:**  
     - Code modifications should not change the program’s expected behavior.  
   - **Action:**  
     - Ensure the refactored version produces the **same output and logic flow** as the original.

29. **Avoid Over-Engineering Rule**  
   - **Condition:**  
     - Unnecessary abstraction or excessive modifications beyond resolving code smells.  
   - **Action:**  
     - Keep the refactoring **minimal but effective** to enhance clarity and maintainability without overcomplicating the design.

---

