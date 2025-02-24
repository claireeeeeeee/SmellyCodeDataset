
| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Python    | Shop   | 1            | Bloaters                   | Large Class                | Entire Class                    | The class has too many responsibilities (order processing, notifications, customer management, etc.) |
| Python    | Shop   | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`bool`) for `frequent_customer_discount` instead of a more expressive construct |
| Python    | Shop   | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`first_name`, `last_name`, `address`, `phone_number`, `email`) that should be encapsulated |
| Python    | Shop   | 4            | Bloaters                   | Long Parameter List        | order_with_unnecessary_details | Method receives multiple unrelated parameters (`first_name`, `last_name`, etc.) |
| Python    | Shop   | 5            | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |
| Python    | Shop   | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`temp_discount_code`, `temp_order_note`) used only under specific conditions |
| Python    | Shop   | 7            | Change Preventers          | Shotgun Surgery           | update_contact_info            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Python    | Shop   | 8            | Change Preventers          | Shotgun Surgery           | update_name                     | Splitting name updates across different methods instead of a single encapsulated update |
| Python    | Shop   | 9            | Change Preventers          | Shotgun Surgery           | update_address                  | Similar to `update_name`, updates should be encapsulated |
| Python    | Shop   | 10           | Change Preventers          | Shotgun Surgery           | update_phone_number             | Separate field update that contributes to shotgun surgery |
| Python    | Shop   | 11           | Change Preventers          | Shotgun Surgery           | update_email                    | Separate field update that contributes to shotgun surgery |
| Python    | Shop   | 12           | Change Preventers          | Divergent Change          | notify_for_promotion            | Multiple notification methods each handling separate concerns |
| Python    | Shop   | 13           | Change Preventers          | Divergent Change          | notify_for_discount             | Related to `notify_for_promotion`, but managed separately |
| Python    | Shop   | 14           | Change Preventers          | Divergent Change          | notify_for_new_arrivals         | Another notification method that should be unified |
| Python    | Shop   | 15           | Change Preventers          | Parallel Inheritance Hierarchies | apply_discount              | Parallel implementation of discount and loyalty points logic |
| Python    | Shop   | 16           | Change Preventers          | Parallel Inheritance Hierarchies | apply_loyalty_points        | Another parallel logic similar to `apply_discount` |
| Python    | Shop   | 17           | Dispensables               | Speculative Generality     | ask_for_receipt                 | Method is present but never used in any flow |
| Python    | Shop   | 18           | Dispensables               | Dead Code                  | another_unused_method           | Unused method that can be removed |
| Python    | Shop   | 19           | Dispensables               | Dead Code                  | yet_another_unused_method       | Another unused method |
| Python    | Shop   | 20           | Couplers                   | Message Chains             | chain_of_methods                | Excessive method chaining (`self.casher.chef.clean_kitchen()`) |
| Python    | Shop   | 21           | Couplers                   | Middle Man                 | middleman_method                | Delegates work without adding value |
| Python    | Shop   | 22           | Couplers                   | Inappropriate Intimacy     | access_internal_details         | Accesses internal attributes (`self.casher.chef.busy`) |
| Python    | Shop   | 23           | Bloaters                   | Long Method                | long_method                     | Performs multiple actions in a single method, reducing readability |

| Language  | Class          | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Python    | Pizza       | 1            | Bloaters                   | Large Class                | Entire Class                    | The class mixes pizza properties, customer management, complaints, and discounts, violating SRP |
| Python    | Pizza       | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`bool`) for `extra_cheese` instead of a more expressive construct |
| Python    | Pizza       | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`customer_first_name`, `customer_last_name`, `customer_address`, etc.) that should be encapsulated |
| Python    | Pizza       | 4            | Bloaters                   | Long Parameter List        | order_with_unnecessary_details | Method receives multiple unrelated parameters (`pizza_type`, `size`, `crust_type`, etc.) |
| Python    | Pizza       | 5            | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |
| Python    | Pizza       | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`temp_discount_code`, `temp_order_note`) used only under specific conditions |
| Python    | Pizza       | 7            | Change Preventers          | Shotgun Surgery           | update_customer_info            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Python    | Pizza       | 8            | Change Preventers          | Shotgun Surgery           | update_customer_name            | Splitting name updates across different methods instead of a single encapsulated update |
| Python    | Pizza       | 9            | Change Preventers          | Shotgun Surgery           | update_customer_address         | Similar to `update_customer_name`, updates should be encapsulated |
| Python    | Pizza       | 10           | Change Preventers          | Shotgun Surgery           | update_customer_phone_number    | Separate field update that contributes to shotgun surgery |
| Python    | Pizza       | 11           | Change Preventers          | Shotgun Surgery           | update_customer_email           | Separate field update that contributes to shotgun surgery |
| Python    | Pizza       | 12           | Change Preventers          | Divergent Change          | notify_for_promotion            | Multiple notification methods each handling separate concerns |
| Python    | Pizza       | 13           | Change Preventers          | Divergent Change          | notify_for_discount             | Related to `notify_for_promotion`, but managed separately |
| Python    | Pizza       | 14           | Change Preventers          | Divergent Change          | notify_for_new_arrivals         | Another notification method that should be unified |
| Python    | Pizza       | 15           | Change Preventers          | Parallel Inheritance Hierarchies | apply_discount              | Parallel implementation of discount and loyalty points logic |
| Python    | Pizza       | 16           | Change Preventers          | Parallel Inheritance Hierarchies | apply_loyalty_points        | Another parallel logic similar to `apply_discount` |
| Python    | Pizza       | 17           | Dispensables               | Speculative Generality     | ask_for_receipt                 | Method is present but never used in any flow |
| Python    | Pizza       | 18           | Dispensables               | Dead Code                  | another_unused_method           | Unused method that can be removed |
| Python    | Pizza       | 19           | Dispensables               | Dead Code                  | yet_another_unused_method       | Another unused method |
| Python    | Pizza       | 20           | Dispensables               | Duplicate Code             | duplicate_method                | Repeated functionality with identical operations on the same attribute |
| Python    | Pizza       | 21           | Couplers                   | Message Chains             | chain_of_methods                | Excessive method chaining (`self.update_customer_address("123 Street")`) |
| Python    | Pizza       | 22           | Couplers                   | Middle Man                 | middleman_method                | Delegates work without adding value |
| Python    | Pizza       | 23           | Couplers                   | Inappropriate Intimacy     | access_internal_details         | Accesses internal attributes (`self.size`, `self.dough_type`, `self.topping`) |
| Python    | Pizza       | 24           | Bloaters                   | Long Method                | long_method                     | Performs multiple actions in a single method, reducing readability |
| Python    | CheesePizza | 25           | Object-Orientation Abusers | Refused Bequest            | __init__                        | Subclass inherits but does not use `cheese_type` |
| Python    | CheesePizza | 26           | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |

