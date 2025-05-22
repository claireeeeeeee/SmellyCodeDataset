/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Drink } = require('./Drink');

class Customer {
    constructor(Shop) {
        this.Shop = Shop;
        this.frequentCustomerDiscount = false;
        this.firstName = null;
        this.lastName = null;
        this.address = null;
        this.phoneNumber = null;
        this.email = null;
        this.tempDiscountCode = null;
        this.tempOrderNote = null;
        this.Drink = new Drink();
    }

    orderPizza(pizzaType) {
        console.log(`Customer is placing an order for ${pizzaType} pizza.`);
        this.Shop.receiveOrder(pizzaType);
    }

    complain(complaint) {
        console.log(`Customer is complaining: ${complaint}`);
        this.Shop.casher.calmCustomerDown();
        this.Shop.casher.chef.cleanKitchen();
    }

    askForReceipt() {
        console.log("Customer is asking for a receipt.");
    }

    anotherUnusedMethod() {
    }

    yetAnotherUnusedMethod() {
    }

    longComplaintMethod() {
        console.log("Customer is complaining about many things");
        this.complain("Pizza is cold");
        this.complain("Pizza is late");
        this.complain("Wrong pizza delivered");
        this.complain("Pizza is burnt");
        this.complain("Too little cheese");
        this.complain("Pizza is undercooked");
        this.askForReceipt();
    }

    orderWithUnnecessaryDetails(pizzaType, size, crustType, toppings, extraCheese, discountCode) {
        console.log(`Customer is placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.orderPizza(pizzaType);
        this.applyDiscount(discountCode);
        this.Shop.casher.deliverPizzaToCustomer();
    }

    duplicateComplaint() {
        console.log("Customer is complaining about duplicate issues");
        this.complain("Pizza is cold");
        this.complain("Pizza is cold");
        this.complain("Pizza is late");
        this.complain("Pizza is late");
    }

    chainOfMethods() {
        console.log("Customer is initiating a message chain");
        this.Shop.casher.chef.cleanKitchen();
    }

    middlemanMethod() {
        console.log("Customer is calling a middleman method");
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
        console.log(`Accessing internal details of Shop: ${this.Shop.casher.chef.busy}`);
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
            this.complain("Pizza is cold");
        } else if (complaint === "late delivery") {
            this.complain("Pizza is late");
        } else if (complaint === "wrong order") {
            this.complain("Wrong pizza delivered");
        } else {
            this.complain("General complaint");
        }
    }

    refusedBequest() {
    }

    orderDrink(drinkType) {
        console.log(`Customer is ordering a ${drinkType} drink.`);
        this.drinkOrder.createOrder(drinkType);
        console.log("Adding the drink order to the current order.");
        this.drinkOrder.addToOrder();
        console.log("Confirming the drink order.");
        this.drinkOrder.confirmOrder();
    }
}

module.exports = { Customer };
