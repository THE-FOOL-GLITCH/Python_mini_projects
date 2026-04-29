from services import game_logic,ui

def main():

    ui.show_welcome()

    while True:
        user_choice = ui.get_user_choice()
        
        if user_choice == "q":
            ui.show_game_over()
            break
        
        validated_choices = ["rock", "paper", "scissors"]
        if user_choice not in validated_choices:
            ui.show_invalid_input()
            continue

        comp_choice = game_logic.get_computer_choice()

        ui.show_choices(user_choice,comp_choice)

        result = game_logic.determine_winner(user_choice,comp_choice)

        ui.show_result(result)

if __name__ == "__main__":
    main()    


