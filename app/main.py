from app.models import BlockSimulationModel
from app.views import BlockSimulationView
from app.controllers import BlockSimulationController

import logging.config

logger = logging.getLogger(__name__)


def run():
    logger.info("Welcome to the app!")
    # Simulation
    BlockSimulationController(
        BlockSimulationModel(),
        BlockSimulationView()
    ).run()
