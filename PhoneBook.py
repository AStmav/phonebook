import csv
from typing import List, Tuple

def main() -> None:
    """
    Основная функция
    """
    contacts: List[List[str]] = read_contacts()

    while True:
        print(">>> Список команд телефонного справочника: <<<")
        print("1. Отобразите существующие контакты")
        print("2. Создайте новый контакт")
        print("3. Редактировать запись")
        print("4. Удалить запись")
        print("5. Поиск записей")
        print("6. Выход")

        choice: str = input("Введите номер команды: ")

        if choice == '1':
            display_contacts(contacts)
        elif choice == '2':
            add_contact(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            search_criteria: str = input("Введите критерии поиска (через запятую): ")
            found_contacts: List[List[str]] = search_contacts(contacts, search_criteria.split(','))
            if found_contacts:
                display_contacts(found_contacts)
            else:
                print("Контакт не найден.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующую команду.")

def read_contacts() -> List[List[str]]:
    """
    Чтение контактов из CSV файла
    """
    contacts: List[List[str]] = []
    with open('contacts.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            while len(row) < 6:
                row.append('')  # Добавляем пустые строки, если не хватает данных
            contacts.append(row)
    return contacts

def display_contacts(contacts: List[List[str]]) -> None:
    """
    Отображение списка контактов
    """
    print("{:<5} {:<15} {:<15} {:<15} {:<20} {:<20} {:<20}".format("Index", "Last Name", "First Name", "Middle Name", "Organization", "Home Phone", "Work Phone"))
    print("="*107)
    for idx, contact in enumerate(contacts):
        if len(contact) >= 6:
            print("{:<5} {:<15} {:<15} {:<15} {:<20} {:<20} {:<20}".format(idx, *contact[:6]))
        else:
            print(f"Контакт с индексом {idx} имеет недостаточно данных для отображения")

def search_contacts(contacts: List[List[str]], search_criteria: List[str]) -> List[List[str]]:
    """
    Поиск контактов по критериям.
    """
    found_contacts: set = set()
    if not search_criteria:
        return contacts
    for contact in contacts:
        for criterion in search_criteria:
            criterion = criterion.strip().lower()
            for field in contact:
                if criterion.lower() in field.lower():
                    found_contacts.add(tuple(contact))
                    break
    return list(found_contacts)

def add_contact(contacts: List[List[str]]) -> None:
    """
    Добавление нового контакта
    """
    with open('contacts.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        contact = input("Введите контакт в формате Фамилия, Имя, Отчество, Название организации, Рабочий телефон, Личный телефон (через запятую): ")
        writer.writerow(contact.split(','))
        contacts.append(contact.split(','))

def edit_contact(contacts: List[List[str]]) -> None:
    """
    Редактирование контакта
    """
    contact_index = int(input("Введите индекс контакта, который вы хотите отредактировать: "))
    new_contact = input("Введите новую информацию о контакте: ")
    contacts[contact_index] = new_contact.split(',')
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

def delete_contact(contacts: List[List[str]]) -> None:
    """
    Удаление контакта
    """
    contact_index = int(input("Введите индекс контакта, который вы хотите удалить: "))
    del contacts[contact_index]
    with open('contacts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

if __name__ == "__main__":
    main()
