from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import ast,hashlib,json,sys
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_internal_jumps'
def check(v,s):
 if not v:raise ValueError(s)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
src=(D/'sources/src__c2_gram.py').read_text();tree=ast.parse(src);names={};facts=[]
for n in ast.walk(tree):
 if isinstance(n,ast.FunctionDef):names.setdefault(n.name,[]).append(n)
def same_func(name,expected):
 n=names[name];check(len(n)==1,'unique '+name);a=n[0];b=ast.parse(expected).body[0]
 if a.body and isinstance(a.body[0],ast.Expr) and isinstance(a.body[0].value,ast.Constant) and isinstance(a.body[0].value.value,str):a.body=a.body[1:]
 check(ast.dump(a)==ast.dump(b),'complete AST '+name);facts.append('Complete '+name+' body matches independently stated reference, excluding docstring only.')
same_func('constraints','''def constraints(NJ, sel):
    rows = []
    for m in range(Mh):
        for join in (tmin, t00):
            for nu in range(NJ + 1):
                row = np.zeros(len(sel))
                for li, gi in enumerate(sel):
                    if gi < nF and int(col_m[gi]) == m:
                        pcs = cols[gi][1]
                        row[li] = (piece_jet(pcs, join, "-", nu) - piece_jet(pcs, join, "+", nu)) * D[gi]
                if np.any(row): rows.append(row)
    return np.array(rows) if rows else np.zeros((0, len(sel)))
''')
same_func('piece_jet','''def piece_jet(pieces, t, side, nu):
    for (a, b, alpha, c) in pieces:
        if side == "-" and b == t: sig = 0.0 if np.isinf(a) else (t - a)
        elif side == "+" and a == t: sig = 0.0
        else: continue
        cc = np.array(c, float)
        for _ in range(nu):
            dc = alpha * cc
            if len(cc) > 1: dc[:-1] += cc[1:] * np.arange(1, len(cc))
            cc = dc
        return float(np.exp(alpha * sig) * np.polyval(cc[::-1], sig))
    return 0.0
''')
main=names['main'][0]
def find_assign(name,expected):
 aa=[n for n in ast.walk(main) if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id==name for t in n.targets)];check(len(aa)==1 and ast.dump(aa[0].value)==ast.dump(ast.parse(expected,mode='eval').body),'assignment '+name);facts.append(name+' = '+expected)
for n,e in [('tmin','float(d["tmin"])'),('t00','float(d["t0"])'),('cols','meta["cols"]'),('nF','len(cols)'),('ntot','nF + 2 + Mh'),('C','constraints(NJ, sel)'),('N','Vct[rank:].T')]:
 if n=='N':continue
 find_assign(n,e)
loop=[n for n in ast.walk(main) if isinstance(n,ast.For) and ast.unparse(n.target)=='(name, sel)'];check(len(loop)==1,'section loop')
expected='[("Fminus", list(range(nF + 2))), ("Fminus_noJ", [i for i in range(nF + 2) if i not in jidx]), ("free", list(range(ntot))), ("free_noJ", [i for i in range(ntot) if i not in jidx])]';check(ast.dump(loop[0].iter)==ast.dump(ast.parse(expected,mode='eval').body),'four section lists');facts.append('All four section selectors include column16 when its label is sp8.')
find_assign('jidx','[i for i, (m, pieces, lab) in enumerate(cols) if lab == "J"]')
find_assign('meta','pickle.load(open(raw.replace(".npz", "_cols.pkl"), "rb"))')
# Source-state only: exact code body has no additional constraints before the stated nullspace.
body=loop[0].body;ci=next(i for i,n in enumerate(body) if isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id=='C');nxt=body[ci+1];check(isinstance(nxt,ast.If) and ast.unparse(nxt.test)=='C.shape[0]','nullspace immediately follows C')
check('np.linalg.svd(C, full_matrices=True)' in ast.unparse(nxt) and 'N = Vct[rank:].T' in ast.unparse(nxt),'nullspace data flow');facts.append('C immediately enters the shown SVD nullspace branch; this certifies source structure, not historical execution.')
fminus=(D/'sources/src__c2_fminus.py').read_text();check('cols=[(m, b.pieces, lab) for (m, b, lab) in cols]' in fminus and 'pickle.dump(dict(' in fminus,'metadata writing')
check('Column functions h_c = x^2 y f_c(t) a_c(theta)' in src and 'a_c = sum_m a_{c,m} cos 2m theta' in src,'documented angular interpretation')
check('acoef = [avec([(int(m), 1.0)]) for (m, pieces, lab) in cols]' in src,'single-mode angular coefficients');facts.append('Documented h=x^2 y f(t) sum_m a_m cos(2m theta) and single-mode angular coefficient construction agree; mode0 factor is x^2y.')
a=json.loads((D/'evidence/compute.json').read_text());ind=json.loads((D/'evidence/independent.json').read_text());ww=a['records'][-1]['witness'];sc=[s for s in ind['raw_scalar_linkage'] if 'copy' in s];check(len(sc)==2,'two extracted scalars only')
for s in sc:
 p=B/s['copy'];check(sha(p)==s['sha256'],'scalar pin');v=np.load(p,allow_pickle=False);check(v.shape==() and v.dtype==np.dtype('float64'),'scalar type');key='tmin_hex' if s['member']=='tmin.npy' else 't0_hex';check(F(float(v))==F(float.fromhex(ww[key])) and F(float(v))==F(s['exact_value']),'independent scalar reread')
facts.append('Primary NumPy scalar reread equals the separate struct-decoded raw NPZ scalar and exact witness endpoint.')
pins={}
for q in [D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/compute.json',D/'evidence/independent.json',Path(__file__),*(D/'sources').iterdir()]:
 if q.is_file():pins[str(q.relative_to(B))]=sha(q)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FROZEN_COMPLETE_CONSTRAINT_SOURCE_AND_SCALAR_BINDING','facts':facts,'files':pins,'scope':'Frozen source-defined mathematical constraints with captured raw endpoint values. Actual historical constraints, N and Q not stored or replayed.'};p=D/'evidence/source_check.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'facts':len(facts),'pins':len(pins)}))
