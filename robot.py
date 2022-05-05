def do():
    speak = input("Speak: ")
    if speak.startswith("robo"):
        print("Hello I am", speak)
    else:
        do()

do()