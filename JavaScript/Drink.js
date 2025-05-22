/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


class Drink {
    constructor() {
        this.drinkType = null;
    }

    createOrder(drinkType) {
        this.drinkType = drinkType;
        console.log(`Creating order for ${drinkType} drink.`);
    }

    addToOrder() {
        console.log(`Adding ${this.drinkType} to the order.`);
    }

    confirmOrder() {
        console.log(`Order for ${this.drinkType} confirmed.`);
    }
}

module.exports = { Drink };
