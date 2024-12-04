def Tictaotoe():
    def print_board(board):
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("--+---+--")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("--+---+--")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    def get_player_move(board):
        while True:
            try:
                move = int(input("Choose a position (1-9): ")) - 1
                if board[move] == ' ':
                    return move
                else:
                    print("That spot is already taken. Choose another spot.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number between 1 and 9.")

    def check_winner(board, player):
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for pos in win_positions:
            if all(board[i] == player for i in pos):
                return True
        return False

    def check_tie(board):
        return ' ' not in board

    def play_game():
        board = [' '] * 9  # Initialize the board
        turn = 'X'  # X starts the game
        
        while True:
            print_board(board)
            move = get_player_move(board)
            board[move] = turn  # Place the player's mark

            if check_winner(board, turn):
                print_board(board)
                print(f"Player {turn} wins!")
                break

            if check_tie(board):
                print_board(board)
                print("It's a tie!")
                break

            turn = 'O' if turn == 'X' else 'X'  # Switch turns

    play_game()


def quiz_game():
    print("***** Welcome to the Quiz *****")
    playing = input("Do you want to play? (yes/no): ").strip().lower()
    if playing != "yes":
        print("Exiting the quiz. Have a nice day!")
        return

    print("Okay, let's play!")
    score = 0

    questions_answers = {
        "What does CPU stand for?": "central processing unit",
        "What does GPU stand for?": "graphics processing unit",
        "What does RAM stand for?": "random access memory",
        "What does ROM stand for?": "read only memory"
    }

    for question, correct_answer in questions_answers.items():
        answer = input(question + " ").strip().lower()
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect! The correct answer is '{correct_answer}'.")

    print(f"Your score is {score}/{len(questions_answers)}")
    print("Thanks for playing!")


def r_p_s():
    import random

    def rock_paper_scissors():
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)

        print("Rock, Paper, Scissors Game")
        user_choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()

        if user_choice not in choices:
            print("Invalid choice!")
            return

        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")

    rock_paper_scissors()


def main():
    while True:
        print("\n***** Welcome to the Gaming Hub *****")
        print("1. Tic Tac Toe")
        print("2. Quiz Game")
        print("3. Rock Paper Scissors")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()  # Remove extra spaces

        if choice == "1":
            Tictaotoe()
        elif choice == "2":
            quiz_game()
        elif choice == "3":
            r_p_s()
        elif choice == "4":
            print("Exiting the Gaming Hub. thank u visit again!")
            break
        else:
            print("Invalid choice! Please select a valid option (1-4).")


if __name__ == "__main__":
    main()
