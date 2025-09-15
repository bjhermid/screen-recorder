from datetime import datetime
from src.recorder import ScreenRecorder
import os


def generate_filename(folder: str = "data", preflix: str = "screen_record", ext: str = "mp4"):
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join(folder, f"{preflix}_{timestamp}.{ext}")


def main():
    output_file = generate_filename('data', 'test_record', 'mp4')
    recorder = ScreenRecorder(output_file, 30)

    print(f"Perekaman Dimulai dengan status Monitor 1 ..... Tekan Ctl+C untuk berhenti")
    try:
        recorder.start()
    except KeyboardInterrupt:
        recorder.stop()


if __name__ == "__main__":
    main()
