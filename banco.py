class Banco:

    def __init__(self, endereco: str):
        self.endereco = endereco

        @property
        def endereco(self):
            return self.__endereco

        @endereco.setter
        def endereco(self, endereco: str) -> None:
            self.__endereco = endereco

