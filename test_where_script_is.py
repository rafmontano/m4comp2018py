# test_where_script_is.py

import os
import sys

print("🔍 Current Working Directory:")
print(os.getcwd())

print("\n📁 Location of this script:")
print(os.path.abspath(__file__))

print("\n📚 sys.path:")
for path in sys.path:
    print("  -", path)

print("\n✅ Sanity Check: Can you import your package?")
try:
    import m4comp2018py
    print("✅ SUCCESS: m4comp2018py is importable")
except Exception as e:
    print("❌ ERROR: Could not import m4comp2018py")
    print("   ", e)