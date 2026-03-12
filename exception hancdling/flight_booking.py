# Flight Database
flights = {
    "F101": {"route": "Delhi to Mumbai", "seats": 5, "price": 5000},
    "F102": {"route": "Kolkata to Bangalore", "seats": 3, "price": 6000},
    "F103": {"route": "Chennai to Hyderabad", "seats": 4, "price": 4000}
}

# Booking records
bookings = {}


# Search Flights
def search_flights():
    print("\nAvailable Flights")
    print("--------------------------------")
    for fid, info in flights.items():
        print("Flight:", fid,
              "| Route:", info["route"],
              "| Seats:", info["seats"],
              "| Price:", info["price"])
    print()


# Book Flight
def book_flight():
    try:
        fid = input("Enter Flight ID: ")

        if fid not in flights:
            raise KeyError("Invalid Flight ID!")

        if flights[fid]["seats"] <= 0:
            raise Exception("Seat not available!")

        name = input("Enter Passenger Name: ").strip()
        age = int(input("Enter Passenger Age: "))

        if name == "" or age <= 0:
            raise ValueError("Invalid passenger details!")

        payment = input("Enter payment method (Card/UPI): ")

        if payment not in ["Card", "UPI"]:
            raise Exception("Payment failure! Invalid method.")

        booking_id = len(bookings) + 1

        bookings[booking_id] = {
            "flight": fid,
            "name": name
        }

        flights[fid]["seats"] -= 1

        print("Booking successful!")
        print("Booking ID:", booking_id, "\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Error:", e)


# Cancel Booking
def cancel_booking():
    try:
        booking_id = int(input("Enter Booking ID to cancel: "))

        if booking_id not in bookings:
            raise KeyError("Booking not found!")

        fid = bookings[booking_id]["flight"]
        flights[fid]["seats"] += 1

        del bookings[booking_id]

        print("Booking cancelled successfully!\n")

    except KeyError as e:
        print("Error:", e)
    except ValueError:
        print("Invalid booking ID!")


# Main Menu
def main():
    while True:
        print("Flight Booking System")
        print("1. Search Flights")
        print("2. Book Flight")
        print("3. Cancel Booking")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                search_flights()
            elif choice == 2:
                book_flight()
            elif choice == 3:
                cancel_booking()
            elif choice == 4:
                print("Thank you for using the system!")
                break
            else:
                print("Invalid choice!\n")

        except ValueError:
            print("Enter a valid number!\n")


main()