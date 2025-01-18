import logging.config

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

from app.models import BlockSimulationModel
from matplotlib.widgets import Slider, Button


logging.getLogger(__name__)


class BlockSimulationView:
    def __init__(self):
        self.__figure, self.__axes = plt.subplots(figsize=(9, 9), layout='constrained')

        # Plot options
        self.__axes.set_visible(False)
        self.__axes = self.__figure.add_axes((0.55, 0.1, 0.4, 0.8))
        self.__axes.set_title('Block Simulation')
        self.__axes.axis([0, 2, 0, 4])
        self.__axes.set_aspect('equal', adjustable='box')

        # Patches
        self.__triangle_patch = None
        self.__sliding_block_patch = None
        self.__collision_block_patch = None

        # Widgets
        self.angle_slider = None
        self.width_slider = None
        self.__coefficient_still_slider = None
        self.__coefficient_moving_slider = None

        self.__start_button = None

    def initialize_view(self, model: BlockSimulationModel):
        # Print triangle
        self.__triangle_patch = patches.Polygon(((0.0, 0.0), (1.0, 0.0), (0.0, model.get_opposite_length(1))), closed=True)
        self.__axes.add_patch(self.__triangle_patch)

        # Print block
        self.__sliding_block_patch = patches.Rectangle((1, 2), model.width, 0.1, angle=-model.angle, color='red')
        self.__axes.add_patch(self.__sliding_block_patch)

        # Collision block
        collision_block_patch = patches.Rectangle((1, 0), 0.3, 0.1, color='green')
        self.__axes.add_patch(collision_block_patch)

        self.angle_slider = self._display_angle_slider(self.__figure, model.angle)

        # Coefficient of friction - still
        self.__coefficient_still_slider = self._display_coefficient_still_slider(self.__figure)

        # Coefficient of friction - moving
        self.__coefficient_moving_slider = self._display_coefficient_moving_slider(self.__figure)

        # Width slider
        self.width_slider = self._display_width_slider(self.__figure, model.width)

        self.__start_button = Button(self.__figure.add_axes((0.18, 0.3, 0.2, 0.04)), 'Place Block (Start)')

    def update_view(self, model: BlockSimulationModel):
        # Patches to update
        self.__triangle_patch.set_xy(((0.0, 0.0), (1.0, 0.0), (0.0, model.get_opposite_length(1))))
        self.__sliding_block_patch.set_angle(-model.angle)

        self.__sliding_block_patch.set_width(model.width)

        # Update
        self.__figure.canvas.draw_idle()

    def show(self):
        plt.grid(True)
        plt.show()

    @staticmethod
    def get_rectangle_center(rectangle):
        x, y, width, height = rectangle.get_x(), rectangle.get_y(), rectangle.get_width(), rectangle.get_height()
        x_center = x + width / 2
        y_center = y + height / 2
        return x_center, y_center

    @staticmethod
    def get_opposite_length(angle, adjacent):
        return np.tan(np.radians(angle)) * adjacent

    def _display_angle_slider(self, figure, initial_angle):
        return Slider(
            ax= figure.add_axes((0.18, 0.8, 0.2, 0.04)),
            label='Angle',
            valmin=0,
            valmax=75,
            valinit=initial_angle,
            orientation='horizontal'
        )

    def _display_width_slider(self, figure, initial_width):
        return Slider(
            ax=figure.add_axes((0.18, 0.7, 0.2, 0.04)),
            label='Width',
            valmin=0.1,
            valmax=0.6,
            valinit=initial_width,
            orientation= 'horizontal'
        )

    def _display_coefficient_still_slider(self, figure):
        return Slider(
            ax=figure.add_axes((0.18, 0.6, 0.2, 0.04)),
            label='Static coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation= 'horizontal'
        )

    def _display_coefficient_moving_slider(self, figure):
        return Slider(
            ax=figure.add_axes((0.18, 0.5, 0.2, 0.04)),
            label='Kinetic coefficient',
            valmin=0.1,
            valmax=0.6,
            valinit=0.3,
            orientation='horizontal'
        )
