import numpy as np

from app.models import BlockSimulationModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view

    def run(self):
        self.view.display(self.model.width, self.model.angle)

    def place_block(self):
        pass

    def _update_view(self):
        pass
