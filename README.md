/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */
package com.mycompany.cosc005w_mock_planeapp;

import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.util.InputMismatchException;
/**
 * // Before you start, complete the following information: 
 * NAME: Aryan 
 * SURNAME: Paudel
 * STUDENT ID: SESSION (Day + time): w2083972(11 to 12:30)
 */
public class App {

      // Global variables
    private static int[][] planeSeats = null; // 2D array for seat availability
    private static int[] pricePerRow = null; // Array for seat prices per row
    private static Payment[] payments = new Payment[260]; // Array to store payment records
    private static int payCount = 0; // Counter for payments

    public static void main(String[] args) {
        System.out.println("Welcome to Flying Java!");
        initialiseRows(); // Task 1: Initialize seating arrangement
        runMenu(); // Start the menu
    }

    // Task 1: Initialize the number of seats per row
    public static void initialiseRows() {
        planeSeats = new int[4][]; // 4 rows
        planeSeats[0] = new int[16]; // Row 1: 16 seats
        planeSeats[1] = new int[22]; // Row 2: 22 seats
        planeSeats[2] = new int[22]; // Row 3: 22 seats
        planeSeats[3] = new int[16]; // Row 4: 16 seats
        pricePerRow = new int[4]; // Prices for each row
        pricePerRow[0] = 50; // Price for Row 1
        pricePerRow[1] = 80; // Price for Row 2
        pricePerRow[2] = 80; // Price for Row 3
        pricePerRow[3] = 50; // Price for Row 4
    }

    // Run the main menu
    public static void runMenu() {
        int option;
        boolean cont = true;

        while (cont) {
            option = getOption(); // Get user option
            switch (option) {
                case 0:
                    cont = false; // Exit the loop
                    break;
                case 1:
                    buyTicket(); // Task 4: Buy a ticket
                    break;
                case 2:
                    showSeatingArea(); // Show seating map
                    break;
                case 3:
                    searchPayments(); // Task 5: Search for payments
                    break;
                case 4:
                    saveToFile(); // Task 6: Save payments to file
                    break;
                default:
                    System.out.println("Option not available. Please select a valid option: ");
            }
        }
    }

    // Get user option from the menu
    private static int getOption() {
        Scanner input = new Scanner(System.in);
        boolean valid = false;
        int option = -1;
        do {
            System.out.println();
            System.out.println("+---------------------------------------------+");
            System.out.println("|                MAIN MENU                    |");
            System.out.println("+---------------------------------------------+");
            System.out.println("|  1) Buy a plane ticket                      |");
            System.out.println("|  2) Show seating area and available seats   |");
            System.out.println("|  3) Search for payments                     |");
            System.out.println("|  4) Save payments to file                   |");
            System.out.println("|  0) Quit                                    |");
            System.out.println("+---------------------------------------------+");
            System.out.print("Please select an option: ");
            try {
                option = input.nextInt();
                valid = true;
            } catch (Exception e) {
                System.out.println("This option is not valid.");
                input.next(); // Clear invalid input
            }
        } while (!valid);
        return option;
    }

