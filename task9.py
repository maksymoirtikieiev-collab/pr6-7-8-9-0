import random
import time

def generate_numbers(size):
    numbers = []

    for _ in range(size):
        numbers.append(random.randint(-10000, 10000))

    return numbers

def method_1(numbers):
    data = numbers.copy()
    n = len(data)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True

        if not swapped:
            break

    return data[5]

def method_2(numbers):
    largest = []

    for number in numbers:
        
        position = 0

        while position < len(largest) and largest[position] >= number:
            position += 1

        
        if position < 6:
            largest.insert(position, number)

            if len(largest) > 6:
                largest.pop()

    return largest[5]


def method_3(numbers):
    data = numbers.copy()

    for _ in range(6):
        maximum = max(data)
        data.remove(maximum)

    return maximum


def measure_time(method, numbers):
    times = []
    result = None

    for _ in range(3):
        start = time.perf_counter()

        result = method(numbers)

        finish = time.perf_counter()
        elapsed_ms = (finish - start) * 1000
        times.append(elapsed_ms)

    average = sum(times) / len(times)
    return result, average, times

sizes = [
    10_000,
    
]

methods = [
    ("Сортування", method_1),
    ("Шість найбільших", method_2),
    ("Пошук максимуму", method_3),
]

for size in sizes:
    print("\nКількість чисел:", size)
    numbers = generate_numbers(size)

    for name, method in methods:
        result, average, times = measure_time(method, numbers)

        print("\nСпосіб:", name)
        print("Шостий найбільший елемент:", result)
        print("Час кожного запуску, мс:")

        for i, value in enumerate(times, start=1):
            print(f"  Запуск {i}: {value:.2f}")

        print(f"Середній час: {average:.2f} мс")