| Language  | Class  | Code Smell # | Category     | Code Smell           | Method          | Type                                                                 |
|-----------|--------|--------------|--------------|----------------------|-----------------|----------------------------------------------------------------------|
| Python    | Drink  | 1            | Dispensables | Data Class           | Entire Class    | Class only stores data (`drink_type`) without meaningful behavior |
| Python    | Drink  | 2            | Bloaters     | Primitive Obsession  | create_order    | Uses a primitive (`string`) instead of a more expressive object for drink type |
| Python    | Drink  | 3            | Bloaters     | Primitive Obsession  | add_to_order    | Uses a primitive (`string`) instead of an object for order processing |
| Python    | Drink  | 4            | Bloaters     | Primitive Obsession  | confirm_order   | Uses a primitive (`string`) instead of an object for order confirmation |

| Language  | Class     | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|----------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Python    | Customer | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: ordering, complaints, contact updates, notifications, and discounts |
| Python    | Customer | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`bool`) for `frequent_customer_discount` instead of a more expressive construct |
| Python    | Customer | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`first_name`, `last_name`, `address`, `phone_number`, `email`) should be encapsulated |
| Python    | Customer | 4            | Bloaters                   | Long Parameter List        | order_with_unnecessary_details | Method receives multiple unrelated parameters (`pizza_type`, `size`, `crust_type`, etc.) |
| Python    | Customer | 5            | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |
| Python    | Customer | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`temp_discount_code`, `temp_order_note`) used only under specific conditions |
| Python    | Customer | 7            | Object-Orientation Abusers | Refused Bequest            | refused_bequest                 | Method is meant for inheritance but is empty |
| Python    | Customer | 8            | Change Preventers          | Shotgun Surgery           | update_contact_info            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Python    | Customer | 9            | Change Preventers          | Shotgun Surgery           | update_name                     | Splitting name updates across different methods instead of a single encapsulated update |
| Python    | Customer | 10           | Change Preventers          | Shotgun Surgery           | update_address                  | Similar to `update_name`, updates should be encapsulated |
| Python    | Customer | 11           | Change Preventers          | Shotgun Surgery           | update_phone_number             | Separate field update that contributes to shotgun surgery |
| Python    | Customer | 12           | Change Preventers          | Shotgun Surgery           | update_email                    | Separate field update that contributes to shotgun surgery |
| Python    | Customer | 13           | Change Preventers          | Divergent Change          | notify_for_promotion            | Multiple notification methods each handling separate concerns |
| Python    | Customer | 14           | Change Preventers          | Divergent Change          | notify_for_discount             | Related to `notify_for_promotion`, but managed separately |
| Python    | Customer | 15           | Change Preventers          | Divergent Change          | notify_for_new_arrivals         | Another notification method that should be unified |
| Python    | Customer | 16           | Change Preventers          | Parallel Inheritance Hierarchies | apply_discount              | Parallel implementation of discount and loyalty points logic |
| Python    | Customer | 17           | Change Preventers          | Parallel Inheritance Hierarchies | apply_loyalty_points        | Another parallel logic similar to `apply_discount` |
| Python    | Customer | 18           | Dispensables               | Speculative Generality     | ask_for_receipt                 | Method is present but never used in any flow |
| Python    | Customer | 19           | Dispensables               | Dead Code                  | another_unused_method           | Unused method that can be removed |
| Python    | Customer | 20           | Dispensables               | Dead Code                  | yet_another_unused_method       | Another unused method |
| Python    | Customer | 21           | Dispensables               | Duplicate Code             | duplicate_complaint             | Repeated functionality with identical operations on the same attribute |
| Python    | Customer | 22           | Couplers                   | Feature Envy               | order_pizza                     | Excessive reliance on another class (`pizza_shop`) for core functionality |
| Python    | Customer | 23           | Couplers                   | Inappropriate Intimacy     | complain                         | Accessing another object's internal details (`self.pizza_shop.casher.chef.clean_kitchen()`) |
| Python    | Customer | 24           | Couplers                   | Message Chains             | chain_of_methods                | Excessive method chaining (`self.pizza_shop.casher.chef.clean_kitchen()`) |
| Python    | Customer | 25           | Couplers                   | Middle Man                 | middleman_method                | Delegates work without adding value |
| Python    | Customer | 26           | Bloaters                   | Long Method                | long_complaint_method           | Performs multiple actions in a single method, reducing readability |
| Python    | Customer | 27           | Dispensables               | Unnecessary Comments       | order_drink                      | Over-commenting explaining self-explanatory steps |

| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Python    | Chef   | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: baking, delivering, cleaning, notifications, complaints, and discounts |
| Python    | Chef   | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`bool`) for `frequent_customer_discount` instead of a more expressive construct |
| Python    | Chef   | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped chef details (`first_name`, `last_name`, `address`, `phone_number`, `email`) should be encapsulated |
| Python    | Chef   | 4            | Bloaters                   | Long Parameter List        | order_with_unnecessary_details | Method receives multiple unrelated parameters (`pizza_type`, `size`, `crust_type`, etc.) |
| Python    | Chef   | 5            | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |
| Python    | Chef   | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`temp_discount_code`, `temp_order_note`) used only under specific conditions |
| Python    | Chef   | 7            | Object-Orientation Abusers | Refused Bequest            | refused_bequest                 | Method is meant for inheritance but is empty |
| Python    | Chef   | 8            | Change Preventers          | Shotgun Surgery           | update_contact_info            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Python    | Chef   | 9            | Change Preventers          | Shotgun Surgery           | update_name                     | Splitting name updates across different methods instead of a single encapsulated update |
| Python    | Chef   | 10           | Change Preventers          | Shotgun Surgery           | update_address                  | Similar to `update_name`, updates should be encapsulated |
| Python    | Chef   | 11           | Change Preventers          | Shotgun Surgery           | update_phone_number             | Separate field update that contributes to shotgun surgery |
| Python    | Chef   | 12           | Change Preventers          | Shotgun Surgery           | update_email                    | Separate field update that contributes to shotgun surgery |
| Python    | Chef   | 13           | Change Preventers          | Divergent Change          | notify_for_promotion            | Multiple notification methods each handling separate concerns |
| Python    | Chef   | 14           | Change Preventers          | Divergent Change          | notify_for_discount             | Related to `notify_for_promotion`, but managed separately |
| Python    | Chef   | 15           | Change Preventers          | Divergent Change          | notify_for_new_arrivals         | Another notification method that should be unified |
| Python    | Chef   | 16           | Change Preventers          | Parallel Inheritance Hierarchies | apply_discount              | Parallel implementation of discount and loyalty points logic |
| Python    | Chef   | 17           | Change Preventers          | Parallel Inheritance Hierarchies | apply_loyalty_points        | Another parallel logic similar to `apply_discount` |
| Python    | Chef   | 18           | Dispensables               | Speculative Generality     | ask_for_receipt                 | Method is present but never used in any flow |
| Python    | Chef   | 19           | Dispensables               | Dead Code                  | another_unused_method           | Unused method that can be removed |
| Python    | Chef   | 20           | Dispensables               | Dead Code                  | yet_another_unused_method       | Another unused method |
| Python    | Chef   | 21           | Dispensables               | Duplicate Code             | duplicate_method                | Repeated functionality with identical operations on the same attribute |
| Python    | Chef   | 22           | Couplers                   | Inappropriate Intimacy     | access_internal_details         | Accesses internal details of the `Pizza` object directly |
| Python    | Chef   | 23           | Couplers                   | Message Chains             | chain_of_methods                | Excessive method chaining (`self.clean_kitchen()`) |
| Python    | Chef   | 24           | Couplers                   | Middle Man                 | middleman_method                | Delegates work without adding value |
| Python    | Chef   | 25           | Bloaters                   | Long Method                | long_method                     | Performs multiple actions in a single method, reducing readability |

| Language  | Class   | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Python    | Cashier | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: order taking, complaints, discounts, customer contact, and deliveries |
| Python    | Cashier | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`bool`) for `frequent_customer_discount` instead of a more expressive construct |
| Python    | Cashier | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`first_name`, `last_name`, `address`, `phone_number`, `email`) should be encapsulated |
| Python    | Cashier | 4            | Bloaters                   | Long Parameter List        | order_with_unnecessary_details | Method receives multiple unrelated parameters (`pizza_type`, `size`, `crust_type`, etc.) |
| Python    | Cashier | 5            | Object-Orientation Abusers | Switch Statements          | handle_complaint                | Overuse of if-else statements to handle different complaints |
| Python    | Cashier | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`temp_discount_code`, `temp_order_note`) used only under specific conditions |
| Python    | Cashier | 7            | Object-Orientation Abusers | Refused Bequest            | refused_bequest                 | Method is meant for inheritance but is empty |
| Python    | Cashier | 8            | Change Preventers          | Shotgun Surgery           | update_contact_info            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Python    | Cashier | 9            | Change Preventers          | Shotgun Surgery           | update_name                     | Splitting name updates across different methods instead of a single encapsulated update |
| Python    | Cashier | 10           | Change Preventers          | Shotgun Surgery           | update_address                  | Similar to `update_name`, updates should be encapsulated |
| Python    | Cashier | 11           | Change Preventers          | Shotgun Surgery           | update_phone_number             | Separate field update that contributes to shotgun surgery |
| Python    | Cashier | 12           | Change Preventers          | Shotgun Surgery           | update_email                    | Separate field update that contributes to shotgun surgery |
| Python    | Cashier | 13           | Change Preventers          | Divergent Change          | notify_for_promotion            | Multiple notification methods each handling separate concerns |
| Python    | Cashier | 14           | Change Preventers          | Divergent Change          | notify_for_discount             | Related to `notify_for_promotion`, but managed separately |
| Python    | Cashier | 15           | Change Preventers          | Divergent Change          | notify_for_new_arrivals         | Another notification method that should be unified |
| Python    | Cashier | 16           | Change Preventers          | Parallel Inheritance Hierarchies | apply_discount              | Parallel implementation of discount and loyalty points logic |
| Python    | Cashier | 17           | Change Preventers          | Parallel Inheritance Hierarchies | apply_loyalty_points        | Another parallel logic similar to `apply_discount` |
| Python    | Cashier | 18           | Dispensables               | Speculative Generality     | ask_for_receipt                 | Method is present but never used in any flow |
| Python    | Cashier | 19           | Dispensables               | Dead Code                  | another_unused_method           | Unused method that can be removed |
| Python    | Cashier | 20           | Dispensables               | Dead Code                  | yet_another_unused_method       | Another unused method |
| Python    | Cashier | 21           | Dispensables               | Duplicate Code             | duplicate_method                | Repeated functionality with identical operations on the same attribute |
| Python    | Cashier | 22           | Couplers                   | Feature Envy               | take_order                      | Excessive reliance on another class (`chef`) for core functionality |
| Python    | Cashier | 23           | Couplers                   | Inappropriate Intimacy     | calm_customer_down              | Accessing internal methods of `chef` (`clean_kitchen()`) |
| Python    | Cashier | 24           | Couplers                   | Message Chains             | chain_of_methods                | Excessive method chaining (`self.chef.clean_kitchen()`) |
| Python    | Cashier | 25           | Couplers                   | Middle Man                 | middleman_method                | Delegates work without adding value |
| Python    | Cashier | 26           | Bloaters                   | Long Method                | long_method                     | Performs multiple actions in a single method, reducing readability |

| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Shop   | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: order processing, customer contact updates, notifications, and discounts |
| Java      | Shop   | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| Java      | Shop   | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| Java      | Shop   | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Shop   | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Shop   | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Shop   | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| Java      | Shop   | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| Java      | Shop   | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| Java      | Shop   | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Shop   | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Shop   | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Shop   | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Shop   | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Shop   | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Shop   | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |

| Language  | Class         | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|-------------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Pizza       | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: pizza properties, customer info, notifications, and complaints |
| Java      | Pizza       | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `extraCheese` instead of a more expressive construct |
| Java      | Pizza       | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`customerFirstName`, `customerLastName`, `customerAddress`, etc.) should be encapsulated |
| Java      | Pizza       | 4            | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails     | Method receives multiple unrelated parameters (`pizzaType`, `size`, `crustType`, etc.) |
| Java      | Pizza       | 5            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Pizza       | 6            | Object-Orientation Abusers | Temporary Field            | __init__                        | Fields (`tempDiscountCode`, `tempOrderNote`) used only under specific conditions |
| Java      | Pizza       | 7            | Change Preventers          | Shotgun Surgery           | updateCustomerInfo              | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Pizza       | 8            | Change Preventers          | Shotgun Surgery           | updateCustomerName              | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Pizza       | 9            | Change Preventers          | Shotgun Surgery           | updateCustomerAddress           | Similar to `updateCustomerName`, updates should be encapsulated |
| Java      | Pizza       | 10           | Change Preventers          | Shotgun Surgery           | updateCustomerPhoneNumber       | Separate field update that contributes to shotgun surgery |
| Java      | Pizza       | 11           | Change Preventers          | Shotgun Surgery           | updateCustomerEmail             | Separate field update that contributes to shotgun surgery |
| Java      | Pizza       | 12           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Pizza       | 13           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Pizza       | 14           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Pizza       | 15           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Pizza       | 16           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Pizza       | 17           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Pizza       | 18           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| Java      | Pizza       | 19           | Dispensables               | Dead Code                  | yetAnotherUnusedMethod          | Another unused method |
| Java      | Pizza       | 20           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |
| Java      | Pizza       | 21           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.updateCustomerAddress("123 Street")`) |
| Java      | Pizza       | 22           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| Java      | Pizza       | 23           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accesses internal attributes (`this.size`, `this.doughType`, `this.topping`) |
| Java      | Pizza       | 24           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| Java      | CheesePizza | 25           | Object-Orientation Abusers | Refused Bequest            | __init__                        | Subclass inherits but does not use `cheeseType` |
| Java      | CheesePizza | 26           | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |

| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Drink  | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: drink properties, customer info, notifications, and complaints |
| Java      | Drink  | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `isLargeSize` instead of a more expressive construct |
| Java      | Drink  | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`customerFirstName`, `customerLastName`, `customerAddress`, etc.) should be encapsulated |
| Java      | Drink  | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Drink  | 5            | Change Preventers          | Shotgun Surgery           | updateCustomerInfo              | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Drink  | 6            | Change Preventers          | Shotgun Surgery           | updateCustomerName              | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Drink  | 7            | Change Preventers          | Shotgun Surgery           | updateCustomerAddress           | Similar to `updateCustomerName`, updates should be encapsulated |
| Java      | Drink  | 8            | Change Preventers          | Shotgun Surgery           | updateCustomerPhoneNumber       | Separate field update that contributes to shotgun surgery |
| Java      | Drink  | 9            | Change Preventers          | Shotgun Surgery           | updateCustomerEmail             | Separate field update that contributes to shotgun surgery |
| Java      | Drink  | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Drink  | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Drink  | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Drink  | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Drink  | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Drink  | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Drink  | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| Java      | Drink  | 17           | Dispensables               | Dead Code                  | yetAnotherUnusedMethod          | Another unused method |
| Java      | Drink  | 18           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |
| Java      | Drink  | 19           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.updateCustomerAddress("456 Avenue")`) |
| Java      | Drink  | 20           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| Java      | Drink  | 21           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accesses internal attributes (`this.drinkType`) |
| Java      | Drink  | 22           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |

