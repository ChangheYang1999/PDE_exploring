"""Admit the reviewed Q10 root-five tail-only prefix refinement."""
from pathlib import Path
from fractions import Fraction as F
import argparse, sys
sys.dont_write_bytecode=True
from certificate_admission import read, ref, checkref, reviewed, admit
ROOT=Path('research/294_q10_tail_prefix')
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
# Keep the complete fourteen-branch table as the baseline before inserting this refinement.
base=read('research/286_period_ten_prefixes/verification/admission.json')
assert base['verdict']=='PROVED' and base['all_receipt_checks_pass']
cp=ROOT/'verification/tail_checks.json.gz';rp=ROOT/'verification/tail_replay.json'
d=read(cp);r=read(rp);p=read(d['prefix']['path']);polar=read(r['polar']['path'])
assert d['all_checks_pass'] and r['all_checks_pass'] and p['all_checks_pass'] and polar['all_checks_pass']
assert (d['bits'],p['bits'],polar['bits'])==(1536,2048,3072)
assert r['source']==ref(cp) and polar['source']==d['prefix'] and (d['Q'],d['root_index'])==(10,5)
for item in d['inputs']+[d['prefix'],r['source'],r['polar']]+p['inputs']+[p['exact_prefix']]:checkref(item)
assert p['maximum_order']==polar['maximum_order']==120
assert p['exact_prefix_comparisons']==800 and polar['independent_norm_comparisons']==240 and polar['independent_tuning_comparisons']==11
assert len(d['cases'])==len(r['rows'])==2
for c,v in zip(d['cases'],r['rows']):
    assert c['N']==v['N'] and c['M']==v['M'] and c['s']==v['s'] and c['q']==v['q'] and c['box']==v['box']
    assert c['N']==10*c['M'] and c['M'] in (10,12) and c['K']==21 and F(c['s'])>0
    assert v['positive_tail_coefficients']==v['positive_denominator_coefficients']==110 and v['finite_inequalities']==21-c['M'] and v['scalar_identities']==60
    checkref(c['box'])
    b=read(c['box']['path']);assert (b['h'],b['Q'],b['B'],b['N'],b['M'])==(1,10,4,c['N'],c['M'])
    assert b['adaptive']['q']==c['q']
    box=list(map(F,b['adaptive']['box']));image=list(map(F,b['adaptive']['image']));initial=list(map(F,b['Y0']))
    assert all(0<=x<=z and 0<=y<=z for x,y,z in zip(image,initial,box))
best=min(d['cases'],key=lambda c:(c['q'],c['N']));before=base['rows'][4];assert before['root_index']==5
review=reviewed(ROOT,a.review)
result=(f"At the fifth period-ten root, the remaining-response lower bounds are "
        +', '.join(f"s={c['s']} for k>={c['M']}" for c in d['cases'])
        +'. Each tail certificate has110 strictly positive shifted numerator coefficients and110 strictly positive denominator coefficients; the two finite ranges contribute20 inequalities. '
        +f"The exact boxes give q={d['cases'][0]['q']} at N100 and q={d['cases'][1]['q']} at N120. "
        +f"The best sufficient exterior is R>2^({F(best['q'],2)})|epsilon|^5, compared with2^({F(before['best_q'],2)}) from the full-range bound. "
        +'All800 exact low-prefix comparisons,240 independently recomputed norms,11 harmonic/response comparisons and120 independently indexed scalar identities pass. '
        +f"Actual runtimes: Cartesian prefix{p['actual_elapsed_s']:.6f}s, polar replay{polar['actual_elapsed_s']:.6f}s, bound construction{d['actual_elapsed_s']:.6f}s, exact replay{r['actual_elapsed_s']:.6f}s.")
admit(ROOT,a.entry,'Period-ten root-five tail-only sufficient radius',
      'The fifth period-ten branch satisfies the certified longer-prefix exterior bounds using only the responses that remain to be inverted.',
      'Use the independently reviewed comparison theorem262, Cartesian2048-bit and polar3072-bit prefixes through120, Fraction polynomial shifts and rational endpoint inequalities, then exact residue-map box reassembly. Check all evidence hashes and preserve the earlier uniform bound.',
      result,'The stated sufficient bounds are PROVED. No optimal radius, coefficient-growth law or whole-plane extension follows.',cp,review,
      dict(replay=ref(rp),prefix=d['prefix'],polar=r['polar'],previous_prefix_admission=ref('research/286_period_ten_prefixes/verification/admission.json'),best_N=best['N'],best_q=best['q'],best_box=best['box'],previous_best_q=before['best_q']))
generator=Path('code/build_current_radius_table.py');g=generator.read_text();marker="add(Path('research/174_adaptive_majorant_boxes/verification/prefix_N90_sharp.json'),'two-mode',5,90)"
assert marker in g and 'research/294_q10_tail_prefix/verification' not in g
new=f"""# Period-ten root-five tail-only boxes admitted in V{a.entry}.
folder=Path('research/294_q10_tail_prefix/verification')
assert json.loads((folder/'admission.json').read_text())['verdict']=='PROVED'
assert json.loads((folder/'tail_replay.json').read_text())['all_checks_pass']
for p in folder.glob('Q10_root5_N*_tail_box.json.gz'):add(p,'two-mode',5)
"""
generator.write_text(g.replace(marker,new+marker))
(ROOT/'sources/admit_q10_tail_prefix.py').write_bytes(Path(__file__).read_bytes())
