# this file store information related to Hotel room

from Hotel_Data import rooms, guest, booking


def show_room():
    print("--" * 4, "ROOM LIST", "--" * 4)
    print(f"{'Room':<8} | {'Type':<10} | {'Price/Night':<12} | {'Status'}")
    print("==" * 23)
    for number, details in rooms.items():
        room_type, price, status = details
        print(f"{number:<8} | {room_type:<10} | Rs. {price:<8} | {status}")


def show_rooms():
    show_room()


def booking_room():
    print("--" * 4, "Book a Room", "--" * 4)

    if not guest:
        print("NO Guest found!!!, Please Add guest first.")
        return

    guest_ID = input("Enter Guest ID : ").strip()
    if guest_ID not in guest:
        print("Guest ID NOT FOUND!!! Please check guest ID then try again.")
        return

    show_room()

    try:
        room_no = int(input("Enter room Number TO book : "))
        days = int(input("Enter Number of Days :"))
    except ValueError:
        print("Please Enter Valid numeric values for room and days.")
        return

    if room_no not in rooms:
        print("That Room number does not exist!!")
        return

    if rooms[room_no][2].lower() == "booked":
        print("This room is already booked, sorry!")
        return

    if days <= 0:
        print("Number of days must be at least 1.")
        return

    price_per_night = rooms[room_no][1]
    total_amount = price_per_night * days
    rooms[room_no][2] = "Booked"

    booking[guest_ID] = [room_no, days, total_amount]

    guest_name = guest[guest_ID][0]
    print(f"Room {room_no} successfully booked for {guest_name}!")
    print(f"Total estimated charge: Rs. {total_amount}")


def book_room():
    booking_room()

