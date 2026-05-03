# main_ci.py
# CI 전용 실행 파일 - GUI 없이 args로 값 입력받음

import argparse
from utils.makeExampleFiles import ExampleFileCreator
from utils.makeAppLog import setup_logger

logger = setup_logger()

if __name__ == '__main__':

    # ── 입력값 파싱 ──────────────────────────────
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', required=True)  # 폴더 경로
    parser.add_argument('--date',        required=True)  # 날짜 (YYYY-MM-DD)
    parser.add_argument('--time',        required=True)  # 시간 (HH-MM-SS)
    args = parser.parse_args()

    # ── 날짜/시간 파싱 ───────────────────────────
    year, month, day       = args.date.split('-')
    hour, minute, second   = args.time.split('-')

    # ── 샘플 파일 생성 ───────────────────────────
    example = ExampleFileCreator()
    example.load_paths()

    # GUI 입력값 직접 주입
    example.paths['output'] = args.output_path
    example.dt = [year, month, day, hour, minute, second]

    example.makeSampleFolder()
    example.create_allFiles()

    logger.info("CI 실행 완료!")