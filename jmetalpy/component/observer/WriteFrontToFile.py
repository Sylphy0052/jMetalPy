import logging
import os

from jmetalpy.core.algorithm.observable import Observer
from jmetalpy.util.solution_list_output import SolutionListOutput

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class WriteFrontToFile(Observer):

    def __init__(self, output_directory):
        super(WriteFrontToFile, self).__init__()
        self.counter = 0
        self.directory = output_directory

        if os.path.isdir(self.directory):
            logger.info("Directory " + self.directory + " exists. Removing contents.")
            for file in os.listdir(self.directory):
                os.remove(self.directory + "/" + file)
        else:
            logger.info("Directory " + self.directory + " does not exist. Creating it.")
            os.mkdir(self.directory)

    def update(self, *args, **kwargs):
        SolutionListOutput.print_function_values_to_file(
            self.directory + "/FUN." + str(self.counter), kwargs["POPULATION"])

        self.counter += 1