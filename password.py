def enumeration(number):
    numbers = ""
    for i in range(1, number+1):
        for k in range(i+1, number+1):
            num_sum = i + k
            if number % num_sum == 0:
                numbers += f"{i}{k}"

    return numbers

number = int(input("Введите ваше число: "))

result = enumeration(number)
print(f"Пароль числа {number}: {result}")
