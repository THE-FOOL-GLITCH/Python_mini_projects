def show_welcome():
    print("="*40)
    print("🎯 Welcome to the Number Guessing Game! 🎯")
    print("="*40)

def get_menu():
    return input("\nPress 'Enter' to play or 'q' to quit: ").lower().strip()

def show_game_start():
    print("\n> Maine 1 se 100 ke beech ek number soch liya hai. Chalo guess karo!")

def get_guess():
    try:
        return int(input("\n Enter your guess: ")).strip()
    except ValueError:
        return None # Agar user ne words type kiye toh None bhej do

def show_invalid_range():
    print("> Arre bhai! Number 1 aur 100 ke beech mein hona chahiye. Try again.")  

def invalid_input():
    print("> Invalid Input! Bhai, sirf numbers (1-100) type karo.")

def show_hint(hint_type):
    if hint_type == "Low":
        print("> Thoda bada number socho! (Too low)")
    elif hint_type == "High":
        print("> Thoda chota number socho! (Too high)")    

def show_win(attempts):
    print(f"> Badhai ho! 🎉 You won! Tumne sirf {attempts} attempts mein sahi number guess kiya.")  

def show_game_over():
    print("Khelne ke liye shukriya! Game Over!!! 👋")