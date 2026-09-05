# file-sync-service

Local folder ↔ Cloud sync service (Python)

Overview

file-sync-service is a small, reliable service that monitors a local folder and synchronizes changes (new files, updates, deletions) to a configured cloud storage provider. It is designed to be simple to configure, run, and deploy on a single machine or small server.

Key features

- Periodic scanning and incremental uploads
- Uploads, updates, and deletions mirrored to cloud
- Basic conflict handling and retry logic
- Pluggable cloud provider integration (Yandex Disk support included)
- Config-driven (paths, intervals, credentials)

Quick start

1. Clone the repo:

   git clone https://github.com/GorVoskanyan/file-sync-service.git
   cd file-sync-service

2. Create a virtual environment and install dependencies:

   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Configure

   Copy `config.example.yaml` to `config.yaml` and set the local folder path, cloud provider credentials, and sync interval.

4. Run

   python main.py --config config.yaml

Tips

- Run as a service (systemd) for production-like reliability.
- Use small sync intervals for near-realtime updates, but be mindful of API rate limits for your cloud provider.

Troubleshooting

- Check logs/ output for retry or network errors.
- If files are not syncing, verify credentials and that the configured local path is accessible to the process.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Contact

- GitHub: https://github.com/GorVoskanyan

---

Կարճ հայերեն բնութագիր

Այս ծրագիրը հետևում է տեղացի թղթապանակին և փոխկապակցում է դրա փոփոխությունները ամպային ծառայության հետ (օր. Yandex Disk):