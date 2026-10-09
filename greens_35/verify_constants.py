"""Exact checks of the numerical constants behind the Green 35 bounds.

Run with `python3 greens_35/verify_constants.py`. The step-function part uses only the standard
library; the Green gamma(p) part needs `mpmath` and is skipped if it is missing.

Step functions: heights a_0..a_{n-1} on n equal cells of [-1/4, 1/4]. The autoconvolution is
piecewise linear with knots at the cell grid, so its supremum is attained at a knot, and
    sup (f*f) / (int f)^2 = 2 n max_k b_k / (sum a)^2,  b = a * a (discrete convolution).
On [0, 1] (the normalisation of 35.lean) the constant is half of that.
"""
import math
from fractions import Fraction
from pathlib import Path

DATA = Path(__file__).parent / "data"

# (file, threshold on [0,1] that 35.lean states)
CONSTRUCTIONS = [
    ("mv10_208.txt", "0.7549"),     # variants.c_inf_upper
    ("ae25_600.txt", "0.75265"),    # variants.c_inf_upper_ae25
    ("ggtw25_1319.txt", "0.7516"),  # variants.c_inf_upper_ggtw25
]


def load(name):
    lines = (DATA / name).read_text().splitlines()
    return [Fraction(s) for s in lines if s and not s.startswith("#")]


def score(a):
    """Exact 2 n max(a*a) / (sum a)^2, computed over a common integer denominator."""
    assert all(x >= 0 for x in a), "heights must be nonnegative"
    den = 1
    for x in a:
        den = den * x.denominator // math.gcd(den, x.denominator)
    ints = [int(x * den) for x in a]
    n = len(ints)
    nz = [(i, x) for i, x in enumerate(ints) if x]
    b = [0] * (2 * n - 1)
    for i, x in nz:
        for j, y in nz:
            b[i + j] += x * y
    s = sum(ints)
    return Fraction(2 * n * max(b), s * s)


def check_step_functions():
    for name, thr in CONSTRUCTIONS:
        a = load(name)
        sc = score(a)
        half = sc / 2
        ok = half <= Fraction(thr)
        print(f"{name:18} n={len(a):5}  [-1/4,1/4]: {float(sc):.7f}  [0,1]: {float(half):.7f}"
              f"  <= {thr}: {ok}  (margin {float(Fraction(thr) - half):.2e})")


def check_green_gamma():
    try:
        import mpmath as mp
    except ImportError:
        print("mpmath not installed; skipping gamma(p)")
        return
    mp.mp.dps = 30
    t = mp.mpf(4) / 3
    S1 = mp.nsum(lambda k: abs(1 / (2 * k) ** 2 - 24 / (mp.pi ** 2 * (2 * k) ** 4)) ** t, [1, mp.inf])
    S2 = mp.nsum(lambda k: abs(1 / (2 * k - 1) ** 3 - 8 / (mp.pi ** 2 * (2 * k - 1) ** 5)) ** t, [1, mp.inf])
    gamma = 2 * (mp.pi ** 2 / 40) ** 4 / (S1 + (6 / mp.pi) ** t * S2) ** 3
    total = (40 / mp.pi ** 2) ** t * (S1 + (6 / mp.pi) ** t * S2)  # sum_{r>=1} |p~(pi r)|^{4/3}
    print(f"Green (25)-(29): S1={mp.nstr(S1, 10)} S2={mp.nstr(S2, 10)} gamma={mp.nstr(gamma, 10)}"
          f" = 1/{mp.nstr(1 / gamma, 8)}")
    print(f"  sum |p~(pi r)|^(4/3) = {mp.nstr(total, 10)}; gamma > 1/7 needs < 14^(1/3) ="
          f" {mp.nstr(mp.cbrt(14), 10)} (slack {mp.nstr(mp.cbrt(14) - total, 4)})")
    print(f"  c(2)^2 >= (1 + gamma)/2 = {mp.nstr((1 + gamma) / 2, 10)}  vs 4/7 = {mp.nstr(mp.mpf(4) / 7, 10)}")


if __name__ == "__main__":
    check_step_functions()
    check_green_gamma()
