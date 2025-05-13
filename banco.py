class Banco:

    def __init__(self, endereco: str):
        self.endereco = endereco

        @property
        def endereco(self):
            return self.__endereco

        @endereco.setter
        def endereco(self, endereco: str) -> None:
            if not isinstance(endereco, str):
                raise TypeError("O tipo de endereco deve ser string")

            if endereco is None or endereco == "":
                raise ValueError("O endereço deve possuir caracters")

            if len(endereco) < 3:
                raise ValueError("O endereco deve ter mais 3 caracters")

            self.__endereco = endereco

