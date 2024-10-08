from view.styles import printE
from view.screens import clear
import sys


def inputt(text: str) -> str:
    try:
        input_user = input(text)
        return input_user
    except KeyboardInterrupt:
        clear()
        printE("⚠️ Programa interrompido ⚠️")
        sys.exit()


def inputStr(text: str) -> str:
    while True:
        user_input = inputt(text)
        if user_input.replace(" ", "").isalpha():
            return user_input.title()
        else:
            printE("Digite somente texto e espaços")  # Mensagem de erro


def inputInt(text: str) -> int:
    while True:
        number = inputt(text)
        if number.isdigit():
            return int(number)
        else:
            printE("Digite apenas númeors inteiros")


def inputFloat(text: str) -> float:
    while True:
        number = inputt(text)
        newNumber = number.replace(",", ".")
        try:
            numberFloat = float(newNumber)
            return numberFloat
        except ValueError:
            printE("Digite apenas número com virgula ou ponto")


if __name__ == '__main__':
    # inputFloat("Digite um float: ")
    # inputInt("Digite um int: ")
    inputStr("Digite uma str: ")
