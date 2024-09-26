def add_digits_to_set(char_set):
    digit_set = {str(i) for i in range(10)} 
    try:
        #додаємо множину цифр до початкової множини символів
        result_set = char_set.union(digit_set)
        print("Результат операції об'єднання множин:")
        print(result_set)
    except TypeError:
        char_list = list(char_set)
        digit_list = list(digit_set)    
        #додавання списків
        result_list = char_list + digit_list       
        #результат назад у множину
        result_set = set(result_list)
        print("Результат операції після перетворення на список:")
        print(result_set)
char_set = {'c', 'd'}
add_digits_to_set(char_set)