import numpy as np

from app.models import BlockSimulationModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view

    def run(self):
        self.view.display(self.model)



    def stop(self):
        pass
