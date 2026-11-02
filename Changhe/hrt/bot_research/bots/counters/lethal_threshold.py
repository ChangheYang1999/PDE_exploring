"""Exact least positive lethal count for a monotone fixed-map damage callback."""
from collections.abc import Callable


def minimum_lethal_count(damage: Callable[[int], int], hp: int, n_max: int = 2000):
    """Return the first lethal count in 1..n_max, or None if none is lethal.

    The caller must supply a deterministic nondecreasing damage function on
    the positive integer domain. No assumption about damage(0) is required.
    """
    if type(hp) is not int or hp <= 0:
        raise ValueError('hp must be a positive integer.')
    if type(n_max) is not int or n_max < 0:
        raise ValueError('n_max must be a nonnegative integer.')
    if n_max == 0:
        return None
    lo, hi = 0, 1
    while damage(hi) < hp:
        lo = hi
        if hi == n_max:
            return None
        hi = min(2 * hi, n_max)
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if damage(mid) >= hp:
            hi = mid
        else:
            lo = mid
    return hi
