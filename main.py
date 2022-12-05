import sys
import importlib
from datetime import date

day = date.today().day
if len(sys.argv) > 1:
    day = sys.argv[1]

solution_for_day = importlib.import_module(f"days.day{day}")
solution_for_day.main()
