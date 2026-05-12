import random
import os

def load_words(filename):
    words_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                words_list.append(line.strip().split(':'))
    return words_list

def get_random_word(words_list):
    if not words_list:
        return None, None
    choice = random.choice(words_list)
    words_list.remove(choice)
    return choice[0].lower(), choice[1]

def create_table(word):
    return ["*"] * len(word)

def show_game_state(table, description, lives):
    frame = "Виселица не найдена"
    filename = f"stage_{lives}.txt"
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            frame = f.read()
    
    print("\n" + "="*30)
    print(frame)
    print(f"\nСлово: {' '.join(table)}")
    print(f"Подсказка: {description}")
    print(f"Жизней осталось: {lives}")

def prompt_guess():
    return input("\nНазовите букву или слово целиком: ").lower().strip()

def update_table(word, table, char):
    found = False
    for i in range(len(word)):
        if word[i] == char:
            table[i] = char.upper()
            found = True
    return found

def is_word_correct(target, guess):
    return target == guess

def is_alive(lives):
    return lives > 0

def is_solved(table):
    return "*" not in table

def show_message(msg):
    print(msg)

def ask_to_continue():
    answer = input("\nХотите сыграть еще раз? (да/нет): ").lower()
    return answer == 'да'

def get_init_lives():
    return 6

def decrease_lives(lives):
    return lives - 1
