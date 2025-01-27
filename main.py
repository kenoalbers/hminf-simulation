"""
Author: Tobias Bielefeld

Umgesetzte Aufgabe: Praxisaufgabe 2: Jäger-Beute System

Das Programm setzt die Darstellung des Lotka-Volterra-Modells zur periodischen Entwicklung einer simulierten
Situation um, in der sich Beutetiere durch eine Nahrung z ernähren und durch Jäger gefressen werden, die sich
durch die Beute x wiederum ernähren.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider, TextBox
import yaml


# Laden der Konfigurationsdatei
def load_config(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)


# Validierung der Konfigurationsdatei
def validate_config(parameters, initial_conditions):
    for key, value in {**parameters, **initial_conditions}.items():
        if value < 0:
            raise ValueError(f"Der Wert für '{key}' darf nicht negativ sein: {value}")


# Erweiterte Lotka-Volterra-Gleichungen mit Nahrung
# Die Funktion berechnet die zeitliche Änderung zum Wachstum der jeweiligen Bestandteile (x, y, z)
def lotka_volterra_with_food(t, u, a, b, c, d, r, k):
    x, y, z = u  # x: Beute, y: Jäger, z: Nahrung
    dxdt = a * x - b * x * y - k * x * z
    dydt = -c * y + d * x * y
    dzdt = r * z - k * x * z
    return [dxdt, dydt, dzdt]


# Konfiguration laden
config = load_config("config.yaml")
parameters = config["parameters"]
initial_conditions = config["initial_conditions"]
simulation = config["simulation"]

# Parameter zuweisen
a = parameters["prey_growth_rate"]["value"]
b = parameters["prey_dying_rate"]["value"]
c = parameters["predator_dying_rate"]["value"]
d = parameters["predator_growth_rate"]["value"]
r = parameters["food_growth_rate"]["value"]
k = parameters["food_consumption_rate"]["value"]

# Anfangswerte zuweisen
initial_prey = initial_conditions["prey"]["value"]
initial_predators = initial_conditions["predators"]["value"]
initial_food = initial_conditions["food"]["value"]

# Zeitschritte- und grenzen zuweisen
time_min = simulation["time_min"]
time_max = simulation["time_max"]
time_step = simulation["time_step"]


# Funktion zur Simulation und Plotten
def update_plot(time_limit, prey_start, predator_start, food_start, a, b, c, d, r, k):
    # Simulationszeitraum
    t_span = (0, time_limit)
    t_eval = np.linspace(t_span[0], t_span[1], 1000)

    # Neue Anfangsbedingungen
    initial_conditions = [prey_start, predator_start, food_start]

    # Simulation
    solution = solve_ivp(
        fun=lotka_volterra_with_food,
        t_span=t_span,
        y0=initial_conditions,
        t_eval=t_eval,
        args=(a, b, c, d, r, k),
        method="BDF"
    )

    # Ergebnisse extrahieren
    t = solution.t
    prey = solution.y[0]  # Beute
    predators = solution.y[1]  # Jäger
    food = solution.y[2]  # Nahrung

    # Mittelwerte berechnen
    mean_prey = np.full_like(prey, np.mean(prey))
    mean_predators = np.full_like(predators, np.mean(predators))
    mean_food = np.full_like(food, np.mean(food))

    # Vorherigen Plot löschen
    ax.clear()

    # Ergebnisse plotten
    ax.plot(t, prey, label='Beute (x)', color='blue')
    ax.plot(t, predators, label='Jäger (y)', color='red')
    ax.plot(t, food, label='Nahrung (z)', color='green')
    ax.plot(t, mean_prey, label="Mittelwert Beute", color="blue", linestyle="dashed")
    ax.plot(t, mean_predators, label="Mittelwert Jäger", color="red", linestyle="dashed")
    ax.plot(t, mean_food, label="Mittelwert Nahrung", color="green", linestyle="dashed")
    ax.set_title("Erweitertes Lotka-Volterra Jäger-Beute-System mit Nahrung")
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Populationsgröße")
    ax.legend(loc="upper right")
    ax.grid()

    # Update the figure
    fig.canvas.draw_idle()


# Callback-Funktion für den Slider
def slider_callback(val):
    time_limit = time_slider.val
    update_plot(time_limit, prey_start, predator_start, food_start, prey_growthRate, prey_dyingRate, predator_dyingRate,
                predator_growthRate, food_growthRate, food_consumptionRate)


# Callback-Funktion für die Eingabefelder
def text_callback(event):
    global prey_start, predator_start, food_start, prey_growthRate, prey_dyingRate, predator_dyingRate, predator_growthRate, food_growthRate, food_consumptionRate

    # Werte aus den Textfeldern aktualisieren
    try:
        prey_start = float(text_box_prey.text)
        predator_start = float(text_box_predator.text)
        food_start = float(text_box_food.text)

        prey_growthRate = float(text_box_prey_growthRate.text)
        prey_dyingRate = float(text_box_prey_dyingRate.text)
        predator_growthRate = float(text_box_predator_growthRate.text)
        predator_dyingRate = float(text_box_predator_dyingRate.text)
        food_growthRate = float(text_box_food_growthRate.text)
        food_consumptionRate = float(text_box_food_consumptionRate.text)

        slider_callback(None)  # Plot aktualisieren
    except ValueError:
        pass  # Ungültige Eingaben werden ignoriert


# Initiales Setup für die Plotting-Umgebung
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.15, top=0.75)  # Platz für die Eingabefelder und Slider

# Schieberegler hinzufügen
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])  # Position: [x, y, Breite, Höhe]
time_slider = Slider(
    ax=ax_slider,
    label='Zeitraum',
    valmin=time_min,
    valmax=time_max,
    valinit=(time_min + time_max) // 2,
    valstep=time_step,
)
time_slider.on_changed(slider_callback)

# Eingabefelder hinzufügen (Positionsschema:  [x, y, Breite, Höhe])
ax_text_prey = plt.axes([0.17, 0.94, 0.08, 0.05])  # Position für Startwerte der Beute
ax_text_predator = plt.axes([0.51, 0.94, 0.08, 0.05])  # Position für Startwerte der Jäger
ax_text_food = plt.axes([0.9, 0.94, 0.08, 0.05])  # Position für Startwerte der Nahrung

ax_text_prey_growthRate = plt.axes([0.17, 0.88, 0.08, 0.05])  # Position für Wachstumsrate der Beute
ax_text_predator_growthRate = plt.axes([0.51, 0.88, 0.08, 0.05])  # Position für Wachstumsrate der Jäger
ax_text_food_growthRate = plt.axes([0.9, 0.88, 0.08, 0.05])  # Position für Wachstumsrate der Nahrung

ax_text_prey_dyingRate = plt.axes([0.17, 0.82, 0.08, 0.05])  # Position für Sterberate der Beute
ax_text_predator_dyingRate = plt.axes([0.51, 0.82, 0.08, 0.05])  # Position für Sterberate der Jäger
ax_text_food_consumptionRate = plt.axes([0.9, 0.82, 0.08, 0.05])  # Position für Konsumrate der Nahrung

# Initialisieren der jeweiligen Textboxen
text_box_prey = TextBox(ax_text_prey, "Anfangswert Beute:", initial=str(initial_prey))
text_box_predator = TextBox(ax_text_predator, "Anfangswert Jäger:", initial=str(initial_predators))
text_box_food = TextBox(ax_text_food, "Anfangswert Nahrung:", initial=str(initial_food))

text_box_prey_growthRate = TextBox(ax_text_prey_growthRate, "Wachstumsrate Beute:", initial=str(a))
text_box_predator_growthRate = TextBox(ax_text_predator_growthRate, "Wachstumsrate Jäger:", initial=str(d))
text_box_food_growthRate = TextBox(ax_text_food_growthRate, "Wachstumsrate Nahrung:", initial=str(r))

text_box_prey_dyingRate = TextBox(ax_text_prey_dyingRate, "Sterberate Beute:", initial=str(b))
text_box_predator_dyingRate = TextBox(ax_text_predator_dyingRate, "Sterberate Jäger:", initial=str(c))
text_box_food_consumptionRate = TextBox(ax_text_food_consumptionRate, "Konsumrate Nahrung:", initial=str(k))

# Validierung der Werte bei Verlassen oder Enter drücken der Textbox
text_box_prey.on_submit(text_callback)
text_box_predator.on_submit(text_callback)
text_box_food.on_submit(text_callback)

text_box_prey_growthRate.on_submit(text_callback)
text_box_predator_growthRate.on_submit(text_callback)
text_box_food_growthRate.on_submit(text_callback)

text_box_prey_dyingRate.on_submit(text_callback)
text_box_predator_dyingRate.on_submit(text_callback)
text_box_food_consumptionRate.on_submit(text_callback)

# Globale Variablen für die Startwerte
prey_start = initial_prey
predator_start = initial_predators
food_start = initial_food

# Globale Variablen für die Werte der Wachstums- und Sterberaten
prey_growthRate = a
prey_dyingRate = b
predator_dyingRate = c
predator_growthRate = d
food_growthRate = r
food_consumptionRate = k

# Initialer Plot
update_plot((time_min + time_max) // 2, prey_start, predator_start, food_start, prey_growthRate, prey_dyingRate,
            predator_dyingRate,
            predator_growthRate, food_growthRate, food_consumptionRate)

plt.show()
