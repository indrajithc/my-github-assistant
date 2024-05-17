import subprocess
import sys

def install_dependencies():
    """
    Install project dependencies.
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)

def main():
    # Install dependencies
    install_dependencies()

if __name__ == "__main__":
    main()
