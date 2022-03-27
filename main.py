#vowel counter functions
import myFun as mf
#for drawing
import matplotlib.pyplot as plt


#Textos a analizar
strSp = "Alicia empezaba ya a cansarse de estar sentada con su hermana a la orilla del rio, sin tener nada que hacer: habia hechado un par de ojeadas al libro que su hermana estaba leyendo, pero no tenia dibujos ni dialogos."
strEn ="ALICE was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it."


# -----------------------MAIN --------------------------

print("***conteo espaniol:")
conteoEs = mf.countVocals(strSp)

print("\n***conteo ingles:")
conteoIn = mf.countVocals(strEn)



def mostrar(conteos):            
    xpoints = conteos.keys()
    ypoints = conteos.values()
    plt.plot(xpoints, ypoints, 'o')
   

mostrar(conteoEs)
mostrar(conteoIn)
plt.show()