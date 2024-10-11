class Client:
    def __init__(self):
        self.name = ""
        self.adress = ""

    def client(
            self, name: str,
            adress: str | None = None,
            table: int | None = None) -> None:
        ...
