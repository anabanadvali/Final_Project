import logging
from datetime import datetime

logging.basicConfig(
    filename="hotel_bookings.log",
    level=logging.INFO
)

class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: float, max_guests: int):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = True
        self.max_guests = max_guests

    def book_room(self):
        self.is_available = False

    def release_room(self):
        self.is_available = True

    def calculate_price(self, nights):
        current_month = datetime.now().month
        base_price = self.price_per_night * nights

        if current_month in [6, 7, 8]:
            return base_price * 1.20
        return base_price

    def __str__(self):
        if self.is_available:
            status = "თავისუფალი"
        else:
            status = "დაკავებული"

        return f"ოთახი #{self.room_number} ({self.room_type}) - ტარიფი: {self.price_per_night}GEL/ღამე  / სტატუსი: {status} / მაქს. სტუმარი: {self.max_guests}"


class Customer:
    def __init__(self, name: str, budget: float):
        self.name = name
        self.budget = budget
        self.booked_rooms = []
        self.reward_points = 0

    def add_room(self, room: Room):
        if room not in self.booked_rooms:
            self.booked_rooms.append(room)

    def remove_room(self, room: Room):
        if room in self.booked_rooms:
            self.booked_rooms.remove(room)

    def pay_for_booking(self, total_price: float):
        if self.budget >= total_price:
            self.budget -= total_price
            earned_points = int(total_price // 10)
            self.reward_points += earned_points
            print(f"გადახდა წარმატებით განხორციელდა. ჩამოგეჭრათ {total_price}GEL. დაგერიცხათ {earned_points} ქულა.")
            return True
        else:
            print(f"გადახდა ვერ განხორციელდა.({total_price - self.budget}GEL)")
            return False

    def show_booking_summary(self):
        if not self.booked_rooms:
            return f"მომხმარებელ {self.name}-ს არ აქვს აქტიური ჯავშნები."

        rooms_info = ", ".join([f"#{r.room_number} ({r.room_type})" for r in self.booked_rooms])
        return (f"მომხმარებელი: {self.name}\n"
                f"   დაჯავშნილი ოთახები: {rooms_info}\n"
                f"   დაგროვილი ქულები: {self.reward_points}\n"
                f"   დარჩენილი ბიუჯეტი: {self.budget:.2f}GEL")


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.bookings_log = []

    def add_room_to_hotel(self, room: Room):
        self.rooms.append(room)

    def show_available_rooms(self, room_type: str = None):
        available = [r for r in self.rooms if r.is_available]
        if room_type:
            available = [r for r in available if r.room_type.lower() == room_type.lower()]
        return available

    def calculate_total_booking(self, room_number: int, nights: int):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.calculate_price(nights)
        return 0.0

    def log_booking(self, customer: Customer, room: Room, total_price: float):
        log_entry = f"დაჯავშნა: მომხმარებელი {customer.name} / ოთახი #{room.room_number} / თანხა: {total_price}GEL"
        self.bookings_log.append(log_entry)
        logging.info(log_entry)

    def book_room_for_customer(self, customer: Customer, room_number: int, nights: int):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_available:
                    print(f"ოთახი #{room_number} უკვე დაკავებულია!")
                    return False

                total_price = room.calculate_price(nights)

                if customer.pay_for_booking(total_price):
                    room.book_room()
                    customer.add_room(room)
                    self.log_booking(customer, room, total_price)
                    print(f"ოთახი #{room_number} წარმატებით დაიჯავშნა {customer.name}-სთვის!")
                    return True
                return False

        print(f"ოთახი #{room_number} ვერ მოიძებნა")
        return False

    def cancel_booking(self, customer: Customer, room_number: int):
        for room in customer.booked_rooms:
            if room.room_number == room_number:
                room.release_room()
                customer.remove_room(room)

                log_entry = f"გაუქმება: მომხმარებელი {customer.name} / ოთახი #{room.room_number}"
                self.bookings_log.append(log_entry)
                logging.info(log_entry)

                print(f"დაჯავშნა გაუქმდა. ოთახი #{room_number} კვლავ თავისუფალია!")
                return
        print(f"მომხმარებელს არ აქვს დაჯავშნილი ოთახი #{room_number}!")

# სასტუმროს მუშაობა
def run_booking_system():
    my_hotel = Hotel("Oasis")
    my_hotel.add_room_to_hotel(Room(101, "Single", 100.0, 1))
    my_hotel.add_room_to_hotel(Room(102, "Double", 150.0, 2))
    my_hotel.add_room_to_hotel(Room(103, "Suite", 300.0, 4))
    my_hotel.add_room_to_hotel(Room(104, "Suite", 350.0, 4))

    print("აირჩიეთ სასურველი შეთავაზება და დაჯავშნეთ ნომერი")

    customer_name = input("გთხოვთ, შეიყვანოთ თქვენი სახელი: ")
    customer_budget = float(input("შეიყვანეთ თქვენი ბიუჯეტი (GEL): "))
    customer = Customer(customer_name, customer_budget)

    while True:
        print("\n აირჩიეთ სასურველი ქმედება:")
        print("1. ოთახის დაჯავშნა")
        print("2. ჩემი აქტიური ჯავშნების ნახვა")
        print("3. დაჯავშნის გაუქმება")
        print("4. პროგრამიდან გასვლა")

        choice = input("შეიყვანეთ მოქმედების ნომერი (1-4): ")

        if choice == "1":
            print("\nნაბიჯი 1: მოთხოვნების შეყვანა")
            room_type = input("შეიყვანეთ სასურველი ოთახის ტიპი (Single, Double, Suite): ")
            nights = int(input("რამდენი ღამით გსურთ დარჩენა?: "))

            print("\nნაბიჯი 2: თავისუფალი ოთახები თქვენი მოთხოვნით")
            available_rooms = my_hotel.show_available_rooms(room_type)

            if not available_rooms:
                print(f"სამწუხაროდ, '{room_type}' ტიპის თავისუფალი ოთახები ვერ მოიძებნა.")
                continue

            for room in available_rooms:
                estimated_price = room.calculate_price(nights)
                print(f"{room} / ჯამური ფასი {nights} ღამით: {estimated_price}GEL")

            print("\nოთახის არჩევა")
            chosen_number = int(input("შეიყვანეთ იმ ოთახის ნომერი, რომლის დაჯავშნაც გსურთ: "))

            print("\nპროცესინგი (ბიუჯეტი, გადახდა, ქულები, ლოგირება)")
            my_hotel.book_room_for_customer(customer, chosen_number, nights)

        elif choice == "2":
            print("\nთქვენი ინფორმაცია")
            print(customer.show_booking_summary())

        elif choice == "3":
            print("\nჯავშნის გაუქმება")
            if not customer.booked_rooms:
                print("თქვენ არ გაქვთ აქტიური ჯავშანი")
                continue

            print("თქვენი დაჯავშნილი ოთახები:")
            for room in customer.booked_rooms:
                print(f"- ოთახი #{room.room_number}")

            cancel_number = int(input("შეიყვანეთ ოთახის ნომერი, რომლის გაუქმებაც გსურთ: "))
            my_hotel.cancel_booking(customer, cancel_number)

        elif choice == "4":
            print("\nგმადლობთ, რომ გვესტუმრეთ.")
            break
        else:
            print("არასწორი არჩევანი. გთხოვთ აირჩიოთ 1, 2, 3 ან 4.")


if __name__ == "__main__":
    run_booking_system()

