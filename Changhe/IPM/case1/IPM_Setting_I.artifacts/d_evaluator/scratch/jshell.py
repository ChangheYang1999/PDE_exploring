"""Verifier scratch (shift 6): J by shells of distance from P (lead NOTES 22:32:29Z item 4 form) from my 857-label jd2 files.
J_i(eps) is label i's integral stopped at distance eps from P (eps list in the file); shell [a, b) of label i = J_i(a) - J_i(b),
[4, inf) = J_i(4); the spread is max - min over labels. Usage: python3 jshell.py file1 file2 ..."""
import sys, json
import numpy as np
for f in sys.argv[1:]:
    d = json.load(open(f)); e = d['summary']['eps_P']
    J = np.array([r['J'] for r in d['rows']], float)
    ix = {x: i for i, x in enumerate(e)}
    sp = lambda v: float(np.nanmax(v) - np.nanmin(v))
    out = {'[4,inf)': sp(J[:, ix[4.0]]), '[2,4)': sp(J[:, ix[2.0]] - J[:, ix[4.0]]), '[1,2)': sp(J[:, ix[1.0]] - J[:, ix[2.0]]),
           '[0.3,1)': sp(J[:, ix[0.3]] - J[:, ix[1.0]]), '[0.03,0.3)': sp(J[:, ix[0.03]] - J[:, ix[0.3]]),
           '[0.01,0.03)': sp(J[:, ix[0.01]] - J[:, ix[0.03]]), 'total eps 0.03': sp(J[:, ix[0.03]]), 'total eps 0.01': sp(J[:, ix[0.01]])}
    print(f.split('/')[-1], ' '.join('%s %.3e' % kv for kv in out.items()))
