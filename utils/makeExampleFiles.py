import gzip
import xml.etree.ElementTree as ET
import os
import shutil
from utils.makeAppLog import setup_logger
logger = setup_logger()

class ExampleFileCreator:
    def __init__(self):

        self.paths = None
        self.dt = None
        self.logformat = ['main', 'system']
        self.standalone_files = [
            "bootup.log",
            "calibration_values.txt",
            "crash.log",
            "Dumpstate.log",
            "events.log",
            "kernel.log",
            "main.log",
            "radio.log",
            "README.log",
            "system.log"
        ]
        self.directories = [
            "CLU",
            "Cali",
            "Sync"
        ]
        pass

    def load_paths(self):
        logger.info("=========== START")
        tree = ET.parse("config/paths.xml")
        root = tree.getroot()
        self.paths = {p.attrib["name"]: p.text for p in root.findall("path")}
        logger.info("=========== END")
        pass

    def load_datetime(self):
        logger.info("=========== START")
        tree = ET.parse("config/date.xml")
        root = tree.getroot()
        self.dt = [root.find(tag).text for tag in ["year", "month", "day", "hour", "minute", "second"]]
        logger.info("=========== END")
        pass

    def makeSampleFolder(self):
        logger.info("=========== START")
        if os.path.exists(self.paths["output"]):
            shutil.rmtree(self.paths["output"])
        os.makedirs(self.paths["output"],mode=0o755)
        logger.debug("Success for making new sample dir.")
        logger.info("=========== END")
        pass

    def create_allFiles(self): # Make Dir/files
        logger.info("=========== START")

        logger.debug("Start making .log.gz")
        for i in range(1, 30):  # .log.gz(main/system) files for 30 minutes
            for name in self.logformat:
                output_path = self.paths['output'] + f'/{i}-{name}.log_{self.dt[0]}_{self.dt[1]}_{self.dt[2]}_{self.dt[3]}_{i}_{self.dt[5]}.log.gz'
                with gzip.open(output_path, "wb"):
                    pass
        logger.debug("End making .log.gz")

        logger.debug("Start making .log/.txt")
        for name in self.standalone_files:  # .log/.txt files
            output_path = os.path.join(self.paths['output'], name)
            with open(output_path, "wb"):
                pass
        logger.debug("End making .log/.txt")

        logger.debug("Start making .dir")
        for dir_name in self.directories:  # .dir
            os.makedirs(os.path.join(self.paths['output'], dir_name), exist_ok=True)
        logger.debug("End making .dir")

        logger.info("=========== END")
        pass