# 冒泡排序
def bubble_sort(num_list):
    for i in range(0, len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
                continue
    return num_list


# 选择排序
def select_sort(num_list):
    l = len(num_list)
    for i in range(l):
        min_index = i
        for j in range(i + 1, l):
            if num_list[j] < num_list[min_index]:
                min_index = j
        if min_index != i:
            num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list


# 插入排序
def insert_sort(num_list):
    l = len(num_list)
    for i in range(1, l):
        for j in range(0, i):
            if num_list[j-1] < num_list[j]:
                num_list[j-1], num_list[j] = num_list[j-1], num_list[j]


data = [2, 4, 3, 3, 11, 5, 10, 8, 6]
print(bubble_sort(data))
print(select_sort(data))
