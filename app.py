from pathlib import Path

a = Path()
for items in a.glob('*.py'):
    print(items)