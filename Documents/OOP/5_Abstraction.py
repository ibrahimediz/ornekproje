from abc import ABC,abstractmethod
class Arac(ABC):
    @abstractmethod
    def yakitTipiSoyle(self):
        pass

# obj = Arac() # TypeError: Can't instantiate abstract class Arac with abstract methods yakitTipiSoyle

# class KaraAraclari(Arac):
#     pass

# objKaraArac = KaraAraclari() #TypeError: Can't instantiate abstract class KaraAraclari with abstract methods yakitTipiSoyle


class KaraAraclari(Arac):
    def yakitTipiSoyle(self):
        print("Benzin")

objKaraArac = KaraAraclari() #TypeError: Can't instantiate abstract class KaraAraclari with abstract methods yakitTipiSoyle
objKaraArac.yakitTipiSoyle()