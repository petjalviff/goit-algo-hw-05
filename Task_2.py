import random

def binary_search(arr, target):
    iterations = 0
    low=0
    high = len(arr) - 1
    mid=0
    upper_bound = None

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]
        iterations += 1

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            upper_bound = mid_value
            high = mid - 1
        else:
            upper_bound = mid_value
            break

    return iterations, upper_bound


#Своримо рамдомний список для даслідження і відразу відсортуємо його
def generate_random_array(size):
    return [round(random.uniform(1.0, 50.0), 2) for _ in range(size)]
size=25
random_array=generate_random_array(size)
# print(random_array)
random_array.sort()
print("відсортований список - ",random_array)
search_value=round(random.uniform(1.0, 50.0), 2)
print("Шуканй елемент - ",search_value)

iterations, upper_bound = binary_search(random_array, search_value)

if upper_bound is not None:
    print(f"Елемент {search_value} знайдено за {iterations} ітерацій. Верхня межа: {upper_bound}")
else:
    print(f"Елемент {search_value} не знайдено у масиві.")