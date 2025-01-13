import json
import yaml
import logging.config

logger = logging.getLogger(__name__)


class FileUtils:
    """
    parse a given file based on the file-type in the according encoding.
    """

    def __init__(self):
        raise NotImplementedError("This class is not meant to be instantiated.")

    @staticmethod
    def parse_file(file_path=None, file_type=None, file_encoding='utf-8'):
        file_data = None
        try:
            with open(file_path, 'r', encoding=file_encoding) as file:
                if file_type == 'json':
                    file_data = FileUtils.__parse_json(file)
                elif file_type == 'yaml':
                    file_data = FileUtils.__parse_yaml(file)
                # add new filetype here
                else:
                    logger.error("Datatype not supported. Please add option to FileUtils.")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
        except Exception as e:
            logger.error(f"Exception occurred while reading the file {file_path}: {e}")
        else:
            logger.info(f"File successfully read: {file_path}")
        return file_data

    @staticmethod
    def __parse_json(file):
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON file: {e}")
            return None

    @staticmethod
    def __parse_yaml(file):
        try:
            return yaml.safe_load(file)
        except yaml.YAMLError as e:
            logger.error(f"Error parsing YAML file: {e}")
            return None