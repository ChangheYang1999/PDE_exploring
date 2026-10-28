"""Print the certified-enclosure table from runs/cert2/*.json with OUTWARD rounding (lower: floor, upper: ceil at 5 decimals)
and a row-to-file manifest."""
import json, glob, os, math
from fractions import Fraction
from flint import arb, ctx
ctx.prec = 200
def ends(sv):
    x = arb(sv); return float(x.lower()), float(x.upper())
rows = []
for f in sorted(glob.glob('../numerics_data/cert2/*.json')):
    r = json.load(open(f)); tag = os.path.basename(f)[:-5]
    lo = ends(r['I_lower'])[0]; up = ends(r['I_upper'])[1]
    if not (math.isfinite(lo) and math.isfinite(up)) or up - lo > 10: continue
    al = Fraction(r['alpha']); a = Fraction(r['a']); p = r['params']
    rows.append((float(al), r.get('zmode', 'poly'), str(al), str(a), math.floor(lo*1e5)/1e5, math.ceil(up*1e5)/1e5, (lo+up)/2, r['cells'], r['time_s'], p['delta'], p['maxdepth'], p['rho_max'], tag + '.json'))
rows.sort()
print(f"{'alpha':>6} {'Z':>5} {'a':>4} {'lower(floor)':>13} {'upper(ceil)':>12} {'mid':>9} {'cells':>8} {'time':>6} {'delta':>6} {'depth':>5} {'rho_max':>8}  file")
for r in rows:
    print(f"{r[2]:>6} {r[1]:>5} {r[3]:>4} {r[4]:13.5f} {r[5]:12.5f} {r[6]:9.5f} {r[7]:8d} {r[8]:6.0f} {r[9]:6.3f} {r[10]:5d} {r[11]:8.0e}  {r[12]}")
