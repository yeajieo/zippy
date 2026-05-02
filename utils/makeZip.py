import os
import shutil
import zipfile
from datetime import datetime, timedelta
from utils.makeAppLog import setup_logger
logger = setup_logger()

class zipFileCreator:

    def __init__(self, samplePath: str, dt: datetime):
        self.dt = dt
        self.std = self.dt - timedelta(minutes=3)
        self.etd = self.dt + timedelta(minutes=6)
        self.samplePath = samplePath
        self.workPath = ""
        pass

    def makeWorkspaceFolder(self):
        logger.info("=========== START")

        # Delete the previous Dir(workSpace).
        for folder in os.listdir(self.samplePath):
            folder_path = os.path.join(self.samplePath, folder)
            if os.path.isdir(folder_path) and folder.startswith("workSpace"):
                shutil.rmtree(folder_path)
        logger.debug("Success for deleting Workspace dir.")

        # Make the new Dir(workSpace).
        self.workPath = os.path.join(self.samplePath, "workSpace")
        os.makedirs(self.workPath, mode=0o755)
        logger.debug("Success for making new Workspace dir.")

        logger.info("=========== END")
        pass

    def exporting(self):
        logger.info("=========== START")
        flag = False # check the status of exporting

        for fileName in os.listdir(self.samplePath):
            target = os.path.join(self.samplePath, fileName)

            # 1. For .gz files
            if fileName.lower().endswith(".gz"):
                title = fileName.split("_")
                prefix = title[0]
                kindOfLog = prefix.split("-")[1]  # name such as main, system and kernel
                if kindOfLog.startswith("main"): # only main log
                    formattedDateTimeStr = f"{title[1]}{title[2]}{title[3]}_{title[4]}{title[5]}"
                    formattedDateTime = datetime.strptime(formattedDateTimeStr, "%Y%m%d_%H%M")
                    if self.std <= formattedDateTime <= self.etd:
                        shutil.copy2(target, self.workPath)
                        flag = True
                        pass
                continue

            # 2. For .log/.txt files
            elif fileName.lower().endswith(".txt") or fileName.lower().endswith(".log"):
                shutil.copy2(target, self.workPath)
            pass

        if flag == False:
            logger.warning("Done - no target file.")
        else :
            logger.debug("Done - check the format of files.")
        logger.info("=========== END")
        return flag

    # 3. Creating a zip file
    def zipping(self):
        logger.info("=========== START")

        date_str = self.dt.strftime("%y%m%d_%H%M")
        zip_path = os.path.join(self.samplePath, f'XXXXLogs_{date_str}.zip')

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(self.workPath):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, self.workPath)
                    zipf.write(file_path, arcname)

        logger.info("=========== END")
        pass
