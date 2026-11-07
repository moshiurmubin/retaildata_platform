
import sys
from pathlib import Path

# Find the project root: parent of the tests directory.
# __file__ is defined when pytest imports this file, but not in interactive

try:
    PROJECT_ROOT = Path(__file__).resolve().parents[1]
except NameError:
    PROJECT_ROOT = Path.cwd()

# Make common_utils importable during pytest collection.
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))