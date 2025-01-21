from matplotlib.animation import FuncAnimation

from app.models import BlockSimulationModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view
        self.animation = None

    def run(self):
        self.view.initialize_view(self.model)

        # Connect widgets to methods
        self.view.angle_slider.on_changed(self.update_angle)
        self.view.width_slider.on_changed(self.update_width)
        self.view.coefficient_still_slider.on_changed(self.update_coefficient_still)
        self.view.coefficient_moving_slider.on_changed(self.update_coefficient_moving)

        # Start animation on button clicked
        self.view.start_button.on_clicked(self.start_animation)

        self.view.show()

    def start_animation(self, event):
        self.animation = FuncAnimation(
            fig=self.view.figure,
            func=self.update_animation,
            frames=200,
            interval=20,
            repeat=False
        )

    def update_animation(self, frame):
        self.model.angle += 1

        self.view.sliding_block_patch.set_angle(-self.model.angle)

        return (self.view.sliding_block_patch,)

    # Update widgets functionality
    def update_angle(self, value):
        self.model.angle = value
        self.view.update_view(self.model)

    def update_width(self, value):
        self.model.width = value
        self.view.update_view(self.model)

    def update_coefficient_still(self, value):
        self.model.coefficient_still = value
        self.view.update_view(self.model)

    def update_coefficient_moving(self, value):
        self.model.coefficient_moving = value
        self.view.update_view(self.model)
