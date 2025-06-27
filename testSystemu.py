import matplotlib.pyplot as plt


def rozmyta_energia(E_bateria, E_solar, O2_poziom, A_zaloga, T_wewn):
    P_zycie = 50
    P_nauka = 50
    I_O2 = 50
    P_termo = 50

    if E_bateria < 25 and E_solar < 8:
        P_zycie = 90
        P_nauka = 0
        I_O2 = 90
        P_termo = 60
    elif A_zaloga > 7 and O2_poziom < 20:
        P_zycie = 85
        I_O2 = 95
        P_termo = 65
    elif 20 <= O2_poziom <= 22 and 3 <= A_zaloga <= 7 and 20 <= T_wewn <= 24:
        P_zycie = 70
        I_O2 = 50
        P_termo = 50
    elif E_bateria > 75 and E_solar > 20 and 20 <= O2_poziom <= 22:
        P_nauka = 100
        P_zycie = 70
    elif T_wewn > 25 and A_zaloga > 7 and E_bateria < 40:
        P_termo = 90
        P_nauka = 30
    elif T_wewn < 18 and E_solar < 5 and E_bateria < 40:
        P_termo = 95
        P_nauka = 0
        P_zycie = 90

    return {
        'P_zycie': round(P_zycie, 2),
        'P_nauka': round(P_nauka, 2),
        'I_O2': round(I_O2, 2),
        'P_termo': round(P_termo, 2)
    }

# ================             Defuzyfikacje (na wyjściu - słownik wartości procentowych)
def defuzyfikacja_srednia_wazona(wyniki):
    
    # =========== Średnia ważona z wagą = wartości (tutaj po prostu średnia ważona z samych wartości)
    
    #============ Dla uproszczenia: zwracamy średnią ważoną, gdzie wagi to wartości same (czyli średnia ważona = średnia)
    
    return sum(wyniki.values()) / len(wyniki)

def defuzyfikacja_max(wyniki):
    
    return max(wyniki.values())

def defuzyfikacja_srednia_prosta(wyniki):
   
    return sum(wyniki.values()) / len(wyniki)


testy = {
    "Minimum (krytyczne)": {'E_bateria': 0, 'E_solar': 0, 'O2_poziom': 16, 'A_zaloga': 0, 'T_wewn': 15},
    "Maksimum (optymalne)": {'E_bateria': 100, 'E_solar': 25, 'O2_poziom': 25, 'A_zaloga': 10, 'T_wewn': 30}
}

print("=== Testy na skrajnych wartościach ===")
for nazwa, dane in testy.items():
    wyniki = rozmyta_energia(**dane)
    print(f"\n{nazwa}:")
    for k, v in wyniki.items():
        print(f"  {k}: {v}%")

    # porównanie defuzyfikacji
    print("  Defuzyfikacja średnia ważona:", defuzyfikacja_srednia_wazona(wyniki))
    print("  Defuzyfikacja max:", defuzyfikacja_max(wyniki))
    print("  Defuzyfikacja średnia prosta:", defuzyfikacja_srednia_prosta(wyniki))


wynik_maks = rozmyta_energia(**testy["Maksimum (optymalne)"])
plt.bar(wynik_maks.keys(), wynik_maks.values(), color=['green', 'blue', 'orange', 'red'])
plt.title("Wizualizacja działania systemu - Maksimum (optymalne warunki)")
plt.ylabel("Procent alokacji mocy [%]")
plt.ylim(0, 110)
plt.show()
