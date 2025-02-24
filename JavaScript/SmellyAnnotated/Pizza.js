/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


class Pizza {
    constructor(size, doughType, topping) {
        this.size = size;
        this.doughType = doughType;
        this.topping = topping;

        // Primitive Obsession
        this.extraCheese = false;

        // Data Clumps
        this.customerFirstName = null;
        this.customerLastName = null;
        this.customerAddress = null;
        this.customerPhoneNumber = null;
        this.customerEmail = null;

        // Temporary Fields
        this.tempDiscountCode = null;
        this.tempOrderNote = null;
    }

    setSize(size) {
        this.size = size;
    }

    setDoughType(doughType) {
        this.doughType = doughType;
    }

    setTopping(topping) {
        this.topping = topping;
    }

    updateCustomerInfo(firstName, lastName, address, phoneNumber, email) {
        // Shotgun Surgery (changing multiple methods to update contact info)
        this.customerFirstName = firstName;
        this.customerLastName = lastName;
        this.customerAddress = address;
        this.customerPhoneNumber = phoneNumber;
        this.customerEmail = email;
    }

    updateCustomerName(firstName, lastName) {
        // Shotgun Surgery (separate method to update name)
        this.customerFirstName = firstName;
        this.customerLastName = lastName;
    }

    updateCustomerAddress(address) {
        // Shotgun Surgery (separate method to update address)
        this.customerAddress = address;
    }

    updateCustomerPhoneNumber(phoneNumber) {
        // Shotgun Surgery (separate method to update phone number)
        this.customerPhoneNumber = phoneNumber;
    }

    updateCustomerEmail(email) {
        // Shotgun Surgery (separate method to update email)
        this.customerEmail = email;
    }

    notifyForPromotion() {
        // Divergent Change (method to notify for promotion)
        console.log("Notifying customer for promotion");
    }

    notifyForDiscount() {
        // Divergent Change (method to notify for discount)
        console.log("Notifying customer for discount");
    }

    notifyForNewArrivals() {
        // Divergent Change (method to notify for new arrivals)
        console.log("Notifying customer for new arrivals");
    }

    applyDiscount() {
        // Parallel Inheritance Hierarchies (method to apply discount)
        console.log("Applying discount for customer");
    }

    applyLoyaltyPoints() {
        // Parallel Inheritance Hierarchies (method to apply loyalty points)
        console.log("Applying loyalty points for customer");
    }

    handleComplaint(complaint) {
        // Switch Statements (using if-else to simulate switch)
        if (complaint === "cold pizza") {
            console.log("Handling complaint: Pizza is cold");
        } else if (complaint === "late delivery") {
            console.log("Handling complaint: Pizza is late");
        } else if (complaint === "wrong order") {
            console.log("Handling complaint: Wrong pizza delivered");
        } else {
            console.log("Handling complaint: General complaint");
        }
    }

    askForReceipt() {
        console.log("Customer is asking for a receipt."); // Speculative Generality (unused method)
    }

    anotherUnusedMethod() {
        // Dead Code (method is never called)
    }

    yetAnotherUnusedMethod() {
        // More Dead Code
    }

    longMethod() {
        // Long Method (too many tasks in a single method)
        console.log("Pizza is handling many tasks in a single method");
        this.setSize("Large");
        this.setDoughType("Thin Crust");
        this.setTopping("Pepperoni");
        this.updateCustomerInfo("John", "Doe", "123 Street", "555-5555", "john.doe@example.com");
        this.notifyForPromotion();
        this.notifyForDiscount();
        this.notifyForNewArrivals();
        this.applyDiscount();
        this.applyLoyaltyPoints();
        this.handleComplaint("cold pizza");
    }

    orderWithUnnecessaryDetails(pizzaType, size, crustType, toppings, extraCheese, discountCode) {
        // Long Parameter List (too many parameters in the method)
        console.log(`Placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.setSize(size);
        this.setDoughType(crustType);
        this.setTopping(toppings);
        this.applyDiscount();
    }

    duplicateMethod() {
        // Duplicate Code (repeating functionality)
        console.log("Customer is making a duplicate order");
        this.setTopping("Cheese");
        this.setTopping("Cheese");
    }

    chainOfMethods() {
        // Message Chain (calling methods on objects returned by another method)
        console.log("Pizza is initiating a message chain");
        this.updateCustomerAddress("123 Street");
    }

    middlemanMethod() {
        // Middle Man (methods that delegate to other methods)
        console.log("Pizza is calling a middleman method");
        this.middleMethod();
    }

    middleMethod() {
        console.log("Middleman method delegating to another method");
        this.realMethod();
    }

    realMethod() {
        console.log("Real method doing the actual work");
    }

    accessInternalDetails() {
        // Inappropriate Intimacy (accessing internal details of another class)
        console.log(`Accessing internal details: ${this.size}, ${this.doughType}, ${this.topping}`);
    }

    refusedBequest() {
        // Refused Bequest (method that should be inherited but is empty)
    }
}

class CheesePizza extends Pizza {
    constructor() {
        super("Medium", "Regular", "Cheese");
        this.cheeseType = "Mozzarella"; // Refused Bequest
    }

    handleComplaint(complaint) {
        // Switch Statements (using if-else to simulate switch)
        if (complaint === "too much cheese") {
            console.log("Handling complaint: Too much cheese");
        } else {
            super.handleComplaint(complaint);
        }
    }
}

class VeggiePizza extends Pizza {
    constructor() {
        super("Medium", "Whole Wheat", "Veggies");
    }
}

class TunaPizza extends Pizza {
    constructor() {
        super("Large", "Thin Crust", "Tuna");
    }
}

class PepperoniPizza extends Pizza {
    constructor() {
        super("Large", "Regular", "Pepperoni");
    }
}

module.exports = { Pizza, CheesePizza, VeggiePizza, TunaPizza, PepperoniPizza };
