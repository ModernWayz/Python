# Logging framework - SQLite - 3 tabellen
# Eén of meerdere klassen die raamwerk beschrijven en van functionaliteit voorzien
# table events: id, beschrijving, gebruiker_id, applicatie_id, timestamp
# table gebruikers: id, voornaam, naam
# table applicaties: id, naam
import time
import sqlite3

class Db():
    """ Klasse voor databankconnectie"""
    def __init__(self, connect, cursor):
        self.connect = connect
        self.cursor = cursor

    def __del__(self):
        # Bij del object wordt deze magic method uitgevoerd
        try:
            # Een try-block omdat deze code 3x wordt uitgevoerd
            self.cursor.close()
            self.connect.close()
            print("Logger object netjes afgesloten...")
        except sqlite3.ProgrammingError:
            pass


class Gebruikers(Db):
    """ Klasse gebruikers: bevat verwante bewerkingsmethods """
    def create(self, voornaam, naam):
        sql = f"INSERT INTO gebruikers (voornaam, naam) VALUES('{voornaam}','{naam}');"
        self.cursor.execute(sql)
        self.connect.commit()
    
    def read_all(self):
        sql = "SELECT * FROM gebruikers"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]} {rij[2]}\n"
        return return_waarde

    def read_one(self, id):
        sql = f"SELECT * FROM gebruikers WHERE id = {id}"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]} {rij[2]}\n"
        return return_waarde

    def update(self, id, voornaam, naam):
        sql = f"UPDATE gebruikers SET voornaam = '{voornaam}', naam = '{naam}' WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()

    def delete(self, id):
        sql = f"DELETE FROM gebruikers WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()


class Events(Db):
    """ Klasse events: bevat verwante bewerkingsmethods """
    def create(self, beschrijving, gebruiker_id, applicatie_id, timestamp):
        sql = f"INSERT INTO events (beschrijving, gebruiker_id, applicatie_id, timestamp) VALUES('{beschrijving}', {gebruiker_id}, {applicatie_id}, {timestamp});"
        self.cursor.execute(sql)
        self.connect.commit()
    
    def read_all(self):
        sql = "SELECT * FROM events"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]} [gebruiker: {rij[2]}, app: {rij[3]}]\n"
        return return_waarde

    def read_one(self, id):
        sql = f"SELECT * FROM events WHERE id = {id}"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]} [gebruiker: {rij[2]}, app: {rij[3]}]\n"
        return return_waarde

    def update(self, id, beschrijving, gebruiker_id, applicatie_id, timestamp):
        sql = f"UPDATE events SET beschrijving = '{beschrijving}', gebruiker_id = {gebruiker_id}, applicatie_id = {applicatie_id}, timestamp = {timestamp} WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()

    def delete(self, id):
        sql = f"DELETE FROM events WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()


class Applicaties(Db):
    """ Klasse applicaties: bevat verwante bewerkingsmethods """
    def create(self, naam):
        sql = f"INSERT INTO applicaties (naam) VALUES('{naam}');"
        self.cursor.execute(sql)
        self.connect.commit()
    
    def read_all(self):
        sql = "SELECT * FROM applicaties"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]}\n"
        return return_waarde

    def read_one(self, id):
        sql = f"SELECT * FROM applicaties WHERE id = {id}"
        alle_rijen = self.cursor.execute(sql).fetchall()
        return_waarde = ""
        for rij in alle_rijen:
            return_waarde += f"{rij[0]}: {rij[1]}\n"
        return return_waarde

    def update(self, id, naam):
        sql = f"UPDATE applicaties SET naam = '{naam}' WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()

    def delete(self, id):
        sql = f"DELETE FROM applicaties WHERE id={id}"
        self.cursor.execute(sql)
        self.connect.commit()

class Logger():
    """ Logger klasse: container-klasse, bevat ook de basisfunctionaliteit """
    def __init__(self, databank="Oplossingen/labo11 - oplossing/labo11.db"):
        connect = sqlite3.connect(databank)
        cursor = connect.cursor()
        self.gebruikers = Gebruikers(connect, cursor)
        self.events = Events(connect, cursor)
        self.applicaties = Applicaties(connect, cursor)
        print("Logger object klaar voor actie")


def main():
    app = Logger()
    print(app.gebruikers.read_one(1))
    print(app.applicaties.read_one(1))
    app.events.create("Dit is een test-event", 1, 1, time.time())
    app.events.create("En nog eentje", 1, 1, time.time())
    app.events.create("En nog eentje om het af te leren", 1, 1, time.time())
    print(app.events.read_all())
    del app

if __name__ == "__main__":
    main()