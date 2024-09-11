import random

def evaluate_state(random_integer):
    # A simple evaluation function: positive for player 1, negative for player 2
    return random_integer

def minmax(depth, player, alpha, beta, random_integer):
    if depth == 0 or random_integer == 1:
        return evaluate_state(random_integer)

    if player == 1:
        max_value = float('-inf')
        for move in (1, 2, 3):
            if move <= random_integer:
                new_random_integer = random_integer - move
                value = minmax(depth - 1, 2, alpha, beta, new_random_integer)
                max_value = max(max_value, value)
                alpha = max(alpha, max_value)
                if alpha >= beta:
                    break
        return max_value

    else:
        min_value = float('inf')
        for move in (1, 2, 3):
            if move <= random_integer:
                new_random_integer = random_integer - move
                value = minmax(depth - 1, 1, alpha, beta, new_random_integer)
                min_value = min(min_value, value)
                beta = min(beta, min_value)
                if alpha >= beta:
                    break
        return min_value

player = 1
random_integer = random.randint(1, 30)

print("The number of objects is now", random_integer)

while True:
    print("Player", player)

    if player == 2:  # Computer's turn
        best_move = None
        best_value = float('-inf')
        for move in (1, 2, 3):
            if move <= random_integer:
                new_random_integer = random_integer - move
                value = minmax(3, 2, float('-inf'), float('inf'), new_random_integer)  # Adjust depth as needed
                if value > best_value:
                    best_move = move
                    best_value = value
        print("Computer's move:", best_move)
        random_integer -= best_move
    else:  # Human's turn
        while True:
            move = input("What is your move? ")

            try:
                move = int(move)
            except ValueError:
                print("Illegal move: Please enter a number.")
                continue

            if move not in (1, 2, 3):
                print("Illegal move: Please enter a number between 1 and 3.")
                continue

            if move > random_integer:
                print("Illegal move: You cannot take more objects than are remaining.")
                continue

            break

        random_integer -= move

    print("The number of objects is now", random_integer)

    if random_integer == 1:
        print("Player", player, "wins!")
        break

    player = 2 if player == 1 else 1

print("Game over.")