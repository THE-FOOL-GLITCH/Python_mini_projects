import random

# Yeh function secret number generate karega
def generate_secret_number():
    return random.randint(1,100)

# Yeh function result check karega
def check_guess(secret_number,user_guess):
    if user_guess == secret_number:
        return "win"
    elif user_guess > secret_number:
        return "High"
    else:
        return "Low"