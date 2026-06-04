import sys
from pathlib import Path

TEST_DIR = Path(__file__).resolve().parent
DAY_DIR = TEST_DIR.parent.name
PROB_SET_DIR = TEST_DIR.name
WEEK_DIR = TEST_DIR.parents[2]
PROBLEM_DIR = WEEK_DIR / DAY_DIR / PROB_SET_DIR

sys.path.insert(0, str(PROBLEM_DIR))
