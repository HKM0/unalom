# BogiKód.py
# 85303060 4006080304

def encode(text, key):
    encoded_text = ""
    for word in text.split():
        encoded_word = "".join(str(key.get(char.lower(), char)) for char in word)
        encoded_text += encoded_word + " "
    return encoded_text.strip()

def decode(text, key):
    decoded_text = ""
    for word in text.split():
        decoded_word = ""
        num = ""
        for char in word:
            if char.isdigit():
                num += char
            else:
                if num:
                    decoded_word += key.get(int(num), num)
                    num = ""
                decoded_word += char
        if num:
            decoded_word += key.get(int(num), num)
        decoded_text += decoded_word + " "
    return decoded_text.strip()

def main():
    dekodolo_kulcs = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
        "k": 20, "l": 30, "m": 40, "n": 50, "o": 60, "p": 70, "r": 80, "s": 90, "t": 100,
        "u": 200, "v": 300, "w": 400, "x": 500, "y": 600, "z": 700, "q": 800, "á": 900,
        "é": 1000, "í": 2000, "ó": 3000, "ö": 4000, "ő": 5000, "ú": 6000, "ü": 7000, "ű": 8000
    }
    
    dekodolo_kulcs2 = {v: k for k, v in dekodolo_kulcs.items()}
    
    while True:
        user_input = input("Input: ")
        if all(char.isalpha() or char.isspace() for char in user_input):
            print(encode(user_input, dekodolo_kulcs))
        elif all(char.isdigit() or char.isspace() for char in user_input):
            print(decode(user_input, dekodolo_kulcs2))
        else:
            print("Invalid input. Please enter only letters or only numbers.")

if __name__ == "__main__":
    main()