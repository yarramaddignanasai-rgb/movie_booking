# -----------------------------
# Singleton Decorator
# -----------------------------
def Singleton(cls):
    instances = []

    def inner():
        if len(instances) == 0:
            obj = cls()
            instances.append(obj)
        return instances[0]

    return inner


# -----------------------------
# Movie 1 Class
# -----------------------------
@Singleton
class Movie1:
    def __init__(self):
        self.m_tic = 150   # available tickets

    def Booking(self):
        print(f"Available Tickets in Movie1: {self.m_tic}")
        count = int(input("Enter number of tickets: "))
        if 0 < count <= self.m_tic:
            self.m_tic -= count
            print("Booked Successfully!")
        else:
            print("Invalid number!")


# -----------------------------
# Movie 2 Class
# -----------------------------
@Singleton
class Movie2:
    def __init__(self):
        self.m_tic = 120

    def Booking(self):
        print(f"Available Tickets in Movie2: {self.m_tic}")
        count = int(input("Enter number of tickets: "))
        if 0 < count <= self.m_tic:
            self.m_tic -= count
            print("Booked Successfully!")
        else:
            print("Invalid number!")


# -----------------------------
# Movie 3 Class
# -----------------------------
@Singleton
class Movie3:
    def __init__(self):
        self.m_tic = 80

    def Booking(self):
        print(f"Available Tickets in Movie3: {self.m_tic}")
        count = int(input("Enter number of tickets: "))
        if 0 < count <= self.m_tic:
            self.m_tic -= count
            print("Booked Successfully!")
        else:
            print("Invalid number!")


# -----------------------------
# Booking System Function
# -----------------------------
def BMySC():
    while True:
        print("\n===== MOVIE BOOKING PORTAL =====")
        print("1. Movie 1")
        print("2. Movie 2")
        print("3. Movie 3")
        print("4. Exit")

        choice = input("Select your choice: ")

        if choice == "1":
            obj = Movie1()
            obj.Booking()

        elif choice == "2":
            obj = Movie2()
            obj.Booking()

        elif choice == "3":
            obj = Movie3()
            obj.Booking()

        elif choice == "4":
            print("Thank you! Enjoy your show.")
            break

        else:
            print("Invalid Choice!")


# -----------------------------
# Run Application
# -----------------------------
BMySC()
