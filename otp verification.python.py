import random
import string

def generate_otp():
    return ''.join(random.choices(string.digits, k=6))

if __name__ == "__main__":
       
    user_email=input("Enter your email address: ")
    otp = generate_otp()

    print(f'OTP sent to (user_email): {otp}')