import logging.config

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from app.models import BlockSimulationModel
from matplotlib.widgets import Slider, Button


logging.getLogger(__name__)


class BlockSimulationView:
    def __init__(self):
        self.figure, self.axes = plt.subplots(figsize=(15, 8), layout='constrained')

        # Plot options
        self.axes.set_visible(False)
        self.axes = self.figure.add_axes((0.55, 0.1, 0.4, 0.8))
        self.axes.set_title('Block Simulation')
        self.axes.axis([0, 4, 0, 4])
        self.axes.set_aspect('equal', adjustable='box')

        # Patches
        self.triangle_patch = None
        self.sliding_block_patch = None
        self.collision_block_patch = None

        # Widgets
        self.angle_slider = None
        self.width_slider = None
        self.coefficient_still_slider = None
        self.coefficient_moving_slider = None

        self.start_button = None

    def initialize_view(self, model: BlockSimulationModel):
        # Print triangle
        self.triangle_patch = patches.Polygon(((0.0, 0.0), (2.0, 0.0), (0.0, model.get_opposite_length(2))), closed=True)
        self.axes.add_patch(self.triangle_patch)

        # Print block
        self.sliding_block_patch = patches.Rectangle((2, 2), model.width, 0.1, angle=-model.angle, color='red')
        self.sliding_block_patch.get_xy()
        self.axes.add_patch(self.sliding_block_patch)

        # Collision block
        self.collision_block_patch = patches.Rectangle(model.block2_position, 0.3, 0.1, color='green')
        self.axes.add_patch(self.collision_block_patch)

        inelastic_collision_patch = patches.Rectangle((2,0), 0.01, 0.2, color='grey')
        self.axes.add_patch(inelastic_collision_patch)

        self.angle_slider = self._display_angle_slider(self.figure, model.angle)

        # Coefficient of friction - still
        self.coefficient_still_slider = self._display_coefficient_still_slider(self.figure, model.coefficient_still)

        # Coefficient of friction - moving
        self.coefficient_moving_slider = self._display_coefficient_moving_slider(self.figure, model.coefficient_moving)

        # Width slider
        self.width_slider = self._display_width_slider(self.figure, model.width)

        self.start_button = Button(self.figure.add_axes((0.18, 0.3, 0.2, 0.04)), 'Place Block (Start)')


    def update_view(self, model: BlockSimulationModel):
        # Patches to update
        self.triangle_patch.set_xy(((0.0, 0.0), (2.0, 0.0), (0.0, model.get_opposite_length(2))))
        self.sliding_block_patch.set_angle(-model.angle)

        self.sliding_block_patch.set_width(model.width)

        # Update
        self.figure.canvas.draw_idle()

    def show(self):
        plt.grid(True)
        plt.show()

    # Protected methods
    def _display_angle_slider(self, figure, initial_angle):
        return Slider(
            ax= figure.add_axes((0.18, 0.8, 0.2, 0.04)),
            label='Angle',
            valmin=0,
            valmax=60,
            valinit=initial_angle,
            orientation='horizontal'
        )

    def _display_width_slider(self, figure, initial_width):
        return Slider(
            ax=figure.add_axes((0.18, 0.7, 0.2, 0.04)),
            label='Width',
            valmin=0.1,
            valmax=0.5,
            valinit=initial_width,
            orientation= 'horizontal'
        )

    def _display_coefficient_still_slider(self, figure, initial_coefficient_still):
        return Slider(
            ax=figure.add_axes((0.18, 0.6, 0.2, 0.04)),
            label='Static coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=initial_coefficient_still,
            orientation= 'horizontal'
        )

    def _display_coefficient_moving_slider(self, figure, initial_coefficient_moving):
        return Slider(
            ax=figure.add_axes((0.18, 0.5, 0.2, 0.04)),
            label='Kinetic coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=initial_coefficient_moving,
            orientation='horizontal'
        )
