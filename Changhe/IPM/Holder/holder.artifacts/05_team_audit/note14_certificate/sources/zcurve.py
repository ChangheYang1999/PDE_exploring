"""Geometry of the zero set Z for the signed-distance witness (beta = pi/4; poles 0 and e1; m = (1/2,0)); arb arithmetic.

Two modes.
 PolyGeom(a): axis + Gamma_1 (segment (1,0)-(1,a) then ray at 60 deg) + Gamma_0 + point reflections   (the polygon of NUM_REPORT sec. 4).
 CurveGeom(y1, q, Ymax): axis + polyline approximation of the EXACT zero curve of nu = K(.-e1) - K(.), K = z1 z2/(pi|z|^4):
   upper-right branch  z1 = 1/2 + b(y), b(y)^2 = [1/4 - y^2 + 2 sqrt(y^4 + y^2/4 + 1/16)]/3  (the verification work's formula, checked numerically);
   vertices (1,0), (1,y1) [vertical start: the exact curve satisfies z1 - 1 = y^4 - 2 y^6 + O(y^8) there], then points on the curve at
   heights y1 q^k <= Ymax rounded to double precision (exact dyadics), then the ray in direction 60 deg from the last vertex.
   The other three branches are the images under z2 -> -z2 and z1 -> 1 - z1.  Any such closed set is admissible.
Each geometry provides: dist(px,py) -> arb enclosure of dist(z,Z); sigma(px,py) -> arb(+-1) or None (undecidable);
exact_radius() -> r such that on B(e1, r) the nearest part of Z is {axis} u {vertical segment through e1};
unique_nearest(cx, cy, rQ, D) -> True if the nearest point of Z is certified unique for every z in B(c, rQ) (D = dist(c,Z) > rQ),
so that dist(.,Z) is C^{1,1} there with |Hess| <= 1/(D - rQ)  (polygonal Z: 0 in straight regimes, 1/D in vertex regimes).
Rigor: all pruning uses certified arb lower bounds (bounding boxes); floating point is used only to PROPOSE a candidate.
Audited: an external review note (repairs applied as recommended).
"""
import math
import numpy as np
from flint import arb

def sqrt_nonneg(x):
    if not x.is_finite():
        raise ValueError("nonfinite square")
    if x > 0:
        return x.sqrt()
    up = arb(x.upper())
    if up < 0:
        raise ValueError("negative square enclosure")
    return arb(0).union(up.sqrt()) if up > 0 else arb(0)

def seg_dist(px, py, ax, ay, bx, by):
    vx = bx - ax; vy = by - ay; L2 = vx*vx + vy*vy
    t = ((px - ax)*vx + (py - ay)*vy)/L2
    t = arb.max(arb.min(t, arb(1)), arb(0))
    dx = px - ax - t*vx; dy = py - ay - t*vy
    return sqrt_nonneg(dx*dx + dy*dy)

def ray_dist(px, py, ax, ay, dx, dy):
    t = arb.max((px - ax)*dx + (py - ay)*dy, arb(0))
    ex = px - ax - t*dx; ey = py - ay - t*dy
    return sqrt_nonneg(ex*ex + ey*ey)


class PolyGeom:
    def __init__(self, a_q):
        self.AA = arb(a_q); self.a = float(a_q.p)/float(a_q.q)
        self.C60 = arb(1)/2; self.S60 = arb(3).sqrt()/2; self.C120 = -arb(1)/2; self.S120 = self.S60
    def piece_dists(self, px, py):
        one = arb(1); zero = arb(0); AA = self.AA
        return [abs(py),
                seg_dist(px, py, one, zero, one, AA), ray_dist(px, py, one, AA, self.C60, self.S60),
                seg_dist(px, py, zero, zero, zero, AA), ray_dist(px, py, zero, AA, self.C120, self.S120),
                seg_dist(px, py, zero, zero, zero, -AA), ray_dist(px, py, zero, -AA, -self.C60, -self.S60),
                seg_dist(px, py, one, zero, one, -AA), ray_dist(px, py, one, -AA, -self.C120, -self.S120)]
    def dist(self, px, py):
        ds = self.piece_dists(px, py); d = ds[0]
        for x in ds[1:]:
            d = arb.min(d, x)
        return d
    def sigma_upper(self, px, py):
        AA = self.AA
        if py <= AA:
            x1 = arb(1); x0 = arb(0)
        elif py > AA:
            x1 = 1 + (py - AA)*self.C60/self.S60; x0 = (py - AA)*self.C120/self.S120
        else:
            return None
        if px > x1 or px < x0:
            return arb(1)
        if px < x1 and px > x0:
            return arb(-1)
        return None
    def sigma(self, px, py):
        if py > 0:
            return self.sigma_upper(px, py)
        if py < 0:
            s = self.sigma_upper(1 - px, -py)
            return None if s is None else -s
        return None
    def exact_radius(self):
        return min(self.a, 1.0)/2
    def unique_nearest(self, cx, cy, rQ, D):
        """nearest piece beats every other piece by more than 2 rQ at c => unique nearest point on the ball (pieces are convex)"""
        ds = self.piece_dists(cx, cy)
        order = sorted(range(len(ds)), key=lambda i: float(ds[i].mid()))
        d2 = ds[order[1]]
        for i in order[2:]:
            d2 = arb.min(d2, ds[i])
        return bool(d2 - ds[order[0]] > 2*rQ)


