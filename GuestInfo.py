from Hotel_Data import guest


def add_guest():
    # Registering a new guest with id, name and contact no.
    
    print("\n")
    print("--" * 4, "Add Guest", "--" * 4)
    guest_ID = input("Enter Guest ID : ")

    if not guest_ID:
        print("Guest ID cannot be empty.")
        return
    if guest_ID in guest:
        print("A guest with this ID is already in hotel.")
        return

    name = input("Enter Guest Name : ").strip()
    if not name:
        print("Guest name cannot be empty.")
        return

    try:
        phone = int(input("Enter Contact Number : "))
    except ValueError:
        print("Contact Number must be numeric.")
        return

    guest[guest_ID] = [name, phone]
    print("Guest Name", name, "added successfully!")


