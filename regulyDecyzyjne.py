def rozmyta_energia(E_bateria, E_solar, O2_poziom, A_zaloga, T_wewn):
    
    P_zycie = 50
    P_nauka = 50
    I_O2 = 50
    P_termo = 50

    # === Reguły ===
    # ============ Jeśli bateria ma krytyczny stan i mało  słońca no to  maks energia na życie, wyłącz naukę bo wyginą astronauci 
    
    if E_bateria < 25 and E_solar < 8:
        P_zycie = 90
        P_nauka = 0
        I_O2 = 90
        P_termo = 60

    # ========= Jeśli załoga pracuje dużo i jest mało tlenu to zwiększ produkcje tlenu w krystalizatorze materii
    elif A_zaloga > 7 and O2_poziom < 20:
        P_zycie = 85
        I_O2 = 95
        P_termo = 65

    # ============= Jeśli tlen jest w  normie i aktywność załogi jest średnia i temperatura normalna to standardowe wartości
    elif 20 <= O2_poziom <= 22 and 3 <= A_zaloga <= 7 and 20 <= T_wewn <= 24:
        P_zycie = 70
        I_O2 = 50
        P_termo = 50

    # -------------- Jeśli bateria wysoka i dużo słońca i tlen jest OK no to przeznacz energię na  pełną nauke
    elif E_bateria > 75 and E_solar > 20 and 20 <= O2_poziom <= 22:
        P_nauka = 100
        P_zycie = 70

    # ========= Jeśli temperatura ciepła i załoga aktywna i bateria niska to daj więcej na chłodzenie
    elif T_wewn > 25 and A_zaloga > 7 and E_bateria < 40:
        P_termo = 90
        P_nauka = 30

    # ========= Zimno i małe słońce i bateria niska to dajemy więcej mocy na grzanie i godne życie
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


wejscia = {
    'E_bateria': 20,    
    'E_solar': 3,       
    'O2_poziom': 19,     
    'A_zaloga': 8,       
    'T_wewn': 24        
}

wyniki = rozmyta_energia(**wejscia)


print("Wyniki decyzyjne systemu:")
for k, v in wyniki.items():
    print(f"{k}: {v}%")
