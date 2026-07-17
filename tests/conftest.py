import sys
from pathlib import Path

# Add the project root to Python's module search path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))