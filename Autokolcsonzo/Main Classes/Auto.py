from abc import ABC, abstractmethod

class Auto(ABC):
    def __init__(self, rendszam, tipus, berletiDij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berletiDij = berletiDij

    @abstractmethod
    def display_info(self):
        pass