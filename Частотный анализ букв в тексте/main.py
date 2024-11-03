# TODO  Напишите функцию count_letters
def count_letters(entered_text:str)->dict:
    dict_letters = {}
    lst_entered_text = list(entered_text.lower())
    for letter in lst_entered_text:
        if letter not in dict_letters.keys():
            if letter.isalpha():
                x = lst_entered_text.count(letter)
                dict_letters[letter] = x
    return dict_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_letters:dict)->dict:
    sum_letters = sum(dict_letters.values())
    for key in dict_letters:
        x = round(dict_letters[key] / sum_letters, 2)
        dict_letters[key] = x
    return dict_letters

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
dict = count_letters(main_str)
freq = calculate_frequency(dict)
for i in freq:
    print(f'{i}: {freq[i]:.2f}')