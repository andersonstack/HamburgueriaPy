from view.styles import printE


def inputStr(text: str) -> str:
    while True:
        user_input = input(text)
        if user_input.isalpha():
            return user_input.title()
        else:
            printE("Digite somente texto")  # Mensagem de erro


def inputInt(text: str) -> int:
    while True:
        number = input(text)
        if number.isdigit():
            return int(number)
        else:
            printE("Digite apenas númeors inteiros")


def inputFloat(text: str) -> float:
    while True:
        number = input(text)
        newNumber = number.replace(",", ".")
        try:
            numberFloat = float(newNumber)
            return numberFloat
        except ValueError:
            printE("Digite apenas número com virgula ou ponto")


if __name__ == '__main__':
    inputFloat("Digite um float: ")
    inputInt("Digite um int: ")
    inputStr("Digite uma str: ")
