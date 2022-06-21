class Fiets():
    """ Klasse Fiets: bestaat uit id en logs """
    index = 1
    def __init__(self):
        self.id = Fiets.index
        Fiets.index += 1