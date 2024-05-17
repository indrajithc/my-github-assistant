import sys
import os

# Add the parent directory of the current script to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)

from src.main import main

if __name__ == "__main__":
    main()