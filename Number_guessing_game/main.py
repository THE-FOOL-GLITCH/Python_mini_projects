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
            
            # Naya logic: Attempts track karne ke liye
            attempts = 0
            MAX_attempts = 10

            while True:
                # UI se kaho ki user ka guess le kar aaye
                guess = ui.get_guess()

                # Agar guess None hai (yani user ne abc type kiya)
                if guess is None:
                    ui.invalid_input()
                    continue
                
                if guess < 1 or guess > 100:
                    ui.show_invalid_range()
                    continue

                # Valid guess hone par attempt count badhao
                attempts += 1
                attempts_left: int = MAX_attempts - attempts

                # Logic se check karwao ki guess kaisa tha
                result = game_logic.check_guess(secret, guess)

                if result == "win":
                    ui.show_win(attempts)
                    break
                else:
                    # Agar abhi jeete nahi, aur attempts zero ho gaye hain
                    if attempts_left == 0:
                        ui.show_loss(secret)
                        break # Inner loop tod do, naya game pucho
                    else:
                        # Agar attempts baaki hain toh hint dikhao
                        ui.show_hint(result,attempts_left)
        else:
            ui.invalid_input()

if __name__ == "__main__":
    main()



