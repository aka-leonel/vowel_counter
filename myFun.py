# Funcion contadora--------------------------
def countVocals(text):
    myDic = {"a": 0,
             "e": 0,
             "i": 0,
             "o": 0,
             "u": 0,
             "b":0,
             "c":0,
             "d":0,
             "f":0,
             "g":0,
             "h":0,
             "j":0,
             "k":0,
             "l":0,
             "m":0,
             "n":0,
             "p":0,
             "q":0,
             "r":0,
             "s":0,
             "t":0,
             "v":0,
             "w":0,
             "x":0,
             "y":0,
             "z":0             
             }
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
        if x == "b":
            myDic["b"] = myDic["b"]+1
        if x == "c":
            myDic["c"] = myDic["c"]+1
        if x == "d":
            myDic["d"] = myDic["d"]+1
        if x == "f":
            myDic["f"] = myDic["f"]+1
        if x == "g":
            myDic["g"] = myDic["g"]+1
        if x == "h":
            myDic["h"] = myDic["h"]+1
        if x == "j":
            myDic["j"] = myDic["j"]+1
        if x == "k":
            myDic["k"] = myDic["k"]+1
        if x == "l":
            myDic["l"] = myDic["l"]+1
        if x == "m":
            myDic["m"] = myDic["m"]+1
        if x == "n":
            myDic["n"] = myDic["n"]+1
       
        if x == "p":
            myDic["p"] = myDic["p"]+1
        if x == "q":
            myDic["q"] = myDic["q"]+1
        if x == "r":
            myDic["r"] = myDic["r"]+1
        if x == "s":
            myDic["s"] = myDic["s"]+1
        if x == "t":
            myDic["t"] = myDic["t"]+1
        if x == "v":
            myDic["v"] = myDic["v"]+1
        if x == "w":
            myDic["w"] = myDic["w"]+1
        if x == "x":
            myDic["x"] = myDic["x"]+1
        if x == "y":
            myDic["y"] = myDic["y"]+1
        if x == "z":
            myDic["z"] = myDic["z"]+1
        
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