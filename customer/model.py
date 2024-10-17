from controller.inputs import inputStr, inputInt, inputIncompleteAds
from typing import Dict, Union


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
            table: int | None = None) -> Dict[str, Union[int, str]]:
        """
        Creates a new client.

        Parameters:
        name (str): The name of the client
        adress (str | None): The adress of the client (optional)
        table (int | None): The table of the client (optional)

        Returns:
        Dict[str, Union[int, str]]: A dictionary with the name,
        adress or table of the client
        """
        ...
        name = inputStr("Nome: ")
        if adress is not None and table is None:
            adress = inputIncompleteAds("Endereço: ")
            return {"name": name, "adress": adress}
        else:
            table = inputInt("Mesa: ")
            return {"name": name, "table": table}
