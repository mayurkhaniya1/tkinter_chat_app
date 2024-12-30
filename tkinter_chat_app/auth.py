import random
from database import insert_user, verify_user

# Generate a dummy OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Register user
def register_user(mobile_number):
    otp = generate_otp()
    insert_user(mobile_number, otp)
    print(f"OTP sent to {mobile_number}: {otp}")
    return otp  # For testing purposes, OTP is printed
