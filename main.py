#mis funciones contadoras
import myFun as mf
import matplotlib.pyplot as plt

#trabajaremos con el primer parrafo de "Alicia..." en ingles y en espaniol
f1 = open("AliceSP.txt", "rt")
f2 = open("AliceEN.txt", "rt")

#leemos el archivo
strSp = f1.read()
strEn = f2.read()
# -----------------------MAIN --------------------------

print("***conteo espaniol:")
conteoEs = mf.countVocals(strSp)

print("\n***conteo ingles:")
conteoIn = mf.countVocals(strEn)


def mostrar(conteos):            
    xpoints = conteos.keys()
    ypoints = conteos.values()
    plt.plot(xpoints, ypoints, 'o')
    plt.xlabel("Letras")
    plt.ylabel("Ocurrencias")
   

mostrar(conteoEs)
mostrar(conteoIn)
plt.show()