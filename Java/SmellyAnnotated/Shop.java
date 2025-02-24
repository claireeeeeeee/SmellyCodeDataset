/*
Copyright (c) 2025 Ahmed R. Sadik, Honda Research Institute Europe GmbH 

This source code is licensed under the MIT License found in the
LICENSE file in the root directory of this source tree. This dataset contains smelly code for research and refactoring purposes.
*/


public class Shop {
    private Chef chef;
    private Cashier cashier;
    private Pizza pizza;

    // Primitive Obsession
    private boolean frequentCustomerDiscount;

    // Data Clumps
    private String firstName;
    private String lastName;
    private String address;
    private String phoneNumber;
    private String email;

    // Temporary Fields
    private String tempDiscountCode;
    private String tempOrderNote;

    public Shop() {
        this.chef = new Chef();
        this.cashier = new Cashier(chef);
        this.frequentCustomerDiscount = false; // Primitive Obsession
    }

    public void receiveOrder(String pizzaType) {
        System.out.println("Shop received order for " + pizzaType + " pizza.");
        this.pizza = createPizza(pizzaType);
        cashier.takeOrder(pizzaType);
    }

    public Pizza createPizza(String pizzaType) {
        if (pizzaType.equals("Cheese")) {
            return new CheesePizza();
        } else if (pizzaType.equals("Veggie")) {
            return new VeggiePizza();
        } else if (pizzaType.equals("Tuna")) {
            return new TunaPizza();
        } else if (pizzaType.equals("Pepperoni")) {
            return new PepperoniPizza();
        } else {
            throw new IllegalArgumentException("Unknown pizza type");
        }
    }

    public Cashier getCashier() {
        return this.cashier;
    }

    public Chef getChef() {
        return this.chef;
    }

    public void updateContactInfo(String firstName, String lastName, String address, String phoneNumber, String email) {
        // Shotgun Surgery (changing multiple methods to update contact info)
        this.firstName = firstName;
        this.lastName = lastName;
        this.address = address;
        this.phoneNumber = phoneNumber;
        this.email = email;
    }

    public void updateName(String firstName, String lastName) {
        // Shotgun Surgery (separate method to update name)
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public void updateAddress(String address) {
        // Shotgun Surgery (separate method to update address)
        this.address = address;
    }

    public void updatePhoneNumber(String phoneNumber) {
        // Shotgun Surgery (separate method to update phone number)
        this.phoneNumber = phoneNumber;
    }

    public void updateEmail(String email) {
        // Shotgun Surgery (separate method to update email)
        this.email = email;
    }

    public void notifyForPromotion() {
        // Divergent Change (method to notify for promotion)
        System.out.println("Notifying customer for promotion");
    }

    public void notifyForDiscount() {
        // Divergent Change (method to notify for discount)
        System.out.println("Notifying customer for discount");
    }

    public void notifyForNewArrivals() {
        // Divergent Change (method to notify for new arrivals)
        System.out.println("Notifying customer for new arrivals");
    }

    public void applyDiscount() {
        // Parallel Inheritance Hierarchies (method to apply discount)
        System.out.println("Applying discount for customer");
    }

    public void applyLoyaltyPoints() {
        // Parallel Inheritance Hierarchies (method to apply loyalty points)
        System.out.println("Applying loyalty points for customer");
    }

    public void handleComplaint(String complaint) {
        // Switch Statements (using if-else to simulate switch)
        if (complaint.equals("cold pizza")) {
            cashier.calmCustomerDown();
        } else if (complaint.equals("late delivery")) {
            cashier.calmCustomerDown();
        } else if (complaint.equals("wrong order")) {
            cashier.calmCustomerDown();
        } else {
            cashier.calmCustomerDown();
        }
    }

    public void askForReceipt() {
        System.out.println("Customer is asking for a receipt.");  // Speculative Generality (unused method)
    }

    public void anotherUnusedMethod() {
        // Dead Code (method is never
