/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


const { Shop } = require('./Shop');
const { Customer } = require('./Customer');

function measureExecutionTime(runs = 10) {
    let totalTime = 0;
    for (let i = 0; i < runs; i++) {
        const startTime = Date.now();

        const shop = new Shop();
        const customer = new Customer(shop);
        customer.orderPizza("Cheese");
        customer.complain("The pizza is too cold.");

        const endTime = Date.now();
        const executionTime = endTime - startTime;
        totalTime += executionTime;
    }

    const averageTime = totalTime / runs;
    return averageTime;
}

const avgTime = measureExecutionTime();
console.log(`Average execution time over multiple runs: ${avgTime} milliseconds`);
