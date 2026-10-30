#!/usr/bin/env python3
"""H18 check (c1-coord 14:29Z part 8): every N4-### / T4-### ID cited in NUMERICS_FINAL.md is named in a header of c1-n4/VERIFY_REPORT.md or AUDIT_SUMMARY.md / c1-t4/VERIFY_REPORT.md (ranges 'a to b', 'a..b', 'a-b' expanded)."""
import re, sys
R='RUN_ROOT'
nf=open(f'{R}/c1-n1/NUMERICS_FINAL.md').read()
def ledger(path, pre):
    ids=set()
    for h in re.findall(r'^##+ (.*)$', open(path).read(), re.M):
        for x in re.findall(pre+r'-(\d+)', h): ids.add(f'{pre}-{int(x):03d}')
        for a,b in re.findall(pre+r'-(\d+)(?:\.\.|-| to '+pre+r'-| to )(\d+)\b', h):
            if int(b)>int(a) and int(b)-int(a)<40:
                for k in range(int(a), int(b)+1): ids.add(f'{pre}-{k:03d}')
    return ids
n4=ledger(f'{R}/c1-n4/VERIFY_REPORT.md','N4') | ledger(f'{R}/c1-n4/AUDIT_SUMMARY.md','N4')
t4=ledger(f'{R}/c1-t4/VERIFY_REPORT.md','T4')
# expand ranges like 'N4-366 to N4-369' and 'T4-438-441'
cited=set(re.findall(r'\b([NT]4-\d{3})\b', nf))
for a,b in re.findall(r'\b([NT]4-\d{3}) to [NT]4-(\d{3})\b', nf) + re.findall(r'\b([NT]4-\d{3})-(\d{3})\b', nf):
    pre=a[:3]; 
    for k in range(int(a[3:]), int(b)+1): cited.add(f'{pre}{k}')
missing=[c for c in sorted(cited) if (c.startswith('N4') and c not in n4) or (c.startswith('T4') and c not in t4)]
print(f'cited IDs: {len(cited)} ({sum(c.startswith("N4") for c in cited)} N4, {sum(c.startswith("T4") for c in cited)} T4); ledger entries: {len(n4)} N4, {len(t4)} T4')
print('missing:', missing if missing else 'none')
