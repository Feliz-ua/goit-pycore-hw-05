from colorama import init, Fore
init (autoreset=True)
# Оголошення функції caching_fibonacci
def caching_fibonacci():
    # Створюємо порожній словник для результатів
    cache={}
    # Оголошуємо внутрішню функцію для обчислення n-ого числа Фібоначчі
    def fibonacci (n):
        # Якщо n меньше або дорівнює 0 - повертаємо 0
        if n<=0:
            return 0
        # Якщо n дорівнює 1 - повертаємо 1
        if n==1:
            return 1
        #  Якщо n все має резкльтат у кєші - повертаємо його
        if n in cache:
            return cache[n]
        # Обчислюємо число Фібоначчі та зберегаємо в кеші
        cache[n]=fibonacci(n-1)+fibonacci(n-2)
        # Повертаємо обчислення та закешоване значення
        return cache[n]
     # Повертаємо обчислення та закешоване значення
    return fibonacci
# Створюємо функцію fibonacci з записом у словник cache 
fib=caching_fibonacci()
# Отримуємо введений номер числа Фібоначчі
n=int(input("Введіть номер числа Фібоначчі для обчислення: "))
# Робимо обчислення та виводим результат
print(f"Число Фібоначчі під номером {n}: {Fore.GREEN}{fib(n)}{Fore.RESET}")

