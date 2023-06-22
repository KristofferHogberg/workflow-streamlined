import subprocess
import webbrowser
import time

def open_tabs(url_list):
    for url in url_list:
        webbrowser.open_new_tab(url)

def start_docker_desktop():
    subprocess.Popen(["C:\Program Files\Docker\Docker\Docker Desktop.exe"])

if __name__ == "__main__":

    urls = ["https://chat.openai.com/", "https://console.cloud.camunda.io/org/", "https://www.google.com/"]

    open_tabs(urls)

    # Wait for Chrome to open
    time.sleep(3)

    start_docker_desktop()

