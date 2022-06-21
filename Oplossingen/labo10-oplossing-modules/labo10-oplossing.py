import pickle
from filmzalen import Filmzalen

def main():
    try:
        with open("labo10-pickle.dat", "rb") as f:
            verder_string = input("\nDruk 'v' om verder te gaan op de vorige situatie of 'o' om opnieuw te beginnen:")
            if verder_string == "v":
                app = pickle.load(f) 
            else:
                app = Filmzalen()
    except FileNotFoundError:
        app = Filmzalen()
    app.terminal_interface_weergeven()
    with open("labo10-pickle.dat", "wb") as f:
        pickle.dump(app, f)

main()