| Language  | Class     | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|----------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Customer | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: ordering, complaints, contact updates, notifications, and discounts |
| Java      | Customer | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| Java      | Customer | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| Java      | Customer | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Customer | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Customer | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Customer | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| Java      | Customer | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| Java      | Customer | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| Java      | Customer | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Customer | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Customer | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Customer | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Customer | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Customer | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Customer | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| Java      | Customer | 17           | Couplers                   | Feature Envy               | orderPizza                      | Excessive reliance on another class (`pizzaShop`) for core functionality |
| Java      | Customer | 18           | Couplers                   | Inappropriate Intimacy     | complain                         | Accessing another object's internal details (`pizzaShop.getCashier().calmCustomerDown()`) |
| Java      | Customer | 19           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`pizzaShop.getCashier().getChef().cleanKitchen()`) |
| Java      | Customer | 20           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| Java      | Customer | 21           | Bloaters                   | Long Method                | longComplaintMethod             | Performs multiple actions in a single method, reducing readability |
| Java      | Customer | 22           | Dispensables               | Duplicate Code             | duplicateComplaint              | Repeated functionality with identical operations on the same attribute |

| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Chef   | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: baking, delivering, cleaning, notifications, complaints, and discounts |
| Java      | Chef   | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `extraCheese` instead of a more expressive construct |
| Java      | Chef   | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped chef details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| Java      | Chef   | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Chef   | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Chef   | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Chef   | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| Java      | Chef   | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| Java      | Chef   | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| Java      | Chef   | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Chef   | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Chef   | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Chef   | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Chef   | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Chef   | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Chef   | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| Java      | Chef   | 17           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`this.pizza.getTopping()`) |
| Java      | Chef   | 18           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.cleanKitchen()`) |
| Java      | Chef   | 19           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| Java      | Chef   | 20           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| Java      | Chef   | 21           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |

| Language  | Class   | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| Java      | Cashier | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: order taking, complaints, discounts, customer contact, and deliveries |
| Java      | Cashier | 2            | Bloaters                   | Primitive Obsession        | __init__                        | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| Java      | Cashier | 3            | Bloaters                   | Data Clumps                | __init__                        | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| Java      | Cashier | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| Java      | Cashier | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| Java      | Cashier | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| Java      | Cashier | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| Java      | Cashier | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| Java      | Cashier | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| Java      | Cashier | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| Java      | Cashier | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| Java      | Cashier | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| Java      | Cashier | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| Java      | Cashier | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| Java      | Cashier | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| Java      | Cashier | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| Java      | Cashier | 17           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`chef.isBusy()`) |
| Java      | Cashier | 18           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.chef.cleanKitchen()`) |
| Java      | Cashier | 19           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| Java      | Cashier | 20           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| Java      | Cashier | 21           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |

| Language  | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|-----------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| JavaScript | Shop  | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: order processing, customer contact updates, notifications, and discounts |
| JavaScript | Shop  | 2            | Bloaters                   | Primitive Obsession        | constructor                     | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| JavaScript | Shop  | 3            | Bloaters                   | Data Clumps                | constructor                     | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| JavaScript | Shop  | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| JavaScript | Shop  | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| JavaScript | Shop  | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| JavaScript | Shop  | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| JavaScript | Shop  | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| JavaScript | Shop  | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| JavaScript | Shop  | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| JavaScript | Shop  | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| JavaScript | Shop  | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| JavaScript | Shop  | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| JavaScript | Shop  | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| JavaScript | Shop  | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| JavaScript | Shop  | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| JavaScript | Shop  | 17           | Dispensables               | Dead Code                  | yetAnotherUnusedMethod          | Another unused method |
| JavaScript | Shop  | 18           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.casher.chef.cleanKitchen()`) |
| JavaScript | Shop  | 19           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| JavaScript | Shop  | 20           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`this.casher.chef.busy`) |
| JavaScript | Shop  | 21           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| JavaScript | Shop  | 22           | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails     | Method receives multiple unrelated parameters |

| Language   | Class         | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|------------|-------------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| JavaScript | Pizza       | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: pizza properties, customer info, notifications, and complaints |
| JavaScript | Pizza       | 2            | Bloaters                   | Primitive Obsession        | constructor                     | Using a primitive (`boolean`) for `extraCheese` instead of a more expressive construct |
| JavaScript | Pizza       | 3            | Bloaters                   | Data Clumps                | constructor                     | Grouped customer details (`customerFirstName`, `customerLastName`, `customerAddress`, etc.) should be encapsulated |
| JavaScript | Pizza       | 4            | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails     | Method receives multiple unrelated parameters (`pizzaType`, `size`, `crustType`, etc.) |
| JavaScript | Pizza       | 5            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| JavaScript | Pizza       | 6            | Object-Orientation Abusers | Temporary Field            | constructor                     | Fields (`tempDiscountCode`, `tempOrderNote`) used only under specific conditions |
| JavaScript | Pizza       | 7            | Change Preventers          | Shotgun Surgery           | updateCustomerInfo              | Multiple update methods modifying individual fields instead of a single encapsulated update |
| JavaScript | Pizza       | 8            | Change Preventers          | Shotgun Surgery           | updateCustomerName              | Splitting name updates across different methods instead of a single encapsulated update |
| JavaScript | Pizza       | 9            | Change Preventers          | Shotgun Surgery           | updateCustomerAddress           | Similar to `updateCustomerName`, updates should be encapsulated |
| JavaScript | Pizza       | 10           | Change Preventers          | Shotgun Surgery           | updateCustomerPhoneNumber       | Separate field update that contributes to shotgun surgery |
| JavaScript | Pizza       | 11           | Change Preventers          | Shotgun Surgery           | updateCustomerEmail             | Separate field update that contributes to shotgun surgery |
| JavaScript | Pizza       | 12           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| JavaScript | Pizza       | 13           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| JavaScript | Pizza       | 14           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| JavaScript | Pizza       | 15           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| JavaScript | Pizza       | 16           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| JavaScript | Pizza       | 17           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| JavaScript | Pizza       | 18           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| JavaScript | Pizza       | 19           | Dispensables               | Dead Code                  | yetAnotherUnusedMethod          | Another unused method |
| JavaScript | Pizza       | 20           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |
| JavaScript | Pizza       | 21           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.updateCustomerAddress("123 Street")`) |
| JavaScript | Pizza       | 22           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| JavaScript | Pizza       | 23           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`this.size`, `this.doughType`, `this.topping`) |
| JavaScript | Pizza       | 24           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| JavaScript | CheesePizza | 25           | Object-Orientation Abusers | Refused Bequest            | constructor                     | Subclass inherits but does not use `cheeseType` |
| JavaScript | CheesePizza | 26           | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |

