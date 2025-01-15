from app.views import BlockPlotView

import logging.config

logger = logging.getLogger(__name__)


def run():
    logger.info("Welcome to the app!")
    BlockPlotView.display()