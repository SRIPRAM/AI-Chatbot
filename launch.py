import subprocess
import webbrowser
import threading
import time
def open_browser():
    time.sleep(1)
    webbrowser.open("http://192.168.231.48:8501")
threading.Thread(target=open_browser).start()
subprocess.run(["streamlit","run","app.py"])
