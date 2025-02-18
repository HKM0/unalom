import sys
import pyperclip


# ----------------kulcsok----------------

dekodolo_kulcs = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
    "k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"r":80,"s":90,"t":100,"u":200,
    "v":300,"w":400,"x":500,"y":600,"z":700,"q":800,"á":900,"é":1000,
    "í":2000,"ó":3000,"ö":4000,"ő":5000,"ú":6000,"ü":7000,"ű":8000,
    "0":9000,"1":10000,"2":20000,"3":30000,"4":40000,"5":50000,"6":60000,
    "7":70000,"8":80000,"9":90000,
    "A":100000, "B":200000, "C":300000, "D":400000, "E":500000, "F":600000, "G":700000, "H":800000, "I":900000, "J":1000000,
    "K":2000000,"L":3000000,"M":4000000,"N":5000000,"O":6000000,"P":7000000,"R":8000000,"S":9000000,"T":10000000,"U":20000000,
    "V":30000000,"W":40000000,"X":50000000,"Y":60000000,"Z":70000000,"Q":80000000,"Á":90000000,"É":100000000,
    "í":200000000,"Ó":300000000,"Ö":400000000,"Ő":500000000,"Ú":600000000,"Ü":700000000,"Ű":800000000, 
    ",":900000000, ".":1000000000, ":":2000000000 ,"/":3000000000 ,
    1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
    20: "k", 30: "l", 40: "m", 50: "n", 60: "o", 70: "p", 80: "r", 90: "s", 100: "t",
    200: "u", 300: "v", 400: "w", 500: "x", 600: "y", 700: "z", 800: "q", 900: "á",
    1000: "é", 2000: "í", 3000: "ó", 4000: "ö", 5000: "ő", 6000: "ú", 7000: "ü", 8000: "ű",
    9000:"0",10000:"1",20000:"2",30000:"3",40000:"4",50000:"5",60000:"6",
    70000:"7",80000:"8",90000:"9",
    100000: "A", 200000: "B", 300000: "C", 400000: "D", 500000: "E", 600000: "F", 700000: "G", 800000: "H", 900000: "I", 1000000: "J",
    2000000: "K", 3000000: "L", 4000000: "M", 5000000: "N", 6000000: "O", 7000000: "P", 8000000: "R", 9000000: "S", 10000000: "T",
    20000000: "U", 30000000: "V", 40000000: "W", 50000000: "X", 60000000: "Y", 70000000: "Z", 80000000: "Q", 90000000: "Á",
    100000000: "É", 200000000: "Í", 300000000: "Ó", 400000000: "Ö", 500000000: "Ö", 600000000: "Ú", 700000000: "Ü", 800000000: "Ű",
    900000000:",", 1000000000:".", 2000000000:":" ,3000000000:"/" ,
}   

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

def Char(a):
    interpreted = karakterListaKepzes(a)
    outstring=""
    for karakter in interpreted:
        if (karakter==" "):
            outstring+=" "
        else:
            outstring+=str(karakter)
    pyperclip.copy(outstring)
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
            interpreted += (dekodolo_kulcs.get(tmpinterpreted[i], str(tmpinterpreted[i])))
    
        else:
            interpreted += str(tmpinterpreted[i])

    result = ""
    for digits in range(len(interpreted)):
        result += f"{interpreted[digits]}"
    #print(result)
    pyperclip.copy(result)
    return result

# ------------------szam------------------
if (len(sys.argv)==2):
        a=sys.argv[1]
        valbool = True
        for char in a:
            if (char.isalpha()): valbool=False; break
        if valbool: print(digit(a))
        else: print(Char(a))

elif (len(sys.argv)==1):
    while True:
        a=input("Input: ")

        if (a == ""): break
        else:
            valbool = True
            for char in a:
                if (char.isalpha()): valbool=False; break
            if valbool: print(digit(a))
            else: print(Char(a))
else:
    raise ValueError(f"Too many arguments, {len(sys.argv)-1} given instead of 1")

# - HeKi