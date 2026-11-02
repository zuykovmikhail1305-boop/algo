import time as time_module
from functools import wraps

import matplotlib.pyplot as plt

sizes = [10, 100, 1_000, 10_000, 100_000, 1_000_000, 2_500_000, 7_500_000, 10_000_000, 25_000_000, 40_000_000, 50_000_000, 60_000_000, 75_000_000,100_000_000]
lists = {size: list(range(size)) for size in sizes}
dicts = {size: dict.fromkeys(values) for size, values in lists.items()}

def time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time_module.time()
        result = func(*args, **kwargs)
        end_time = time_module.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result, execution_time

    return wrapper

@time
def search_in_list(arr, value):
    for i in arr:
        if i == value:
            return True
    return False

@time
def search_in_dict(d, key):
    return d[key]


list_times = []
dict_times = []

for size in sizes:
    value = size - 1
    _, list_time = search_in_list(lists[size], value)
    _, dict_time = search_in_dict(dicts[size], value)
    list_times.append(list_time)
    dict_times.append(dict_time)
    print("================================================================")


plt.figure(figsize=(10, 6))

x = [f"{size:,}" for size in sizes]
y1 = list_times
y2 = dict_times

plt.plot(x, y1, marker='o', label='List Search Time')
plt.plot(x, y2, marker='o', label='Dict Search Time')
plt.title('Search Time Comparison: List vs Dict')
plt.yscale('log')
plt.xlabel('Number of Elements')
plt.ylabel('Execution Time (seconds)')
plt.show()
