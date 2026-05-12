import random
import os

def start_game():
    try:
        with open("words.txt", "r", encoding="utf-8") as file:
            words_list = [line.strip().split(':') for line in file if ':' in line]
    except FileNotFoundError:
        print("Файл не найден")
        return

    if not words_list:
        print("Список слов пуст")
        return

    word_data = random.choice(words_list)
    target_word = word_data[0].lower()
    description = word_data[1]

    table = ["*"] * len(target_word)
    lives = 6

    print("Добро пожаловать в игру Виселица!")

    while lives > 0 and "*" in table:
        stage_file = f"stage_{lives}.txt"
        if os.path.exists(stage_file):
            with open(stage_file, "r", encoding="utf-8") as f:
                print(f"\n{f.read()}")
        else:
            print("\n[Изображение виселицы отсутствует]")

        print(f"Подсказка: {description}")
        print(f"Слово: {''.join(table)}")
        print(f"Осталось попыток: {lives}")

        guess = input("\nВведите букву или слово целиком: ").strip().lower()

        if guess == target_word:
            table = list(target_word)
            break

        if len(guess) == 1 and guess in target_word:
            for i in range(len(target_word)):
                if target_word[i] == guess:
                    table[i] = guess
            print("Верно! Вы открыли букву.")
        else:
            lives -= 1
            print("Неправильно! Вы теряете жизнь.")

    if "*" not in table:
        print(f"\nПоздравляем! Вы угадали слово: {target_word.upper()}")
    else:
        if os.path.exists("stage_0.txt"):
            with open("stage_0.txt", "r", encoding="utf-8") as f:
                print(f"\n{f.read()}")
        print(f"\nВы проиграли. Загаданное слово было: {target_word.upper()}")

start_game()
