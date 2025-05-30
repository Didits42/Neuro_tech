import re

def checker(text):
    lines = re.split(r'\s*/\s*', text.strip())

    if len(lines) != 3:
        return "Не хайку. Должно быть 3 строки."

    def count_vowels(s):
        return len(re.findall(r'[аеёиоуыэюяАЕЁИОУЫЭЮЯ]', s))

    vowels_num = [count_vowels(line) for line in lines]
    if vowels_num == [5, 7, 5]:
        return "Хайку!"
    else:
        return "Не хайку."


def checker_without_re(text):
    lines = [line.strip() for line in text.split('/')]

    if len(lines) != 3:
        return "Не хайку. Должно быть 3 строки."

    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"

    def count_vowels(s):
        count = 0
        for ch in s:
            if ch in vowels:
                count += 1
        return count

    vowels_num = [count_vowels(line) for line in lines]

    if vowels_num == [5, 7, 5]:
        return "Хайку!"
    else:
        return "Не хайку."


inputs = [
    "Вечер за окном. / Еще один день прожит. / Жизнь скоротечна...",
    "Просто текст",
    "Как вишня расцвела! / Она с коня согнала / И князя-гордеца."
]

for text in inputs:
    print(checker(text))

print(f"\nПроверка без регулярки:")

for text in inputs:
    print(checker_without_re(text))