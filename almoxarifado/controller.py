from data.saveJson import SaveJson


class Almoxarifado:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.quantity = 0
        self.almoxarifado = SaveJson("almoxarifado.json")
        self.len_almoxarifado = self.almoxarifado.load_json()

    def add_buy(self, name: str, quantity: int) -> int:
        # Gerar um novo ID baseado no maior ID existente
        if self.len_almoxarifado:
            id_ = len(self.len_almoxarifado) + 1
        else:
            id_ = 1  # Começa com 1 se não houver itens

        new_item = {id_: [name, quantity]}
        self.almoxarifado.modify_json(data=new_item)
        return id_

    def view_buy(self, id) -> dict:
        return {}

    def delete_buy(self, id) -> bool:
        return True

    def edit_buy(self, id) -> dict:
        return {}
