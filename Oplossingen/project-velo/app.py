# Projectopdracht - modeloplossing
# Je start de toepassing via dit bestand!
# worden nog eerstdaags toegevoegd aan de modeloplossing: cli-start van de simulator en transporteurs in actie
import pickle
from velo import Velo
            
def main():
    try:
        with open("velodata.dat", "rb") as f:
            verder_string = input("\nDruk 'v' om verder te gaan op de vorige situatie of 'o' om opnieuw te beginnen:")
            if verder_string == "v":
                app = pickle.load(f) 
            else:
                app = Velo()
    except FileNotFoundError:
        app = Velo()
    app.terminal_interface_weergeven()
    with open("velodata.dat", "wb") as f:
        pickle.dump(app, f)

main()