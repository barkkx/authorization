import os
from cryptography.fernet import Fernet


def write_key(file_name):
    if not os.path.exists(file_name):
        key = Fernet.generate_key()
        with open(file_name, "wb") as secret_key:
            secret_key.write(key)
        print('Пароль создан и сорханен!')
        return key
    else:
        print('Пароль уже создан')
        with open(file_name, 'rb') as secret_key:
            return secret_key.read()


def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
    return Fernet(key)


def add(file_load):
    login = input('Введите логин: ')
    password = input('Введите пароль: ')
    encrypted_pass = file_load.encrypt(password.encode())
    with open('passwords.txt', 'a') as file:
        file.write(f"{login} | {encrypted_pass.decode()}\n")


def view(file_load):
    with open('passwords.txt', 'r') as file:
        for line in file:
            login, encrypted_pass = line.strip().split('|')
            password = file_load.decrypt(encrypted_pass.encode()).decode()
            print(f'Логин: {login} | Пароль: {password}')


def main():
    file_name = "key.key"
    key = write_key(file_name)
    file_load = load_key()

    while True:
        choice = input('Выберите действие(1-3): 1.Существующие пароли, 2.Добавить новый пароль, 3.Выйти: ').strip()

        if choice == '1':
            view(file_load)
        elif choice == '2':
            add(file_load)
        elif choice == '3':
            print('Выход из программы...')
            break
        else:
            print('Ошибка, попробуйте еще раз.')


if __name__ == "__main__":

    main()
