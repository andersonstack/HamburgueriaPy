def cabecalho(title: str) -> None:
    line = "=" * (len(title) + 2)
    print(f"=|{line}|=")
    print(f" | {title} |")
    print(f"=|{line}|=")


if __name__ == "__main__":
    cabecalho("TELA PRINCIPAL")
    cabecalho("ALMOXARIFADO")
    cabecalho("FUNCIONARIOS")
    cabecalho("CLIENTES")
    cabecalho("RELATORIOS")
    cabecalho("INFORMAÇÕES")