class CurveGeom:
    def __init__(self, y1=1.0/64, q=1.1, Ymax=500.0):
        a0 = 0.5
        xs = [1.0, 1.0]; ys = [0.0, y1]
        y = y1
        while y*q <= Ymax:
            y *= q
            b = math.sqrt((a0*a0 - y*y + 2*math.sqrt(y**4 + a0*a0*y*y + a0**4))/3)
            xs.append(0.5 + b); ys.append(y)
        self.xs, self.ys = xs, ys
        self.N = len(xs) - 1                     # segments 0..N-1 (segment i joins vertices i, i+1); feature N = ray from vertex N
        self.AX = [arb(x) for x in xs]; self.AY = [arb(v) for v in ys]
        self.DX = arb(1)/2; self.DY = arb(3).sqrt()/2
        self.y1 = y1
        # arb bounding boxes of groups of G consecutive segments (certified lower distance bounds for pruning)
        self.G = 8
        self.groups = []
        for g0 in range(0, self.N, self.G):
            g1 = min(self.N, g0 + self.G)
            xs_g = xs[g0:g1 + 1]; ys_g = ys[g0:g1 + 1]
            self.groups.append((g0, g1, arb(min(xs_g)), arb(max(xs_g)), arb(min(ys_g)), arb(max(ys_g))))
        # float copies, used only to propose an initial candidate
        self.fax = np.array(xs[:-1]); self.fay = np.array(ys[:-1]); self.fbx = np.array(xs[1:]); self.fby = np.array(ys[1:])
        self.fvx = self.fbx - self.fax; self.fvy = self.fby - self.fay; self.fL2 = self.fvx**2 + self.fvy**2
        self.frx, self.fry = xs[-1], ys[-1]; self.fdx, self.fdy = 0.5, math.sqrt(3)/2

    # --- elementary feature distances (arb)
    def _seg(self, i, px, py):
        return seg_dist(px, py, self.AX[i], self.AY[i], self.AX[i+1], self.AY[i+1])
    def _ray(self, px, py):
        return ray_dist(px, py, self.AX[self.N], self.AY[self.N], self.DX, self.DY)
    def feat_dist(self, i, px, py):
        return self._ray(px, py) if i >= self.N else self._seg(i, px, py)
    def float_dists(self, px, py):
        t = np.clip(((px - self.fax)*self.fvx + (py - self.fay)*self.fvy)/self.fL2, 0.0, 1.0)
        d = np.hypot(px - self.fax - t*self.fvx, py - self.fay - t*self.fvy)
        tr = max((px - self.frx)*self.fdx + (py - self.fry)*self.fdy, 0.0)
        dr = math.hypot(px - self.frx - tr*self.fdx, py - self.fry - tr*self.fdy)
        return np.append(d, dr)
    @staticmethod
    def box_lb(px, py, xmin, xmax, ymin, ymax):
        """certified lower bound (arb, exact) for the distance from the ball (px,py) to the box"""
        gx = arb.max(arb.max(xmin - px, px - xmax), arb(0)); gy = arb.max(arb.max(ymin - py, py - ymax), arb(0))
        return arb(sqrt_nonneg(gx*gx + gy*gy).lower())
    def ray_lb(self, px, py):
        """certified lower bound for the distance to the ray: the ray lies in {x >= AX[N], y >= AY[N]}"""
        return self.box_lb(px, py, self.AX[self.N], arb('1e300'), self.AY[self.N], arb('1e300'))
    def features_within(self, px, py, thresh):
        """RIGOROUS: all features whose distance to the ball (px,py) may be <= thresh (arb), as [(i, arb distance)].
        A feature is discarded only if a certified lower bound (group box, then segment box) exceeds thresh."""
        out = []
        for (g0, g1, xmin, xmax, ymin, ymax) in self.groups:
            if self.box_lb(px, py, xmin, xmax, ymin, ymax) > thresh:
                continue
            for i in range(g0, g1):
                lbx = arb.min(self.AX[i], self.AX[i+1]); ubx = arb.max(self.AX[i], self.AX[i+1])
                if self.box_lb(px, py, lbx, ubx, self.AY[i], self.AY[i+1]) > thresh:
                    continue
                d = self._seg(i, px, py)
                if not (d > thresh):
                    out.append((i, d))
        if not (self.ray_lb(px, py) > thresh):
            d = self._ray(px, py)
            if not (d > thresh):
                out.append((self.N, d))
        return out
    def branch_dist(self, px, py):
        """arb enclosure of the distance to the branch. Floats propose a feature i0; its arb distance gives an upper bound U;
        every other feature is discarded only by a certified lower bound > U (box bounds); the rest are evaluated in arb."""
        d = self.float_dists(float(px.mid()), float(py.mid()))
        i0 = int(np.argmin(d))
        best = self.feat_dist(i0, px, py)
        for (i, di) in self.features_within(px, py, arb(best.upper())):
            best = arb.min(best, di)
        return best
    # --- the four branches via symmetries of the query point
    def queries(self, px, py):
        return [(px, py), (px, -py), (1 - px, py), (1 - px, -py)]
    def dist(self, px, py):
        d = abs(py)
        for (qx, qy) in self.queries(px, py):
            d = arb.min(d, self.branch_dist(qx, qy))
        return d
    # --- sign
    def x_at(self, y):
        """enclosure of {x(eta): eta in the ball y} for the upper-right branch x(eta) (piecewise linear, then the ray), eta > 0.
        All segments whose height interval may intersect the ball are evaluated with the full ball and united."""
        res = None
        for j in range(self.N):
            if (self.AY[j+1] < y) or (self.AY[j] > y):
                continue
            t = (y - self.AY[j])/(self.AY[j+1] - self.AY[j])
            t = arb.max(arb.min(t, arb(1)), arb(0))
            x = self.AX[j] + t*(self.AX[j+1] - self.AX[j])
            res = x if res is None else res.union(x)
        if not (y < self.AY[self.N]):
            x = self.AX[self.N] + arb.max(y - self.AY[self.N], arb(0))*self.DX/self.DY
            res = x if res is None else res.union(x)
        if res is None:
            raise ValueError("x_at: height not covered")
        return res
    def sigma_upper(self, px, py):
        xR = self.x_at(py); xL = 1 - xR
        if px > xR or px < xL:
            return arb(1)
        if px < xR and px > xL:
            return arb(-1)
        return None
    def sigma(self, px, py):
        if py > 0:
            return self.sigma_upper(px, py)
        if py < 0:
            s = self.sigma_upper(1 - px, -py)
            return None if s is None else -s
        return None
    def exact_radius(self):
        return self.y1/2
    # --- uniqueness of the nearest point on B(c, rQ)
    def unique_nearest(self, cx, cy, rQ, D):
        """features farther than D + 2 rQ at c cannot be nearest anywhere on the ball (feature distances are 1-Lipschitz).
        One feature left: unique (convex). Two adjacent features of one branch sharing vertex V (complete list): unique if the
        ball misses the bisector ray from V in direction e1 + e2 (proof in an external review note, section 3). Else: not certified."""
        thresh = arb((D + 2*rQ).upper())
        feats = []   # (branch, index, distance)
        if not (abs(cy) > thresh):
            feats.append(('axis', -1, abs(cy)))
        for bidx, (qx, qy) in enumerate(self.queries(cx, cy)):
            for (i, d) in self.features_within(qx, qy, thresh):
                feats.append((bidx, i, d))
        if len(feats) <= 1:
            return True
        if len(feats) == 2 and feats[0][0] == feats[1][0] and feats[0][0] != 'axis':
            (b, i, di), (_, j, dj) = feats
            if abs(i - j) == 1:
                qx, qy = self.queries(cx, cy)[b]
                V = max(i, j)
                Vx, Vy = self.AX[V], self.AY[V]
                e1x = self.AX[V-1] - Vx; e1y = self.AY[V-1] - Vy; n1 = sqrt_nonneg(e1x*e1x + e1y*e1y); e1x /= n1; e1y /= n1
                if V >= self.N:   # second feature is the ray
                    e2x, e2y = self.DX, self.DY
                else:
                    e2x = self.AX[V+1] - Vx; e2y = self.AY[V+1] - Vy; n2 = sqrt_nonneg(e2x*e2x + e2y*e2y); e2x /= n2; e2y /= n2
                ux = e1x + e2x; uy = e1y + e2y; nn = sqrt_nonneg(ux*ux + uy*uy)
                if not (nn > 0):
                    return False
                ux /= nn; uy /= nn
                return bool(ray_dist(qx, qy, Vx, Vy, ux, uy) > rQ)
        return False


