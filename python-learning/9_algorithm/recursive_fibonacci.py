from functools import lru_cache

@lru_cache(maxsize=None)  # Автоматичне кешування результатів
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Виводимо перші 10 чисел Фібоначчі:
for i in range(10):
    print(fibonacci(i), end=" ")
# Виведе: 0 1 1 2 3 5 8 13 21 34