# list23.txt (display for draft 82) against the external 49 patterns
import re, glob, os
t = open('../../../questions/ed82/list23.txt').read()
L = re.findall(r'\((\d+); ([\d, ]+)\)', t)
mine = ['%s_%s' % (a, '_'.join(x.split(', '))) for a, x in L]
ext = set(os.path.basename(f)[:-5] for f in glob.glob('../../../referee/x3q/d23/certificates/*.json')
          if not f.endswith(('_stage.json', '_real.json', 'summary.json')))
print(len(mine), len(set(mine)), len(ext), set(mine) == ext, sorted(set(mine) ^ ext))
print('3_3_3_2_2' in mine, '1_5_5_1' in mine)
print(t.rstrip().endswith('1, 1).'), max(len(l) for l in t.split('\n')))
