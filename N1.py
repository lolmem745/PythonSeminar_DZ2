def numInput(message):
    is_ok = True
    while is_ok:
        try:
            number = float(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number


def sumOfDigits(number):
    sum = 0
    for i in str(number):
        if i != ".":
            sum += int(i)
    return sum


number = numInput("Введите вещественное число: ")

print(f"Сумма цифр: {sumOfDigits(number)}")
