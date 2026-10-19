"""GPU (torch, float64) port of the lead's matrix-free linearised operator CentreDerivative
(lead work/c6: centre_fit.py + linearized.py + solver.py + stationary.py), numerics lane, 2026-10-18.

Every table (grid, fields at the linearisation point, spline/angular basis tensors, quadrature weights, row
selection and weights, the k column, the two centre rows) is taken from the lead's CPU objects, so the
discretisation is the lead's; only the evaluation of J v and J^T u is done on the GPU:
  * the DST/DCT of scipy are replaced by products with the lead's own sin/cos tables (identical to 1e-14,
    checked in the numerics WORKLOG 2026-10-18T11:45Z);
  * the one-pole radial recurrences of modal_integrals (scipy lfilter) and their adjoints are evaluated by a
    doubling (Hillis-Steele) scan, exact in structure, rounding O(eps);
  * everything else is the same arithmetic in the same order up to BLAS/elementwise association.
Validated against the CPU operator by test_gpu_op.py (random vectors, adjoint identity).
Usage: op = CentreDerivative(s, z) (CPU, lead code); g = GPUDerivative(op); g.matvec(v_t), g.rmatvec(u_t) on torch
tensors (float64, cuda); shapes (ncol,) -> (nrow,) and (nrow,) -> (ncol,), nrow = op.shape[0] (includes the source
row and the two centre rows), ncol = len(z) (the k column included; a fixed-c_l solve zeroes its scale)."""
import numpy as np
import torch


def scan_forward(drive, e):
    """ans[i] = drive[i] + e * ans[i-1] along axis 0 (e per column), by doubling."""
    x = drive.clone()
    n = x.shape[0]
    s = 1
    es = e.clone()
    while s < n:
        x = torch.cat([x[:s], x[s:] + es * x[:-s]], dim=0)
        s *= 2
        es = es * es
    return x


def scan_backward(grad, e):
    """drivebar[i] = grad[i] + e * drivebar[i+1] (adjoint of scan_forward)."""
    return torch.flip(scan_forward(torch.flip(grad, [0]), e), [0])


