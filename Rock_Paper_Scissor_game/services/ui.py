def show_welcome():
    print("=" * 40)
    print(" ✊ ✋ ✌️  ROCK, PAPER, SCISSORS ✌️ ✋ ✊ ")
    print("=" * 40)
    print("> Welcome to the ultimate battle of minds!")
    print("> Type 'rock', 'paper', or 'scissors' to play.")
    print("> Type 'q' anytime to quit.")
    print("-" * 40)

def get_user_choice():
    return input("\n Enter your move (Rock,Paper,Scissor or q to quit):").strip().lower()

def show_invalid_input():
    print("> ❌ Invalid Input! Bhai, sirf 'rock', 'paper', ya 'scissors' type karo.")

def show_choices():
    print(f"\n 👉 You played {user_choice.title()}")
    print(f"\n🤖 Computer played: {comp_choice.title()} ")    

def show_result(result):
    if result == "win":
        print("> 🎉 YOU WIN! Awesome job!")
    elif result == "lose":
        print("> 💀 YOU LOSE! The computer got you.")
    elif result == "tie":
        print("> 🤝 IT'S A TIE! Great minds think alike.")

def show_game_over():
    print("\nThanks for playing! Game Over!!! 👋")           
