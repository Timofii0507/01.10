print("Введіть елементи списку цілих, розділені пробілами:")
list_str = input()
list_int = [int(x) for x in list_str.split()]
print("Введіть деяке число:")
num = int(input())
count = list_int.count(num)
print(f"Число {num} присутнє в списку {count} разів.")
