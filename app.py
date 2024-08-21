from abc import ABC,abstractmethod

class Veiculo(ABC):
    def __init__(self,marca,modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f'Marca: {self._marca} -  Modelo: {self._modelo} - Status: {status}'

    @abstractmethod
    def ligar(self):
        pass
    
    
class Carro(Veiculo):
    def __init__(self,marca,modelo,portas,cor):
        super().__init__(marca,modelo)
        self._portas = portas
        self._cor = cor
    
    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f'Marca: {self._marca} -  Modelo: {self._modelo} - Status: {status} - Quantidade de Portas: {self._portas} - Cor: {self._cor}'

    def ligar(self):
        pass
    
class Moto(Veiculo):
    def __init__(self,marca,modelo,categoria):
        super().__init__(marca,modelo)
        self._categoria = categoria

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f'Marca: {self._marca} -  Modelo: {self._modelo} - Status: {status} - Categoria: {self._categoria}'
    
    def ligar(self):
        pass