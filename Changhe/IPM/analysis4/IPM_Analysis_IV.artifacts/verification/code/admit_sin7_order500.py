"""Admit finite order-500 checks with a separate centered least-squares replay."""
from pathlib import Path
from hashlib import sha256
import argparse,gzip,json,time
from flint import arb,ctx,fmpq
from stream_precision_audit import dyadic
from certificate_admission import read,ref,checkref,reviewed,stamp,next_entry
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
start=time.monotonic();ctx.prec=3072
base=Path('research/293_sin7_order500');v=base/'verification';cp=v/'sin7/checks.json.gz';fp=v/'sin7/fits.json';op=v/'overlap.json'
c=read(cp);f=read(fp);o=read(op)
assert c['all_checks_pass'] and o['all_checks_pass'] and f['complete']
assert c['M']==f['M']==7 and c['h']==f['h']==2 and c['Q']==f['Q']==5
assert c['maximum_order']==f['N']==500 and c['independent_prefix_order']==20
assert c['bits']==2048 and f['bits']==2304 and o['through_order']==300
assert [r['n'] for r in c['norms']]==list(range(1,501))
assert [r['n'] for r in c['nonlinear']]==[400,500]
assert c['counts']['nonlinear_pairs']==399+499 and c['counts']['statistics']==500
assert c['untuned_final_stream_orders']==[500]
assert f['prior']==ref(cp) and f['harmonics']==c['harmonics']
for r in [c['source'],c['harmonics'],c['log'],c['selected_source'],f['source']]+o['inputs']+o['source_checksums']:checkref(r)
assert sha256(gzip.decompress(Path(c['selected_source']['path']).read_bytes())).hexdigest()==c['selected_raw_sha256']
assert o['printed_norm_equalities']==300 and o['excluded_final_free_harmonic']['frequency']==238
assert o['excluded_final_free_harmonic']['old_zero'] and o['excluded_final_free_harmonic']['overlaps']
ln10=arb(10).log()
y={r['n']:arb(dyadic(*r['f_norm'][:2]),dyadic(*r['f_norm'][2:])).log()/ln10 for r in c['norms']}
replayed=[]
for row in f['fits']:
 L=row['L'];U=row['U'];assert L in [100,200,300,400] and U==500
 ns=list(range(L,U+1));N=len(ns);assert row['sample_count']==N
 sx=sum(ns);sy=sum((y[n] for n in ns),arb(0));mx=arb(sx)/N;my=sy/N
 xs={n:arb(n)-mx for n in ns};ys={n:y[n]-my for n in ns}
 xx=sum((xs[n]**2 for n in ns),arb(0));xy=sum((xs[n]*ys[n] for n in ns),arb(0))
 if row['model']=='n,1':
  assert xx>0;sol=[xy/xx];sol.append(my-sol[0]*mx)
 else:
  assert row['model']=='n,log10(n),1'
  z={n:arb(n).log()/ln10 for n in ns};mz=sum(z.values(),arb(0))/N;z={n:q-mz for n,q in z.items()}
  zz=sum((q*q for q in z.values()),arb(0));xz=sum((xs[n]*z[n] for n in ns),arb(0));zy=sum((z[n]*ys[n] for n in ns),arb(0))
  det=xx*zz-xz*xz;assert det>0
  sol=[(xy*zz-zy*xz)/det,(zy*xx-xy*xz)/det];sol.append(my-sol[0]*mx-sol[1]*mz)
 assert len(sol)==len(row['coefficients']) and all(x.overlaps(arb(q)) for x,q in zip(sol,row['coefficients']))
 A=(sol[0]*ln10).exp();R=(sol[0]*ln10*fmpq(5,4)).exp();assert A.overlaps(arb(row['A'])) and R.overlaps(arb(row['R_fit']))
 replayed.append(dict(L=L,U=U,model=row['model'],coefficients=[q.str(45) for q in sol],A=A.str(45),R_fit=R.str(45)))
