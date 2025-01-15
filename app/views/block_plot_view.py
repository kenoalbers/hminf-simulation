import logging.config
import matplotlib.pyplot as plot
import matplotlib.patches as patches

logging.getLogger(__name__)


class BlockPlotView:

    @staticmethod
    def display():
        # Erstelle eine neue Abbildung
        fig, ax = plot.subplots(figsize=(8, 6))

        # Füge ein Dreieck hinzu
        triangle = patches.Polygon([[0.2, 0.2], [0.5, 0.8], [0.8, 0.2]], closed=True, color="lightblue",
                                   edgecolor="blue", label="Dreieck")
        ax.add_patch(triangle)

        # Füge ein Rechteck hinzu
        rectangle = patches.Rectangle((0.1, 0.6), 0.3, 0.2, color="lightgreen", edgecolor="green", label="Rechteck")
        ax.add_patch(rectangle)

        # Füge einen Kreis hinzu
        circle = patches.Circle((0.7, 0.7), 0.1, color="pink", edgecolor="red", label="Kreis")
        ax.add_patch(circle)

        # Zusätzliche Optionen
        ax.set_xlim(0, 1)  # x-Achsenbereich
        ax.set_ylim(0, 1)  # y-Achsenbereich
        ax.set_aspect('equal', adjustable='box')  # Gleiche Skalierung für x und y
        ax.set_title("Zeichnung mit verschiedenen Formen", fontsize=14)
        ax.legend()

        # Anzeige
        plot.grid(True)
        plot.show()
