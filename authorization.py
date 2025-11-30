from main import load_key
from cryptography.fernet import Fernet


def authorization(login_input, password_input, fernet):
    with open('passwords.txt', 'r') as password_file:
        for line in password_file.readlines():
            login, encrypted_password = line.strip().split(' | ')
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            if login == login_input and decrypted_password == password_input:
                return True 
    return False


def main(): 
    fernet = load_key()
    while True:
        login = input('Ваш логин: ')
        password = input('Ваш пароль: ')
        if authorization(login, password, fernet):
            print('Вы авторизованы!')
            break
        else:
            print('Пользователя не найдено. Неверный логин или пароль')


if __name__ == "__main__":
    main()

