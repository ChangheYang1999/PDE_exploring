"""Independent recomputation (mpmath, 50 digits) of the strict identity-term savings eta_2 + eta_4 = p J s^2 + q K s^4 of the lead's Theorem 3.9
(the verification work V195/V198; lead Note 49), at the local radius s = 1/2: p = alpha(1-alpha), q = p(2-alpha)(3-alpha), J = 653/288 - (63/8) log(4/3),
K = 56627/138240 - (729/512) log(4/3). Output: runs/eta_check.log (agreement with the lead's six-digit values to all printed digits)."""
from mpmath import mp, mpf, log
mp.dps = 50
L = log(mpf(4)/3); J = mpf(653)/288 - mpf(63)/8*L; K = mpf(56627)/138240 - mpf(729)/512*L
print(f"J = {J}  K = {K}")
rows = [('1/20', mpf(1)/20, '2.24579e-5'), ('1/10', mpf(1)/10, '4.25267e-5'), ('1/5', mpf(1)/5, '7.55168e-5'), ('3/10', mpf(3)/10, '9.90074e-5'),
        ('1/2', mpf(1)/2, '1.176250e-4'), ('3/4', mpf(3)/4, '8.80171e-5'), ('9/10', mpf(9)/10, '4.21963e-5'), ('99/100', mpf(99)/100, '4.63842e-6')]
s = mpf(1)/2
for name, a, lead in rows:
    p = a*(1 - a); q = p*(2 - a)*(3 - a); eta = p*J*s**2 + q*K*s**4
    print(f"alpha {name:6s}: eta_2 + eta_4 = {mp.nstr(eta, 12):>16s}   lead/V198: {lead}   ratio {mp.nstr(eta/mpf(lead), 10)}")
