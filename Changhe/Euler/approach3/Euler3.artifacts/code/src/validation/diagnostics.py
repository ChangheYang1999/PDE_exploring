"""Candidate diagnostics (JSON-able): per-shell RMS of the residual and of every term, maximum scaled residuals,
relative defects with small-denominator flags, nontriviality (vorticity, rotation content, non-axisymmetric
fractions of core and tail), strain identity at the vorticity maximum, core location and width, spectral decay,
tail amplitudes, gauge values."""
from __future__ import annotations
import math
import numpy as np
import torch
from ..equations.fields import alpha_of
from ..equations import residuals as res

def eigvalsh_chunked(A, chunk=8192):
    """Batched symmetric eigenvalues in chunks (cuSOLVER batched syev fails for very large batches)."""
    shp = A.shape[:-2]
    flat = A.reshape(-1, A.shape[-2], A.shape[-1])
    out = torch.cat([torch.linalg.eigvalsh(flat[i:i + chunk]) for i in range(0, flat.shape[0], chunk)], 0)
    return out.reshape(*shp, A.shape[-1])



def _shell_rms_terms(prob, terms, scale, keys):
    out = {}
    for k in keys:
        sh, glob = prob.shell_rms(terms[k], scale)
        out[k] = dict(shells=sh, global_rms=glob)
    return out


def _rel_defect(term_rms, keys, resid_key="sum", floor=1e-12):
    """per shell: RMS(residual) / sum_k RMS(term_k), flagged when denominator is tiny."""
    nsh = len(term_rms[resid_key]["shells"])
    rel, flags = [], []
    for s in range(nsh):
        den = sum(term_rms[k]["shells"][s] for k in keys)
        num = term_rms[resid_key]["shells"][s]
        if den < floor:
            rel.append(None); flags.append("zero_denominator")
        else:
            rel.append(num / den); flags.append("")
    return rel, flags


