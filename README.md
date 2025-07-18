
# 🎰 Slot Machine — Python Terminal Game

Welcome to the **Slot Machine** game written in Python!  
This is a simple command-line-based game where you can simulate a slot machine, place bets, and try your luck.

---

## 📌 Overview

This project simulates a **3x3 slot machine** with symbols `A`, `B`, `C`, and `D`, each having different **frequencies** and **payout values**.

You can:
- Deposit money
- Choose how many lines to bet on
- Set your bet per line
- Spin the machine
- Win or lose based on the symbol combinations!

---

## 🧑‍💻 How to Run the Program

### 📦 Requirements
Only **Python 3** is required. No external libraries are used.

### ▶️ To Run
```bash
python slot_machine.py
```

---

## 🧠 Game Logic and Flow

### 🎯 Goal
Bet money on 1 to 3 lines of a 3x3 grid. If the same symbol appears **horizontally** across a line, you **win** based on that symbol's payout multiplier!

---

## 🧱 Symbol Details

| Symbol | Frequency (Chance of Appearing) | Value (Multiplier) |
|--------|----------------------------------|---------------------|
| A      | 2 (rare)                         | 5x                  |
| B      | 4                                | 4x                  |
| C      | 6                                | 3x                  |
| D      | 8 (common)                       | 2x                  |

Higher-value symbols are harder to land!

---

## 🔁 Game Steps (Interactive Walkthrough)

### 1. 💰 Deposit Money
You'll be prompted:
```
What would you like to deposit? $
```
Only positive integers are accepted.

---

### 2. 🎯 Choose Number of Lines
You can bet on up to **3 horizontal lines**:
```
Enter the number of lines to bet on (1-3)?
```

---

### 3. 🎲 Place Your Bet
Decide how much to bet **per line**:
```
What would you like to bet on each line? $
```
The total bet will be:
```
bet amount × number of lines
```
It must not exceed your current balance.

---

### 4. 🌀 Spin the Machine
After placing the bet, the machine will spin and show a 3x3 grid like:
```
A | C | D
B | B | B
D | A | D
```

---

### 5. 🏆 Win or Lose
You win if **all symbols match in a line** (left to right).

If you win:
- You'll see which lines you won
- Your winnings are shown

Example:
```
You won $12.
You won on lines: 2
```

Winnings are calculated as:
```
symbol multiplier × bet amount
```

---

### 6. 🔄 Keep Playing or Quit
You can play again or quit:
```
Press enter to play (q to quit).
```

---

## 🧠 Code Structure

| Function | Purpose |
|----------|---------|
| `deposit()` | Ask the user to deposit money |
| `get_number_of_lines()` | Ask user how many lines to bet on |
| `get_bet()` | Ask how much to bet per line |
| `get_slot_machine_spin()` | Randomly generate a 3x3 symbol grid |
| `print_slot_machine()` | Display the slot machine on screen |
| `check_winnings()` | Evaluate winnings based on lines |
| `spin()` | Main spin logic: input → output |
| `main()` | Runs the game loop |

---

## 📚 Educational Concepts Demonstrated

- Loops and conditionals
- User input validation
- Use of functions for modular design
- Randomized behavior with weighted probability
- Simple game economy simulation

---

## 🚀 Future Improvements (Ideas)

- Add vertical and diagonal line checks  
- Display total games played and win rate  
- Allow custom symbols or grid sizes  
- Implement a GUI (Tkinter / Web interface)

---

## 🧑 Author

Developed as a beginner-friendly terminal game to learn programming, logic, and modular Python.

