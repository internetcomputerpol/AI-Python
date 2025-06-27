import numpy as np
import matplotlib.pyplot as plt

#================================== Funkcje przynależności
def trapezoidal(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a)/(b - a + 1e-6), 1), (d - x)/(d - c + 1e-6)))

def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a)/(b - a + 1e-6), (c - x)/(c - b + 1e-6)))

def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma)**2)

#==================================Funkcja pomocnicza do rysowania

def plot_membership(x, functions: dict, title: str, xlabel: str):
    plt.figure(figsize=(8, 5))
    for label, y in functions.items():
        plt.plot(x, y, label=label, linewidth=2)
    plt.title(title, fontsize=14)
    plt.xlabel(xlabel)
    plt.ylabel("Przynależność")
    plt.ylim(-0.05, 1.05)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()



x_battery = np.linspace(0, 100, 1000)
plot_membership(x_battery, {
    "Krytyczny 🔴": trapezoidal(x_battery, 0, 0, 15, 25),
    "Niski 🟠": trapezoidal(x_battery, 20, 30, 40, 50),
    "Średni 🟡": trapezoidal(x_battery, 45, 55, 65, 75),
    "Wysoki 🟢": trapezoidal(x_battery, 70, 80, 100, 100)
}, "🔋 Poziom energii baterii", "Poziom [%]")


x_solar = np.linspace(0, 25, 1000)
plot_membership(x_solar, {
    "Niska ☁️": triangular(x_solar, 0, 0, 8),
    "Średnia ⛅": triangular(x_solar, 5, 12.5, 20),
    "Wysoka ☀️": triangular(x_solar, 15, 25, 25)
}, "☀️ Produkcja energii słonecznej", "Moc [kW]")


x_o2 = np.linspace(16, 25, 1000)
plot_membership(x_o2, {
    "Krytyczny 🚨": gaussian(x_o2, 18, 1.0),
    "Niski ⚠️": gaussian(x_o2, 19.5, 0.8),
    "Normalny ✅": gaussian(x_o2, 21, 1.2),
    "Wysoki 🔼": gaussian(x_o2, 23, 1.0)
}, "🫁 Poziom tlenu", "Stężenie [% obj.]")


x_activity = np.linspace(0, 10, 1000)
plot_membership(x_activity, {
    "Niska 🛌": triangular(x_activity, 0, 0, 3),
    "Średnia 🚶": triangular(x_activity, 2, 5, 8),
    "Wysoka 🏃": triangular(x_activity, 7, 10, 10)
}, "👨‍🚀 Aktywność załogi", "Poziom aktywności")


x_temp = np.linspace(15, 30, 1000)
plot_membership(x_temp, {
    "Zimna ❄️": gaussian(x_temp, 18, 2.0),
    "Normalna 🌡️": gaussian(x_temp, 22, 2.5),
    "Ciepła 🔥": gaussian(x_temp, 26, 2.0)
}, "🌡️ Temperatura wewnętrzna", "Temperatura [°C]")


#==============================ZMIENNE WYJŚCIOWE
x_power = np.linspace(0, 100, 1000)

#==================================  SYSTEMY ŻYCIOWE !!!!!!!!!!!!!!!!!!!!!!!!!!
plot_membership(x_power, {
    "Minimalna ⚠️": trapezoidal(x_power, 0, 0, 20, 30),
    "Standardowa ✅": trapezoidal(x_power, 25, 40, 60, 75),
    "Maksymalna 🟥": trapezoidal(x_power, 70, 85, 100, 100)
}, "❤️ Alokacja energii – systemy życiowe", "Procent mocy [%]")


plot_membership(x_power, {
    "Wyłączona ❌": triangular(x_power, 0, 0, 15),
    "Ograniczona ⚠️": triangular(x_power, 10, 25, 40),
    "Normalna ✅": triangular(x_power, 30, 50, 70),
    "Pełna 🔬": triangular(x_power, 60, 80, 100)
}, "🔬 Alokacja energii – systemy naukowe", "Procent mocy [%]")


plot_membership(x_power, {
    "Minimalna 🟠": gaussian(x_power, 15, 8),
    "Normalna 🟢": gaussian(x_power, 50, 15),
    "Intensywna 🔵": gaussian(x_power, 85, 10)
}, "🧪 Intensywność produkcji tlenu", "Procent wydajności [%]")


plot_membership(x_power, {
    "Niska ❄️": triangular(x_power, 0, 0, 25),
    "Średnia 🌡️": triangular(x_power, 20, 50, 80),
    "Wysoka 🔥": triangular(x_power, 75, 100, 100)
}, "❄️🔥 Moc systemów termoregulacji", "Procent mocy [%]")
