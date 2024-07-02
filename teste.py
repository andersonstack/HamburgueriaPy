from data import *
from views import *

for data, compra in compras.items():
    print_alinhado("\033[1mDATA:",f"{data}\033[m")
    print("=" * 50)
    for detalhes in compra:
        print_alinhado("Hora:",detalhes['hora'])
        print_alinhado("Nome:", detalhes['nome'])
        print_alinhado("Quantidade:", f"{detalhes['quantidade']} unidades")
        print_alinhado("Preço",f"R$ {detalhes['preço']}")
        print("=" * 50)
