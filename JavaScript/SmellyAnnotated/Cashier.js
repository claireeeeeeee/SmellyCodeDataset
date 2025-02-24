/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Pizza } = require('./Pizza');

class Cashier {
    constructor(chef) {
        this.chef = chef; // Control Coupling
        this.frequentCustomerDiscount = false; // Primitive Obsession

        // Data Clumps
        this.firstName = null;
        this.lastName = null;
        this.address = null;
        this.phoneNumber = null;
        this.email = null;

        // Temporary Fields
        this.tempDiscountCode = null;
        this.tempOrderNote = null;
    }

    takeOrder(pizzaType) {
        console.log(`Cashier is taking order for ${pizzaType} pizza.`);
        this.chef.bakePizza(pizzaType); // Feature Envy
    }

    hurryUpChef() {
        console.log("Cashier is hurrying up the chef.");
        this.chef.hurryUp();
    }

    calmCustomerDown() {
        console.log("Cashier is calming the customer down.");
        this.chef.cleanKitchen(); // Inappropriate Intimacy
    }

    deliverPizzaToCustomer() {
        console.log("Cashier is delivering pizza to the customer.");
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
        console.log("Cashier is handling many tasks in a single method");
        this.takeOrder("Cheese");
        this.hurryUpChef();
        this.calmCustomerDown();
        this.deliverPizzaToCustomer();
        this.askForReceipt();
    }

    orderWithUnnecessaryDetails(pizzaType, size, crustType, toppings, extraCheese, discountCode) {
        // Long Parameter List (too many parameters in the method)
        console.log(`Placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.takeOrder(pizzaType);
        this.applyDiscount(discountCode);
        this.deliverPizzaToCustomer();
    }

    duplicateMethod() {
        // Duplicate Code (repeating functionality)
        console.log("Customer is making a duplicate order");
        this.takeOrder("Cheese");
        this.takeOrder("Cheese");
    }

    chainOfMethods() {
        // Message Chain (calling methods on objects returned by another method)
        console.log("Cashier is initiating a message chain");
        this.chef.cleanKitchen();
    }

    middlemanMethod() {
        // Middle Man (methods that delegate to other methods)
        console.log("Cashier is calling a middleman method");
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
        console.log(`Accessing internal details: ${this.chef.busy}`);
    }

    updateContactInfo(firstName, lastName, address, phoneNumber, email) {
        // Shotgun Surgery (changing multiple methods to update contact info)
        this.firstName = firstName;
        this.lastName = lastName;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    updateName(firstName, lastName) {
        // Shotgun Surgery (separate method to update name)
        this.firstName = firstName;
        this.lastName = lastName;
    }

    updateAddress(address) {
        // Shotgun Surgery (separate method to update address)
        this.address = address;
    }

    updatePhoneNumber(phoneNumber) {
        // Shotgun Surgery (separate method to update phone number)
        this.phoneNumber = phoneNumber;
    }

    updateEmail(email) {
        // Shotgun Surgery (separate method to update email)
        this.email = email;
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

    applyDiscount(discountCode) {
        // Parallel Inheritance Hierarchies (method to apply discount)
        console.log(`Applying discount for customer with code ${discountCode}`);
    }

    applyLoyaltyPoints() {
        // Parallel Inheritance Hierarchies (method to apply loyalty points)
        console.log("Applying loyalty points for customer");
    }

    handleComplaint(complaint) {
        // Switch Statements (using if-else to simulate switch)
        if (complaint === "cold pizza") {
            this.calmCustomerDown();
        } else if (complaint === "late delivery") {
            this.calmCustomerDown();
        } else if (complaint === "wrong order") {
            this.calmCustomerDown();
        } else {
            this.calmCustomerDown();
        }
    }

    refusedBequest() {
        // Refused Bequest (method that should be inherited but is empty)
    }
}

module.exports = { Cashier };
