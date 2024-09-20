import json
import os


class SaveJson:
    def __init__(self, name_file) -> None:
        self.path = os.path.join("./data/arquivos_json")
        os.makedirs(self.path, exist_ok=True)
        self.file = os.path.join(self.path, name_file)

    def create_json(self, data) -> None:
        if os.path.exists(self.file):
            with open(self.file, 'r') as arq:
                try:
                    existing_data = json.load(arq)
                except json.JSONDecodeError:
                    existing_data = {}
        else:
            existing_data = {}

        existing_data.update(data)

        with open(self.file, "w") as arq:
            json.dump(existing_data, arq, indent=1)


if __name__ == "__main__":

    arq = {}

    arq["COCA"] = 200
    save_json = SaveJson('data.json')
    save_json.create_json(arq)

    for keys, values in arq.items():
        print(keys, values)
