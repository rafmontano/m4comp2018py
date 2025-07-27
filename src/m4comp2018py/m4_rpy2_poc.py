# File: m4_rpy2_poc.py

import os
import rpy2.robjects as robjects
from rpy2.robjects import r
import numpy as np

# Step 1: Resolve path
rda_path = os.path.abspath("./data/M4.rda")
print(f"\n📁 Python resolved path: {rda_path}")

# Step 2: Check if file exists from Python perspective
if os.path.exists(rda_path):
    print("✅ Python confirms the file exists.\n")
else:
    print("❌ Python says the file does NOT exist. Check your path.\n")
    exit(1)

# Step 3: Attempt to load in R
try:
    r(f'load("{rda_path}")')
    print("✅ R successfully loaded the .rda file.")
except Exception as e:
    print("❌ R failed to load the file.")
    print("🔍 R Exception:", str(e))
    exit(1)

# Step 4: Access the 'M4' object
try:
    M4 = robjects.globalenv['M4']
    print(f"✅ Retrieved M4 object from R. Total series: {len(M4)}")
except Exception as e:
    print("❌ Could not retrieve 'M4' object.")
    print("🔍 R Exception:", str(e))
    exit(1)

# Step 5: Inspect a single time series
try:
    ts1 = M4[0]  # First element (Python index starts at 0)
    print("\n📈 First Time Series Sample:")
    print("🔹 Name:", ts1.rx2("st")[0])
    print("🔹 Train sample (first 5):", np.array(ts1.rx2("x"))[:5])
    print("🔹 Test sample (first 5):", np.array(ts1.rx2("xx"))[:5])
except Exception as e:
    print("❌ Failed to inspect first time series.")
    print("🔍 Exception:", str(e))