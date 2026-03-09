class Movie:
    def __init__(self, name, showtime, seats):
        self.name = name
        self.showtime = showtime
        self.seats = seats  # total seats
        self.booked_seats = []

    def show_details(self):
        print(f"\nMovie: {self.name}")
        print(f"Showtime: {self.showtime}")
        print(f"Available Seats: {self.seats - len(self.booked_seats)}")

    def display_seats(self):
        print("\nAvailable Seats:")
        for i in range(1, self.seats + 1):
            if i in self.booked_seats:
                print(f"[X]", end=" ")
            else:
                print(f"[{i}]", end=" ")
        print()

    def book_seat(self, seat_number):
        if seat_number in self.booked_seats:
            print("Seat already booked!")
        elif seat_number > self.seats or seat_number <= 0:
            print("Invalid seat number!")
        else:
            self.booked_seats.append(seat_number)
            print("Seat booked successfully!")

    def print_ticket(self, seat_number):
        print("\n------ TICKET ------")
        print(f"Movie: {self.name}")
        print(f"Showtime: {self.showtime}")
        print(f"Seat Number: {seat_number}")
        print("--------------------")


# Create Movie Object
movie1 = Movie("Avengers", "6:00 PM", 10)

while True:
    print("\n1. Show Movie Details")
    print("2. Display Seats")
    print("3. Book Seat")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        movie1.show_details()

    elif choice == "2":
        movie1.display_seats()

    elif choice == "3":
        seat = int(input("Enter seat number to book: "))
        movie1.book_seat(seat)
        if seat in movie1.booked_seats:
            movie1.print_ticket(seat)

    elif choice == "4":
        print("Thank you for using Movie Booking System!")
        break

    else:
        print("Invalid choice!")