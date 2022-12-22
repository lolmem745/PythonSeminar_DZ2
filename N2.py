def numInput(message):
    is_ok = True
    while is_ok:
        try:
            number = int(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number

def multi(num):
    if num ==1:
        return 1
    else:
        return num*multi(num-1)

number = numInput("Введите число: ")

list = []
for i in range (1,number + 1):
    list.append(multi(i))

print(f"Произведения чисел от 1 до {number}:  {list}")