# This is main output file for project
from Hotel_Data import guest, booking
from GuestInfo import add_guest
from Roominfo import show_room, booking_room

show_rooms = show_room
book_room = booking_room


def Bill():
    print("--" * 4, "View Bill", "--" * 4)
    guest_ID = input("Enter Guest ID : ").strip()

    if guest_ID not in booking:
        print("No booking found with this booking ID.")
        return

    room_no, days, total_amount = booking[guest_ID]
    guest_name = guest[guest_ID][0]

    print(" " + " = " * 32)
    print("           HOTEL INVOICE         ")
    print("=" * 32)
    print(f" Guest Name : {guest_name}")
    print(f" Guest ID   : {guest_ID}")
    print(f" Room No.   : {room_no}")
    print(f" Stay Period: {days} days")
    print("--" * 16)
    print(f" Total Due  : Rs. {total_amount}")
    print("==" * 16)


def main():
    while True:
        # print("==" * 16)
        # print("WELCOME TO MANAGEMENT SYSTEM OF HOTEL GRAND SWAN PARAISE INDORE  ")
        print("==" * 16)
        print("    HOTEL MANAGEMENT SYSTEM   ")
        print("==" * 16)
        print("1.  Add Guest")
        print("2.  Show Rooms")
        print("3.  Book Room")
        print("4.  View Bill")
        print("5.  Exit")
        print("==" * 16)

        choice = input("Enter your Choice (1-5): ").strip()

        if choice == "1":
            add_guest()
        elif choice == "2":
            show_rooms()
        elif choice == "3":
            book_room()
        elif choice == "4":
            Bill()
        elif choice == "5":
            print("Thank you for using hotel Management System. Have a great day!")
            break
        else:
            print("Invalid Choice! Please Enter valid choice.")


if __name__ == "__main__":
    main()
