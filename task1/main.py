def split_list(lst, split_value):
    less_or_equal = []
    greater = []  
    for element in lst:
        if element <= split_value:
            less_or_equal.append(element)
        else:
            greater.append(element)
    return less_or_equal, greater
#fункція для отримання списку від користувача
def input_list():
    user_input = input("Введіть елементи списку через пробіл: ")
    #перетворюємо рядок у список цілих чисел
    lst = list(map(int, user_input.split()))
    return lst
if __name__ == "__main__":
    lst = input_list()
    split_value = int(input("Введіть значення для розбиття: "))
    less_or_equal, greater = split_list(lst, split_value)
    print(f"Елементи, менші або рівні {split_value}: {less_or_equal}")
    print(f"Елементи, більші за {split_value}: {greater}")
