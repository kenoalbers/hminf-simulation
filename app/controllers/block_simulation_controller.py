from app.models import BlockSimulationModel
from app.views import BlockSimulationView


class BlockSimulationController:
    def __init__(self, model: BlockSimulationModel, view: BlockSimulationView):
        self.model = model
        self.view = view

    def run(self):
        self.view.initialize_view(self.model)
        self.view.display()
        self.view.show()

    def update_angle(self, value):
       # self.model.angle = value
        pass

    def update_width(self, value):
        self.model.width = value


    def place_block(self):
        pass

    def _update_view(self):
        pass
