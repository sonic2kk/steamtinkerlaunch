
from pathlib import Path

import os

def subscript(file: Path, suffix: str) -> Path:
    return file.parent / (file.name + suffix)
