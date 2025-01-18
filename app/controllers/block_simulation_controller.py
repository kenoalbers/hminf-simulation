from app.models import BlockSimulationModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view

    def run(self):
        self.view.initialize_view(self.model)

        # Connect widgets to methods
        self.view.angle_slider.on_changed(self.update_angle)
        self.view.width_slider.on_changed(self.update_width)

        self.view.show()

    def update_angle(self, value):
        self.model.angle = value
        self.view.update_view(self.model)

    def update_width(self, value):
        self.model.width = value
        self.view.update_view(self.model)
