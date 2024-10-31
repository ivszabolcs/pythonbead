from datetime import datetime
from Berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def autoBerlese(self, rendszam, datum):
        if not self.datumEll(datum):
            print("Érvénytelen dátum formátum. Használj YYYY-MM-DD formátumot.")
            return

        auto = next((auto for auto in self.autok if auto.rendszam == rendszam), None)
        if not auto:
            print("Az autó nem található.")
            return

        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                print(f"A(z) ({rendszam}) rendszámú autó már foglalt ezen a napon: {datum}")
                return

        berles = Berles(auto, datum)
        self.berlesek.append(berles)
        print(f"Sikeresen lefoglalta az autót: {rendszam} a(z) {datum} dátumra.")

    def berlesLemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print(f"Sikeresen lemondta a bérlést a ({rendszam}) autóra")
                return
        print("Nem található ilyen bérlés")

    def berlesekListazasa(self):
        if not self.berlesek:
            print("Jelenleg nincsen kibérelt autó")
        for berles in self.berlesek:
            berles.display_info()

    def elerhetoAutokListazasa(self):
        print("\nElérhető autók:")
        elerhetoAutok = [auto for auto in self.autok]
        if not elerhetoAutok:
            print("Nincsen szabad autó")
        else:
            for auto in elerhetoAutok:
                auto.display_info()

    def datumEll(self, datum):
        try:
            datetime.strptime(datum, '%Y-%m-%d')
            return True
        except ValueError:
            return False