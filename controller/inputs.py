def inputStr(text: str) -> str:
    while True:
        text = input(text)
        if all(not char.isdigit() for char in text):
            return text
        else:
            print("Digite somente texto.\n")  # Mensagem de erro


if __name__ == '__main__':
    ...