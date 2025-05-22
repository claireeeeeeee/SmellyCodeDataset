/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Pizza } = require('./Pizza');

class Cashier {
    constructor(chef) {
        this.chef = chef;
        this.frequentCustomerDiscount = false;
        this.firstName = null;
        this.lastName = null;
        this.address = null;
        this.phoneNumber = null;
        this.email = null;
        this.tempDiscountCode = null;
        this.tempOrderNote = null;
    }

    takeOrder(pizzaType) {
        console.log(`Cashier is taking order for ${pizzaType} pizza.`);
        this.chef.bakePizza(pizzaType);
    }

    hurryUpChef() {
        console.log("Cashier is hurrying up the chef.");
        this.chef.hurryUp();
    }

    calmCustomerDown() {
        console.log("Cashier is calming the customer down.");
        this.chef.cleanKitchen();
    }

    deliverPizzaToCustomer() {
        console.log("Cashier is delivering pizza to the customer.");
    }

    askForReceipt() {
        console.log("Customer is asking for a receipt.");
    }

    anotherUnusedMethod() {
    }

    yetAnotherUnusedMethod() {
    }

    longMethod() {
        console.log("Cashier is handling many tasks in a single method");
        this.takeOrder("Cheese");
        this.hurryUpChef();
        this.calmCustomerDown();
        this.deliverPizzaToCustomer();
        this.askForReceipt();
    }

    orderWithUnnecessaryDetails(pizzaType, size, crustType, toppings, extraCheese, discountCode) {
        console.log(`Placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.takeOrder(pizzaType);
        this.applyDiscount(discountCode);
        this.deliverPizzaToCustomer();
    }

    duplicateMethod() {
        console.log("Customer is making a duplicate order");
        this.takeOrder("Cheese");
        this.takeOrder("Cheese");
    }

    chainOfMethods() {
        console.log("Cashier is initiating a message chain");
        this.chef.cleanKitchen();
    }

    middlemanMethod() {
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
        console.log(`Accessing internal details: ${this.chef.busy}`);
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

    applyDiscount(discountCode) {
        console.log(`Applying discount for customer with code ${discountCode}`);
    }

    applyLoyaltyPoints() {
        console.log("Applying loyalty points for customer");
    }

    handleComplaint(complaint) {
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
    }
}

module.exports = { Cashier };
