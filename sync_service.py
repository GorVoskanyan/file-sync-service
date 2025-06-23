import argparse
import logging
import os
import time
from pathlib import Path

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError as exc:  # pragma: no cover - watchdog optional
    raise SystemExit("watchdog package is required to run the sync service") from exc

from yandex_disk_client import YandexDiskClient


logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")
logger = logging.getLogger(__name__)


class SyncEventHandler(FileSystemEventHandler):
    def __init__(self, client: YandexDiskClient, root: Path):
        super().__init__()
        self.client = client
        self.root = root

    def _remote_path(self, src_path: str) -> str:
        rel = Path(src_path).relative_to(self.root)
        return f"/{rel.as_posix()}"

    def on_created(self, event):
        if event.is_directory:
            return
        logger.info("created %s", event.src_path)
        self.client.upload_file(event.src_path, self._remote_path(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            return
        logger.info("modified %s", event.src_path)
        self.client.upload_file(event.src_path, self._remote_path(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            return
        logger.info("deleted %s", event.src_path)
        self.client.delete_file(self._remote_path(event.src_path))

    def on_moved(self, event):
        if event.is_directory:
            return
        logger.info("moved %s -> %s", event.src_path, event.dest_path)
        self.client.delete_file(self._remote_path(event.src_path))
        self.client.upload_file(event.dest_path, self._remote_path(event.dest_path))


def run_sync(directory: str, token: str):
    path = Path(directory).resolve()
    client = YandexDiskClient(token)
    event_handler = SyncEventHandler(client, path)
    observer = Observer()
    observer.schedule(event_handler, str(path), recursive=True)
    observer.start()
    logger.info("Watching %s", path)
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Watch directory and sync to Yandex Disk")
    parser.add_argument("directory", help="Directory to watch")
    parser.add_argument("token", help="OAuth token for Yandex Disk")
    args = parser.parse_args()
    run_sync(args.directory, args.token)
