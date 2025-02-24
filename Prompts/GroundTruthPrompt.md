
### Please analyze the attached code file for code smells.

The code snippet is always pasted at the end of this prompt after the delimiter line **"### CODE STARTS HERE"**. The code may be written in **Java, JavaScript, Python, or C++** and may contain various code smells categorized as follows:

---

### **1. Bloaters**  
(When code, methods, or classes grow excessively large and become difficult to manage)  
- **Large Class**  A class that has too many responsibilities. *(Must be checked explicitly, as it is not always commented)*  
- **Long Method/Function**  A method or function that is too long and complex. *(Detect from comments, but verify method complexity if needed)*  
- **Primitive Obsession**  Overuse of primitive data types instead of objects. *(Detect based on annotations in comments)*  
- **Long Parameter List**  Methods with too many parameters. *(Detect based on comments or excessive parameter count)*  
- **Data Clumps**  Related data fields that should be encapsulated together. *(Detect from comments)*  

---

### **2. Object-Orientation Abusers**  
(When object-oriented principles are misused)  
- **Switch Statements**  Overuse of switch/case or if-else chains. *(Detect based on comments, but also verify presence of excessive conditional structures)*  
- **Temporary Field**  Fields used only under certain conditions. *(Detect from comments or check for instance variables that are seldom used)*  
- **Refused Bequest**  Subclasses inheriting unused methods. *(Detect if indicated in comments)*  
- **Speculative Generality**  Unnecessary abstractions or unused code meant for future use. *(Detect from comments or identify unused generalization structures)*  

---

### **3. Change Preventers**  
(When small changes require widespread modifications)  
- **Divergent Change**  A class that changes for multiple reasons. *(Detect from comments)*  
- **Shotgun Surgery**  A single change requires updates in many places. *(Detect from comments and check for multiple small update methods related to the same field)*  
- **Parallel Inheritance Hierarchies**  One hierarchy forces modifications in another. *(Detect from comments or class hierarchy structures)*  

---

### **4. Dispensables**  
(When code is unnecessary and should be removed)  
- **Comments**  Over-reliance on comments instead of clear code. *(Detect by analyzing excessive or redundant comments)*  
- **Duplicate Code**  Identical or similar code in multiple places. *(Detect from comments and structural duplication checks)*  
- **Lazy Class**  A class that does too little. *(Detect from comments or identify classes with minimal functionality)*  
- **Data Class**  A class that only contains data without behavior. *(Detect from comments or check for behaviorless classes)*  
- **Dead Code**  Unused code that remains in the system. *(Detect from comments and check for unreachable methods)*  

---

### **5. Couplers**  
(When code elements are too dependent on each other)  
- **Feature Envy**  A method overly reliant on another class’s data. *(Detect from comments or excessive calls to other classes' attributes/methods)*  
- **Inappropriate Intimacy**  Classes tightly coupled and exposing internals. *(Detect from comments or identify classes accessing each other’s private fields)*  
- **Message Chains**  A sequence of method calls creating dependencies. *(Detect from comments or analyze method chaining depth)*  
- **Middle Man**  A class that delegates too much without adding value. *(Detect from comments or find classes with methods that only call other methods)*  

---

### **Instructions:**  
1. **Each occurrence of a code smell should be uniquely numbered (1 to N)**. Even if the same smell appears multiple times, **each occurrence should have a unique row**.  
2. **Do NOT include line numbers or location details** in the output.  
3. The output should be **strictly formatted as a Markdown (.md) table** with the following columns: 


   - **Language** (Java, JavaScript, Python, or C++)  
   - **Class**  
   - **Code Smell #**  
   - **Category** (Bloaters, Object-Orientation Abusers, Change Preventers, Dispensables, Couplers)  
   - **Code Smell**  
   - **Method**  
   - **Type**  

---

### **Example Markdown Table Output:**  
```markdown
| Language  | Class       | Code Smell # | Category                     | Code Smell                     | Method                      | Type                                                                                                       |
|-----------|------------|--------------|------------------------------|--------------------------------|-----------------------------|------------------------------------------------------------------------------------------------------------|
| Python    | Pizza      | 1            | Bloaters                     | Primitive Obsession            | __init__                    | Using a primitive (Boolean) to represent extra cheese instead of a more expressive construct                |
| Java      | Order      | 2            | Bloaters                     | Data Clumps                    | updateCustomerDetails       | Grouped customer information fields that might be refactored into their own object                         |
| C++       | Inventory  | 3            | Bloaters                     | Long Parameter List            | processOrder                | Method accepting an excessive number of parameters                                                          |
| JavaScript| Cart       | 4            | Dispensables                 | Duplicate Code                 | addItem                     | Repeated functionality leading to redundant logic                                                           |
| Java      | Payment    | 5            | Couplers                      | Feature Envy                   | calculateDiscount           | A method overly relies on data from another class                                                           |