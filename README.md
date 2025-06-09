# 🛰️ Network Monitor Dashboard (Flask + Windows Folder Picker)
A beginner-friendly tool to monitor network reachability (via ping), save results to a chosen folder, and view your history in a clean web dashboard — all running locally on your machine.

---

## Features

- 🔍 Ping any hostname or IP address
- ✍️ Custom or default log filename
- 🌐 Web dashboard with dark mode
- ✅ Input validation
- 📜 Keeps result history during session
- 🧹 "Clear All" button to reset fields
- 📁 Choose a folder to save logs in a particular directory (`.txt` format)
- 📂 "Open Folder" button to view logs directory

---

## Requirements

- Windows
- Python 3.7+
- Flask
- Tkinter (comes with standard Python on Windows)

---

## Setup Instructions

### 1. Create and activate a virtual environment:

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 2. Install dependencies:
`pip install flask`

### 3. Run the app:
`python web_app.py` Then open your browser and go to: http://127.0.0.1:5000

# Optional: Build into a Windows.exe:
### 1. Install PyInstaller: 
`pip install pyinstaller`
### 2. Run this command to build the executable:
`pyinstaller --noconsole --add-data "templates;templates" web_app.py`
### 3. Run the app via:
`dist\web_app\wep_app.exe`

## File Structure:
```
project/
├── web_app.py
├── templates/
│   └── index.html
├── saved_logs/
└── README.md
```
## Notes:
- The folder picker uses tkinter, which must be installed (included by default on Windows).
- Results are saved as .txt files in the folder you select.
- Log file defaults to log.txt if left blank.
