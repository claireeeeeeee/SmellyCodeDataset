/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Pizza } = require('./Pizza');

class Chef {
    constructor() {
        this.pizza = null;
        this.busy = false;
        this.completedOrders = 0;
        this.breaksTaken = 0;
        this.kitchenClean = true;
        this.frequentCustomerDiscount = false;
        this.firstName = null;
        this.lastName = null;
        this.address = null;
        this.phoneNumber = null;
        this.email = null;
        this.tempDiscountCode = null;
        this.tempOrderNote = null;
    }

    bakePizza(pizzaType) {
        console.log(`Chef is baking ${pizzaType} pizza.`);
        this.pizza = new Pizza("Unknown", "Unknown", pizzaType);
        this.cutPizzaAndPutInBox();
    }

    cutPizzaAndPutInBox() {
        console.log(`Chef is cutting the ${this.pizza.topping} pizza and putting it in a box.`);
        this.deliverPizza();
    }

    deliverPizza() {
        console.log("Chef is delivering the pizza to the cashier.");
    }

    hurryUp() {
        console.log("Chef is hurrying up.");
    }

    cleanKitchen() {
        console.log("Chef is cleaning the kitchen.");
        this.kitchenClean = true;
    }

    updateContactInfo(firstName, lastName, address, phoneNumber, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    updateName(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    updateAddress(address) {
        this.address = address;
    }

    updatePhoneNumber(phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    updateEmail(email) {
        this.email = email;
    }

    notifyForPromotion() {
        console.log("Notifying customer for promotion");
    }

    notifyForDiscount() {
        console.log("Notifying customer for discount");
    }

    notifyForNewArrivals() {
        console.log("Notifying customer for new arrivals");
    }

    applyDiscount() {
        console.log("Applying discount for customer");
    }

    applyLoyaltyPoints() {
        console.log("Applying loyalty points for customer");
    }

    handleComplaint(complaint) {
        if (complaint === "cold pizza") {
            this.cleanKitchen();
        } else if (complaint === "late delivery") {
            this.cleanKitchen();
        } else if (complaint === "wrong order") {
            this.cleanKitchen();
        } else {
            this.cleanKitchen();
        }
    }

    askForReceipt() {
        console.log("Customer is asking for a receipt.");
    }

    anotherUnusedMethod() {
    }

    yetAnotherUnusedMethod() {
    }

    longMethod() {
        console.log("Chef is handling many tasks in a single method");
        this.bakePizza("Cheese");
        this.cutPizzaAndPutInBox();
        this.deliverPizza();
        this.hurryUp();
        this.cleanKitchen();
        this.updateContactInfo("John", "Doe", "123 Street", "555-5555", "john.doe@example.com");
        this.notifyForPromotion();
        this.notifyForDiscount();
        this.notifyForNewArrivals();
        this.applyDiscount();
        this.applyLoyaltyPoints();
        this.handleComplaint("cold pizza");
    }

    orderWithUnnecessaryDetails(pizzaType, size, crustType, toppings, extraCheese, discountCode) {
        console.log(`Placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.bakePizza(pizzaType);
        this.applyDiscount(discountCode);
        this.deliverPizza();
    }

    duplicateMethod() {
        console.log("Customer is making a duplicate order");
        this.bakePizza("Cheese");
        this.bakePizza("Cheese");
    }

    chainOfMethods() {
        console.log("Chef is initiating a message chain");
        this.cleanKitchen();
    }

    middlemanMethod() {
        console.log("Chef is calling a middleman method");
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
        console.log(`Accessing internal details: ${this.pizza}`);
    }

    refusedBequest() {
    }
}

module.exports = { Chef };
