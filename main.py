import random
import timeit

# Size of the testing arrays
sizes = [100, 200, 300, 400, 500]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def generate_random_data(size):
    return [random.randint(1, 10000) for _ in range(size)]

def generate_sorted_data(size):
    return list(range(size))

def generate_reverse_sorted_data(size):
    return list(range(size, 0, -1))

def generate_uniform_data(size):
    value = random.randint(1, 10000)
    return [value for _ in range(size)]

def measure_sort_time(sort_func, data):
    copied_data = data.copy()
    timer = timeit.Timer(lambda: sort_func(copied_data))
    return min(timer.repeat(repeat=3, number=1))

data_types = {
    'Random': generate_random_data,
    'Sorted': generate_sorted_data,
    'Reverse Sorted': generate_reverse_sorted_data,
    'Uniform': generate_uniform_data
}

# Launching
results = {}
for size in sizes:
    results[size] = {}
    for data_type_name, data_generator in data_types.items():
        data = data_generator(size)
        results[size][data_type_name] = {
            'Insertion Sort': measure_sort_time(insertion_sort, data),
            'Merge Sort': measure_sort_time(merge_sort, data),
            'Timsort': measure_sort_time(sorted, data)
        }

# Results
for size in sizes:
    print(f"\nSize: {size}")
    for data_type, timings in results[size].items():
        print(f"  Data type: {data_type}")
        for sort_name, time in timings.items():
            print(f"    {sort_name}: {time:.6f} seconds")
