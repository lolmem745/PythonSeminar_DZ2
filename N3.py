def numInput(message):
    is_ok = True
    while is_ok:
        try:
            number = int(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number

def formula(num):
    return (1 + 1/num) ** num


number = numInput("Введите число: ")

list =[]
sum = 0
for i in range(1, number+1):
    list.append(round(formula(i),4))
    sum+=list[i-1]

print(f"Сумма элементов списка - {list} равна {sum}.")