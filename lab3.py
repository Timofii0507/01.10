print("Введіть елементи списку цілих, розділені пробілами:")
list_str = input()
list_int = [int(x) for x in list_str.split()]
sum = 0
for x in list_int:
    sum += x
average = sum / len(list_int)
print(f"Сума всіх елементів списку: {sum}")
print(f"Середньоарифметичне всіх елементів списку: {average}")
