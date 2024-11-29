#bog-bogi code
#85303060 4006080304

while True:
    a=input("Input: ");q=[]
    q2=[]
    p=""
    w=""
    dekodolo_kulcs = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
      "k":20,"l":30,"m":40,"n":50,"o":60,"p":70,"r":80,"s":90,"t":100,"u":200,
      "v":300,"w":400,"x":500,"y":600,"z":700,"q":800,"á":900,"é":1000,
      "í":2000,"ó":3000,"ö":4000,"ő":5000,"ú":6000,"ü":7000,"ű":8000,}
    
    if all(char.isalpha() or char.isspace() for char in a):
        q.extend(a.split())
        q2=[list(word) for word in q]
        for word in q2: 
            p=""
            for char in word: p+=str(dekodolo_kulcs.get(char.lower(), char))
            w+=p+" "
        print(w)
        w=""
    elif all(char.isdigit() or char.isspace() for char in a):
        q.extend(map(str, a.split()))
        q2=[list(word) for word in q]
        dekodolo_kulcs2=   {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
                           20: "k", 30: "l", 40: "m", 50: "n", 60: "o", 70: "p", 80: "r", 90: "s", 100: "t",
                           200: "u", 300: "v", 400: "w", 500: "x", 600: "y", 700: "z", 800: "q", 900: "á",
                           1000: "é", 2000: "í", 3000: "ó", 4000: "ö", 5000: "ő", 6000: "ú", 7000: "ü", 8000: "ű"}
        LTA=[]
        for i in q2:
            LTT=[]; LNK=[]; k=0; z=0; p=""
            for x in i:
                k+=1
                if x!="0":
                    if LNK==[]: LNK.append(x)
                    elif LNK!=[]:
                        if z!=0:
                            for s in range(z): LNK.append("0")
                            LTT.append(LNK);  LNK=[]; z=0; LNK.append(x)
                        elif z==0:
                            LTT.append(LNK); LNK=[]; LNK.append(x)
                elif x=="0": z+=1
                else: print("sex")
                if k==len(i):
                    if z!=0:
                        for s in range(z): LNK.append("0"); LTT.append(LNK)
                    else: LTT.append(LNK)
                #print(f"i={i} x={x} z={z} LNK={LNK}")
            LTA.append(LTT)
        szamlista=[]
        LT2=[]
        for x in LTA: 
            a=""
            LT1=[]
            for y in x:
                a=""
                for i in range(len(y)): a+=y[i]
                LT1.append(a)
            LT2.append(LT1)
        szamlista.append(LT2)
        dec_lista = []
        for s in szamlista:
            dec_s = []
            for belso_lista in s:
                dec_belso_lista = [dekodolo_kulcs2.get(int(char), char) for char in belso_lista]
                dec_s.append(dec_belso_lista)
            dec_lista.append(dec_s)
        b=""
        ac=[]
        for i in dec_lista:
            for a in i:
                for x in a: b+=x; 
                ac.append(b); b=" "
        b="".join(ac)
        print(b.strip())