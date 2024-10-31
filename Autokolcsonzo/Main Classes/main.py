from Autokolcsonzo import Autokolcsonzo
from Szemelyauto import Szemelyauto
from Teherauto import Teherauto

def felhasznaloi_interfesz(kolcsonzo):
    while True:
        print("----------Autókölcsönző Menü----------")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        valasztas = input("Válassz egy opciót(a sorszámát írd be): ")

        if valasztas == "1":
            kolcsonzo.elerhetoAutokListazasa()
            print("\n")
            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            kolcsonzo.autoBerlese(rendszam, datum)
        elif valasztas == "2":
            rendszam = input("Add meg a lemondani kívánt autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            kolcsonzo.berlesLemondasa(rendszam, datum)
        elif valasztas == "3":
            kolcsonzo.berlesekListazasa()
        else:
            print("Ilyen opció nincsen!")

def main():
    kolcsonzo = Autokolcsonzo("Teszt Kölcsönző")

    auto1 = Szemelyauto("ABC-123", "Sedan", 10000, 3, "Kék")
    auto2 = Teherauto("DEF-456", "Teherautó", 20000, 1500)
    auto3 = Szemelyauto("GHI-789", "Kombi", 12000, 5, "Piros")

    kolcsonzo.autok.append(auto1)
    kolcsonzo.autok.append(auto2)
    kolcsonzo.autok.append(auto3)

    kolcsonzo.autoBerlese("ABC-123", "2024-10-20")
    kolcsonzo.autoBerlese("DEF-456", "2024-10-21")
    kolcsonzo.autoBerlese("GHI-789", "2024-10-22")
    kolcsonzo.autoBerlese("ABC-123", "2024-10-23")

    felhasznaloi_interfesz(kolcsonzo)

if __name__ == "__main__":
    main()