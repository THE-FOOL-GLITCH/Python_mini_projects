def show_welcome():
    print("="*40)
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("="*40)

def get_menu():
    return input("\nPress 'Enter' to play or 'q' to quit: ").lower().strip()

def show_game_start():
    # Update: User ko batao ki sirf 10 tries hain
    print("\n> Maine 1 se 100 ke beech ek number soch liya hai. Chalo guess karo!")
    print("> Tumhare paas isko guess karne ke liye SIRF 10 ATTEMPTS hain. Best of luck!")

def get_guess():
    try:
        return int(input("\n Enter your guess: ").strip())
    except ValueError:
        return None # Agar user ne words type kiye toh None bhej do

def show_invalid_range():
    print("> Arre bhai! Number 1 aur 100 ke beech mein hona chahiye. Try again.")  

def invalid_input():
    print("> Invalid Input! Bhai, sirf numbers (1-100) type karo.")

# Update: Ab hint ke sath attempts_left bhi print karenge
def show_hint(hint_type,attempts_left):
    if hint_type == "Low":
        print(f"> Thoda bada number socho! (Too low) - Sirf {attempts_left} tries baaki hain!")
    elif hint_type == "High":
        print(f"> Thoda chota number socho! (Too high) - Sirf {attempts_left} tries baaki hain!")    

def show_win(attempts):
    print(f"> Badhai ho! 🎉 You won! Tumne sirf {attempts} attempts mein sahi number guess kiya.") 

# New Function: Agar user haar gaya toh yeh message dikhao
def show_loss(secret_number):
    print(f"\n> Oops! 😭 Tumhare 10 attempts khatam ho gaye.")
    print(f"> Sahi number tha: {secret_number}. Better luck next time!")     

def show_game_over():
    print("Khelne ke liye shukriya! Game Over!!! 👋")