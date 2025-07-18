import random  # For generating random slot outcomes

# Constants
MAX_LINES = 3        # Max number of lines user can bet on
MAX_BET = 100        # Max amount allowed per line
MIN_BET = 1          # Minimum bet per line

ROWS = 3             # Slot machine rows
COLS = 3             # Slot machine columns

# Frequency of each symbol in the pool
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Multiplier value for each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    """
    Check which lines won and calculate the total winnings.
    A line wins if all symbols in that horizontal line match across all columns.
    """
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]  # Take symbol from the first column
        for column in columns:
            if column[line] != symbol:  # Check if symbol matches across the line
                break
        else:  # Only executes if inner loop didn't break (i.e., it's a winning line)
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)  # Lines are 1-indexed for user

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Randomly generate symbols for each column of the slot machine.
    Ensures that symbols are chosen based on their frequency.
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        all_symbols.extend([symbol] * symbol_count)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]  # Copy to avoid repetition within same column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Print the slot machine grid row by row.
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    """
    Prompt the user to deposit money and validate the input.
    """
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def get_number_of_lines():
    """
    Prompt user to choose number of lines to bet on.
    """
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    """
    Prompt the user to enter a bet amount per line and validate it.
    """
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount


def spin(balance):
    """
    Handle one spin round:
    - Ask user for lines and bets.
    - Generate the slot grid.
    - Print it and calculate winnings.
    - Return the net result (winnings - total bet).
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)

    return winnings - total_bet  # Net change to the balance


def main():
    """
    Entry point of the program.
    Handles the game loop until user quits.
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


# Run the program
main()