    // Task 4: Buy a ticket
    private static void buyTicket() {
        Scanner input = new Scanner(System.in);
        String email = "";
        int row = 0, seat = 0;
        boolean email_check = false;

        // Validate email input
        do {
            System.out.print("Enter your email: ");
            email = input.nextLine();
            if (email.contains(".") && email.contains("@")) {
                email_check = true;
            } else {
                System.out.println("Invalid email");
            }
        } while (!email_check);

        // Validate row input
        do {
            try {
                System.out.print("Enter row number (1-4): ");
                row = input.nextInt() - 1; // Adjust for 0 -based index
                if (row < 0 || row > 3) {
                    System.out.println("Row number must be between 1 and 4!");
                } else {
                    System.out.println("Row number " + (row + 1) + " is valid.");
                }
            } catch (InputMismatchException e) {
                System.out.println("Row number should be a valid integer.");
                input.next(); // Clear invalid input
            }
        } while (row < 0 || row > 3);

        // Validate seat input
        boolean seat_check = false;
        do {
            try {
                System.out.print("Enter seat number (1-" + planeSeats[row].length + "): ");
                seat = input.nextInt() - 1; // Adjust for 0-based index
                if (seat < 0 || seat >= planeSeats[row].length) {
                    System.out.println("Seat number must be between 1 and " + planeSeats[row].length + "!");
                }
            } catch (InputMismatchException e) {
                System.out.println("Seat number should be a valid integer.");
                input.next(); // Clear invalid input
            }
        } while (seat < 0 || seat >= planeSeats[row].length);

        // Check if the seat is available
        if (planeSeats[row][seat] == 0) {
            planeSeats[row][seat] = 1; // Mark seat as taken
            Payment payment = new Payment(email, pricePerRow[row]); // Create payment object
            if (payCount < payments.length) {
                payments[payCount] = payment; // Store payment
                payCount++;
                System.out.println("Purchase successful.");
                showSeatingArea(); // Show updated seating area
            } else {
                System.out.println("Sorry, the payment record limit has been reached.");
            }
        } else {
            System.out.println("This seat is already taken.");
        }
    }

    // Task 2: Show seating area
    private static void showSeatingArea() {
        int rows = planeSeats.length;
        char aisle = '|';

        System.out.println("=".repeat(76));
        System.out.println("                              PLANE SEATING MAP ");
        System.out.println("=".repeat(76));

        for (int row = 0; row < rows; row++) {
            System.out.print("Row " + (row + 1) + " (£" + pricePerRow[row] + ")  ");
            int seatsPerRow = planeSeats[row].length;
            for (int seat = 0; seat < seatsPerRow; seat++) {
                if (seat == 9) { // Create aisles
                    System.out.print(" " + aisle + " ");
                }
                if (planeSeats[row][seat] == 0) { // Available seat
                    System.out.print("[O]");
                } else { // Not available seat
                    System.out.print("[X]");
                }
            }
            System.out.println();
        }
        System.out.println("=".repeat(76));
        System.out.println("LEGEND: [O] = Seat available, [X] = Seat not available, | = Aisle");
        System.out.println("=".repeat(76));
        System.out.println();
    }

    // Task 5: Search for payments based on amount
    private static void searchPayments() {
        Scanner input = new Scanner(System.in);
        boolean found = false;
        System.out.print("Enter the amount to search: ");
        int searchAmount = input.nextInt();
        System.out.println("Emails for the given search amount: ");
        for (int i = 0; i < payCount; i++) {
            if (payments[i].getPaymentAmount() == searchAmount) {
                payments[i].printPayment(); // Print payment details
                found = true;
            }
        }
        if (!found) {
            System.out.println("Not found");
        }
    }

    // Task 6: Save payments to a file
    private static void saveToFile() {
        try {
            File file = new File("records.txt");
            if (!file.exists()) {
                file.createNewFile(); // Create file if it doesn't exist
            }
            FileWriter writer = new FileWriter("records.txt");
            for (int i = 0; i < payCount; i++) {
                writer.write(payments[i].getEmail() + ", " + payments[i].getPaymentAmount() + "\n");                
            }
            writer.close();
            System.out.println("Payments successfully saved to records.txt");
        } catch (Exception e) {
            System.out.println("Error saving to the file.");
        }
    }
}/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.cosc005w_mock_planeapp;

/**
 *
 * @author aayu0
 */
public class Payment {
    private String email;
    private int paymentAmount;
    
    public Payment(String email, int paymentAmount){
        this.email = email;
        this.paymentAmount = paymentAmount;
    }
    
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email =email;
    }
    
     public int getPaymentAmount(){
        return paymentAmount;
    }
    public void setPaymentAmount(int paymentAmount){
        this.paymentAmount = paymentAmount;
    }
    
    public void printPayment(){
        System.out.println(email+", "+ paymentAmount);
    }
}
