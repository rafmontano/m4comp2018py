import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='rpy2')

from m4comp2018py.loader import load_m4
from m4comp2018py.m4series import M4Series
import numpy as np

def main():
    print("🚀 Starting test for M4 dataset loader with M4Series wrapper...")

    try:
        print("📦 Calling load_m4()...")
        m4 = load_m4(force=False)

        print(f"✅ Retrieved M4 object from R. Total series: {len(m4)}")

        # Wrap the first series using M4Series
        ts1 = M4Series(m4[0])

        print("📈 First Time Series Sample:")
        print(f"🔹 Name         : {ts1.st[0]}")
        print(f"🔹 Train (x)    : {np.array(ts1.x)[:5]}")
        print(f"🔹 Test  (xx)   : {np.array(ts1.xx)[:5]}")
        print(f"🔹 Horizon (h)  : {ts1.h[0]}")
        print(f"🔹 Period       : {ts1.period[0]}")
        print(f"🔹 Type         : {ts1.type[0]}")
        print(f"🔹 Fields       : {ts1.keys()}")

        print("✅ Test completed successfully.")

    except Exception as e:
        print("❌ ERROR during M4 loading or inspection:")
        print(f"   {type(e).__name__} - {str(e)}")

if __name__ == "__main__":
    main()