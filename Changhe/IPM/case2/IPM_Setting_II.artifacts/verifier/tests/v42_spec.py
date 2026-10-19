"""Angular spectrum of a state per radial band: max over the band of |rho_m| / |rho_0| for selected m (fractions of
Nyquist).  Usage: python3 tests/v42_spec.py FILE [FILE ...]  (own format rho,r,th or lead/numerics format g,lr,th; p
taken from the file or the name)."""
import sys, re, numpy as np
for f in sys.argv[1:]:
    d = np.load(f, allow_pickle=True)
    if 'rho' in d.files:
        rho = d['rho']; t = np.log(d['r'])
    else:
        mm = re.search(r'p([0-9.]+?)_', f.split('/')[-1]); p = float(mm.group(1)) if mm else float(d['p'])
        t = d['lr']; rho = np.exp(p*t)[:, None]*d['g']
    nt = rho.shape[1]; F = np.abs(np.fft.rfft(rho, axis=1))
    ms = [nt//16, nt//8, nt//4, nt//2 - 8, nt//2 - 3, nt//2]
    print(f.split('/')[-1], 'nt', nt, 'm =', ms)
    for lo_, hi_ in ((-16, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 3)):
        k = (t >= lo_) & (t < hi_)
        if k.sum() == 0:
            continue
        print('  t %g..%g ' % (lo_, hi_) + ' '.join('%.1e' % (F[k][:, m]/F[k][:, 0]).max() for m in ms))
