from view.screens import clear
from view.styles import printE
import sys
import re


def inputt(text: str) -> str:
    try:
        input_user = input(text)
        return input_user
    except KeyboardInterrupt:
        clear()
        printE("⚠️ Programa interrompido ⚠️")
        sys.exit()


def inputPhone(text: str) -> str:
    while True:
        user_input = input(text)
        if re.match(r"^\(\d{2}\) \d{4,5}-\d{4}$", user_input):
            return user_input
        else:
            print("Telefone inválido. Use o formato (XX) XXXX-XXXX")


def inputIncompleteAds(text: str) -> str:
    while True:
        user_input = inputt(text)

        if re.match(r"^[A-Za-z\s]+$", user_input):
            return user_input.lower()
        else:
            printE("Digite o endereço corretamente: Rua Número")


def inputDate(text: str) -> str:
    while True:
        user_input = inputt(text)

        if re.match(r"\d{2}/\d{2}/\d{4}", user_input):
            return user_input.replace("/", "_")
        else:
            printE("Data inválida")


def inputAdrs(text: str) -> str:
    while True:
        user_input = inputt(text)

        if re.match(r"^[A-Za-z\s]+/[A-Za-z]{2}$", user_input):
            city, uf = user_input.split("/")
            return f"{city.title()}/{uf.upper()}"
        printE("> Endereço deve estar no formato Cidade/UF")


def inputStr(text: str) -> str:
    while True:
        user_input = inputt(text)

        if re.match(r"^[A-Za-z\s]+$", user_input):
            return user_input.lower()
        else:
            printE("Digite somente texto e espaços")


def inputCPF(text: str) -> str:
    while True:
        user_input = input(text)

        if re.match(r"^\d{11}$", user_input):
            return user_input
        else:
            print("Digite um CPF válido (11 dígitos).")


def inputInt(text: str) -> int:
    while True:
        user_input = inputt(text)

        if re.match(r"^\d+$", user_input):
            return int(user_input)
        else:
            printE("Digite apenas números inteiros")


def inputFloat(text: str) -> float:
    while True:
        user_input = inputt(text)

        user_input = user_input.replace(",", ".")
        if re.match(r"^\d+(\.\d+)?$", user_input):
            return float(user_input)
        else:
            printE("Digite apenas número com vírgula ou ponto")


if __name__ == '__main__':
    # inputFloat("Digite um float: ")
    # inputInt("Digite um int: ")
    inputStr("Digite uma str: ")
