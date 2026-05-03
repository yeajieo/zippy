# main_ci.py
# CI 전용 실행 파일 - GUI 없이 args로 값 입력받음

import argparse
from datetime import datetime
from utils.makeExampleFiles import ExampleFileCreator
from utils.makeZip import zipFileCreator
from utils.makeAppLog import setup_logger
logger = setup_logger()

if __name__ == '__main__':

    logger.info("=========== START")

    # Generate sample log files.
    example = ExampleFileCreator()
    example.load_paths()
    example.load_datetime()
    example.makeSampleFolder()
    example.create_allFiles()

    # ── Parsing ──────────────────────────────
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', required=True)  # 폴더 경로
    parser.add_argument('--date',        required=True)  # 날짜 (YYYY-MM-DD)
    parser.add_argument('--time',        required=True)  # 시간 (HH-MM-SS)
    args = parser.parse_args()

    targetDate = datetime.strptime(f"{args.date} {args.time}", "%Y-%m-%d %H-%M-%S")
    logger.debug(f"path : {args.output_path}")
    logger.debug(f"date : {targetDate}")

    mz = zipFileCreator(args.output_path, targetDate)
    mz.makeWorkspaceFolder()
    flag = mz.exporting()
    mz.zipping()

    if flag == True:
        logger.info(f"All process is successfully done.")
    else:
        logger.info(f"No log files.")
    logger.info("=========== END")









