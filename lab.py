def process_text(input_text):
    capitalized_text = ". ".join(sentence.capitalize() for sentence in input_text.split('. '))
    digit_count = sum(c.isdigit() for c in input_text)
    punctuation_count = sum(c in ",.!?;:" for c in input_text)
    exclamation_count = input_text.count("!")
    return capitalized_text, digit_count, punctuation_count, exclamation_count
user_input = input("Введіть текст: ")
processed_text, digit_count, punctuation_count, exclamation_count = process_text(user_input)
print("\nТекст з великою літерою на початку кожного речення:")
print(processed_text)
print("\nКількість цифр у тексті:", digit_count)
print("Кількість розділових знаків у тексті:", punctuation_count)
print("Кількість знаків оклику у тексті:", exclamation_count)