import yaml
import logging.config


class LoggingUtil:

    @staticmethod
    def __load_config():
        with open('app/configs/logging_config.yaml', 'rt') as file:
            return yaml.safe_load(file.read())

    @staticmethod
    def setup():
        logging.config.dictConfig(LoggingUtil.__load_config())