def candidate_diagnostics(prob, z, holdout=None):
    model = prob.model
    aT, aS, c_l, omega = model.unpack(z)
    c_lf, omf = float(c_l), float(omega)
    alpha = alpha_of(c_lf)
    ev = prob.evaluate(z)
    F = ev['F']
    d = dict(c_l=c_lf, omega=omf, alpha=alpha, omega_over_c_l=omf / c_lf, formulation=prob.formulation,
             L=model.L, Nk=model.Nk, Nr=model.Nr, Na=model.Na, m_parity=model.m_parity, R0=model.R0,
             shell_edges=[float(e) for e in prob.shell_edges[:prob.n_shells + 1]])
    sm = prob.scale_mom(c_l); sv = prob.scale_vort(c_l)
    w_ang = prob.w_ang
    if 'R_u' in ev:
        keys = ['lin', 'adv', 'rot', 'gradP', 'sum']
        tr = _shell_rms_terms(prob, ev['mom_terms'], sm, keys)
        rel, flags = _rel_defect(tr, ['lin', 'adv', 'rot', 'gradP'])
        d['momentum'] = dict(terms=tr, rel_defect_shells=rel, flags=flags,
                             max_scaled=(ev['R_u'].abs().amax(0) * sm[:, None]).max().item(),
                             rms_weighted=tr['sum']['global_rms'])
        f = res.pressure_source(F['GU'])
        d['pressure'] = dict(max_abs_P=ev['P'].abs().max().item(), monopole_int_f=prob.pressure.volume_integral(f).item(),
                             p0=prob.pressure.p0)
    if 'R_Om' in ev:
        keys = ['lin', 'adv', 'rot', 'stretch', 'sum']
        tr = _shell_rms_terms(prob, ev['vort_terms'], sv, keys)
        rel, flags = _rel_defect(tr, ['lin', 'adv', 'rot', 'stretch'])
        d['vorticity'] = dict(terms=tr, rel_defect_shells=rel, flags=flags,
                              max_scaled=(ev['R_Om'].abs().amax(0) * sv[:, None]).max().item(),
                              rms_weighted=tr['sum']['global_rms'])
    # nontriviality
    U, GU = F['U'], F['GU']
    Om = F['Om'] if 'Om' in F else None
    if Om is None:
        # vorticity from GU: Om_i = eps_ijk d_j U_k
        Om = torch.stack([GU[1, 2] - GU[2, 1], GU[2, 0] - GU[0, 2], GU[0, 1] - GU[1, 0]], 0)
    absU = U.norm(dim=0); absOm = Om.norm(dim=0)
    rc = res.rotation_content(F)
    def wnorm(X):   # weighted L2 norm with the fixed-gauge momentum scaling
        return math.sqrt(((X ** 2).sum(0) * sm[:, None] ** 2 * w_ang[None, :] * prob.w_node[:, None]).sum().item())
    d['nontriviality'] = dict(max_abs_U=absU.max().item(), max_abs_Omega=absOm.max().item(),
                              rotation_content_rel=wnorm(rc) / max(wnorm(U), 1e-300),
                              U_wnorm=wnorm(U), Omega_wnorm=wnorm(Om))
    # strain identity at |Omega| max: Omega . S Omega / |Omega|^2 (= 1 for exact smooth decaying profile)
    idx = absOm.flatten().argmax().item(); j, a = divmod(idx, model.Na)
    S = 0.5 * (GU[:, :, j, a] + GU[:, :, j, a].T)
    om = Om[:, j, a]
    strain_val = (om @ (S @ om) / max((om @ om).item(), 1e-300)).item()
    Sfull = 0.5 * (GU + GU.transpose(0, 1))                      # (3,3,Nr,Na)
    eig = eigvalsh_chunked(Sfull.permute(2, 3, 0, 1))          # (Nr,Na,3)
    d['strain'] = dict(omega_S_omega_over_omega2_at_max=strain_val, lambda_max_S_global=eig[..., -1].max().item(),
                       r_at_Omega_max=model.r[j].item(), theta_at_Omega_max=model.grid.theta[a].item(),
                       phi_at_Omega_max=model.grid.phi[a].item())
    # core profile: angular RMS of |Omega| vs r
    prof = ((absOm ** 2) * w_ang[None, :]).sum(1).sqrt()          # (Nr,)
    pmax = prof.max().item(); jpk = prof.argmax().item()
    above = (prof > 0.5 * pmax).nonzero().flatten()
    d['core'] = dict(r_peak_Omega=model.r[jpk].item(), Omega_profile_max=pmax,
                     r_halfmax_lo=model.r[above.min()].item(), r_halfmax_hi=model.r[above.max()].item(),
                     Omega_profile=[float(v) for v in prof.cpu().numpy()], r_nodes=[float(v) for v in model.r.cpu().numpy()])
    # tail amplitudes and non-axisymmetric fractions
    l = model.l_arr; m = model.m_arr
    eT, eS = prob.mode_tail_energies(aT, aS, c_l, omega)
    tot = (eT + eS).sum().item()
    d['tail'] = dict(norm2=tot, nonaxi_fraction=((eT + eS)[m > 0].sum().item() / max(tot, 1e-300)),
                     toroidal_fraction=eT.sum().item() / max(tot, 1e-300),
                     by_l={int(ll): float((eT + eS)[l == ll].sum().item() / max(tot, 1e-300)) for ll in sorted(set(l.tolist()))},
                     by_m={int(mm): float((eT + eS)[m == mm].sum().item() / max(tot, 1e-300)) for mm in sorted(set(m.tolist()))})
    # coefficient spectra (core): energy per k and per l of all coefficients
    c2 = aT ** 2 + aS ** 2
    d['spectra'] = dict(per_k=[float(v) for v in (c2.sum(1) / c2.sum()).cpu().numpy()],
                        per_l={int(ll): float(c2[:, l == ll].sum().item() / c2.sum().item()) for ll in sorted(set(l.tolist()))},
                        nonaxi_coef_fraction=c2[:, m > 0].sum().item() / c2.sum().item(),
                        top_k_fraction=float(c2[-1].sum().item() / c2.sum().item()),
                        top_l_fraction=float(c2[:, l == l.max()].sum().item() / c2.sum().item()))
    d['gauge'] = dict(tail_norm2=prob.tail_norm2(aT, aS, c_l, omega).item(),
                      pivot=prob.pivot, gauge_residuals=[float(v) for v in prob.gauge_residuals(aT, aS, c_l, omega, z=z).detach().cpu().numpy()])
    return d


def summary_line(d):
    parts = [f"c_l={d['c_l']:.4f} omega={d['omega']:.4f}"]
    if 'momentum' in d:
        parts.append(f"R_u rms={d['momentum']['rms_weighted']:.3e} max={d['momentum']['max_scaled']:.2e}")
    if 'vorticity' in d:
        parts.append(f"R_Om rms={d['vorticity']['rms_weighted']:.3e} max={d['vorticity']['max_scaled']:.2e}")
    n = d['nontriviality']
    parts.append(f"|Om|max={n['max_abs_Omega']:.2e} rot={n['rotation_content_rel']:.2f} tail_nonaxi={d['tail']['nonaxi_fraction']:.2f} strain={d['strain']['omega_S_omega_over_omega2_at_max']:.2f}")
    return " ".join(parts)
