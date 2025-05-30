import re
def vasyaFunc(test):
    numbers = re.findall(r'\d+', test)
    expression = [3 * int(x) ** 2 + 5 for x in numbers]
    return f"{expression[0]} + {expression[1]} = {expression[2]}"

def vasyaFunc_without_re(test):
    numbers = []
    for n in test.split():
        if n.isdigit():
            numbers.append(int(n))
    expression = [3 * x ** 2 + 5 for x in numbers]
    return f"{expression[0]} + {expression[1]} = {expression[2]}"

tests = [
    "20 + 22 = 42",
    "0 + 0 = 0",
    "1 + 2 = 3",
    "1000 + 0 = 1000",
    "474747474747 + 5 = 474747474752",]

for test in tests:
    print(vasyaFunc(test))

print(f"\nПроверка без регулярки:")
for test in tests:
    print(vasyaFunc_without_re(test))
