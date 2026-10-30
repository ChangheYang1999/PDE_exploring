"""Exact successor rounding, constant rescaling and source-root audit."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys,time,re
from flint import arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=1024
B=Path(__file__).resolve().parents[1];start=time.monotonic();checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads((B/p).read_text())
def need(k,v):
 assert bool(v),k
 checks.append(k)
def ar(q):
 q=Q(q);return arb(q.numerator)/q.denominator
def interval(s):
 t=str(s).strip().strip('[]').strip()
 if '+/-' in t:
  a,b=t.split('+/-');m=Q(a.strip() or '0');r=Q(b.strip());assert r>=0;return m-r,m+r
 x=Q(t);return x,x
def bound(x,places,upper=False):
 # Recover the exact binary endpoint before decimal outward rounding.
 v=x.upper() if upper else x.lower();m,e=v.man_exp();m,e=int(m),int(e)
 q=Q(m*2**e) if e>=0 else Q(m,2**(-e));den=10**places
 z=q.numerator*den//q.denominator
 return Q(z+1 if upper else z-1,den)
def unit(text,digits):
 e=int(text.lower().split('e')[1]);return Q(10)**(e-digits+1)
manifest=read('data/manifest.json')
for r in manifest:need('frozen '+r['local'],sha(B/r['local'])==r['sha256'])
pars=read('data/parameters.json');orig=read('../weight_uniform_gram_audit/verification/result.json');tight=read('../weight_uniform_review_acceptance/verification/result.json');params=read('../weight_uniform_review_acceptance/data/parameters.json');peer=read('source/T2_scope.json')
need('accepted original320 and tight364',orig['check_count']==320 and all(orig['checks'].values()) and tight['check_count']==len(tight['checks'])==364)
need('peer scope11',peer['checks']==11 and not peer['fails'])
need('peer exact original binding',peer['inputs']['c1-t4/research/weight_uniform_gram_audit/verification/result.json']==sha(B/'../weight_uniform_gram_audit/verification/result.json'))
ss=ar(params['sigma']);pi=arb.pi();M=pi.sqrt()*((1-ss)/2).gamma()/2;W=8*arb(5).sqrt()*arb(6)**(-arb(3)/5)/5
k1=M+arb(8)/5;cr=3*M/2+arb(32)/15;c8=1+3*pi*W/4;dtop=1+pi*W/2;K=2*dtop+6*c8+24*(cr+2*k1)+32*k1
q0=1/(2*pi.sqrt());ps=arb(2)**ss*(1+ss).sqrt()/(2*pi.sqrt());P0=ps*(1+W*M*ss)+W*M*ss/(2*pi.sqrt());v=arb(4)/5*q0+q0*(1+4*W*M*ss)+arb(19)/5*P0
k=Q(params['K_lower']);u=Q(params['cU_lower']);f=(ar(k)/K).sqrt()*ar(u)/v;f2=ar(k*u*u)/(K*v*v)
need('K matches accepted enclosure',arb(orig['K']).contains(K));need('v matches accepted enclosure',arb(orig['v']).contains(v))
need('positive strict lower constants',0<ar(k)<K and 0<ar(u)<v)
need('exact scale and square',f*f==f2 or (f*f).overlaps(f2))
need('factor strict improvement bounds',0<f<1 and 0<1-f<ar(pars['gap_factor_upper']))
need('factor display source contains own',arb(peer['factor_sqrt']).contains(f))
rows=[]
need('seven complete rows',len(tight['rows'])==len(peer['rows'])==len(pars['displays'])==7)
for old,p,newdisplay in zip(tight['rows'],peer['rows'],pars['displays'],strict=True):
 label=old['label'];q=Q(old['exact_f_at_test_mu']);upper=Q(old['exact_supremum_square_upper']);lo=ar(q).sqrt()*f;hi=ar(upper).sqrt()*f;d=Q(newdisplay);half=Q(pars['half_unit'])
 need(label+' row identity',label==p['label'] and Q(old['six_digit_rounded_display'])==Q(p['six_digits_at_k_u']) and d==Q(p['six_digits_at_K_v']))
 need(label+' positive accepted exact interval',0<q<upper and upper==q*(1+Q(2,10**7)))
 need(label+' scaled squared formula',lo.overlaps((ar(q)*f2).sqrt()) and hi.overlaps((ar(upper)*f2).sqrt()))
 need(label+' full interval in six digit cell',ar(d-half)<lo.lower() and hi.upper()<ar(d+half))
 dl=bound(lo,24);dh=bound(hi,24,True)
 need(label+' outward exact endpoints',0<ar(dl)<lo.lower() and hi.upper()<ar(dh) and dl<dh)
 # A nearest12digit source endpoint is compared only to its own rounding cell.
 source_ends=p['enclosure_at_K_v'];margin=Q(1,10**16)
 need(label+' source approximate enclosure compatible',ar(Q(source_ends[0])-margin)<lo.lower() and hi.upper()<ar(Q(source_ends[1])+margin))
 rows.append({'label':label,'six_digits_at_lower_constants':old['six_digit_rounded_display'],'six_digits_at_exact_constants':newdisplay,'strict_outer_lower_exact':str(dl),'strict_outer_upper_exact':str(dh),'lower_ball':lo.str(90),'upper_ball':hi.str(90)})
c0=Q(pars['c0']);delta=1-1/c0;need('exact delta identity',delta==Q(pars['delta']));places=pars['delta_places'];den=10**places;z=delta.numerator*den//delta.denominator;dlo=Q(z,den);dhi=Q(z+1,den)
need('delta exact decimal prefix',dlo<=delta<dhi)
bad=Q(pars['bad_delta']);need('old delta prefix refuted',not bad<=delta<bad+Q(1,10**5));need('old delta nearest5dec refuted',not bad-Q(1,2*10**5)<=delta<bad+Q(1,2*10**5))
need('kappa D exact identity',c0*(4+delta)==5*c0-1)
text=(B/'../theory_v08_published_audit/source/theory_v08.md').read_text();badlines=[j for j,s in enumerate(text.splitlines(),1) if '0.44764...' in s];need('two frozen incorrect display locations',badlines==[189,413])
roots=read('source/T2_root_result.json');oldcov=read('../h18_coverage_audit/verification/result.json');cov=read('../h18_coverage_audit/data/coverage.json');families=read('../h18_coverage_audit/data/families.json')
need('root revision189 pass',roots['checks']==189 and not roots['fails'])
need('root revision same proof input',roots['inputs']['c1-t4/research/h18_coverage_audit/PROOF.md']==sha(B/'../h18_coverage_audit/PROOF.md'))
need('root revision same result input',roots['inputs']['c1-t4/research/h18_coverage_audit/verification/result.json']==sha(B/'../h18_coverage_audit/verification/result.json'))
need('own806 old pass',oldcov['checks_passed']==806)
need('24 complete candidate rows',[r['number'] for r in roots['B']['rows']]==[r['number'] for r in cov['rows']]==[i for i in range(2,27) if i!=11])
oldrows={r['number']:r for r in oldcov['weak_candidates']};bindings={r['number']:r for r in cov['rows']};rr=[]
for row in roots['B']['rows']:
 n=row['number'];label=f'candidate{n:03d}';source=oldrows[n];I,D,H=[Q(source[key]) for key in ['I_lower_exact','D_upper_exact','H_upper_exact']];ell=Q(row['root_lower_exact']);S=2**pars['root_bits'];z=S*(2*H*ell+D);disc=S*S*(D*D+4*H*I)
 need(label+' root exact integer square enclosure',z.denominator==1 and z>=0 and z*z<=disc<(z+1)**2)
 need(label+' root positivity and fixed floor',ell>Q(1,1000) and I-D/1000-H/10**6>0 and I-D*ell-H*ell**2>=0)
 d=Q(row['root_lower']);step=unit(row['root_lower'],pars['root_significant_digits']);need(label+' root directed floor',d<=ell<d+step)
 b=bindings[n];path='../h18_coverage_audit/'+b['result'];raw=read(path);need(label+' accepted weak source hash',sha(B/path)==b['result_sha256']==source['result_sha256'])
 if 'rows' in raw:
  source_row=next(x for x in raw['rows'] if x['k']==b['probe_k']);stored=interval(source_row['L2_radius_lower'])[0]
 else:stored=Q(raw['strict_lower_exact']) if 'strict_lower_exact' in raw else interval(raw['radius'])[0]
 dstore=Q(row['stored_lower']);stepstore=unit(row['stored_lower'],pars['root_significant_digits']);need(label+' stored lower directed floor',dstore<=stored<dstore+stepstore)
 rr.append({'number':n,'root_lower_exact':str(ell),'root_display_floor':row['root_lower'],'stored_lower_exact':str(stored),'stored_display_floor':row['stored_lower']})
need('same least root index',min(rr,key=lambda r:Q(r['root_lower_exact']))['number']==roots['B']['least_root'][1]==15)
least=min(Q(r['root_lower_exact']) for r in rr);need('least display directed',Q(roots['B']['least_root'][0])<=least<Q(roots['B']['least_root'][0])+unit(roots['B']['least_root'][0],12))
cr=[]
need('eight exact family names',set(roots['C'])=={r['name'] for r in families['rows']} and len(roots['C'])==8)
for row in families['rows']:
 label=row['name'];mu,C,cU,sw=[Q(row[k]) for k in ['mu','C','cU','sqrtW2']];square=4*mu**3/(27*C*cU*cU*sw*sw);display=roots['C'][label];d=Q(display);step=unit(display,pars['ceiling_significant_digits'])
 need(label+' exact directed upper',d-step>=0 and (d-step)**2<square<=d*d)
 need(label+' unchanged common scalar ceiling',square<Q(families['common_scalar_upper'])**2)
 cr.append({'name':label,'square_exact':str(square),'directed_upper_display':display})
for r in manifest:need('unchanged '+r['local'],sha(B/r['local'])==r['sha256'])
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'check_count':len(checks),'checks':checks,'proof_sha256':sha(B/'PROOF.md'),'checker_sha256':sha(Path(__file__)),'manifest_sha256':sha(B/'data/manifest.json'),'K':K.str(100),'v':v.str(100),'factor':f.str(100),'one_minus_factor':(1-f).str(70),'rows':rows,'delta_exact':str(delta),'delta_outer_bracket_exact':[str(dlo),str(dhi)],'bad_delta_lines':badlines,'root_rows':rr,'family_rows':cr,'foreign_code_executed':False,'new_optimization':False,'new_candidate_integrals':False,'verdict':'CONFIRMED seven exactK/v rounded relaxed budgets,48 directed lower displays and8 scalar upper displays; REFUTED the two0.44764 delta prefixes. Exclusions and full-PDE sharpness scope unchanged.'}
with (B/'verification/result.json').open('x') as stream:json.dump(out,stream,indent=2);stream.write('\n')
print('PASS',len(checks),out['utc'],out['elapsed_seconds'],sha(B/'verification/result.json'));print('FACTOR',f.str(30),'ONE_MINUS',(1-f).str(20));print('DELTA',str(dlo),str(dhi));print('EXACT_CONSTANT_DISPLAYS',','.join(r['six_digits_at_exact_constants'] for r in rows));print('DIRECTED_DISPLAYS',len(rr)*2+len(cr))
