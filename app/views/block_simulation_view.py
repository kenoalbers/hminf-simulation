import logging.config
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from app.models import BlockSimulationModel
from matplotlib.widgets import Slider, Button


logging.getLogger(__name__)


class BlockSimulationView:
    @staticmethod
    def get_opposite_length(angle, adjacent):
        return np.tan(np.radians(angle)) * adjacent

    @staticmethod
    def display(model: BlockSimulationModel):
        # Create new plot
        fig, ax = plt.subplots(figsize=(9, 9), layout='constrained')

        ax.set_visible(False)
        ax = fig.add_axes((0.55, 0.1, 0.4, 0.8))
        ax.set_title('Block Simulation')
        ax.axis([0, 2, 0, 4])
        ax.set_aspect('equal', adjustable='box')

        # Print triangle
        model.angle = 45
        triangle_opposite = BlockSimulationView.get_opposite_length(model.angle, 1)
        triangle_patch = patches.Polygon(((0.0, 0.0), (1.0, 0.0), (0.0, triangle_opposite)), closed=True)
        ax.add_patch(triangle_patch)

        # Print block
        model.width = 0.3
        block_patch = patches.Rectangle((1, 2), model.width, 0.1, angle=-model.angle, color='red')
        ax.add_patch(block_patch)

        # Collision block
        collision_block_patch = patches.Rectangle((1, 0), 0.3, 0.1, color='green')
        ax.add_patch(collision_block_patch)

        # Angle slider
        ax_angle_slider = fig.add_axes((0.18, 0.8, 0.2, 0.04))
        angle_slider = Slider(
            ax=ax_angle_slider,
            label='Angle',
            valmin=0,
            valmax=75,
            valinit=model.angle,
            orientation= 'horizontal'
        )

        def update_angle(value):
            model.angle = value

            new_opposite_length = BlockSimulationView.get_opposite_length(model.angle, 1)
            triangle_patch.set_xy(((0.0, 0.0), (1.0, 0.0), (0.0, new_opposite_length)))
            block_patch.set_angle(-model.angle)

            fig.canvas.draw_idle()

        # Width slider
        ax_width_slider = fig.add_axes((0.18, 0.7, 0.2, 0.04))
        width_slider = Slider(
            ax=ax_width_slider,
            label='Width',
            valmin=0.1,
            valmax=0.6,
            valinit=model.width,
            orientation= 'horizontal'
        )

        def update_width(value):
            model.width = value

            block_patch.set_width(model.width)

            fig.canvas.draw_idle()

        # Coefficient of friction - still
        ax_coefficient_still_slider = fig.add_axes((0.18, 0.6, 0.2, 0.04))
        coefficient_still_slider = Slider(
            ax=ax_coefficient_still_slider,
            label='Static coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation= 'horizontal'
        )

        # Coefficient of friction - moving
        ax_coefficient_moving_slider = fig.add_axes((0.18, 0.5, 0.2, 0.04))
        coefficient_moving_slider = Slider(
            ax=ax_coefficient_moving_slider,
            label='Kinetic coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation='horizontal'
        )

        ax_start_button = fig.add_axes((0.18, 0.3, 0.2, 0.04))
        place_block_button = Button(ax_start_button, 'Place Block (Start)')

        def place_block(event):
            opposite_length = BlockSimulationView.get_opposite_length(model.angle, 1)
            block_patch.set_xy((0.0, opposite_length))

            # Deactivate slider
            angle_slider.set_active(False)
            width_slider.set_active(False)
            coefficient_still_slider.set_active(False)
            coefficient_moving_slider.set_active(False)

            fig.canvas.draw_idle()

        place_block_button.on_clicked(place_block)

        angle_slider.on_changed(update_angle)
        width_slider.on_changed(update_width)

        plt.grid(True)
        plt.show()
