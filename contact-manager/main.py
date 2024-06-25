import os.path

import tabulate


class Phonebook:
    def __init__(self, file):
        if os.path.exists(file):
            self.data = file
            self.flag = True
        else:
            print('ERROR: FileNotFound')
            self.flag = False

    def show_contacts(self) -> None:
        if not self.flag:
            return
        contacts_table: list[list[str]] = []
        with open(self.data) as file:
            for line in file.readlines():
                contacts_table.append([line.split(' ')[0], line.split(' ')[1], line.split(' ')[2]])
        print(tabulate.tabulate(contacts_table, tablefmt='pretty', stralign='center', headers=['ID', 'Name', 'Phone']))

    def add_contact(self, new_contact_name: str, new_contact_phone_number: str) -> None:
        if not self.flag:
            return
        contacts_number = ''
        with open(self.data, 'r') as file:
            contacts_number = file.readlines()[-1].split(' ')[0]
        with open(self.data, 'a') as file:
            file.write(str(contacts_number + 1) + ' ' + new_contact_name + ' ' + new_contact_phone_number + '\n')

    def edit_contact_name(self, contact_id: int, contact_new_name: str):
        if not self.flag:
            return
        with open(self.data, 'r') as file:
            contacts = {line.split(' ')[0]: [line.split(' ')[1], line.split(' ')[2]]
                        for line in file.readlines()}
        contact_id = str(contact_id)
        contacts[contact_id][0] = contact_new_name
        with open(self.data, 'w') as file:
            for key, value in contacts.items():
                file.write(key + ' ' + value[0] + ' ' + value[1])

    def edit_contact_phone_number(self, contact_id: int, contact_new_phone_number: str) -> None:
        if not self.flag:
            return
        with open(self.data, 'r') as file:
            contacts = {line.split(' ')[0]: [line.split(' ')[1], line.split(' ')[2]]
                        for line in file.readlines()}
        contact_id = str(contact_id)
        contacts[contact_id][1] = contact_new_phone_number
        with open(self.data, 'w') as file:
            for key, value in contacts.items():
                file.write(key + ' ' + value[0] + ' ' + value[1])

    def delete_contact(self, contact_id) -> None:
        if not self.flag:
            return
        with open(self.data, 'r') as file:
            contacts = {line.split(' ')[0]: [line.split(' ')[1], line.split(' ')[2]]
                        for line in file.readlines()}
        contact_id = str(contact_id)
        with open(self.data, 'w') as file:
            for key, value in contacts.items():
                if key < contact_id:
                    file.write(key + ' ' + value[0] + ' ' + value[1])
                elif key > contact_id:
                    file.write(str(int(key) - 1) + ' ' + value[0] + ' ' + value[1])


def main():
    # print('Выберите действие:\n'
    #       '1. Просмотреть контакты\n'
    #       '2. Добавить контакт\n'
    #       '3. Редактировать контакт\n'
    #       '4. Удалить контакт\n'
    #       '5. Выход')
    # inp = int(input('>> '))
    inp = -1
    phonebook = Phonebook('data.txt')
    while inp != 5:
        print('Выберите действие:\n'
              '1. Просмотреть контакты\n'
              '2. Добавить контакт\n'
              '3. Редактировать контакт\n'
              '4. Удалить контакт\n'
              '5. Выход')
        inp = int(input('>> '))
        match inp:
            case 1:
                phonebook.show_contacts()
            case 2:
                new_name = input('Введите имя контакта: ')
                new_phone_number = input('Введите номер контакта: ')
                phonebook.add_contact(new_name, new_phone_number)
            case 3:
                contact_to_edit_id = int(input('Введите ID контакта: '))
                print('Что хотите редактировать?\n'
                      '1 - имя контакта\n'
                      '2 - номер контакта')
                key = input('>> ')
                if key == 1:
                    edited_name = input('Введите новое имя контакта: ')
                    phonebook.edit_contact_name(contact_to_edit_id, edited_name)
                elif key == 2:
                    edited_phone_number = input('Введите новый номер телефона контакта: ')
                    phonebook.edit_contact_phone_number(contact_to_edit_id, edited_phone_number)
            case 4:
                contact_to_delete_id = int(input('Введите ID контакта: '))
                phonebook.delete_contact(contact_to_delete_id)
    else:
        print('Спасибо за пользование!')

if __name__ == '__main__':
    main()
