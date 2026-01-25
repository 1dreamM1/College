import random
answer = "АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!"
answer2 = "ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!"
answer3 = "ДО СВИДАНИЯ, МИЛЫЙ!"
count = 0

print(answer2)

while True:
    message = input("> ")
    if message == "ПОКА!":
        count += 1
    else:
        count = 0

    if count == 3:
        print(answer3)
        break

    if message.isupper():
        year = random.randint(1930, 1950)
        print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
    else:
        print(answer)