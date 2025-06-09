from flask import Flask, render_template, request, redirect, url_for, session
import subprocess
from datetime import datetime
import os
import tkinter as tk
from tkinter import filedialog
import threading
import webbrowser
import time

app = Flask(__name__)
app.secret_key = "abc123-super-secret"  # Needed for session support
log_data = []
selected_folder = ""

def ping_host(host):
    try:
        result = subprocess.run(['ping', '-n', '1', '-w', '1000', host],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return result.returncode == 0
    except Exception:
        return False

def open_folder_dialog_sync():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    folder = filedialog.askdirectory()
    root.destroy()
    return folder

@app.route("/", methods=["GET", "POST"])
def index():
    global selected_folder
    result = ""
    error = ""
    hostname = session.get("hostname", "")
    filename = session.get("filename", "")
    result_history = session.get("result_history", [])

    if request.method == "POST":
        action = request.form.get("action")
        hostname = request.form.get("hostname", "").strip()
        filename = request.form.get("filename", "").strip()

        if action == "choose_folder":
            selected = open_folder_dialog_sync()
            if selected:
                selected_folder = selected
            return redirect(url_for("index"))

        if action == "open_folder":
            if selected_folder and os.path.isdir(selected_folder):
                os.startfile(selected_folder)
            return redirect(url_for("index"))

        if action == "clear":
            session["hostname"] = ""
            session["filename"] = ""
            return redirect(url_for("index"))

        if action == "ping":
            session["hostname"] = hostname
            session["filename"] = filename

            if not filename:
                filename = "log"
            if not filename.endswith(".txt"):
                filename += ".txt"

            if not hostname:
                error = "Hostname/IP is required."
            else:
                status = ping_host(hostname)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if not status:
                    error = f"[{timestamp}] ERROR: {hostname} is unreachable."
                    result_history.append(error)
                else:
                    result = f"[{timestamp}] {hostname} is UP"
                    result_history.append(result)
                    if selected_folder and os.path.isdir(selected_folder):
                        filepath = os.path.join(selected_folder, filename)
                        with open(filepath, "a") as f:
                            f.write(result + "\n")

            session["result_history"] = result_history

    return render_template(
        "index.html",
        result=result,
        error=error,
        folder=selected_folder,
        hostname=hostname,
        filename=filename,
        history=session.get("result_history", [])
    )


def open_browser():
    time.sleep(1.5)  # give Flask time to start
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=False)