/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Cashier } = require('./Cashier');
const { Chef } = require('./Chef');
const { Pizza, CheesePizza, VeggiePizza, TunaPizza, PepperoniPizza } = require('./Pizza');

class Shop {
    constructor() {
        this.chef = new Chef();
        this.casher = new Cashier(this.chef);
        this.pizza = null;

        // Primitive Obsession
        this.frequentCustomerDiscount = false;

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

    createPizza(pizzaType) {
        if (pizzaType === "Cheese") {
            return new CheesePizza();
        } else if (pizzaType === "Veggie") {
            return new VeggiePizza();
        } else if (pizzaType === "Tuna") {
            return new TunaPizza();
        } else if (pizzaType === "Pepperoni") {
            return new PepperoniPizza();
        } else {
            throw new Error("Unknown pizza type");
        }
    }

    receiveOrder(pizzaType) {
        console.log(`Pizza Shop received order for ${pizzaType} pizza.`);
        this.pizza = this.createPizza(pizzaType);
        this.casher.takeOrder(pizzaType);
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
            this.casher.calmCustomerDown();
        } else if (complaint === "late delivery") {
            this.casher.calmCustomerDown();
        } else if (complaint === "wrong order") {
            this.casher.calmCustomerDown();
        } else {
            this.casher.calmCustomerDown();
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

    chainOfMethods() {
        // Message Chain (calling methods on objects returned by another method)
        console.log("Shop is initiating a message chain");
        this.casher.chef.cleanKitchen();
    }

    middlemanMethod() {
        // Middle Man (methods that delegate to other methods)
        console.log("Shop is calling a middleman method");
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
        console.log(`Accessing internal details: ${this.casher.chef.busy}`);
    }

    longMethod() {
        // Long Method (too many tasks in a single method)
        console.log("Shop is handling many tasks in a single method");
        this.updateContactInfo("John", "Doe", "123 Street", "555-5555", "john.doe@example.com");
        this.updateName("John", "Doe");
        this.updateAddress("123 Street");
        this.updatePhoneNumber("555-5555");
        this.updateEmail("john.doe@example.com");
        this.notifyForPromotion();
        this.notifyForDiscount();
        this.notifyForNewArrivals();
        this.applyDiscount();
        this.applyLoyaltyPoints();
        this.handleComplaint("cold pizza");
        this.askForReceipt();
        this.chainOfMethods();
        this.middlemanMethod();
        this.accessInternalDetails();
    }

    orderWithUnnecessaryDetails() {
        // Long Parameter List (too many parameters in the method)
        console.log("Shop is placing a detailed order");
        this.receiveOrder("Veggie");
        this.updateContactInfo("John", "Doe", "123 Street", "555-5555", "john.doe@example.com");
        this.applyDiscount();
        this.applyLoyaltyPoints();
    }
}

module.exports = { Shop };
