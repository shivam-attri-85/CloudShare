# CloudShare

> Simple, fast, and private personal file sharing with Flask.

CloudShare is a lightweight web application for uploading, listing, downloading, and managing files from a browser. It is designed for personal use and can run locally or on an AWS EC2 instance so the service remains available when your local computer is offline.

## Features

- Upload files from a browser
- Simple file listing and download workflow
- Refresh the file list without reloading the page
- Health check endpoint for monitoring
- CORS support for API access
- Compatible with AWS EC2 and systemd deployments

## Tech Stack

- Python 3
- Flask
- Flask-CORS
- HTML5, CSS3, and JavaScript
- AWS EC2 with Ubuntu/Linux
- systemd for background service management

## Project Structure

```text
CloudShare/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── backend/               # Backend package
├── templates/
│   └── index.html         # Web interface
├── static/
│   └── style.css          # Application styles
├── uploads/               # Uploaded files, kept local and ignored by Git
└── frontend/              # Frontend-related project files
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/shivam-attri-85/CloudShare.git
cd CloudShare
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

## AWS EC2 Deployment

After connecting to an Ubuntu EC2 instance:

```bash
git clone https://github.com/shivam-attri-85/CloudShare.git
cd CloudShare
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

The application listens on `0.0.0.0:5000`. Allow TCP port `5000` in the EC2 security group's inbound rules, then visit:

```text
http://YOUR_EC2_PUBLIC_IP:5000
```

For production use, place the application behind a reverse proxy such as Nginx and configure HTTPS.

## Run as a systemd Service

Create `/etc/systemd/system/cloudshare.service`:

```ini
[Unit]
Description=CloudShare Flask Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/CloudShare
Environment="PATH=/home/ubuntu/CloudShare/venv/bin"
ExecStart=/home/ubuntu/CloudShare/venv/bin/python /home/ubuntu/CloudShare/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable cloudshare
sudo systemctl start cloudshare
sudo systemctl status cloudshare
```

## API Reference

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | CloudShare web interface |
| `GET` | `/health` | Server health check |
| `POST` | `/upload` | Upload a file using the `file` form field |
| `GET` | `/files` | Return the uploaded file list |
| `GET` | `/download/<filename>` | Download a file |
| `DELETE` | `/delete/<filename>` | Delete a file |

### Health Check

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{
  "status": "healthy"
}
```

### Upload and Download

```bash
curl -X POST -F "file=@test.txt" http://localhost:5000/upload
curl http://localhost:5000/files
curl -O http://localhost:5000/download/test.txt
```

## Security Considerations

CloudShare is intended for personal or private deployments. Before exposing it to the public internet, add:

- User authentication and authorization
- Secure filename handling
- File type and size restrictions
- HTTPS/TLS
- Rate limiting
- Access logging
- Per-user storage controls
- Persistent storage such as Amazon S3

Do not expose a personal deployment publicly without appropriate authentication and security controls.

## Roadmap

- User registration and login
- Multiple-user support
- File search and folder management
- Storage usage dashboard
- File previews
- Shareable download links
- QR-code sharing
- HTTPS configuration
- Amazon S3 integration
- File encryption

## License

This project is available under the MIT License.

## Author

**Shivam Kumar**

CloudShare is a personal cloud file-sharing project built with Flask, JavaScript, and AWS EC2.