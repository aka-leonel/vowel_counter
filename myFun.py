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