import sys
    
dekodolo_kulcs = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
    "k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"r":80,"s":90,"t":100,"u":200,
    "v":300,"w":400,"x":500,"y":600,"z":700,"q":800,"á":900,"é":1000,
    "í":2000,"ó":3000,"ö":4000,"ő":5000,"ú":6000,"ü":7000,"ű":8000,}

dekodolo_kulcs2= {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
    20: "k", 30: "l", 40: "m", 50: "n", 60: "o", 70: "p", 80: "r", 90: "s", 100: "t",
    200: "u", 300: "v", 400: "w", 500: "x", 600: "y", 700: "z", 800: "q", 900: "á",
    1000: "é", 2000: "í", 3000: "ó", 4000: "ö", 5000: "ő", 6000: "ú", 7000: "ü", 8000: "ű"}

# ----------------karakter----------------
# karakter -> done
def karakterListaKepzes(a):
    temp = a.split(" ")
    interpreted=[]
    tmp=""
    for i in range(len(temp)):
        for char in temp[i]: tmp+=str(dekodolo_kulcs.get(char.lower(), char))
        interpreted.append(int(tmp))
        tmp=""
        if (len(temp)-1!=i):
            interpreted.append(" ")
    return interpreted

def char(a):
    interpreted = karakterListaKepzes(a)
    outstring=""
    for karakter in interpreted:
        if (karakter==" "):
            outstring+=" "
        else:
            outstring+=str(karakter)
    return outstring

# ------------------szam------------------
def szamListaLekepzes(a):
    a = a.strip()
    temp = ""
    tmpinterpreted = []
    for p in a:
        if temp == "" and p != "0":
            temp += p
        elif temp != "" and p != "0":
            if (p == " "):
                tmpinterpreted.append(int(temp))
                temp = ""
                tmpinterpreted.append(" ")
            else:
                tmpinterpreted.append(int(temp))
                temp = f"{p}"
        elif p == "0": 
            temp += p
    if temp:
        tmpinterpreted.append(int(temp))
    try:
        tmpinterpreted[0]=int(tmpinterpreted[0])
    except:pass
    return tmpinterpreted

# szamok -> done
def digit(a):
    tmpinterpreted = szamListaLekepzes(a)
    interpreted = ""
    # decode
    for i in range(len(tmpinterpreted)):
        if isinstance(tmpinterpreted[i], int):
            interpreted += (dekodolo_kulcs2.get(tmpinterpreted[i], str(tmpinterpreted[i])))
    
        else:
            interpreted += str(tmpinterpreted[i])

    result = ""
    for digits in range(len(interpreted)):
        result += f"{interpreted[digits]}"
    #print(result)
    return result

if (len(sys.argv)==2):
        a=sys.argv[1]
        if all(char.isdigit() or char.isspace() for char in a): digit(a)
        elif all(char.isalpha() or char.isspace() for char in a): char(a)

elif (len(sys.argv)==1):
    while True:
        a=input("Input: ")

        if (a == ""): break
        elif all(char.isdigit() or char.isspace() for char in a): print(digit(a))
        elif all(char.isalpha() or char.isspace() for char in a): print(char(a))
else:
    raise ValueError(f"Too many arguments, {len(sys.argv)-1} given instead of 1")