# my d = 23 survivors (enum21 filters) against the external list of 49 (x3q certificates)
import json, glob, os
src = open('../d81/enum21.py').read().split('for d in range(5, 23, 2):')[0]; exec(src)
P = list(pats(23)); R = [p for p in P if excluded(*p) is None]
mine = set('%d_%s' % (A0, '_'.join(map(str, mu))) for A0, mu in R)
ext = set(os.path.basename(f)[:-5] for f in glob.glob('../../../referee/x3q/d23/certificates/*.json')
          if not f.endswith(('_stage.json', '_real.json', 'summary.json')))
print(len(P), len(R), len(ext), 'mine - ext:', sorted(mine - ext), 'ext - mine:', sorted(ext - mine))
