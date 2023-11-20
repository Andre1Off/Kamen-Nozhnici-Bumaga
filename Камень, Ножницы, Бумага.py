import sys
import random

print("Камень, Ножницы, Бумага 1, 2, 3!")
a = input()
letters_list: list[str] = ["Камень", "Ножницы", "Бумага"]
random_index = random.randint(0, len(letters_list) - 1)
print(letters_list[random_index])

if a == "Камень" and letters_list[random_index] == 'Камень' or a == "камень" and letters_list[random_index] == 'Камень':
    print('Ничья')
elif a == "Ножницы" and letters_list[random_index] == 'Ножницы' or a == "ножницы" and letters_list[random_index] == 'Ножницы':
    print('Ничья')
elif a == "Бумага" and letters_list[random_index] == 'Бумага' or "бумага" and letters_list[random_index] == 'Бумага':
    print('Ничья')
elif a == "Камень" and letters_list[random_index] == 'Ножницы' or a == "камень" and letters_list[random_index] == 'Ножницы':
    print('Ты победил!!!')
elif a == "Камень" and letters_list[random_index] == 'Бумага' or a == "камень" and letters_list[random_index] == 'Бумага':
    print('Ты проиграл')
elif a == "Ножницы" and letters_list[random_index] == 'Камень' or a == "ножницы" and letters_list[random_index] == 'Камень':
    print('Ты проиграл')
elif a == "Ножницы" and letters_list[random_index] == 'Бумага' or a == "ножницы" and letters_list[random_index] == 'Бумага':
    print('Ты победил!!!')
elif a == "Бумага" and letters_list[random_index] == 'Ножницы' or a == "бумага" and letters_list[random_index] == 'Ножницы':
    print('Ты проиграл')
elif a == "Бумага" and letters_list[random_index] == 'Камень' or a == "бумага" and letters_list[random_index] == 'Камень':
    print('Ты победил!!!')
else:
    print('ошибка')
    sys.exit()