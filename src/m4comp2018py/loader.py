# loader.py
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='rpy2')


import os
import urllib.request
import tarfile
from pathlib import Path
from rpy2.robjects import r, globalenv
from rpy2.robjects.vectors import ListVector
from m4comp2018py import config


def download_m4_tarball():
    os.makedirs(config.DATA_DIR, exist_ok=True)
    print("⬇️ Downloading M4 dataset...")
    urllib.request.urlretrieve(config.M4_TARBALL_URL, config.M4_TARBALL_PATH)
    print(f"✅ Downloaded to: {config.M4_TARBALL_PATH}")


def extract_rda_from_tarball():
    print("📦 Extracting M4.rda from tar.gz...")
    with tarfile.open(config.M4_TARBALL_PATH, "r:gz") as tar:
        # Find actual member that ends with M4.rda
        member = next((m for m in tar.getmembers() if m.name.endswith("M4.rda")), None)
        if not member:
            raise KeyError("❌ M4.rda not found in the tarball.")

        tar.extract(member, path=config.DATA_DIR)

        # Move to expected location with flat name
        extracted_path = config.DATA_DIR / member.name
        final_path = config.RDA_PATH

        # Ensure parent directory exists (already ensured by download step)
        final_path.parent.mkdir(parents=True, exist_ok=True)

        # If nested, move/rename it to flat path
        if extracted_path != final_path:
            extracted_path.rename(final_path)

    print(f"✅ Extracted: {final_path}")

def load_m4(force=False):
    if force or not os.path.exists(config.RDA_PATH):
        print("♻️ Force reload or M4.rda missing. Downloading and extracting...")
        download_m4_tarball()
        extract_rda_from_tarball()
    else:
        print(f"📁 Loading M4.rda from: {config.RDA_PATH}")

    # Load RDA file using R
    if not os.path.exists(config.RDA_PATH):
        raise FileNotFoundError(f"❌ M4.rda not found at: {config.RDA_PATH}")

    r(f'load("{config.RDA_PATH}")')
    m4_data = globalenv['M4']
    print(f"✅ Retrieved M4 object from R. Total series: {len(m4_data)}")
    return m4_data

def extract_series_fields(ts_r_obj):
    """Convert a single R list vector (one M4 series) to a Python dict."""
    return {str(name): ts_r_obj.rx2(name) for name in ts_r_obj.names}