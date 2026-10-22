"""Artifact tests on a state: (1) nontriviality: size of Theta, Omega, U relative to the linear strain; (2) the nonlinear
advection U.grad is not negligible relative to beta X.grad (not a linear/polynomial solution); (3) sign structure of Omega
on Q1 (fraction with Omega > 0, max positive, max negative); (4) c from the global inverse; (5) hidden symmetry: is Theta
accidentally of the form y F(y) (x-independent) or Omega of a product form; (6) far-field amplitudes A_1 (free r^-1/beta
part) estimated from g_1 r^{1/beta} at large r."""
import sys, math, json, torch; sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from polarlib import *; from evalfields import *
device = dev()
P, cT, cO, NT, NO, K = load_coefs(sys.argv[1]); beta = P.beta
qmax = P.q_of_u(torch.tensor(1e6, dtype=DT)).item()
r = P.u_of_q(torch.linspace(0, qmax, 1501, dtype=DT, device=device)[1:]) * P.L
th = (torch.arange(60, dtype=DT, device=device) + 0.5) / 60 * (math.pi / 2)
prof = radial_profiles(P, cT, cO, r, NT, NO, K); F = fields_at(prof, r, th, beta, NT, NO)
R = r[:, None].expand_as(F['Th'])
out = dict(file=sys.argv[1], beta=beta, c=prof['c'])
inner = R < 100
out['max_abs_Theta_r<100'] = float(F['Th'][inner].abs().max()); out['max_abs_Omega'] = float(F['Om'].abs().max())
out['max_abs_U_r<100'] = float(torch.sqrt(F['U1'] ** 2 + F['U2'] ** 2)[inner].max())
# nonlinear advection vs linear strain (Theta equation), excluding axes
adv_nl = (F['U1'] * F['Thx'] + F['U2'] * F['Thy']).abs(); adv_lin = (beta * (F['X'] * F['Thx'] + F['Y'] * F['Thy'])).abs()
out['median_ratio_UgradTheta_over_betaXgradTheta_r<100'] = float((adv_nl[inner] / (adv_lin[inner] + 1e-300)).median())
out['max_ratio_UgradTheta_over_betaXgradTheta_r<100'] = float((adv_nl[inner] / (adv_lin[inner] + 1e-300)).max())
# U relative to the pure origin strain (2x, -2y): if U were exactly the strain, Omega = 0 (gauge artifact)
Us = torch.sqrt((F['U1'] - 2 * F['X']) ** 2 + (F['U2'] + 2 * F['Y']) ** 2); Un = torch.sqrt(F['U1'] ** 2 + F['U2'] ** 2)
out['max_|U-strain|/|U|_r<100'] = float((Us[inner] / (Un[inner] + 1e-300)).max())
# sign structure of Omega on Q1 (area-weighted fraction by r dr dphi over r<100)
# area weights r dr dphi: the grid is uniform in q, dr = (dr/dq) dq with dr/dq = L (1/mu)(1-q)^(-2/mu-1)/u ; angles uniform
qg = torch.linspace(0, qmax, 1501, dtype=DT, device=device)[1:]; ug = r / P.L
drdq = P.L * (1 / P.mu) * (1 - qg) ** (-2 / P.mu - 1) / ug
Aw = (r * drdq)[:, None].expand_as(F['Om'])
pos = (F['Om'][inner] > 0).to(DT)
out['area_fraction_Omega_positive_r<100'] = float((pos * Aw[inner]).sum() / Aw[inner].sum())
out['max_positive_Omega'] = float(F['Om'].max()); out['min_Omega'] = float(F['Om'].min())
om_pos_loc = torch.nonzero(F['Om'] == F['Om'].max())[0]; out['argmax_Omega_(r,deg)'] = [float(r[om_pos_loc[0]]), float(th[om_pos_loc[1]] * 180 / math.pi)]
om_neg_loc = torch.nonzero(F['Om'] == F['Om'].min())[0]; out['argmin_Omega_(r,deg)'] = [float(r[om_neg_loc[0]]), float(th[om_neg_loc[1]] * 180 / math.pi)]
# Theta_x sign structure
out['area_fraction_Theta_x_positive_r<100'] = float(((F['Thx'][inner] > 0).to(DT) * Aw[inner]).sum() / Aw[inner].sum())
# hidden symmetry: x-independence of Theta: compare Theta(r,phi)/y with its value on the y axis
Thy_axis = F['Th_y'][:, -1:]
out['max_rel_x_variation_of_Theta/y_r<100'] = float(((F['Th_y'] - Thy_axis).abs() / Thy_axis.abs())[inner].max())
# far-field amplitudes
rr = r.cpu().numpy(); g1 = prof['g'][0].cpu().numpy(); f0 = prof['f'][0].cpu().numpy()
for dec in (1e3, 1e4, 1e5, 1e6):
    i = int(abs(rr - dec).argmin()); out['g1*r^(1/beta)_at_%g' % dec] = float(g1[i] * rr[i] ** (1 / beta)); out['f0*r^-(1-2/beta)_at_%g' % dec] = float(f0[i] * rr[i] ** (-(1 - 2 / beta)))
# energy-like norms (diagnostics only)
print(json.dumps(out, indent=1))
