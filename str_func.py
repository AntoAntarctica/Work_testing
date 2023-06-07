def conv_to_uppercase(input_string):
    return input_string.upper()

def capitalize_first_letters(input_string):
    words = input_string.split()                               # Разбиваем строку на список слов
    capitalized_words = [word.capitalize() for word in words]  # Заглавные первые буквы каждого слова
    capitalized_string = ' '.join(capitalized_words)           # Собираем обновленные слова обратно в строку
    return capitalized_string

