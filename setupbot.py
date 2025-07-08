import subprocess
import os

python_packages = [
    "requests",
    "flask",
    "openai",
    "pandas",
    "aiohttp",
    "beautifulsoup4"
]

system_packages = [
    "git",
    "docker.io",
    "python3-pip"
]

repo_url = "https://github.com/DustinBrooks521/bot-launcher.git"
repo_dir = "bot-launcher"

def install_system_packages():
    print("\n[+] Installing system packages...")
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "install", "-y"] + system_packages)

def install_python_packages():
    print("\n[+] Installing Python packages...")
    subprocess.run(["pip3", "install"] + python_packages)

def clone_repo():
    if not os.path.exists(repo_dir):
        print(f"\n[+] Cloning repo into {repo_dir}...")
        subprocess.run(["git", "clone", repo_url])
    else:
        print(f"\n[!] Repo {repo_dir} already exists. Skipping clone.")

def launch_masterbot():
    print("\n[+] Launching MasterBot...")
    subprocess.run(["python3", f"{repo_dir}/masterbot.py"])

if __name__ == "__main__":
    install_system_packages()
    install_python_packages()
    clone_repo()
    launch_masterbot()