class GPUDerivative:
    def __init__(self, op, device="cuda"):
        base = op.base
        s = base.s
        p = base.p
        f = base.f
        assert not base.fixed, "CentreDerivative uses fixed=False (k column present)"
        assert p.tail_terms == 2 and p.quadrature_order == 4 and s.radial_basis == "spline"
        # referee (astra/gpuport, 12:00Z): the shared Shape may hold a basis built at another k; rebuild before copying.
        if s.basis_k != base.k:
            s.build_basis(base.k)
        assert s.basis_k == base.k
        self.dev = device

        def T(a):
            return torch.as_tensor(np.ascontiguousarray(np.asarray(a, dtype=float)), dtype=torch.float64, device=device)

        self.k = float(base.k)
        self.cl = float(base.cl)
        self.L2 = float(base.L2)
        self.c = float(f["c"])
        self.nr, self.nt = p.nr, p.nt
        self.R = float(p.R)
        self.m = T(p.m)
        self.objective = s.objective
        for name in ("rho", "rt", "ra", "ht", "ha", "ur", "ua", "ux", "uy"):
            setattr(self, name, T(f[name]))
        self.E = T(base.E)
        self.D = T(base.D)
        self.Uadv = T(base.Uadv)
        self.sgn_ht = torch.sign(3 + self.ht)
        self.sgn_U = torch.sign(self.L2 * self.Uadv)
        self.ct = T(p.ct)
        self.st = T(p.st)
        self.rr = T(p.rr)
        self.sin = T(p.sin)
        self.cos = T(p.cos)
        self.sin_int = self.sin[:, 1:-1].contiguous()
        self.project = T(p.project)
        self.mix = T(base.mix)
        self.mcos_last = T(p.m * p.cos[:, -1])
        self.tensor_b = T(s.tensor_b)
        self.tensor_bt = T(s.tensor_bt)
        self.tensor_mult = T(s.tensor_mult)
        self.tensor_lt = T(s.tensor_lt)
        self.tensor_cos = T(s.tensor_cos)
        self.tensor_sinprime = T(s.tensor_sinprime)
        self.singular, self.angular, self.degree = int(s.singular), int(s.angular), int(s.degree)
        if self.singular:
            self.tensor_sg = T(s.tensor_sg)
            self.tensor_sgt = T(s.tensor_sgt)
            self.tensor_sga = T(s.tensor_sga)
            self.tensor_sgap = T(s.tensor_sgap)
        self.rows = torch.as_tensor(np.flatnonzero(s.rows), device=device)
        self.cols = torch.as_tensor(np.asarray(s.cols), device=device)
        self.weight = T(s.weight)
        self.projector = T(p.weights[:, None] * p.sodd.T)
        self.interpolation = None if base.interpolation is None else T(base.interpolation)
        self.source_ratio = float(base.source_ratio) if base.interpolation is not None else None
        self.source_weight = float(s.source_weight)
        self.k_column = T(base.k_column)
        self.J = T(op.J)
        self.e = [T(p.quad4[side][0]) for side in (0, 1)]
        self.w = [T(p.quad4[side][1]) for side in (0, 1)]
        self.ext_lo = T([4., -6., 4., -1.])[:, None]
        self.ext_hi = T([-1., 4., -6., 4.])[:, None]
        self.nrow = int(op.shape[0])
        self.ncol = int(op.shape[1])
        self.shape = (self.nrow, self.ncol)
        self.nbase = (self.angular + 1) * self.degree

    # ---- basis ----
    def apply_basis(self, coef):
        co = coef[:self.nbase].reshape(self.angular + 1, self.degree)
        b = self.tensor_b @ co.T
        bt = (self.tensor_bt @ co.T + self.tensor_lt * b) * self.tensor_mult
        b = b * self.tensor_mult
        h = b @ self.tensor_cos
        ht = bt @ self.tensor_cos
        ha = b @ self.tensor_sinprime
        if self.singular:
            sg = self.tensor_sg @ coef[-self.singular:]
            sgt = self.tensor_sgt @ coef[-self.singular:]
            h = h + sg[:, None] * self.tensor_sga
            ht = ht + sgt[:, None] * self.tensor_sga
            ha = ha + sg[:, None] * self.tensor_sgap
        return h, ht, ha

    def transpose_basis(self, h, ht, ha):
        gh = (h @ self.tensor_cos.T + ha @ self.tensor_sinprime.T) * self.tensor_mult
        gt = (ht @ self.tensor_cos.T) * self.tensor_mult
        co = (self.tensor_b.T @ (gh + self.tensor_lt * gt) + self.tensor_bt.T @ gt).T.reshape(-1)
        if self.singular:
            sg = self.tensor_sg.T @ (h @ self.tensor_sga + ha @ self.tensor_sgap)
            sg = sg + self.tensor_sgt.T @ (ht @ self.tensor_sga)
            co = torch.cat([co, sg])
        return co

    # ---- modal integrals (quadrature order 4, two-term tail: tail_B given) ----
    def _drive(self, vals, side, initial):
        w = self.w[side]
        low = 4 * vals[0] - 6 * vals[1] + 4 * vals[2] - vals[3]
        high = 4 * vals[-1] - 6 * vals[-2] + 4 * vals[-3] - vals[-4]
        ext = torch.cat([low[None], vals, high[None]], dim=0)
        body = (w[:, 0] * ext[:-3] + w[:, 1] * ext[1:-2] + w[:, 2] * ext[2:-1] + w[:, 3] * ext[3:])
        return torch.cat([initial[None], body], dim=0)

    def modal_integrals(self, f, tail_B):
        A = scan_forward(self._drive(f, 0, f[0] / (self.m + 4)), self.e[0])
        fr = torch.flip(f, [0])
        B = torch.flip(scan_forward(self._drive(fr, 1, tail_B), self.e[1]), [0])
        return A, B

    def _drive_transpose(self, drivebar, side):
        w = self.w[side]
        nr = self.nr
        d1 = drivebar[1:]
        extbar = torch.zeros((nr + 2, drivebar.shape[1]), dtype=drivebar.dtype, device=self.dev)
        for off in range(4):
            extbar[off:off + nr - 1] += w[:, off] * d1
        valsbar = extbar[1:-1].clone()
        valsbar[:4] += self.ext_lo * extbar[0][None, :]
        valsbar[-4:] += self.ext_hi * extbar[-1][None, :]
        return valsbar

    def modal_integrals_transpose(self, Abar, Bbar):
        d0 = scan_backward(Abar, self.e[0])
        v0 = self._drive_transpose(d0, 0)
        v0[0] += d0[0] / (self.m + 4)
        d1 = scan_backward(torch.flip(Bbar, [0]), self.e[1])
        v1 = self._drive_transpose(d1, 1)
        fbar = v0 + torch.flip(v1, [0])
        boundarybar = d1[0].clone()
        return fbar, boundarybar

    # ---- tail ----
    def _tail(self, drho_last, drt_last, dra_last):
        k, m, R = self.k, self.m, self.R
        modes = drho_last @ self.projector
        modes_t = drt_last @ self.projector
        second = (modes_t - k * modes) / (k - 1)
        answer = torch.zeros_like(m)
        for exponent, part in ((k, modes - second), (2 * k - 1, second)):
            answer = answer + ((exponent - m + 1) * part[:-1] + (exponent + m + 1) * part[1:]) / (2 * R * (m - 1 - exponent))
        return answer

    # ---- matvec ----
    def matvec(self, vector):
        coef = vector[1:]
        k, cl, L2, m = self.k, self.cl, self.L2, self.m
        dh, dht, dha = self.apply_basis(coef)
        drho = self.rho * dh
        drt = self.rt * dh + self.rho * dht
        dra = self.ra * dh + self.rho * dha
        df = ((drt * self.ct - dra * self.st) / self.rr) @ self.project
        boundary = self._tail(drho[-1], drt[-1], dra[-1])
        A, B = self.modal_integrals(df, boundary)
        dq = (A + B) / (2 * m)
        dv = (B - A) / 2
        dur = -((dq * m) @ self.cos)
        dua = dv @ self.sin
        dvm = dv @ m
        dquot = torch.cat([dvm[:, None], dua[:, 1:-1] * self.mix, (2 * (dv @ self.mcos_last))[:, None]], dim=1)
        dc = (B[0, 0] + df[0, 0] / 2) / 2
        dL2 = -L2 * dc / self.c
        dUadv = (3 + self.ht) * dur + self.ha * dua + dquot + self.ur * dht + self.ua * dha
        total = L2 * dUadv + self.Uadv * dL2
        de = cl * dht + total
        dd = self.sgn_ht * dht
        if self.objective == "normalized":
            dd = dd + self.sgn_U * total
        if self.objective == "absolute":
            dd = torch.zeros_like(dd)
        full = de / self.D - self.E * dd / self.D ** 2
        answer = (full[self.rows][:, self.cols] * self.weight).reshape(-1)
        if self.interpolation is not None:
            tau = self.source_ratio
            da = L2 * dur[:, 0] + self.ux[:, 0] * dL2
            db = L2 * (dur[:, 0] + dvm) + self.uy[:, 0] * dL2
            source = self.source_weight * torch.dot(self.interpolation, db - tau * da)
        else:
            source = torch.zeros((), dtype=torch.float64, device=self.dev)
        answer = torch.cat([answer, source[None]])
        answer = answer + vector[0] * self.k_column
        return torch.cat([answer, self.J @ vector])

    # ---- rmatvec ----
    def rmatvec(self, vec):
        vector = vec[:-2]
        cl, L2, m, k = self.cl, self.L2, self.m, self.k
        v = torch.zeros((self.nr, self.nt + 1), dtype=torch.float64, device=self.dev)
        v[self.rows[:, None], self.cols[None, :]] = vector[:-1].reshape(self.weight.shape) * self.weight
        ge = v / self.D
        gd = -v * self.E / self.D ** 2
        totalbar = ge
        if self.objective == "normalized":
            totalbar = totalbar + gd * self.sgn_U
        htbar = cl * ge
        if self.objective != "absolute":
            htbar = htbar + gd * self.sgn_ht
        ubar = L2 * totalbar
        durbar = ubar * (3 + self.ht)
        duabar = ubar * self.ha
        dquotbar = ubar
        htbar = htbar + ubar * self.ur
        habar = ubar * self.ua
        Lbar = torch.sum(totalbar * self.Uadv)
        dvbar = torch.zeros((self.nr, self.nt - 1), dtype=torch.float64, device=self.dev)
        if self.interpolation is not None:
            sourcebar = vector[-1] * self.source_weight * self.interpolation
            tau = self.source_ratio
            durbar = durbar.clone()
            durbar[:, 0] += L2 * (1 - tau) * sourcebar
            dvbar = dvbar + L2 * sourcebar[:, None] * m
            Lbar = Lbar + torch.dot(sourcebar, self.uy[:, 0] - tau * self.ux[:, 0])
        dqbar = -(durbar @ self.cos.T) * m
        dvbar = dvbar + duabar @ self.sin.T
        dvbar = dvbar + (dquotbar[:, 1:-1] * self.mix) @ self.sin_int.T
        dvbar = dvbar + dquotbar[:, 0, None] * m
        dvbar = dvbar + 2 * dquotbar[:, -1, None] * self.mcos_last
        Abar = dqbar / (2 * m) - dvbar / 2
        Bbar = dqbar / (2 * m) + dvbar / 2
        cbar = -L2 * Lbar / self.c
        Bbar[0, 0] += cbar / 2
        dfbar, boundarybar = self.modal_integrals_transpose(Abar, Bbar)
        dfbar[0, 0] += cbar / 4
        dfxbar = (2 / self.nt) * (dfbar @ self.sin)
        drtbar = dfxbar * self.ct / self.rr
        drabar = -dfxbar * self.st / self.rr
        partbars = []
        for exponent in (k, 2 * k - 1):
            valuebar = boundarybar / (2 * self.R * (m - 1 - exponent))
            partbar = torch.zeros(self.nt, dtype=torch.float64, device=self.dev)
            partbar[:-1] += (exponent - m + 1) * valuebar
            partbar[1:] += (exponent + m + 1) * valuebar
            partbars.append(partbar)
        secondbar = partbars[1] - partbars[0]
        modesbar = partbars[0] - k * secondbar / (k - 1)
        modestbar = secondbar / (k - 1)
        drhobar_last = modesbar @ self.projector.T
        drtbar = drtbar.clone()
        drtbar[-1] += modestbar @ self.projector.T
        hbar = self.rt * drtbar + self.ra * drabar
        hbar[-1] += self.rho[-1] * drhobar_last
        htbar = htbar + self.rho * drtbar
        habar = habar + self.rho * drabar
        answer = self.transpose_basis(hbar, htbar, habar)
        k_part = torch.dot(vector, self.k_column)
        answer = torch.cat([k_part[None], answer])
        return answer + self.J.T @ vec[-2:]
