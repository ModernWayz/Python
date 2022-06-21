class MobielToestel():
    def __init__(self):
        pass

    def kies_nummer(self, nummer):
        return f'Draait: {nummer}'


class SmartPhone(MobielToestel):

    def open_app(self, appnaam):
        return (f"Opent de {appnaam}-toepassing")


class iPhone(SmartPhone):
    def kies_nummer(self, nummer):
        return super().kies_nummer(nummer).lower()


oMobielToestel1 = MobielToestel()
print(oMobielToestel1.kies_nummer('0467 62 31 21'))
oSmartPhone1 = SmartPhone()
print(oSmartPhone1.kies_nummer('0467 62 31 21'))
print(oSmartPhone1.open_app('Instagram'))
oiPhone1 = iPhone()
print(oiPhone1.kies_nummer('0467 62 31 21'))
print(oiPhone1.open_app('Instagram'))
