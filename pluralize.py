
userInputNumber = int(input(""))
userInputWord = input("")
"""
if userInputNumber > 1 or userInputNumber == 0:
    print(userInputWord + "s")
else:
    print(userInputWord) """
if userInputNumber == 1:
    print(str(userInputNumber) + " " + userInputWord)
if userInputNumber > 1 or userInputNumber == 0:
 
    if userInputWord.endswith("life"):
        print(str(userInputNumber) + " " + userInputWord[:-3] + "ive")
   
    elif userInputWord.endswith("sh") or userInputWord.endswith("ch"):
        print(str(userInputNumber) + " " + userInputWord + "es")
    
    elif userInputWord.endswith("us"):
        print(str(userInputNumber) + " " + userInputWord[:-2] + "i")
   
        #-ay/oy/ey/uy
    elif userInputWord.endswith("ay") or userInputWord.endswith("oy") or userInputWord.endswith("ey") or userInputWord.endswith("uy"):
        print(str(userInputNumber) + " " + userInputWord + "s")

    elif userInputWord.endswith("y"):
        print(str(userInputNumber) + " " + userInputWord[:-1] + "ies")

    else:
        print(str(userInputNumber) + " " + userInputWord + "s")
