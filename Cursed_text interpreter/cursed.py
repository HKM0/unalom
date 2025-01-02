from random import choice
import pyperclip

# ötletek és forrás: 
# https://en.wikipedia.org/wiki/Unicode
# https://en.wikipedia.org/wiki/Diacritic

komplexitas:int = 30 #százalékos komplexitás


def void_text(szoveg):
    diacritics = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030A',
        '\u030B', '\u030C', '\u030D', '\u030E', '\u030F', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315',
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B', '\u031C', '\u031D', '\u031E', '\u031F', '\u0320',
        '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032A', '\u032B',
        '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331', '\u0332', '\u0333', '\u0334', '\u0335', '\u0336',
        '\u0337', '\u0338', '\u0339', '\u033A', '\u033B', '\u033C', '\u033D', '\u033E', '\u033F', '\u0340', '\u0341',
        '\u0342', '\u0343', '\u0344', '\u0345', '\u0346', '\u0347', '\u0348', '\u0349', '\u034A', '\u034B', '\u034C',
        '\u034D', '\u034E', '\u034F', '\u0350', '\u0351', '\u0352', '\u0353', '\u0354', '\u0355', '\u0356', '\u0357',
        '\u0358', '\u0359', '\u035A', '\u035B', '\u035C', '\u035D', '\u035E', '\u035F', '\u0360', '\u0361', '\u0362',
        '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036A', '\u036B', '\u036C', '\u036D',
        '\u036E', '\u036F'
        ]
    #   diacritics = list(map(chr, range(768, 879)))


    if szoveg[1] in diacritics:
        devoided_text = ''.join([char for char in szoveg if char not in diacritics])
        pyperclip.copy(devoided_text)
        return devoided_text
    
    elif szoveg == "\0":
        exit()
        return ""
    
    else: 
        szavak = szoveg.split()
        voided_text = ' '.join(''.join(k + ''.join(choice(diacritics) for _ in range(((komplexitas-1)//2)) if k.isalnum()) for k in resz) for i, resz in enumerate(szavak))
        #        voided_text = ' '.join(''.join(k + ''.join(choice(diacritics) for _ in range(((komplexitas-1)//2)) if k.isalnum()) for k in resz) for i, resz in enumerate(szavak))
        pyperclip.copy(voided_text)
        return voided_text


print("|----------------------|\n| Zalgo szöveg forditó |\n|----------------------|\n> Írd be a le/vissza fordítani kívánt szöveget\n> Kilépéshez üss egy Entert\n> A kimenet a vágólapra kerül!\n")
while True:
    szoveg:str = input("Be: ")
    if szoveg == "":
        break
    print(f"\nKi: {void_text(szoveg)}\n")