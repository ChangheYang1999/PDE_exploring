#!/usr/bin/env python3
"""Exact radial arithmetic and transcription audit for result163."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,resource,time,re
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(25,25))
out=Path('research/general_trace_resonance_audit/verification');t0=time.monotonic();counts={}
assert (out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,name):
 counts[name]=counts.get(name,0)+1
 if not b:raise AssertionError(name)
for row in json.loads((out/'manifest.json').read_text())['files']:
 ck(hashlib.sha256(Path(row['frozen']).read_bytes()).hexdigest()==row['sha256'],'frozen_hash')
a=json.loads((out/'result156.json').read_text());b=json.loads((out/'result157.json').read_text());c=json.loads((out/'result158.json').read_text())
records=[]
for case,cont,poly in zip(a['cases'],b['cases'],c['cases']):
 ell=F(case['ell']);K=case['K'];M=case['M'];p=1/ell;delta=1-p
 ck((ell,K,M) in ((F(3),5,2),(F(5,2),9,4)),'case_scope')
 ck(p-K*delta==-M-1,'first_resonance_index')
 pure={k*delta:k for k in range(K+2)};mixed=[];allD=set()
 for l in [0]+list(range(2,(M+2)//2+1)):
  for k in range(int(F(M+2)/delta)+1):
   D=k*delta+2*l
   if D<=M+2:
    allD.add(D)
    if l: mixed.append((k,l,D))
 for k,l,D in mixed:
  for kk in range(K+1):ck(D!=kk*delta,'mixed_sector_isolation')
 resonances=[]
 for D in sorted(allD):
  q=abs(p+1-D)
  # Exhaustive: this bound includes every positive even integer in the radial range.
  for n in range(2,M+4,2):
   if q==n:resonances.append((D,n))
 ck(resonances==[(K*delta,M)],'all_sectors_first_resonance')
 s=[p-i*delta for i in range(K+1)]
 for i in range(K):
  for n in range(2,M+6,2):
   ck(n*n!=(s[i]+1)**2,'precritical_nonresonant_mode')
   ck(s[i]!=-n-1,'precritical_harmonic_velocity_distinct')
 ck((s[K]-(M-1))/2==-M and (s[K]+M+1)/2==0,'critical_source_extraction')
 # Recompute majorants from nearest neighbors, without running either earlier recurrence implementation.
 L=[];C=[F(1)]
 for i in range(K):
  q=abs(s[i]+1);ns=[n for n in range(2,M+6,2) if n<=q]+[n for n in range(2,M+6,2) if n>=q][:1]
  B=max((F(n)+q)/abs(F(n)-q) for n in set(ns or [2]))
  Li=B*((F(3,2)**K)+1)/2;L.append(Li)
  ck(B==F(cont['B'][i]) and Li==F(cont['L'][i]),'majorant_transcription')
 for k in range(1,K+1):
  v=sum(L[i]*(abs(s[k-1-i])+1)*C[i]*C[k-1-i] for i in range(k))/(ell*k*delta);C.append(v)
  ck(v==F(cont['C'][k]),'majorant_recursion')
 g0=F(case['g_epsilon'][0]);eps0=min(F(1),abs(g0)/(2*M*(K+1)*C[K]*(2**K+1)**K))
 ck(eps0==F(cont['epsilon0']),'exact_persistence_radius')
 g2=F(case['g_epsilon'][2]);mod=1000003
 ck(F(case['g_epsilon'][1])==0 and g2!=0,'highmode_nonzero_quadratic')
 ck(g2.denominator%mod!=0 and (g2.numerator*pow(g2.denominator,-1,mod))%mod==case['quadratic_residue'],'modular_transcription')
 coeff=[F(x) for x in poly['g_coefficients']];ints=list(map(int,poly['g_primitive_integer']))
 ck(len(coeff)==K+2 and coeff[-1]!=0,'degree_from_nonzero_leading_coefficient')
 factor=F(ints[0])/coeff[0]
 ck(factor>0 and all(F(i)==factor*q for i,q in zip(ints,coeff)),'positive_integer_polynomial_scale')
 variation=poly['sturm_variations'];nroot=2 if ell==3 else 4
 ck(variation['minus_infinity']-variation['plus_infinity']==nroot==variation['zero']-variation['one'],'exact_root_count_transcription')
 ck(len(poly['root_brackets'])==nroot,'all_brackets_transcribed')
 for r in poly['root_brackets']:
  low,high=map(F,r['refined']);initial=list(map(F,r['initial']))
  ck(0<initial[0]<=low<high<=initial[1]<1,'root_brackets_inside_positive_trace_range')
 t=p-M-2
 ck(ell*t-1==-ell*(M+2),'density_log_transport_divisor')
 ck(-F(1,2)/(ell*(M+2))==-F(1,4)/(ell*(F(M,2)+1)),'report_half_frequency_prefactor')
 # Exhaustive finite signed-frequency collision check under the proof's larger support bounds.
 for N in (4*K+5,101):
  ck(N%2==1 and N>4*K+4,'stable_frequency_N')
  for e in range(K+2):
   by_signed={};by_absolute={}
   for aa in range(-e,e+1,2):
    for bb in range(-(2*K+1-e),2*K+2-e):
     signed=aa*N+bb;pair=(aa,bb)
     ck(signed not in by_signed or by_signed[signed]==pair,'signed_frequency_injective')
     by_signed[signed]=pair;af=abs(signed)
     if af in by_absolute:
      prior=by_absolute[af];ck(pair==prior or pair==(-prior[0],-prior[1]),'absolute_frequency_only_sign_collision')
     else:by_absolute[af]=pair
   if e==1:ck(all(abs(freq)!=M-1 for freq in by_signed),'linear_highmode_absent')
  ck(abs(N)==abs(-N) and (1,0)!=(-1,0),'literal_absolute_injectivity_counterexample')
 records.append(dict(ell=str(ell),K=K,M=M,mixed_deficits=sorted(set(str(D) for k,l,D in mixed)),resonance=[[str(D),n] for D,n in resonances],epsilon0=str(eps0),g_primitive_integer=ints))
# The displayed ell=3 polynomial, parsed from the frozen main text, not typed from result158.
text=(out/'main.v1.src').read_text();display=' '.join(line[2:].strip() for line in text.splitlines() if line.startswith('@@'))
parts=re.findall(r'([+-]?)\s*(\d+)\s*(?:eps(?:\^(\d+))?)?',display)
parsed={}
for sign,number,power in parts:
 # Exponents are matched within the same regex; plain final constant has no eps.
 pass
pattern=r'([+-]?)\s*(\d+)\s*(eps(?:\^(\d+))?)?'
for match in re.finditer(pattern,display):
 sign,num,eps,power=match.groups();degree=int(power) if power else (1 if eps else 0)
 parsed[degree]=(-1 if sign=='-' else 1)*int(num)
ck([parsed[i] for i in range(7)]==records[0]['g_primitive_integer'],'displayed_polynomial_exact_transcription')
res=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS with stated textual repairs',checks=sum(counts.values()),counts=counts,elapsed_seconds=time.monotonic()-t0,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=records,scope='Exact radial arithmetic and comparison to independently generated156-158 certificates. Does not rerun producer code or certify a profile. Absolute-injectivity assertion has an explicit counterexample.')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
