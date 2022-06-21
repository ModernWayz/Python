import input
import output

def main():
    input.initialiseren()
    output.verwijder_site("_site")
    output.maak_site("_site", "pages", input.pages)
    output.maak_site("_site", "posts", input.posts)
    output.kopieer_assets("assets", "_site")

if __name__ == '__main__':
    main()

