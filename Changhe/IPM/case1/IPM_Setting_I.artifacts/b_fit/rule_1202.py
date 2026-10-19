"""Lead (2026-10-18 13:00Z): the 12:02Z reading rule for s2g (fixed c_l) against seg3g (free) from the CPU scans
(32768 x 640 and 24576 x 960) and the 185-label J of my post; the 857-label J is the verifier's (entered by hand).
Usage: python3 rule_1202.py A B"""
import json, sys, re
def summ(tag):
    out = {}
    for suf, nt in (('_scan.json', 640), ('_scan960.json', 960)):
        d = json.load(open(tag + suf)); b = d['bands']
        inner = [k for k in b if k.endswith('/all') and not k.startswith('all') and not k.startswith('1000')]
        out[nt] = dict(Nf_box=b['all/all']['max'], at=(b['all/all']['r_max'], b['all/all']['theta_max']),
                       Nv_le1000=max(b[k]['N4_max'] for k in inner), Nv_gt1000=b['1000<=r<=R/all']['N4_max'], cl=d['cl'])
    try:
        txt = open(tag + '_jsplit.txt').read()
    except OSError:
        txt = ''
    m = re.search(r'spread by region \(max - min over labels\): total ([0-9.e+-]+)', txt)
    out['J185'] = float(m.group(1)) if m else None
    return out
A, B = sys.argv[1], sys.argv[2]
a, b = summ(A), summ(B)
for nt in (640, 960):
    print('%d angles: %s Nf_box %.4e at r %.3f th %.4f | Nv r<=1000 %.4e | Nv r>1000 %.4e | c_l %.9f' % (nt, A, a[nt]['Nf_box'], *a[nt]['at'], a[nt]['Nv_le1000'], a[nt]['Nv_gt1000'], a[nt]['cl']))
    print('%d angles: %s Nf_box %.4e at r %.3f th %.4f | Nv r<=1000 %.4e | Nv r>1000 %.4e | c_l %.9f' % (nt, B, b[nt]['Nf_box'], *b[nt]['at'], b[nt]['Nv_le1000'], b[nt]['Nv_gt1000'], b[nt]['cl']))
    ok = a[nt]['Nf_box'] < b[nt]['Nf_box'] and a[nt]['Nv_le1000'] <= b[nt]['Nv_le1000'] and a[nt]['Nv_gt1000'] <= b[nt]['Nv_gt1000']
    print('   %s lower whole-box N_f and N_v not higher (both ranges): %s' % (A, ok))
print('J185 spread: %s %s, %s %s (the rule reads the 857-label J of the verifier)' % (A, a['J185'], B, b['J185']))
