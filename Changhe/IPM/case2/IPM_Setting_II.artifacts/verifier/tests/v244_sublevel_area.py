# V244: exponent check for the sublevel-area integral I(T) = int da int_0^T e^(2 l t) 1[0 <= e^t f(a) < h] dt
# used in the verifier note (s1'): for f with only simple zeros I(T) ~ e^((2l - 1) T); for a double zero
# (f >= 0 nearby) I(T) ~ e^((2l - 1/2) T). Inner integral done in closed form, outer by a fine midpoint rule.
import numpy as np
def I(f, l, T, h=1.0, n=4_000_000):
    a = (np.arange(n) + 0.5) * 2 * np.pi / n
    fa = f(a)
    tmax = np.where(fa > 0, np.minimum(T, np.log(h / np.where(fa > 0, fa, 1.0))), 0.0)
    tmax = np.where(fa == 0, T, np.maximum(tmax, 0.0))
    inner = (np.exp(2 * l * tmax) - 1) / (2 * l)
    return inner.sum() * 2 * np.pi / n
for l in (1.2, 1.5, 3.0):
    for name, f in (('cos (simple)', np.cos), ('cos^2 (double)', lambda a: np.cos(a) ** 2),
                    ('cos^3 (triple, sign change)', lambda a: np.cos(a) ** 3),
                    ('-cos^2 (double, f <= 0)', lambda a: -np.cos(a) ** 2)):
        Ts = np.array([4.0, 6.0, 8.0])
        v = np.array([I(f, l, T) for T in Ts])
        slope = np.diff(np.log(np.maximum(v, 1e-300))) / np.diff(Ts)
        print('l=%.1f %-28s I=%s slopes=%s  (2l-1=%.2f, 2l-1/2=%.2f, 2l-1/3=%.2f)'
              % (l, name, np.array2string(v, precision=3), np.array2string(slope, precision=3),
                 2 * l - 1, 2 * l - 0.5, 2 * l - 1 / 3))
