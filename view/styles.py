def printE(text: str) -> None:
    print(f"\033[1;31;41m{text:^114}\033[m")


def printS(text: str) -> None:
    print(f"\033[1;30;42m{text:^114}\033[m")


def printW(text: str) -> None:
    print(f"\033[1;33;43m{text:^114}\033[m")


if __name__ == '__main__':
    printE("Error")
    printS("Sucesso")
    printW("Wait")
