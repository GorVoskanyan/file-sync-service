# file-sync-service

A simple service that monitors a local directory and mirrors any file changes to Yandex Disk. The tool uses the Yandex Disk REST API and the `watchdog` library to watch the filesystem in real time.

## Requirements

- Python 3.8+
- [`requests`](https://pypi.org/project/requests/)
- [`watchdog`](https://pypi.org/project/watchdog/)

Install the dependencies with:

```bash
pip install requests watchdog
```

## Usage

Provide the directory you want to watch and a valid OAuth token for Yandex Disk:

```bash
python sync_service.py <directory> <token>
```

The service will start watching the directory and upload, update or delete files on Yandex Disk as changes occur.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
