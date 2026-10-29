"""Lead cross-review of the verifier's b-family exclusion (phi = z(1 + b z^2)/(2(1 + a s + z^2)^(p + 1)), p = 1/(2c)).
On the upper axis, with w = c z + 2 phi(0, z), x = z^(-2p): h = H z^(-2p)(1 - b x + o(x)) and e = 2h(h - 1)/w has the coefficient
(2H/c)(H + b + b/c) of z^(-1 - 4p), while -Delta_5 phi on the axis has only the powers z^(-1 - 2p - 2j)."""
import json, time
import sympy as sp
t0 = time.time()
z, b, H, p = sp.symbols('z b H p', positive=True)
c = 1/(2*p)
res = {}
# leading terms of phi(0, z) for large z: (b/2) z^(1 - 2p) (1 + O(z^-2)); keep w = c z + b z^(1 - 2p)
w = c*z + b*z**(1 - 2*p)
rate = sp.simplify((sp.diff(w, z) - (1 + c))/w)
# expand rate in y = z^(-2p) at fixed z prefactor: rate = -2p/z + C z^(-1 - 2p) + O(z^(-1 - 4p))
y = sp.symbols('y', positive=True)
rate_y = sp.simplify((rate*z).subs(z**(-2*p), y).subs(z**(2*p), 1/y))
rate_y = sp.simplify(rate_y.rewrite(sp.exp))
ser = sp.series(sp.simplify(((sp.diff(w, z) - (1 + c))*z/w).subs(z, y**(-1/(2*p)))), y, 0, 2).removeO()
res['rate_series'] = str(sp.simplify(ser))
res['rate_ok'] = sp.simplify(ser - (-2*p + 2*p*b*y)) == 0
# h = H z^(-2p) exp(-b y + ...): d/dz log h = -2p/z + 2 p b z^(-1-2p): check derivative of -b z^(-2p) equals 2 p b z^(-1-2p)
res['log_h_ok'] = sp.simplify(sp.diff(-b*z**(-2*p), z) - 2*p*b*z**(-1 - 2*p)) == 0
h = H*y*(1 - b*y)
e = 2*h*(h - 1)/(c*(1 + b*y/c))   # times 1/z
es = sp.series(e, y, 0, 3).removeO()
coef1 = sp.simplify(es.coeff(y, 1)); coef2 = sp.simplify(es.coeff(y, 2))
res['e_y1'] = str(coef1); res['e_y2'] = str(sp.factor(coef2))
res['e_y2_ok'] = sp.simplify(coef2 - (2*H/c)*(H + b + b/c)) == 0
res['seconds'] = round(time.time() - t0, 1)
print(json.dumps(res, indent=1))
json.dump(res, open('checks/t1bfamily_check_output.json', 'w'), indent=1)
