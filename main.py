import random

print("🎯 Bine ai venit la jocul Tablei Înmulțirii!")
print("Introdu 'stop' pentru a ieși.\n")

scor = 0
intrebari = 0

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    raspuns_corect = a * b

    raspuns = input(f"Cât face {a} x {b}? ")

    if raspuns.lower() == "stop":
        break

    if raspuns.isdigit() and int(raspuns) == raspuns_corect:
        print("✅ Corect!\n")
        scor += 1
    else:
        print(f"❌ Greșit. Răspunsul corect era {raspuns_corect}.\n")

    intrebari += 1

print(f"Joc terminat! Ai avut {scor} răspunsuri corecte din {intrebari}. 👏")
