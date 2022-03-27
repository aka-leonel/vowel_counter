#mis funciones contadoras
import myFun as mf
import matplotlib.pyplot as plt

#----------------LECTURA------------------
#hoy trabajaremos con el primer parrafo de "Alicia..." tanto en ingles y como en espaniol
#puede utilizar otro texto reemplazando el primer argumento de open()
f1 = open("AliceSP.txt", "rt")
f2 = open("AliceEN.txt", "rt")
#leemos cada archivo
strSp = f1.read()
strEn = f2.read()

# -----------------------MAIN --------------------------

print("***conteo espaniol:")
conteoEs = mf.countVocals(strSp)
print("\n***conteo ingles:")
conteoIn = mf.countVocals(strEn)

eje_x_es = conteoEs.keys()
eje_y_es = conteoEs.values()
eje_x_en =conteoIn.keys()
eje_y_en = conteoIn.values()

plt.plot(eje_x_es, eje_y_es, 'o r')#espanion dots red
plt.plot(eje_x_en, eje_y_en, 'o b')#ingles dots blue
plt.xlabel("Letras: rojo (esp), azul(ing)")
plt.ylabel("Ocurrencias")
plt.title("Frecuencia de letras en ESP/ENG")
plt.show()
