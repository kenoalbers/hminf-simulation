import logging.config
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from app.models import BlockSimulationModel
from matplotlib.widgets import Slider, Button


logging.getLogger(__name__)


class BlockSimulationView:

    @staticmethod
    def get_rectangle_center(rectangle):
        x, y, width, height = rectangle.get_x(), rectangle.get_y(), rectangle.get_width(), rectangle.get_height()
        x_center = x + width / 2
        y_center = y + height / 2
        return x_center, y_center

    @staticmethod
    def get_opposite_length(angle, adjacent):
        return np.tan(np.radians(angle)) * adjacent

    def _display_angle_slider(self, fig, initial_angle):
        return Slider(
            ax= fig.add_axes((0.18, 0.8, 0.2, 0.04)),
            label='Angle',
            valmin=0,
            valmax=75,
            valinit=initial_angle,
            orientation='horizontal'
        )

    def _display_width_slider(self, fig, initial_width):
        return Slider(
            ax=fig.add_axes((0.18, 0.7, 0.2, 0.04)),
            label='Width',
            valmin=0.1,
            valmax=0.6,
            valinit=initial_width,
            orientation= 'horizontal'
        )

    def _display_coefficient_still_slider(self, fig):
        return Slider(
            ax=fig.add_axes((0.18, 0.6, 0.2, 0.04)),
            label='Static coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation= 'horizontal'
        )

    def _display_coefficient_moving_slider(self, fig):
        return Slider(
            ax=fig.add_axes((0.18, 0.5, 0.2, 0.04)),
            label='Kinetic coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation='horizontal'
        )

    def display(self, width, angle):
        # Create new plot
        figure, axes = plt.subplots(figsize=(9, 9), layout='constrained')

        axes.set_visible(False)
        axes = figure.add_axes((0.55, 0.1, 0.4, 0.8))
        axes.set_title('Block Simulation')
        axes.axis([0, 2, 0, 4])
        axes.set_aspect('equal', adjustable='box')

        # Print triangle
        angle = 45
        triangle_opposite = BlockSimulationView.get_opposite_length(angle, 1)
        triangle_patch = patches.Polygon(((0.0, 0.0), (1.0, 0.0), (0.0, triangle_opposite)), closed=True)
        axes.add_patch(triangle_patch)

        # Print block
        width = 0.3
        block_patch = patches.Rectangle((1, 2), width, 0.1, angle=-angle, color='red')
        axes.add_patch(block_patch)

        # Collision block
        collision_block_patch = patches.Rectangle((1, 0), 0.3, 0.1, color='green')
        axes.add_patch(collision_block_patch)

        angle_slider = self._display_angle_slider(figure, angle)

        def update_angle(value):
            angle = value

            new_opposite_length = BlockSimulationView.get_opposite_length(angle, 1)
            triangle_patch.set_xy(((0.0, 0.0), (1.0, 0.0), (0.0, new_opposite_length)))
            block_patch.set_angle(-angle)

            figure.canvas.draw_idle()

        # Width slider
        width_slider = self._display_width_slider(figure, width)

        def update_width(value):
            width = value

            block_patch.set_width(width)

            figure.canvas.draw_idle()

        # Coefficient of friction - still
        coefficient_still_slider = self._display_coefficient_still_slider(figure)

        # Coefficient of friction - moving
        coefficient_moving_slider = self._display_coefficient_moving_slider(figure)

        ax_start_button = figure.add_axes((0.18, 0.3, 0.2, 0.04))
        place_block_button = Button(ax_start_button, 'Place Block (Start)')

        def place_block(event):
            opposite_length = BlockSimulationView.get_opposite_length(angle, 1)
            block_patch.set_xy((0.0, opposite_length))

            # Deactivate slider
            angle_slider.set_active(False)
            width_slider.set_active(False)
            coefficient_still_slider.set_active(False)
            coefficient_moving_slider.set_active(False)

            x_center, y_center = BlockSimulationView.get_rectangle_center(block_patch)

            print(f"{x_center}, {y_center}")

            figure.canvas.draw_idle()

        place_block_button.on_clicked(place_block)

        angle_slider.on_changed(update_angle)
        width_slider.on_changed(update_width)

        plt.grid(True)
        plt.show()


