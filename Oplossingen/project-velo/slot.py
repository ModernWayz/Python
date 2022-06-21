class Slot():
    """ Klasse Slot: bestaat uit id en inhoud (zal None bevatten of fiets-object) """
    index = 1
    def __init__(self):
        self.id = Slot.index
        self.inhoud = None
        Slot.index += 1

    def fiets_toevoegen(self, fiets):
        self.inhoud = fiets