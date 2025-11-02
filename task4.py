from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
    
# Створюємо декоратор для обробки помилок вводу
def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # Обробка помилки, коли контакт не знайдено
        except KeyError:
            return "Contact not found, please check the name."
        # Обробка помилки, коли недостатньо аршументів для імені та телефону
        except ValueError:
            return "Give me name and phone please."
        # Обробка помилки, коли відсутнє ім'я для пошуку
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    # Розбиваємо рядок введення на команду та аргументи
    cmd, *args = user_input.split()
    # Приводимо команду до нижнього регістру для уніфікації
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    # Додаємо контакт: потрібно два аргументи - ім'я та телефон
    # якщо аргументів менше 2 - буде ValueError
    name, phone = args  
    # записуємо у словник
    contacts[name] = phone  
    return "Contact added."

@input_error
def change_contact(args, contacts):
    # Змінюємо номер телефону у існуючого контакту
    name, phone = args
    if name not in contacts:
        # якщо немає такого контакту - виняток
        raise KeyError  
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    # Показуємо номер телефону по імені
    # якщо args пустий — буде IndexError
    name = args[0]  
    if name not in contacts:
        # якщо контакт не знайдено - виняток
        raise KeyError  
    return contacts[name]

def show_all(contacts):
    # Показуємо всі контакти у списку
    if not contacts:
        return "Contact list is empty."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    # Основна функція - цикл прийому команд і виклик функцій
    # словник для збереження контактів
    contacts = {}  
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            # Якщо користувач не ввів команду
            print("Invalid command.")
            continue
        # Обробка введеною команди
        command, args = parse_input(user_input)

        # Обробка команд бота
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
