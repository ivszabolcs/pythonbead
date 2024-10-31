class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum
        self.ar = auto.berletiDij

    def display_info(self):
        print(f"Bérlés - Autó: {self.auto.rendszam}, Dátum: {self.datum}, Ár: {self.ar} ft")