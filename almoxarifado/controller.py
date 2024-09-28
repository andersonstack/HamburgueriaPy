from data.saveJson import SaveJson
from typing import Dict


class Almoxarifado:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.quantity = 0
        self.almoxarifado = SaveJson("almoxarifado.json")
        self.load_almoxarifado = self.almoxarifado.load_json()

    def add_buy(self, name: str, quantity: int) -> int:
        if self.load_almoxarifado:
            id_ = len(self.load_almoxarifado) + 1
        else:
            id_ = 1

        add_buy = self._verify_buy(name)
        if len(add_buy) > 0:
            for key in add_buy:
                self._udpate_quantity(key, quantity)
                return key

        new_item = {id_: [name, quantity]}
        self.almoxarifado.modify_json(data=new_item)
        return id_

    def view_buy(self, id) -> dict:
        return {}

    def delete_buy(self, id) -> bool:
        return True

    def edit_buy(self, id) -> dict:
        return {}

    def _verify_buy(self, name) -> Dict[int, list]:
        for cod, det in self.load_almoxarifado.items():
            if name.upper() == det[0].upper():
                return {cod: det}
        return {}

    def _udpate_quantity(self, key, quantity):
        if key in self.load_almoxarifado:
            self.load_almoxarifado[key][1] += quantity
            self.almoxarifado.modify_json(self.load_almoxarifado)