class Z0Geom:
    """Axis-direction polygon zero set Z0(b) (kernel cos 2theta/(2 pi r^2), beta = 0): midline {z1 = 1/2}; the X segments e1-(1/2,+-1/2),
    0-(1/2,+-1/2); diagonal segments e1-(1+b,+-b) and 0-(-b,+-b); rays from (1+b,+-b) in direction (cos30,+-sin30) and from (-b,+-b)
    in direction (-cos30,+-sin30).  sigma: for z1 > 1/2 with w = z - e1: +1 if |w2| < B(w1), -1 if |w2| > B(w1), where
    B(w1) = -w1 (w1 <= 0), w1 (0 <= w1 <= b), b + (w1 - b) tan30 (w1 > b); sigma(Mz) = -sigma(z), M(z) = (1 - z1, z2).
    Matches structured_lb.sigma0 / make_Z0 (float)."""
    def __init__(self, b_q):
        self.B = arb(b_q); self.b = float(b_q.p)/float(b_q.q)
        self.C30 = arb(3).sqrt()/2; self.S30 = arb(1)/2; self.T30 = self.S30/self.C30
        one = arb(1); zero = arb(0); half = arb(1)/2; B = self.B
        self.segs = [(one, zero, half, half), (one, zero, half, -half), (zero, zero, half, half), (zero, zero, half, -half),
                     (one, zero, 1 + B, B), (one, zero, 1 + B, -B), (zero, zero, -B, B), (zero, zero, -B, -B)]
        self.rays = [(1 + B, B, self.C30, self.S30), (1 + B, -B, self.C30, -self.S30), (-B, B, -self.C30, self.S30), (-B, -B, -self.C30, -self.S30)]
    def piece_dists(self, px, py):
        ds = [abs(px - arb(1)/2)]
        ds += [seg_dist(px, py, *s) for s in self.segs]
        ds += [ray_dist(px, py, *r) for r in self.rays]
        return ds
    def dist(self, px, py):
        ds = self.piece_dists(px, py); d = ds[0]
        for x in ds[1:]:
            d = arb.min(d, x)
        return d
    def sigma_right(self, qx, qy):
        """sign for a point with q1 > 1/2 (certified) or None"""
        w1 = qx - 1; w2 = abs(qy)
        if w1 <= 0:
            Bv = -w1
        elif w1 <= self.B:
            Bv = w1
        elif w1 > self.B:
            Bv = self.B + (w1 - self.B)*self.T30
        else:
            return None
        if w2 < Bv:
            return arb(1)
        if w2 > Bv:
            return arb(-1)
        return None
    def sigma(self, px, py):
        half = arb(1)/2
        if px > half:
            return self.sigma_right(px, py)
        if px < half:
            s = self.sigma_right(1 - px, py)
            return None if s is None else -s
        return None
    def exact_radius(self):
        return 0.0   # no exact own-kernel formula is used for this geometry (see certify_lattice.py)
    def unique_nearest(self, cx, cy, rQ, D):
        ds = self.piece_dists(cx, cy)
        order = sorted(range(len(ds)), key=lambda i: float(ds[i].mid()))
        d2 = ds[order[1]]
        for i in order[2:]:
            d2 = arb.min(d2, ds[i])
        return bool(d2 - ds[order[0]] > 2*rQ)
