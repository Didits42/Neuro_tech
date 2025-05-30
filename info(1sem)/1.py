#print(465786%5) -> 1 (;)
#print(465786%4) -> 2 (-{)
#print(465786%7) -> 6 (P)
# ;-{P

import re

tests = [
    "Текст без смайликов",
    "Смотрите! Смайлик: ;-{P",
    ";-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P;-{P",
    ";-{Phjede;-{Pekpp[sldjndw[wp---;-{-ejek;-{Psdlf;dslp;{Prj",
    ";-;---{P{P;;-{P-;-;-{P-;-{P;--;-{P-{P{P;-{;-{PP{;-{P-P;-{P;-{P"
]


while True:
    print("Выберите тест (0-4) или 'w', чтобы ввести свой текст для подсчета:")
    n = input("Введите: ")

    if n == 'w':
        text = input("Введите ваш текст: ")
        break
    elif n in ['0', '1', '2', '3', '4']:
        text = tests[int(n)]
        break
    else:
        print("Ошибка. Нужно ввести 0-4 или w. Введите еще раз...")
        continue

def count_without_re(text):
    count = 0
    i = 0
    while i < len(text) - 3:
        if text[i] == ';' and text[i + 1] == '-' and text[i + 2] == '{' and text[i + 3] == 'P':
            count += 1
            i += 4
        else:
            i += 1
    return count

count1 = len(re.findall(';-{P', text))
count2 = count_without_re(text)

print(f"\nПроанализированный текст: {text}")
print(f"Найдено смайликов (с регулярным выражением): {count1}")
print(f"Найдено смайликов (без регулярного выражения): {count2}")