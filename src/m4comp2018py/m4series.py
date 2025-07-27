# src/m4comp2018py/m4series.py
class M4Series:
    def __init__(self, r_series):
        self._r = r_series
        self._fields = list(map(str, r_series.names))

    def __getattr__(self, name):
        if name in self._fields:
            return self._r.rx2(name)
        raise AttributeError(f"'M4Series' object has no attribute '{name}'")

    def keys(self):
        return self._fields

    def to_dict(self, convert_numpy=False):
        """Return all fields as a Python dict. Optionally convert vectors to NumPy arrays."""
        if convert_numpy:
            import numpy as np
            return {k: np.array(self._r.rx2(k)) for k in self._fields}
        return {k: self._r.rx2(k) for k in self._fields}

    def __repr__(self):
        return f"<M4Series: {self.st[0]} | fields: {', '.join(self._fields)}>"