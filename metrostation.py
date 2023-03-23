from time import sleep
stations = [
    "Tucuruvi",
    "Parada Inglesa",
    "Jardim São Paulo - Ayrton Senna",
    "Santana",
    "Carandiru",
    "Portuguesa - Tietê",
    "Armênia",
    "Tiradentes",
    "Luz",
    "São Bento",
    "Sé",
    "Japão - Liberdade",
    "São Joaquim",
    "Vergueiro",
    "Paraíso",
    "Ana Rosa",
    "Vila Mariana",
    "Santa Cruz",
    "Praça da Árvore",
    "Saúde",
    "São Judas",
    "Conceição",
    "Jabaquara"
]

i = 0

first = True
last = False
goal = stations[len(stations) - 1]

def goto():
    global i
    global first, last
    global goal

    if first == True and stations[i] != stations[len(stations) - 1]:
        i += 1
        goal = stations[len(stations) - 1]

    elif last == True and stations[i] != stations[0]:
        i -= 1
        goal = stations[0]
    
    elif stations[i] == stations[len(stations) - 1]:
        first = False
        last = True

    elif stations[i] == stations[0]:
        first = True
        last = False

    else:
        print("I didnt quite undestand that")
        sleep(1)
        goto()

start = input()
if "y" in start:
    while True:
        if stations[i] != stations[0]:
            print(f"\nPREVIOUS STATION : {stations[i-1]} : {i-1}")
        else: 
            print("\nFIRST STATION")
        print(f"CURRENT STATION : {stations[i]} : {i}")
        if stations[i] != stations[len(stations) - 1]:
            print(f"NEXT STATION : {stations[i+1]} : {i+1}\n")
        else:
            print("LAST STATION\n")
        
        print(f"STATION GOAL : {goal}")
        
        sleep(1)
        goto()
