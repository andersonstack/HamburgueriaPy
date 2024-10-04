def inputStr(text: str) -> str:
    while True:
        text = input(text)
        if all(not char.isdigit() for char in text):
            return text
        else:
            print("Digite somente texto.\n")  # Mensagem de erro


def inputInt(text: str) -> int:
    while True:
        number = input(text)
        if number.isdigit():
            return int(number)
        else:
            print("Digite apenas númeors inteiros.\n")


def inputFloat(text: str) -> float:
    while True:
        number = input(text)
        newNumber = number.replace(",", ".")
        try:
            numberFloat = float(newNumber)
            return numberFloat
        except ValueError:
            print("Digite apenas número com virgula ou ponto.\n")


if __name__ == '__main__':
    inputFloat("Digite uma quantia: ")
