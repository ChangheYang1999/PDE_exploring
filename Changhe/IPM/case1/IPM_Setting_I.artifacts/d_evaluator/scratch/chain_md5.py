"""Compare every GPU end shape recorded in the chain log ("step K: <tag> ..." start line, "step K done: ... md5 <m>")
with <tag>_shape.npz in the artifacts tree a_coefficients (or a given directory). Usage: python3 scratch/chain_md5.py [dir]"""
import re, sys, hashlib, os
T = 'artifacts'
A = sys.argv[1] if len(sys.argv) > 1 else T + '/a_coefficients'
L = open('gpu_chain.log').read().splitlines()
tag, md5 = {}, {}
for l in L:
    m = re.match(r'\S+Z step (\d+[a-z]?): (\S+) ', l)
    if m: tag[m.group(1)] = m.group(2)
    m = re.match(r'\S+Z step (\d+[a-z]?) done.*md5 ([0-9a-f]{32})', l)
    if m: md5[m.group(1)] = m.group(2)
ok = bad = miss = 0
for k in sorted(md5, key=lambda s: int(re.match(r'\d+', s).group())):
    t = tag.get(k, '?'); f = os.path.join(A, t + '_shape.npz')
    if not os.path.exists(f): print('step %s %s: MISSING' % (k, t)); miss += 1; continue
    h = hashlib.md5(open(f, 'rb').read()).hexdigest()
    s = 'ok' if h == md5[k] else 'DIFFERS (%s)' % h
    ok += h == md5[k]; bad += h != md5[k]
    print('step %s %s: %s' % (k, t, s))
print('ok %d, differ %d, missing %d' % (ok, bad, miss))
