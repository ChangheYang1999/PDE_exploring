#!/usr/bin/env python3
"""H18 check: every long decimal (>= 7 significant digits, the certified distances, gaps, ceilings and enclosures) quoted in NUMERICS_FINAL.md also appears verbatim in c1-shared/closure_matrix.md (the coordinator's record of the N4/T4 results). Numbers absent from the matrix are listed with their context for manual review."""
import re
R='RUN_ROOT'
nf=open(f'{R}/c1-n1/NUMERICS_FINAL.md').read(); cm=open(f'{R}/c1-shared/closure_matrix.md').read()
nums=set(re.findall(r'(?<![\d.])\d+\.\d{6,}(?:e[+-]?\d+)?', nf))
src={'N4 ledger': open(f'{R}/c1-n4/VERIFY_REPORT.md').read(), 'T4 ledger': open(f'{R}/c1-t4/VERIFY_REPORT.md').read(), 'theory_v03': open(f'{R}/c1-shared/theory_requirements/theory_v03.md').read()}
def sig(x):  # first 8 significant characters of the mantissa (prefix match = truncation/rounding variant)
    m=x.split('e')[0].lstrip('0.'); return x[:x.index(m)+8] if len(m)>=8 else x.split('e')[0]
miss=[]; variant=[]
for x in sorted(nums):
    if x in cm: continue
    pf=sig(x); where=[k for k,t in [('matrix',cm)]+list(src.items()) if pf in t]
    (variant if where else miss).append((x, where, nf[max(0,nf.find(x)-70):nf.find(x)+20].replace('\n',' ')))
print(f'long decimals in NUMERICS_FINAL: {len(nums)}; verbatim in the matrix: {len(nums)-len(miss)-len(variant)}; prefix variant found in a source: {len(variant)}; unmatched: {len(miss)}')
for x,w,c in variant: print(f'  variant {x} -> {w}')
for x,w,c in miss: print(f'  UNMATCHED {x}  <- ...{c}...')
