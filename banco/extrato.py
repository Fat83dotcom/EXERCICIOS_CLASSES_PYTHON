from typing import List


class Extrato:
    def __init__(self) -> None:
        self.transacoes: List[list] = []

    def extrato(self, numeroconta):
        print(f'Extrato: {numeroconta}')

        for item in self.transacoes:
            print()
