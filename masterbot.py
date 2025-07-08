import subprocess
import json
import threading

def run_bot(name, command):
    def _runner():
        print(f"[+] Starting {name}...")
        subprocess.run(command, shell=True)
    return threading.Thread(target=_runner)

with open("config.json") as f:
    config = json.load(f)

bots = []

if config.get("enable_scraper_bot"):
    bots.append(run_bot("ScraperBot", "python3 scraper_bot.py"))

if config.get("enable_clip_bot"):
    bots.append(run_bot("ClipBot", "python3 clip_bot.py"))

if config.get("enable_monitor_bot"):
    bots.append(run_bot("MonitorBot", "python3 monitor_bot.py"))

if config.get("enable_cronk_bridge"):
    bots.append(run_bot("CronkBridge", "python3 cronk_bridge.py"))

for bot in bots:
    bot.start()

for bot in bots:
    bot.join()
