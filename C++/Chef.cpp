/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


#include "Chef.h"
#include "Pizza.h"
#include <iostream>

Chef::Chef() {
    busy = false;
    completedOrders = 0;
    breaksTaken = 0;
    kitchenClean = true;
    pizza = nullptr;  
    extraCheese = false; 
}

void Chef::bakePizza(const std::string& pizzaType) {
    std::cout << "Chef is baking " << pizzaType << " pizza." << std::endl;
    pizza = new Pizza("Unknown", "Unknown", pizzaType); 
    cutPizzaAndPutInBox();
}

void Chef::cutPizzaAndPutInBox() {
    if (pizza) {
        std::cout << "Chef is cutting the " << pizza->getTopping() << " pizza and putting it in a box." << std::endl;
        deliverPizza();
    }
}

void Chef::deliverPizza() {
    std::cout << "Chef is delivering the pizza to the cashier." << std::endl;
}

void Chef::hurryUp() {
    std::cout << "Chef is hurrying up." << std::endl;
}

void Chef::cleanKitchen() {
    std::cout << "Chef is cleaning the kitchen." << std::endl;
    kitchenClean = true;
}

bool Chef::isBusy() const {
    return busy;
}


void Chef::updateContactInfo(const std::string& firstName, const std::string& lastName, const std::string& address, const std::string& phoneNumber, const std::string& email) {

    this->firstName = firstName;
    this->lastName = lastName;
    this->address = address;
    this->phoneNumber = phoneNumber;
    this->email = email;
}

void Chef::notifyForPromotion() {
    std::cout << "Notifying customer for promotion" << std::endl;
}

void Chef::notifyForDiscount() {
    std::cout << "Notifying customer for discount" << std::endl;
}

void Chef::notifyForNewArrivals() {
    std::cout << "Notifying customer for new arrivals" << std::endl;
}

void Chef::applyDiscount() {
    std::cout << "Applying discount for customer" << std::endl;
}

void Chef::applyLoyaltyPoints() {
    std::cout << "Applying loyalty points for customer" << std::endl;
}

void Chef::handleComplaint(const std::string& complaint) {
    if (complaint == "cold pizza") {
        std::cout << "Handling complaint: Pizza is cold" << std::endl;
    } else if (complaint == "late delivery") {
        std::cout << "Handling complaint: Pizza is late" << std::endl;
    } else if (complaint == "wrong order") {
        std::cout << "Handling complaint: Wrong pizza delivered" << std::endl;
    } else {
        std::cout << "Handling complaint: General complaint" << std::endl;
    }
}

void Chef::askForReceipt() {
    std::cout << "Customer is asking for a receipt." << std::endl;
}

void Chef::anotherUnusedMethod() {
}

void Chef::longMethod() {
    std::cout << "Chef is handling many tasks in a single method" << std::endl;
    this->bakePizza("Cheese");
    this->cutPizzaAndPutInBox();
    this->deliverPizza();
    this->hurryUp();
    this->cleanKitchen();
    this->updateContactInfo("John", "Doe", "123 Street", "555-5555", "john.doe@example.com");
    this->notifyForPromotion();
    this->notifyForDiscount();
    this->notifyForNewArrivals();
    this->applyDiscount();
    this->applyLoyaltyPoints();
    this->handleComplaint("cold pizza");
    this->askForReceipt();
    this->chainOfMethods();
    this->middlemanMethod();
    this->accessInternalDetails();
}

void Chef::orderWithUnnecessaryDetails() {
    std::cout << "Placing a detailed order for pizza with extra cheese and discount code" << std::endl;
    this->bakePizza("Veggie");
    this->applyDiscount();
    this->applyLoyaltyPoints();
}

void Chef::duplicateMethod() {
    std::cout << "Chef is making a duplicate order" << std::endl;
    this->bakePizza("Cheese");
    this->bakePizza("Cheese");
}

void Chef::chainOfMethods() {
    std::cout << "Chef is initiating a message chain" << std::endl;
    this->cleanKitchen();
}

void Chef::middlemanMethod() {
    std::cout << "Chef is calling a middleman method" << std::endl;
    this->middleMethod();
}

void Chef::middleMethod() {
    std::cout << "Middleman method delegating to another method" << std::endl;
    this->realMethod();
}

void Chef::realMethod() {
    std::cout << "Real method doing the actual work" << std::endl;
}

void Chef::accessInternalDetails() {
    std::cout << "Accessing internal details of Pizza: " << this->pizza->getTopping() << std::endl;
}

void Chef::refusedBequest() {
}
