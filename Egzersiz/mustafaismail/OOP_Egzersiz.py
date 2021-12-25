class Hero:
    """
    kahramanların tanımlanabileceği bir yapı oluşturun
    parametre olarak adi,guc,saglik
    darbe,vurma adında iki fonksiyon ile secilen karakterin güçleri 
    ölçüsünde diğer karakterin sağlığında eksiltmesini sağlayalım
    istenildiğinde tek bir fonksiyon ile karakterin durumunu görebilelim
    """

    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health
    

    def __repr__(self):
        return self.name + "Health" + str(self.health)

    def darbe(self):
        self.health -= self.power * 0.2

    def vurma(self):
        self.health -= self.power * 0.1    