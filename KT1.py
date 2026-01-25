import random
year=random.randint(1941,1960)
answer="АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!"
answer2="ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!"
answer3=f"НЕТ, НИ РАЗУ С {year} ГОДА!"
options=[answer, answer2]
while True: print(random.choice(options))