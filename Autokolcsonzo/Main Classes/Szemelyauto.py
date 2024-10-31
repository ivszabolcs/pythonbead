from Auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berletiDij, ulesekSzama, szin):
        super().__init__(rendszam, tipus, berletiDij)
        self.ulesekSzama = ulesekSzama
        self.szin = szin

    def display_info(self):
        print(f"Személyautó - Rendszáma: {self.rendszam}, Típusa: {self.tipus}, Bérleti díja: {self.berletiDij} ft, Színe: {self.szin}")