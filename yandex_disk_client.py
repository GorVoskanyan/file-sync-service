import os
import requests


class YandexDiskClient:
    """Simple Yandex Disk REST API client."""

    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://cloud-api.yandex.net/v1/disk"
        self.headers = {"Authorization": f"OAuth {self.token}"}

    def _get_upload_url(self, path: str) -> str:
        url = f"{self.base_url}/resources/upload"
        params = {"path": path, "overwrite": "true"}
        resp = requests.get(url, headers=self.headers, params=params)
        resp.raise_for_status()
        return resp.json().get("href")

    def upload_file(self, local_path: str, remote_path: str) -> None:
        """Upload a local file to Yandex Disk"""
        href = self._get_upload_url(remote_path)
        with open(local_path, "rb") as f:
            resp = requests.put(href, files={"file": f})
        resp.raise_for_status()

    def delete_file(self, remote_path: str) -> None:
        url = f"{self.base_url}/resources"
        resp = requests.delete(url, headers=self.headers, params={"path": remote_path})
        if resp.status_code not in (200, 202, 204, 404):
            resp.raise_for_status()
