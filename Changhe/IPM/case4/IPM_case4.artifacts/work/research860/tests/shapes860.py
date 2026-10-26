"""Provider shapes for the T2.6 gates (SPEC v9): one-point Model860, batch Model860 (all points in one call), stateless provider."""
import math, numpy as np
import basis860 as B
from model860 import Model860
from fields860 import residual as stateless_residual
from absolute_common import A_REF
from absolute_model import FrozenLogMesh
from origin860 import ORIGIN_RADIUS

SHARED_SERIES = {}      # {(P bytes, g bytes): Decimal origin-series cache} shared by every shape of the same coefficients (values unchanged; saves the order-48 series per model)

def share_prepared(prepared, P, g):
    """Let a stateless `prepared` dict use the shared origin-series cache of its coefficients."""
    key = (np.asarray(P, float).tobytes(), np.asarray(g, float).tobytes()); prepared['_taylor_cache'] = SHARED_SERIES.setdefault(key, prepared['_taylor_cache']); return prepared

def point_model(xs, ys, workers=1, shared=None):
    """Model860 over an arbitrary point set: a FrozenLogMesh carries (log r, theta); the exact binary64 coordinates are installed directly."""
    xs = np.asarray(xs, float); ys = np.asarray(ys, float); r = np.hypot(xs, ys)
    mesh = FrozenLogMesh(np.log(r), np.arctan2(ys, xs), np.ones(len(xs)), 'pts')
    m = Model860(mesh, A_REF, block_size=4096, mode_block=64, workers=workers, shared_series_cache=SHARED_SERIES if shared is None else shared); m.x = xs.copy(); m.y = ys.copy()
    m.small = r <= ORIGIN_RADIUS; m.direct = np.flatnonzero(~m.small); m.stable = r[m.direct] >= B.R_SWITCH
    return m, np.sqrt(2*mesh.weights/(np.pi*A_REF**2))

def production_single(P, high, x, y, columns=True):
    m, root = point_model([x], [y]); rf = m.fun(P, high)/root
    return (float(rf[0]), (m.jacobian(P, high)/root[:, None])[0]) if columns else (float(rf[0]), None)

def production_batch(P, high, xs, ys, columns=True):
    m, root = point_model(xs, ys); rf = m.fun(P, high)/root
    return (rf, m.jacobian(P, high)/root[:, None]) if columns else (rf, None)

def stateless(prepared, xs, ys, columns=True):
    if columns: rf, dr = stateless_residual(prepared, xs, ys, derivatives=True); return rf, dr
    return stateless_residual(prepared, xs, ys), None
