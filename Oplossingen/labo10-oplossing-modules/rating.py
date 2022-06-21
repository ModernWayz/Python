import time

class Rating():
    """ Klasse rating: bevat gebruiker_id, score en tijdstip """
    def __init__(self, gebruiker_id, rating):
        self.gebruiker_id = gebruiker_id
        self.score = rating
        self.tijdstip = time.time()