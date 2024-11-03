# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, dividing_sign=","):
    common_list = []
    first = first.split(dividing_sign)
    second = second.split(dividing_sign)
    for i in first:
        for j in second:
            if j == i:
                common_list.append(j)
    common_list.sort()
    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_surnames = find_common_participants(first=participants_first_group,
                                           second=participants_second_group,
                                           dividing_sign="|")
print(common_surnames)
