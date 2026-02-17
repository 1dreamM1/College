import func as game

def start_game():
    words_pool = game.load_words("words.txt")
    
    keep_playing = True
    while keep_playing:
        current_word, description = game.get_random_word(words_pool)
        
        if not current_word:
            game.show_message("Слова в списке закончились!")
            break
            
        table = game.create_table(current_word)
        lives = game.get_init_lives()
        
        while game.is_alive(lives):
            game.show_game_state(table, description, lives)
            answer = game.prompt_guess()
            
            if game.is_word_correct(current_word, answer):
                game.show_message(f"Поздравляем! Вы угадали слово: {current_word.upper()}")
                break
            
            if len(answer) == 1 and game.update_table(current_word, table, answer):
                if game.is_solved(table):
                    game.show_game_state(table, description, lives)
                    game.show_message("Вы открыли все буквы! Победа!")
                    break
            else:
                lives = game.decrease_lives(lives)
                game.show_message("Неправильно! Вы теряете жизнь.")
        
        if not game.is_alive(lives):
            game.show_message(f"Вы проиграли. Загаданное слово было: {current_word.upper()}")
            
        keep_playing = game.ask_to_continue()

if __name__ == "__main__":

    start_game_session()
