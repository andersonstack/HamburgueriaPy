from data.model import SaveDatabase  # type: ignore
from typing import Dict
from warehouse.view import infor_warehouse


class Warehouse:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.quantity = 0
        self.warehouse = SaveDatabase("almoxarifado.json")
        self.load_warehouse = self.warehouse.load_json()

    def add_buy(self, name: str, quantity: int) -> int:
        if self.load_warehouse:
            last_key = int(list(self.load_warehouse.keys())[-1])
            id_ = last_key + 1
        else:
            id_ = 1

        add_buy = self._verify_buy(name)
        if len(add_buy) > 0:
            for key in add_buy:
                self._udpate_quantity(key, quantity)
                return key

        new_item = {id_: [name, quantity]}
        self.warehouse.modify_json(data=new_item)
        return id_

    def view_warehouse(self) -> None:
        infor_warehouse(self.load_warehouse, "Items em almoxarifado:")

    def view_buy(self, ids: str) -> bool:
        if ids not in self.load_warehouse:
            return False

        new_dict = {ids: self.load_warehouse[ids]}
        infor_warehouse(new_dict, "")
        return True

    def delete_buy(self, ids: str) -> None:
        del self.load_warehouse[ids]
        new_dict = self.load_warehouse
        self.warehouse.update_json(new_dict)

    def edit_buy(self, ids: str, name: str) -> None:
        for key, value in self.load_warehouse.items():
            if key == ids:
                self.load_warehouse[ids] = [name, value[1]]
                self.warehouse.update_json(self.load_warehouse)

    def _verify_buy(self, name) -> Dict[int, list]:
        for cod, det in self.load_warehouse.items():
            if name.upper() == det[0].upper():
                return {cod: det}
        return {}

    def _udpate_quantity(self, key, quantity) -> None:
        if key in self.load_warehouse:
            self.load_warehouse[key][1] += quantity
            self.warehouse.modify_json(self.load_warehouse)


if __name__ == '__main__':
    buy = Warehouse()
    buy.edit_buy(str(5), "Queijo")
