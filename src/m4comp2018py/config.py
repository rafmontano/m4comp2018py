# config.py
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "m4comp2018py/data"

RDA_FILENAME = "M4.rda"
TAR_FILENAME = "M4comp2018_0.2.0.tar.gz"

RDA_PATH = DATA_DIR / RDA_FILENAME
M4_TARBALL_PATH = DATA_DIR / TAR_FILENAME

M4_TARBALL_URL = "https://github.com/carlanetto/M4comp2018/releases/download/0.2.0/M4comp2018_0.2.0.tar.gz"