

# bootstrap src path onto PYTHONPATH

import sys, os

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'src'))

print(f"The PYTHON PATH = {sys.path}")

# try to import rule.myrule

import rule.myrule
