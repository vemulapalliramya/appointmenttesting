class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.available_slots = {}

    def add_available_slot(self, date, start_time, end_time):
        slot = (start_time, end_time)
        if date in self.available_slots:
            self.available_slots[date].append(slot)
        else:
            self.available_slots[date] = [slot]

    def show_available_slots(self, date):
        if date in self.available_slots:
            print(f"Available slots for Dr. {self.name} on {date}:")
            for i, slot in enumerate(self.available_slots[date], start=1):
                print(f"{i}. {slot[0]} - {slot[1]}")
        else:
            print(f"No available slots for Dr. {self.name} on {date}.")


class Patient:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Appointment:
    def __init__(self, doctor, patient, date, start_time, end_time):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.start_time = start_time
        self.end_time = end_time

    def display_details(self):
        print("Appointment Details:")
        print(f"Doctor: {self.doctor.name}, Specialization: {self.doctor.specialization}")
        print(f"Patient: {self.patient.name}, Email: {self.patient.email}, Phone: {self.patient.phone}")
        print(f"Date: {self.date}, Time: {self.start_time} - {self.end_time}")


class Feedback:
    def __init__(self, doctor, rating, comments):
        self.doctor = doctor
        self.rating = rating
        self.comments = comments


class Payment:
    def __init__(self, patient, amount, payment_method):
        self.patient = patient
        self.amount = amount
        self.payment_method = payment_method


class Registration:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email


class LoginSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password, email):
        if username in self.users:
            print("Username already exists. Please choose another one.")
            return False
        else:
            self.users[username] = {'password': password, 'email': email}
            print("Registration successful.")
            return True

    def login(self, username, password):
        if username in self.users and self.users[username]['password'] == password:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False


# Example usage
if __name__ == "__main__":
    # Create a login system
    login_system = LoginSystem()

    # Register users
    login_system.register_user("user1", "password1", "user1@example.com")
    login_system.register_user("user2", "password2", "user2@example.com")

    # Login with valid credentials
    login_system.login("user1", "password1")

    # Login with invalid credentials
    login_system.login("user1", "wrong_password")