assert len(replayed)==8 and {(r['L'],r['model']) for r in replayed}=={(L,m) for L in [100,200,300,400] for m in ['n,1','n,log10(n),1']}
endpoint=(y[500]-y[100])/400
assert endpoint.overlaps(arb(f['endpoint100_to_N']['slope']))
assert (endpoint*ln10).exp().overlaps(arb(f['endpoint100_to_N']['A']))
assert (endpoint*ln10*fmpq(5,4)).exp().overlaps(arb(f['endpoint100_to_N']['R_fit']))
review=reviewed(base,a.review);now=stamp();ledger,old=next_entry(a.entry)
replay=v/'fit_replay.json';replay.write_text(json.dumps(dict(at=now,all_checks_pass=True,bits=ctx.prec,method='Center each regressor, solve the one- or two-regressor covariance system, then recover the intercept.',rows=replayed,evidence=ref(fp),actual_elapsed_s=time.monotonic()-start),indent=2)+'\n')
cc=c['counts'];last=c['norms'][-1];lines=[r for r in replayed if r['model']=='n,1']
result=(f"The unit sin7, delta4/5 run through500 passes independent Cartesian prefix20 comparisons on{cc['prefix_f']} density and{cc['prefix_g']} stream coefficients and{cc['prefix_tuning']} tuned harmonics. All{cc['poisson']} Poisson coefficients,{cc['denominators']} denominator checks and500 logged density norms pass. Complete nonlinear sums at400 and500 check{cc['nonlinear_pairs']} ordered products and{cc['nonlinear_coefficients']} residual coefficients. The order500 density root is{last['f_root']}; maximum input norm-relative radius is{c['maximum_norm_relative_radius']}. Packed overlap through300 is exact on{o['packed_equalities']['f']} density and{o['packed_equalities']['g']} stream entries, with300 identical printed norms; the previously unset g300 mode238 is separately verified against H300. The final g500 free harmonic is unset, so its full norm is excluded. All eight fits are independently replayed at3072bits. The line-fit A values for lower endpoints100,200,300,400 are{[r['A'] for r in lines]}, with radius diagnostics{[r['R_fit'] for r in lines]}. The distinct100..500 endpoint base is{f['endpoint100_to_N']['A']} and its radius diagnostic is{f['endpoint100_to_N']['R_fit']}. Main finite audit runtime{c['actual_elapsed_s']:.6f}seconds.")
scope='CONFIRMED for finite arithmetic and recurrence consistency under the stated coefficient-enclosure hypotheses. The independent centered fit replay validates only the stated finite statistics. The earlier separate convergence theorem is unchanged; no sharp radius, eventual growth law, or uncomputed continuation is inferred.'
p=base/'PROOF.md';(base/'sources'/f'PROOF_before_V{a.entry}.md').write_bytes(p.read_bytes());text=p.read_text();i=text.index('Status:');j=text.index('\n',i);p.write_text(text[:i]+f'Status: finite verification CONFIRMED in V{a.entry} on {now}.'+text[j:]+f'\n## Completed checks\n\n{result}\n\n{scope}\n');snapshot=base/'sources'/f'PROOF_at_V{a.entry}.md';snapshot.write_bytes(p.read_bytes())
receipt=dict(at=now,entry=a.entry,all_checks_pass=True,verdict='CONFIRMED_FINITE',evidence=ref(cp),fits=ref(fp),overlap=ref(op),fit_replay=ref(replay),proof=ref(snapshot),independent_review=ref(review),scope=scope)
(v/'admission.json').write_text(json.dumps(receipt,indent=2)+'\n')
ledger.write_text(old+f'\n## V{a.entry} | {now} | Tuned sin7 finite extension through500\n\n**Claim.** The order500 checkpoint and finite statistics agree with the audited recurrence and preserve the earlier computed prefix.\n\n**Method.** Independent Cartesian prefix, all-order differential Poisson checks, complete nonlinear sums at400 and500, packed overlap, and a separate centered least-squares replay.\n\n**Result.** {result}\n\n**Verdict: {scope}** Evidence: {v}/admission.json.\n')
notes=Path('NOTES_FOR_TEAM.md');notes.write_text(f'## {now} VERIFIER -> TEAM: V{a.entry}, sin7 extension through500\n\n{result}\n\n{scope}\n\n'+notes.read_text())
for name,line in [('WORKLOG.md',f'{now}: V{a.entry} admitted the finite sin7 extension through500.'),('VERIFY_SUMMARY.md',f'V{a.entry}: {result} {scope}'),('research/INDEX.md',f'Update {now}:293 finite arithmetic admittedV{a.entry}, without an infinite tail inference.')]:
 with Path(name).open('a') as h:h.write('\n'+line+'\n')
(base/'sources/admit_sin7_order500.py').write_bytes(Path(__file__).read_bytes());print(json.dumps(dict(at=now,entry=a.entry,result=result)))
