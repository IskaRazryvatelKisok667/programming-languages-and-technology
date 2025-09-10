lst = [1, 6, 9, 3, 0]
print("Исходный список:", lst)
print("Обратный список:", lst[::-1])
def list_sort(lst):
    return sorted(lst, key=abs, reverse=True)
nums = [3, -10, 5, -2, 7, -8]
print("Список:", nums)
print("Сортировка по убыванию абсолютных значений:", list_sort(nums))
def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
arr = [10, 20, 30, 40, 50]
print("До:", arr)
print("После:", change(arr)) 