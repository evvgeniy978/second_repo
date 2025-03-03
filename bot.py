def parse_input(user_input):
    """
    Розбирає введений користувачем рядок на команду та аргументи.
    Повертає кортеж: команду (у нижньому регістрі) та список аргументів.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Додає новий контакт до словника contacts.
    Аргументи: список [name, phone].
    Повертає повідомлення "Contact added.".
    """
    if len(args) < 2:
        raise ValueError("not enough values to unpack (expected 2, got 0)")
    name, phone = args
    contacts[name.lower()] = phone  # Зберігаємо ім’я в нижньому регістрі
    return "Contact added."

def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    Аргументи: список [username, new_phone].
    Повертає "Contact phone changed." або "Contact not found.".
    """
    if len(args) < 2:
        raise ValueError("not enough values to unpack (expected 2, got 0)")
    username, new_phone = args
    if username.lower() in contacts:
        contacts[username.lower()] = new_phone
        return "Contact phone changed."
    return "Contact not found."

def phone_contact(args, contacts):
    """
    Виводить номер телефону для контакту.
    Аргументи: список [username].
    Повертає номер телефону або "Contact not found.".
    """
    if len(args) < 1:
        raise ValueError("not enough values to unpack (expected 1, got 0)")
    username = args[0].lower()  # Переводимо введене ім’я в нижній регістр
    if username in contacts:
        return contacts[username]
    return "Contact not found."

def show_all_contacts(contacts):
    """
    Виводить усі контакти у форматі "name : phone".
    Якщо контактів немає, повертає "No contacts found.".
    """
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name} : {phone}")
    return "\n".join(result)

def main():
    """
    Основна функція бота. Запускає цикл введення команд.
    """
    contacts = {}  # Словник для зберігання контактів
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            try:
                print(add_contact(args, contacts))
            except ValueError as e:
                print(e)
        elif command == "change":
            try:
                print(change_contact(args, contacts))
            except ValueError as e:
                print(e)
        elif command == "phone":
            try:
                print(phone_contact(args, contacts))
            except ValueError as e:
                print(e)
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()