/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Drink} = require('./Drink');

class Customer {
    constructor(Shop) {
        this.Shop = Shop; // Dependency Injection (Control Coupling)
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

        // Lazy Class
        this.Drink= new Drink();
    }

    orderPizza(pizzaType) {
        console.log(`Customer is placing an order for ${pizzaType} pizza.`);
        this.Shop.receiveOrder(pizzaType); // Feature Envy (refers to another class to do its work)
    }

    complain(complaint) {
        console.log(`Customer is complaining: ${complaint}`);
        this.Shop.casher.calmCustomerDown(); // Inappropriate Intimacy (accessing another object's internal details)
        this.Shop.casher.chef.cleanKitchen(); // Inappropriate Intimacy (accessing another object's internal details)
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

    longComplaintMethod() {
        // Long Method (too many complaints handled in one method)
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
        // Long Parameter List (too many parameters in the method)
        console.log(`Customer is placing a detailed order for ${pizzaType} pizza with ${size}, ${crustType}, ${toppings}, extra cheese: ${extraCheese}, discount code: ${discountCode}`);
        this.orderPizza(pizzaType);
        this.applyDiscount(discountCode);
        this.Shop.casher.deliverPizzaToCustomer();
    }

    duplicateComplaint() {
        // Duplicate Code (repeating complaint functionality)
        console.log("Customer is complaining about duplicate issues");
        this.complain("Pizza is cold");
        this.complain("Pizza is cold");
        this.complain("Pizza is late");
        this.complain("Pizza is late");
    }

    chainOfMethods() {
        // Message Chain (calling methods on objects returned by another method)
        console.log("Customer is initiating a message chain");
        this.Shop.casher.chef.cleanKitchen();
    }

    middlemanMethod() {
        // Middle Man (methods that delegate to other methods)
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
        // Inappropriate Intimacy (accessing internal details of another class)
        console.log(`Accessing internal details of Shop: ${this.Shop.casher.chef.busy}`);
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
        // Refused Bequest (method that should be inherited but is empty)
    }

    orderDrink(drinkType) {
        // Unnecessary Comments (explaining what each line does)
        console.log(`Customer is ordering a ${drinkType} drink.`);
        this.drinkOrder.createOrder(drinkType);
        console.log("Adding the drink order to the current order.");
        this.drinkOrder.addToOrder();
        console.log("Confirming the drink order.");
        this.drinkOrder.confirmOrder();
    }
}

module.exports = { Customer };
