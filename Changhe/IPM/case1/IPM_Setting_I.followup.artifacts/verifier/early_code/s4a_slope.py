"""verifier: slopes dB_3^nat/dc_l over the ten fixed-c_l traces from data/s4a_ver_ten_wpp_ode.json (s4a_ver.py)."""
import json, sys
import numpy as np
d = json.load(open('verifier/early_data/s4a_ver_ten_wpp_ode.json'))
names = list(d.keys())
DATA = [k for k in d[names[0]].keys()]
lead = dict(fxn24g=0.30027, fxn16g=0.29694, fxn8g=0.29781, fxn4g=0.29985, fxm2g=0.29952, c6g=0.29961, c6gF=0.29914,
            fxu2g=0.29826, fxu3g=0.29806, fxv24g=0.29817)
print('traces:', names)
cl = np.array([d[n][DATA[0]]['c_l_file'] for n in names])
print('c_l:', ' '.join('%.6f' % v for v in cl))
allslopes = []
for dv in DATA:
    ib = np.array([np.array(d[n][dv]['ibp'], float) for n in names])      # (ntr, 24, 4)
    med = np.nanmedian(ib.reshape(len(names), -1), axis=1)
    sl = []
    for i in range(ib.shape[1]):
        for e in range(ib.shape[2]):
            yv = ib[:, i, e]
            ok = np.isfinite(yv)
            if ok.sum() >= 5:
                sl.append(np.polyfit(cl[ok], yv[ok], 1)[0])
    sl = np.array(sl)
    allslopes.append(sl)
    p = np.polyfit(cl, med, 1)
    resid = med - np.polyval(p, cl)
    print('%-8s medians %s | slope of medians %+.4f (resid rms %.4f) | variant slopes: median %+.4f, IQR [%+.4f, %+.4f], '
          'range [%+.3f, %+.3f], frac<0 %.2f'
          % (dv, ' '.join('%.4f' % v for v in med), p[0], resid.std(), np.median(sl), np.percentile(sl, 25),
             np.percentile(sl, 75), sl.min(), sl.max(), (sl < 0).mean()))
lm = np.array([lead[n] for n in names])
pl = np.polyfit(cl, lm, 1)
print('lead     medians %s | slope of medians %+.4f (resid rms %.4f)' % (' '.join('%.4f' % v for v in lm), pl[0],
      (lm - np.polyval(pl, cl)).std()))
sa = np.concatenate(allslopes)
print('all variants: %d slopes, median %+.4f, IQR [%+.4f, %+.4f], frac<0 %.2f' % (len(sa), np.median(sa),
      np.percentile(sa, 25), np.percentile(sa, 75), (sa < 0).mean()))
# per-trace spread over data variants (method spread)
for n in names:
    meds = [np.nanmedian(np.array(d[n][dv]['ibp'], float)) for dv in DATA]
    print('%-7s c_l %.6f  data-variant medians %s  spread %.4f  lead %.5f' % (n, d[n][DATA[0]]['c_l_file'],
          ' '.join('%.4f' % v for v in meds), max(meds) - min(meds), lead[n]))
