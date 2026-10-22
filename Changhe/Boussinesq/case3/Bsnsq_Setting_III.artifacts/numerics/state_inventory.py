"""Inventory of the archived continuation states (shift 8): beta, lambda, K, Nt, Nphi, a0, continuation_accepted, beta_basis per npz.
Usage: python3 code/state_inventory.py [glob ...] > runs/state_inventory.txt   (default globs: the lineage-1 / lineage-2 / mscan archives)."""
import sys, glob, os, numpy as np
pats = sys.argv[1:] or ['runs/blam*_beta*.npz', 'runs/blam*_lambda*.npz', 'runs/mscanL2*.npz', 'runs/quad*_beta*.npz']
files = sorted({f for p in pats for f in glob.glob(p) if '_sec' not in f})
def fmt(d, k):
    if k not in d.files: return '-'
    v = d[k]
    try: return f'{float(v):.10g}'
    except Exception: return str(v)
for f in files:
    try: d = np.load(f, allow_pickle=True)
    except Exception as e: print(f, 'ERR', e); continue
    print(f"{os.path.basename(f):44s} beta={fmt(d,'beta'):12s} lam={fmt(d,'lam'):14s} K={fmt(d,'K'):3s} Nt={fmt(d,'Nt'):3s} Nphi={fmt(d,'Nphi'):3s} a0={fmt(d,'a0'):10s} acc={fmt(d,'continuation_accepted'):3s} beta_basis={fmt(d,'beta_basis')}")
