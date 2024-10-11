class Client:
    def __init__(self):
        """
        Constructor method.

        Parameters:
        self (Client): The instance of the class
        """
        self.table = 0
        self.name = ""
        self.adress = ""

    def client(
            self, name: str,
            adress: str | None = None,
            table: int | None = None) -> None:
        """
        Creates a new client.

        Parameters:
        name (str): The name of the client
        adress (str | None): The adress of the client (optional)
        table (int | None): The table of the client (optional)

        Returns:
        None
        """
        ...
