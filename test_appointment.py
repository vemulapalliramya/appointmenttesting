import unittest
from appointment import Doctor, Patient, Appointment, Feedback, Payment, Registration, LoginSystem
import contextlib
import io
import sys

@contextlib.contextmanager
def captured_output():
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

class TestAppointment(unittest.TestCase):
    def setUp(self):
        self.doctor = Doctor("Dr. Smith", "Cardiology")
        self.patient = Patient("John Doe", "johndoe@example.com", "1234567890")

    def test_display_details(self):
        appointment = Appointment(self.doctor, self.patient, "2024-05-05", "10:00 AM", "11:00 AM")
        expected_output = (
            "Appointment Details:\n"
            "Doctor: Dr. Smith, Specialization: Cardiology\n"
            "Patient: John Doe, Email: johndoe@example.com, Phone: 1234567890\n"
            "Date: 2024-05-05, Time: 10:00 AM - 11:00 AM"
        )
        with captured_output() as (out, _):
            appointment.display_details()
            output = out.getvalue().strip()
            self.assertEqual(output, expected_output)

class TestFeedback(unittest.TestCase):
    def test_feedback_creation(self):
        doctor = Doctor("Dr. Smith", "Cardiology")
        feedback = Feedback(doctor, 5, "Great doctor!")
        self.assertEqual(feedback.rating, 5)
        self.assertEqual(feedback.comments, "Great doctor!")

class TestPayment(unittest.TestCase):
    def test_payment_creation(self):
        patient = Patient("John Doe", "johndoe@example.com", "1234567890")
        payment = Payment(patient, 100, "Credit Card")
        self.assertEqual(payment.amount, 100)
        self.assertEqual(payment.payment_method, "Credit Card")

class TestRegistration(unittest.TestCase):
    def test_registration_creation(self):
        registration = Registration("user1", "password1", "user1@example.com")
        self.assertEqual(registration.username, "user1")
        self.assertEqual(registration.email, "user1@example.com")

class TestLoginSystem(unittest.TestCase):
    def setUp(self):
        self.login_system = LoginSystem()
        self.login_system.register_user("user1", "password1", "user1@example.com")

    def test_register_user(self):
        self.assertFalse(self.login_system.register_user("user1", "password2", "user2@example.com"))
        self.assertTrue(self.login_system.register_user("user2", "password2", "user2@example.com"))

    def test_login_successful(self):
        self.assertTrue(self.login_system.login("user1", "password1"))

    def test_login_invalid_username(self):
        self.assertFalse(self.login_system.login("user2", "password1"))

    def test_login_invalid_password(self):
        self.assertFalse(self.login_system.login("user1", "wrong_password"))

if __name__ == "__main__":
    unittest.main()