| Language   | Class  | Code Smell # | Category     | Code Smell           | Method          | Type                                                                 |
|------------|--------|--------------|--------------|----------------------|-----------------|----------------------------------------------------------------------|
| JavaScript | Drink  | 1            | Dispensables | Data Class           | Entire Class    | Class only stores data (`drinkType`) without meaningful behavior |
| JavaScript | Drink  | 2            | Bloaters     | Primitive Obsession  | createOrder     | Uses a primitive (`string`) instead of a more expressive object for drink type |
| JavaScript | Drink  | 3            | Bloaters     | Primitive Obsession  | addToOrder      | Uses a primitive (`string`) instead of an object for order processing |
| JavaScript | Drink  | 4            | Bloaters     | Primitive Obsession  | confirmOrder    | Uses a primitive (`string`) instead of an object for order confirmation |

| Language   | Class     | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|------------|----------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| JavaScript | Customer | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: ordering, complaints, contact updates, notifications, and discounts |
| JavaScript | Customer | 2            | Bloaters                   | Primitive Obsession        | constructor                     | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| JavaScript | Customer | 3            | Bloaters                   | Data Clumps                | constructor                     | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| JavaScript | Customer | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| JavaScript | Customer | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| JavaScript | Customer | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| JavaScript | Customer | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| JavaScript | Customer | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| JavaScript | Customer | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| JavaScript | Customer | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| JavaScript | Customer | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| JavaScript | Customer | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| JavaScript | Customer | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| JavaScript | Customer | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| JavaScript | Customer | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| JavaScript | Customer | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| JavaScript | Customer | 17           | Couplers                   | Feature Envy               | orderPizza                      | Excessive reliance on another class (`Shop`) for core functionality |
| JavaScript | Customer | 18           | Couplers                   | Inappropriate Intimacy     | complain                         | Accessing another object's internal details (`Shop.casher.cleanKitchen()`) |
| JavaScript | Customer | 19           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`Shop.casher.chef.cleanKitchen()`) |
| JavaScript | Customer | 20           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| JavaScript | Customer | 21           | Bloaters                   | Long Method                | longComplaintMethod             | Performs multiple actions in a single method, reducing readability |
| JavaScript | Customer | 22           | Dispensables               | Duplicate Code             | duplicateComplaint              | Repeated functionality with identical operations on the same attribute |

