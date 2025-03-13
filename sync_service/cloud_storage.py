import requests
from loguru import logger


class CloudStorage:
    def __init__(self, cloud_folder):
        self.cloud_folder = cloud_folder
        self.access_token = os.getenv("ACCESS_TOKEN")

    def upload(self, file_path):
        """Upload file to cloud storage."""
        logger.info(f"Uploading {file_path} to cloud storage.")
        # Logic to upload file

    def update(self, file_path):
        """Update file in cloud storage."""
        logger.info(f"Updating {file_path} in cloud storage.")
        # Logic to update file

    def delete(self, filename):
        """Delete file from cloud storage."""
        logger.info(f"Deleting {filename} from cloud storage.")
        # Logic to delete file

    def get_info(self):
        """Get information about files in cloud storage."""
        logger.info("Fetching information from cloud storage.")
        # Logic to get file information
