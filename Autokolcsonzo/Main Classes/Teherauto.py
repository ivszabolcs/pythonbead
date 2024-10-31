from Auto import Auto

class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, maxTeherbiras):
        super().__init__(rendszam, tipus, berletiDij)
        self.maxTeherbiras = maxTeherbiras

    def display_info(self):
        print(f"Teherautó - Rendszáma: {self.rendszam}, Típusa: {self.tipus}, Bérleti díja: {self.berletiDij} ft, Maximum teherbírása: {self.maxTeherbiras} kg")