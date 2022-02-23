def is_integer(text):
    text = "".join(text.split())
    if len(text) >= 1 and text.isdigit():
        return True
    if text.startswith("+") and text[1:].isdigit() or text.startswith("-") and text[1:].isdigit():
        return True
    return False

def main():
    text = input("Typ iet jong: ")
    if is_integer(text):
        print(f"{text} is een integer.")
    else:
        print(f"{text} is geen integer.")

# Prevent main conflict on import
if __name__ == "__main__":
    main()