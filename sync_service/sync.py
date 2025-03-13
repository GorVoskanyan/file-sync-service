import os
import time
from dotenv import load_dotenv
from loguru import logger
from cloud_storage import CloudStorage

# Load environment variables
load_dotenv()

SYNC_FOLDER = os.getenv("SYNC_FOLDER")
CLOUD_FOLDER = os.getenv("CLOUD_FOLDER")
SYNC_PERIOD = int(os.getenv("SYNC_PERIOD", 60))


def sync_files():
    """Main function to synchronize files between local folder and cloud storage."""
    cloud_storage = CloudStorage(CLOUD_FOLDER)

    if not os.path.exists(SYNC_FOLDER):
        logger.error(f"Sync folder does not exist: {SYNC_FOLDER}")
        return

    logger.info(f"Starting synchronization for folder: {SYNC_FOLDER}")

    while True:
        # Logic to check and synchronize files
        # Example: upload new files, update modified ones, delete removed ones

        time.sleep(SYNC_PERIOD)  # Wait before next synchronization


if __name__ == "__main__":
    sync_files()
