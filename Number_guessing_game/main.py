from services import game_logic,ui

def main():
    # UI se kaho ki welcome message dikhaye
    ui.show_welcome()

    while True:
        # UI se kaho ki user ki choice le kar aaye
        choice = ui.get_menu()

        if choice == 'q':
            ui.show_game_over()
            break
        elif choice == "":
            secret = game_logic.generate_secret_number()
            ui.show_game_start()
            attempts = 0

            while True:
                # UI se kaho ki user ka guess le kar aaye
                guess = ui.get_guess()

                # Agar guess None hai (yani user ne abc type kiya)
                if guess is None:
                    ui.invalid_input()
                    continue
                attempts += 1

                if guess < 1 and guess > 100:
                    ui.show_invalid_range()
                    continue

                # Logic se check karwao ki guess kaisa tha
                result = game_logic.check_guess(secret, guess)

                if result == "win":
                    ui.show_win()
                    break
                else:
                    ui.show_hint(result)
        else:
            ui.invalid_input()

if __name__ == "__main__":
    main()