| Language   | Class  | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|------------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| JavaScript | Chef   | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: baking, delivering, cleaning, notifications, complaints, and discounts |
| JavaScript | Chef   | 2            | Bloaters                   | Primitive Obsession        | constructor                     | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| JavaScript | Chef   | 3            | Bloaters                   | Data Clumps                | constructor                     | Grouped chef details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| JavaScript | Chef   | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| JavaScript | Chef   | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| JavaScript | Chef   | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| JavaScript | Chef   | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| JavaScript | Chef   | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| JavaScript | Chef   | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| JavaScript | Chef   | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| JavaScript | Chef   | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| JavaScript | Chef   | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| JavaScript | Chef   | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| JavaScript | Chef   | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| JavaScript | Chef   | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| JavaScript | Chef   | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| JavaScript | Chef   | 17           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`this.pizza`) |
| JavaScript | Chef   | 18           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.cleanKitchen()`) |
| JavaScript | Chef   | 19           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| JavaScript | Chef   | 20           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| JavaScript | Chef   | 21           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |

| Language   | Class   | Code Smell # | Category                   | Code Smell                 | Method                          | Type                                                                 |
|------------|--------|--------------|----------------------------|----------------------------|--------------------------------|----------------------------------------------------------------------|
| JavaScript | Cashier | 1            | Bloaters                   | Large Class                | Entire Class                    | The class handles multiple responsibilities: order taking, complaints, discounts, customer contact, and deliveries |
| JavaScript | Cashier | 2            | Bloaters                   | Primitive Obsession        | constructor                     | Using a primitive (`boolean`) for `frequentCustomerDiscount` instead of a more expressive construct |
| JavaScript | Cashier | 3            | Bloaters                   | Data Clumps                | constructor                     | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| JavaScript | Cashier | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint                 | Overuse of if-else statements to handle different complaints |
| JavaScript | Cashier | 5            | Change Preventers          | Shotgun Surgery           | updateContactInfo               | Multiple update methods modifying individual fields instead of a single encapsulated update |
| JavaScript | Cashier | 6            | Change Preventers          | Shotgun Surgery           | updateName                      | Splitting name updates across different methods instead of a single encapsulated update |
| JavaScript | Cashier | 7            | Change Preventers          | Shotgun Surgery           | updateAddress                   | Similar to `updateName`, updates should be encapsulated |
| JavaScript | Cashier | 8            | Change Preventers          | Shotgun Surgery           | updatePhoneNumber               | Separate field update that contributes to shotgun surgery |
| JavaScript | Cashier | 9            | Change Preventers          | Shotgun Surgery           | updateEmail                     | Separate field update that contributes to shotgun surgery |
| JavaScript | Cashier | 10           | Change Preventers          | Divergent Change          | notifyForPromotion              | Multiple notification methods each handling separate concerns |
| JavaScript | Cashier | 11           | Change Preventers          | Divergent Change          | notifyForDiscount               | Related to `notifyForPromotion`, but managed separately |
| JavaScript | Cashier | 12           | Change Preventers          | Divergent Change          | notifyForNewArrivals            | Another notification method that should be unified |
| JavaScript | Cashier | 13           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount              | Parallel implementation of discount and loyalty points logic |
| JavaScript | Cashier | 14           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints        | Another parallel logic similar to `applyDiscount` |
| JavaScript | Cashier | 15           | Dispensables               | Speculative Generality     | askForReceipt                   | Method is present but never used in any flow |
| JavaScript | Cashier | 16           | Dispensables               | Dead Code                  | anotherUnusedMethod             | Unused method that can be removed |
| JavaScript | Cashier | 17           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails           | Accessing internal attributes (`this.chef.busy`) |
| JavaScript | Cashier | 18           | Couplers                   | Message Chains             | chainOfMethods                  | Excessive method chaining (`this.chef.cleanKitchen()`) |
| JavaScript | Cashier | 19           | Couplers                   | Middle Man                 | middlemanMethod                 | Delegates work without adding value |
| JavaScript | Cashier | 20           | Bloaters                   | Long Method                | longMethod                      | Performs multiple actions in a single method, reducing readability |
| JavaScript | Cashier | 21           | Dispensables               | Duplicate Code             | duplicateMethod                 | Repeated functionality with identical operations on the same attribute |

| Language | Class  | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|--------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Shop   | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: order processing, cashier interactions, and pizza creation |
| C++      | Shop   | 2            | Object-Orientation Abusers | Switch Statements          | createPizza                   | Overuse of if-else statements to create different pizza types |
| C++      | Shop   | 3            | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing internal attributes of `Cashier` (`cashier->getChef()->isBusy()`) |
| C++      | Shop   | 4            | Change Preventers          | Divergent Change           | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Shop   | 5            | Change Preventers          | Divergent Change           | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Shop   | 6            | Change Preventers          | Divergent Change           | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Shop   | 7            | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Shop   | 8            | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Shop   | 9            | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Shop   | 10           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Shop   | 11           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`cashier->getChef()->cleanKitchen()`) |
| C++      | Shop   | 12           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Shop   | 13           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |
| C++      | Shop   | 14           | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails   | Method receives multiple unrelated parameters |

| Language | Class         | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|-------------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Pizza       | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: pizza properties, customer info, notifications, and complaints |
| C++      | Pizza       | 2            | Bloaters                   | Primitive Obsession        | Constructor                    | Using a primitive (`bool`) for `extraCheese` instead of a more expressive construct |
| C++      | Pizza       | 3            | Bloaters                   | Data Clumps                | Constructor                    | Grouped customer details (`customerFirstName`, `customerLastName`, `customerAddress`, etc.) should be encapsulated |
| C++      | Pizza       | 4            | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails   | Method receives multiple unrelated parameters (`pizzaType`, `size`, `crustType`, etc.) |
| C++      | Pizza       | 5            | Object-Orientation Abusers | Switch Statements          | handleComplaint               | Overuse of if-else statements to handle different complaints |
| C++      | Pizza       | 6            | Object-Orientation Abusers | Temporary Field            | Constructor                    | Fields (`tempDiscountCode`, `tempOrderNote`) used only under specific conditions |
| C++      | Pizza       | 7            | Change Preventers          | Shotgun Surgery           | updateCustomerInfo            | Multiple update methods modifying individual fields instead of a single encapsulated update |
| C++      | Pizza       | 8            | Change Preventers          | Shotgun Surgery           | updateCustomerName            | Splitting name updates across different methods instead of a single encapsulated update |
| C++      | Pizza       | 9            | Change Preventers          | Shotgun Surgery           | updateCustomerAddress         | Similar to `updateCustomerName`, updates should be encapsulated |
| C++      | Pizza       | 10           | Change Preventers          | Shotgun Surgery           | updateCustomerPhoneNumber     | Separate field update that contributes to shotgun surgery |
| C++      | Pizza       | 11           | Change Preventers          | Shotgun Surgery           | updateCustomerEmail           | Separate field update that contributes to shotgun surgery |
| C++      | Pizza       | 12           | Change Preventers          | Divergent Change          | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Pizza       | 13           | Change Preventers          | Divergent Change          | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Pizza       | 14           | Change Preventers          | Divergent Change          | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Pizza       | 15           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Pizza       | 16           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Pizza       | 17           | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Pizza       | 18           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Pizza       | 19           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`updateCustomerAddress("123 Street")`) |
| C++      | Pizza       | 20           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Pizza       | 21           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing internal attributes (`size`, `doughType`, `topping`) |
| C++      | Pizza       | 22           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |
| C++      | CheesePizza | 23           | Object-Orientation Abusers | Refused Bequest            | Constructor                    | Subclass inherits but does not use `cheeseType` |

| Language | Class  | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|--------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Drink  | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: drink properties, customer info, promotions, and complaints |
| C++      | Drink  | 2            | Bloaters                   | Primitive Obsession        | Constructor                    | Using primitive (`bool`) for `ice` and `lemon` instead of a more expressive construct |
| C++      | Drink  | 3            | Bloaters                   | Data Clumps                | Constructor                    | Grouped customer details (`customerFirstName`, `customerLastName`, `customerAddress`, etc.) should be encapsulated |
| C++      | Drink  | 4            | Bloaters                   | Long Parameter List        | orderWithUnnecessaryDetails   | Method receives multiple unrelated parameters (`drinkType`, `size`, `ice`, `lemon`, `discountCode`) |
| C++      | Drink  | 5            | Object-Orientation Abusers | Switch Statements          | handleComplaint               | Overuse of if-else statements to handle different complaints |
| C++      | Drink  | 6            | Object-Orientation Abusers | Temporary Field            | Constructor                    | Fields (`tempDiscountCode`, `tempOrderNote`) used only under specific conditions |
| C++      | Drink  | 7            | Change Preventers          | Divergent Change           | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Drink  | 8            | Change Preventers          | Divergent Change           | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Drink  | 9            | Change Preventers          | Divergent Change           | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Drink  | 10           | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Drink  | 11           | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Drink  | 12           | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Drink  | 13           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Drink  | 14           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`cleanup()`) |
| C++      | Drink  | 15           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Drink  | 16           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing internal attributes (`size`, `drinkType`) |
| C++      | Drink  | 17           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |

| Language | Class     | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|----------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Customer | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: ordering, complaints, contact updates, notifications, and discounts |
| C++      | Customer | 2            | Bloaters                   | Primitive Obsession        | Constructor                    | Using a primitive (`bool`) for `frequentCustomerDiscount` instead of a more expressive construct |
| C++      | Customer | 3            | Bloaters                   | Data Clumps                | Constructor                    | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| C++      | Customer | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint               | Overuse of if-else statements to handle different complaints |
| C++      | Customer | 5            | Change Preventers          | Divergent Change           | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Customer | 6            | Change Preventers          | Divergent Change           | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Customer | 7            | Change Preventers          | Divergent Change           | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Customer | 8            | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Customer | 9            | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Customer | 10           | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Customer | 11           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Customer | 12           | Couplers                   | Feature Envy               | orderPizza                    | Excessive reliance on another class (`pizzaShop`) for core functionality |
| C++      | Customer | 13           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing another object's internal details (`pizzaShop->getCashier()->hurryUpChef()`) |
| C++      | Customer | 14           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`pizzaShop->getCashier()->hurryUpChef()`) |
| C++      | Customer | 15           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Customer | 16           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |
| C++      | Customer | 17           | Dispensables               | Duplicate Code             | duplicateMethod               | Repeated functionality with identical operations on the same attribute |

| Language | Class  | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|--------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Chef   | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: baking, delivering, cleaning, notifications, complaints, and discounts |
| C++      | Chef   | 2            | Bloaters                   | Primitive Obsession        | Constructor                    | Using a primitive (`bool`) for `extraCheese` instead of a more expressive construct |
| C++      | Chef   | 3            | Bloaters                   | Data Clumps                | Constructor                    | Grouped chef details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| C++      | Chef   | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint               | Overuse of if-else statements to handle different complaints |
| C++      | Chef   | 5            | Change Preventers          | Divergent Change           | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Chef   | 6            | Change Preventers          | Divergent Change           | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Chef   | 7            | Change Preventers          | Divergent Change           | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Chef   | 8            | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Chef   | 9            | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Chef   | 10           | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Chef   | 11           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Chef   | 12           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing another object's internal details (`this->pizza->getTopping()`) |
| C++      | Chef   | 13           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`cleanKitchen()`) |
| C++      | Chef   | 14           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Chef   | 15           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |
| C++      | Chef   | 16           | Dispensables               | Duplicate Code             | duplicateMethod               | Repeated functionality with identical operations on the same attribute |

| Language | Class   | Code Smell # | Category                   | Code Smell                 | Method                        | Type                                                                 |
|----------|--------|--------------|----------------------------|----------------------------|-------------------------------|----------------------------------------------------------------------|
| C++      | Cashier | 1            | Bloaters                   | Large Class                | Entire Class                  | The class handles multiple responsibilities: order taking, complaints, discounts, customer contact, and deliveries |
| C++      | Cashier | 2            | Bloaters                   | Primitive Obsession        | Constructor                    | Using a primitive (`bool`) for `frequentCustomerDiscount` instead of a more expressive construct |
| C++      | Cashier | 3            | Bloaters                   | Data Clumps                | Constructor                    | Grouped customer details (`firstName`, `lastName`, `address`, `phoneNumber`, `email`) should be encapsulated |
| C++      | Cashier | 4            | Object-Orientation Abusers | Switch Statements          | handleComplaint               | Overuse of if-else statements to handle different complaints |
| C++      | Cashier | 5            | Change Preventers          | Divergent Change           | notifyForPromotion            | Multiple notification methods each handling separate concerns |
| C++      | Cashier | 6            | Change Preventers          | Divergent Change           | notifyForDiscount             | Related to `notifyForPromotion`, but managed separately |
| C++      | Cashier | 7            | Change Preventers          | Divergent Change           | notifyForNewArrivals          | Another notification method that should be unified |
| C++      | Cashier | 8            | Change Preventers          | Parallel Inheritance Hierarchies | applyDiscount             | Parallel implementation of discount and loyalty points logic |
| C++      | Cashier | 9            | Change Preventers          | Parallel Inheritance Hierarchies | applyLoyaltyPoints       | Another parallel logic similar to `applyDiscount` |
| C++      | Cashier | 10           | Dispensables               | Speculative Generality     | askForReceipt                 | Method is present but never used in any flow |
| C++      | Cashier | 11           | Dispensables               | Dead Code                  | anotherUnusedMethod           | Unused method that can be removed |
| C++      | Cashier | 12           | Couplers                   | Inappropriate Intimacy     | accessInternalDetails         | Accessing internal attributes (`chef->isBusy()`) |
| C++      | Cashier | 13           | Couplers                   | Message Chains             | chainOfMethods                | Excessive method chaining (`accessInternalDetails()`) |
| C++      | Cashier | 14           | Couplers                   | Middle Man                 | middlemanMethod               | Delegates work without adding value |
| C++      | Cashier | 15           | Bloaters                   | Long Method                | longMethod                    | Performs multiple actions in a single method, reducing readability |
| C++      | Cashier | 16           | Dispensables               | Duplicate Code             | duplicateMethod               | Repeated functionality with identical operations on the same attribute |
