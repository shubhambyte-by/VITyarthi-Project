# Hotel Management System

## Problem Statement

Managing basic hotel details manually can become confusing, especially when we have to keep track of guests, available rooms, bookings and bills at the same time.

For this project, I created a simple Hotel Management System in Python. The main idea was to make a program where hotel staff can add a guest, check the rooms, book a room and view the bill from one menu.

## Scope of the Project

This is a basic console-based project made using Python. The project currently allows the user to:

- add a new guest with Guest ID, name and contact number;
- view room number, room type, price and availability;
- book an available room for a registered guest;
- calculate the room charge according to the number of days;
- view the bill for a booking;
- handle common wrong inputs such as an empty Guest ID, invalid room number or non-numeric input.

The data is stored temporarily in Python dictionaries, so it remains available only while the program is running. Features such as permanent database storage, online payment, login and a graphical interface are not included in this version.

## Target Users

This project is mainly designed for:

- hotel reception or front-desk staff;
- small hotels and guest houses;
- students who want to understand how Python can be used for a simple real-life application.

## High-Level Features

1. **Add Guest** – Stores the Guest ID, name and contact number after basic validation.
2. **Show Rooms** – Displays the room number, type, price per night and current status.
3. **Book Room** – Allows a registered guest to book an available room.
4. **Automatic Bill Calculation** – Calculates the total room charge using room price × number of days.
5. **View Bill** – Shows guest name, Guest ID, room number, stay period and total amount.
6. **Input Checking** – Handles common invalid inputs and displays suitable messages.
