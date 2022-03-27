#El objetivo de este ejercicio es notar cuales son las vocales mas usadas
#  tanto en español como en inglés

#Ambos textos son el comienzo de Alicia en el pais de las maravillas, de Lweis Carroll.

# Global vars --------------------------
strSp = """Alicia empezaba ya a cansarse de estar sentada con su hermana a la orilla del rio, sin tener nada que hacer: habia hechado un par de ojeadas al libro que su hermana estaba leyendo, pero no tenia dibujos ni dialogos."""
strEn ="""ALICE was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it."""

# Funcion contadora--------------------------
def countVocals(text):
    myDic = {"a": 0,
             "e": 0,
             "i": 0,
             "o": 0,
             "u": 0}
    #to_lowerCase
    text = text.lower()

    # Python does not have (switch) statement
    for x in text:
        if x == "a":
            myDic["a"] = myDic["a"]+1
        if x == "e":
            myDic["e"] = myDic["e"]+1
        if x == "i":
            myDic["i"] = myDic["i"]+1
        if x == "o":
            myDic["o"] = myDic["o"]+1
        if x == "u":
            myDic["u"] = myDic["u"]+1
        
    print("a: ", myDic["a"])
    print("e: ", myDic["e"])
    print("i: ", myDic["i"])
    print("o: ", myDic["o"])
    print("u: ", myDic["u"])
    
    totalVocales = myDic["a"] + myDic["e"] + myDic["i"] + myDic["o"] + myDic["u"]
    print("longitud texto: ", len(text))
    print("total vocales: ", totalVocales)
    print("no-vocales: ", len(text)-totalVocales)
    return myDic
# MAIN --------------------------

print("***conteo espaniol:")
conteoEs = countVocals(strSp)

print("\n***conteo ingles:")
conteoIn = countVocals(strEn)
#vamos a mostrar en un grafico
import matplotlib.pyplot as plt
import numpy as np

#deberian hacer lo mismo
xpoints=np.array(['a','e','i','o','u'])
#xpoints = conteoEs.keys()

ypoints =(conteoEs.values())
#ypoints=([conteoEs.values()])

plt.plot(xpoints, ypoints, 'o')
plt.show()