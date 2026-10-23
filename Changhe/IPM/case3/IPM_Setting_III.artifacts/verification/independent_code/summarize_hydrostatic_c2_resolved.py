"""Result235: independent c2 record audit and positive-beta finite constant reconstruction."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,math,sys
import mpmath as mp
sys.set_int_max_str_digits(0)
ROOT=Path('research/hydrostatic_c2_resolved_audit');V=ROOT/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
checks=[]
def check(name,test,evidence=None):checks.append(dict(name=name,passed=bool(test),evidence=evidence))
regions=[('tiny',0.,.01),('inner',.01,.1),('core',.1,1.),('annulus',1.,100.),('far',100.,float('inf')),('extent10',0.,10.),('extent100',0.,100.),('extent10000',0.,10000.000001)]
def maxima(rows):
    out={}
    for name,lo,hi in regions:
        chosen=[a for a in rows if lo<=math.hypot(a['x'],a['y'])<hi]
        if not chosen:continue
        t=dict(count=len(chosen),undefined_Nf=sum(a['Nf']==0 for a in chosen),undefined_Nv=sum(a['Nv']==0 for a in chosen))
        for key in ['R','R_Nf','R_Nv']:
            good=[a for a in chosen if a[key] is not None]
            if good:t[key]=max(good,key=lambda a:abs(a[key]))
        out[name]=t
    return out

def examine(rows,c,label):
    finite=nulls=bounds=horizontal=True;errs=[]
    for a in rows:
        x,y,g,gx,gy,v1,v2=(a[k]for k in ['x','y','g','gx','gy','V1','V2'])
        A=(c*x+v1)*gx;B=(c*y+v2)*gy
        vals=dict(R=A+B-g,Nf=abs(A)+abs(B)+abs(g),Nv=abs(g)+abs(x*gx+y*gy)+abs(v1*gx+v2*gy))
        finite &= all(math.isfinite(z)for z in [x,y,g,gx,gy,v1,v2,*vals.values()])
        errs.extend(abs(a[k]-z)/(1+abs(z))for k,z in vals.items())
        for key,N in [('R_Nf','Nf'),('R_Nv','Nv')]:
            if vals[N]==0:nulls &= a[key] is None
            else:
                nulls &= a[key] is not None
                if a[key] is not None:errs.append(abs(a[key]-abs(vals['R'])/vals[N]))
        bounds &= (a['R_Nf'] is None or a['R_Nf']<=1+1e-13) and (a['R_Nv'] is None or a['R_Nv']<=max(c,1)+1e-13)
        if y==0:horizontal &= vals['R']==vals['Nf']==vals['Nv']==0
    check(label+' finite',finite);check(label+' recomputedR_Nf_Nv',max(errs)<1e-12,max(errs));check(label+' zeroDenominators',nulls);check(label+' triangleBounds',bounds);check(label+' horizontalAxis',horizontal)

def changes(A,B):
    A={(a['x'],a['y']):a for a in A};B={(a['x'],a['y']):a for a in B};common=sorted(A.keys()&B.keys());out={}
    for key in ['V1','V2','R','R_Nf','R_Nv']:
        good=[dict(x=x,y=y,change=B[x,y][key]-A[x,y][key],before=A[x,y][key],after=B[x,y][key])for x,y in common if A[x,y][key]is not None and B[x,y][key]is not None]
        out[key]=max(good,key=lambda a:abs(a['change']))if good else None
    return dict(common_points=len(common),pointwise_maximum_changes=out)

def exactmp(t):return mp.mpf(t[0])/mp.mpf(t[1])
def reconstruct_far(cert,c):
    coeff=cert['k_w']+cert['H_w']
    size=max(max(0,len(str(abs(int(n))))-len(str(abs(int(d)))))for n,d in coeff)
    digits=max(180,size+120)
    with mp.workdps(digits):
        P=exactmp(cert['P']);L=exactmp(cert['L']);C=L/4;p=mp.mpf('.5')
        assert P==2 and c==2
        k=list(map(exactmp,cert['k_w']));h=list(map(exactmp,cert['H_w']))
        K=h[1]*mp.sqrt(C);Q=k[1]*mp.sqrt(C)/2
        c2=C*(h[2]-h[1]/4);c3=C**mp.mpf('1.5')*(h[3]-h[2]/2-h[1]/32)
        B=C*(k[2]-k[1]/4);r2=-c2+2*K*Q
        beta=mp.mpf(2)/3;terms=[]
        for j in range(3,len(k)):
            terms.append(j*k[j]*beta)
            beta*=mp.mpf(j-2)/(mp.mpf(j)-mp.mpf('.5'))
        M=C*(k[1]*(-mp.mpf('.5')-mp.log(2))+k[2]*(4*mp.log(2)-3)+mp.fsum(terms))-B*mp.log(C)
        vals=dict(p=p,cp_minus1=c*p-1,K=K,Q=Q,c2=c2,c3=c3,B_log=B,M=M,r2=r2,residual_sqrt=r2/(2*K),residual_log=B/4,residual_constant=M/4-c3/K-r2*(2*c2+r2)/(4*K*K))
        return dict(precision=digits,values={k:mp.nstr(z,80)for k,z in vals.items()},absolute_sum=mp.nstr(C*mp.fsum(abs(z)for z in terms),40))

def horner(co,x):
    v=mp.mpf(0)
    for a in reversed(co):v=v*x+a
    return v

def extra_records(a,cert,far,tag):
    with mp.workdps(far['precision']):
        ff={k:mp.mpf(v)for k,v in far['values'].items()};K=ff['K'];C=exactmp(cert['L'])/4;H=list(map(exactmp,cert['H_w']));dH=[j*H[j]for j in range(1,len(H))]
        check(tag+' exact p c match',ff['p']==mp.mpf('.5')and ff['cp_minus1']==0)
        check(tag+' cusp two precisions',[t['digits']for t in a['cusp']]==[150,210])
        ce=max(abs(mp.mpf(t['Cp'])-mp.mpf(t['monomial_Cp']))/max(1,abs(mp.mpf(t['Cp'])))for t in a['cusp'])
        check(tag+' cusp separate formula agreement',ce<mp.mpf('1e-80'),mp.nstr(ce,20))
        ce=max(abs(mp.mpf(t['Cp'])/K-mp.mpf(t['Cp_K']))for t in a['cusp'])
        check(tag+' cusp independent K normalization',ce<mp.mpf('1e-60'),mp.nstr(ce,20))
        check(tag+' cusp extra precision',a['cusp'][0]['Cp']==a['cusp'][1]['Cp']and a['cusp'][0]['Cp_K']==a['cusp'][1]['Cp_K'])
        check(tag+' two axis runs',len(a['axis_log_runs'])==2)
        expected=[100,1000,10000,10**6,10**8,10**12,10**20,10**28]
        for n,run in enumerate(a['axis_log_runs']):
            check(tag+' axis radii '+str(n),[int(mp.mpf(t['y']))for t in run['points']]==expected)
            for t in run['points']:
                z={k:mp.mpf(v)for k,v in t.items()};y=z['y'];w=z['w'];G=y*horner(H,w);Gy=horner(H,w)-w*(1-w)*horner(dH,w)/(2-mp.mpf('1.5')*w)
                V=z['V2'];R=(2*y+V)*Gy-G;Nf=abs((2*y+V)*Gy)+abs(G)
                pred=ff['residual_sqrt']*mp.sqrt(y)+ff['residual_log']*mp.log(y)+ff['residual_constant']
                want=dict(g=G,gy=Gy,R=R,Nf=Nf,y_signed_R_Nf=y*R/Nf,asymptotic_prediction=pred,asymptotic_remainder=y*R/Nf-pred)
                err=max(abs(v-z[k])/max(1,abs(v))for k,v in want.items())
                label=tag+' axis '+str(n)+' y'+str(int(y))
                check(label+' independently reconstructed',err<mp.mpf('1e-45'),mp.nstr(err,20))
                check(label+' map identity',abs(C*mp.sqrt(1-w)/w**2/y-1)<mp.mpf('1e-70'))
                check(label+' nonnegative tail bound',z['remainder_bound']>=0)
        ae=max(abs(mp.mpf(t[k])-mp.mpf(u[k]))/max(1,abs(mp.mpf(u[k])))for t,u in zip(a['axis_log_runs'][0]['points'],a['axis_log_runs'][1]['points'])for k in ['g','gy','V2','R','Nf','y_signed_R_Nf'])
        check(tag+' axis independent precision comparison',ae<mp.mpf('1e-65'),mp.nstr(ae,20))
        old=next(t for t in a['levels'][-1]['points']if t['x']==0 and t['y']==10000.)
        new=next(t for t in a['axis_log_runs'][-1]['points']if mp.mpf(t['y'])==10000)
        errs={k:abs(float(new[k])-old[k])for k in ['g','gy','V2','R','Nf']}
        check(tag+' Cartesian crosscheck record',errs==a['axis_log_crosscheck']['absolute_errors'])
        check(tag+' resolved full inverse agrees with axis series',errs['V2']<3e-8 and errs['R']<1e-9,errs)
        points=a['axis_log_runs'][-1]['points'];remainders=[abs(mp.mpf(t['asymptotic_remainder']))for t in points[-3:]]
        check(tag+' observed asymptotic remainders decrease',remainders[0]>remainders[1]>remainders[2],list(map(lambda z:mp.nstr(z,20),remainders)))
        return dict(cusp=a['cusp'][-1],axis_points=points,axis_crosscheck=errs)

def main():
    pipe=json.loads((V/'PIPELINE.json').read_text())
    if pipe['status']!='DONE':raise SystemExit('235 incomplete; no summary written')
    inputs=json.loads((V/'INPUTS.json').read_text());inputs={a['tag']:a for a in inputs['states']};points=json.loads((V/'POINTS.json').read_text())['points'];out=[]
    check('pipeline checks',all(a['passed']for a in pipe['checks']),len(pipe['checks']))
    check('two states',len(pipe['states'])==2 and len(inputs)==2)
    check('input manifest hash',sha(V/'INPUTS.json')==pipe['input_sha256'])
    for p,h in pipe['code_and_proof_sha256'].items():check('unchanged code or proof '+p,sha(p)==h)
    for a in pipe['checks']:
        if a['name'].startswith('parent gate '):check('parent gate frozen '+a['name'],sha(a['evidence']['path'])==a['evidence']['sha256'])
    for entry in pipe['states']:
        tag=entry['tag'];a=json.loads((V/(tag+'.json')).read_text());inp=inputs[tag];meta=a['metadata'];c=meta['cl'];ex=a['exact']
        check(tag+' completed',a['status']==entry['status']=='DONE');check(tag+' result hash',sha(V/(tag+'.json'))==entry['result_sha256']);check(tag+' source hash',sha(inp['frozen'])==inp['sha256']==a['source_sha256']==meta['sha256'])
        certpath=V/(tag+'.polynomials.json');check(tag+' exact certificate hash',sha(certpath)==a['polynomial_sha256']);cert=json.loads(certpath.read_text())
        check(tag+' stored nodes',meta['basis_nodes_source']=='stored' and meta['basis']=='local');check(tag+' node reconstruction',a['node_reconstruction']['mode_values_absolute_max']<1e-10,a['node_reconstruction'])
        aa=F(ex['a']);ch=F(ex['cH']);delta=F(ex['delta']);check(tag+' exact center relation',delta==F(c)+ch-1);check(tag+' genuine auxiliary slope',aa!=0)
        af,chf,df=map(float,[aa,ch,delta]);b,e,E=map(float,[ex['b'],ex['e'],ex['E']]);cubic=(2+3*df)*e-af*b/3
        check(tag+' reported E',abs(E-e/af)<1e-12*max(1,abs(E)));check(tag+' reported cubic',abs(cubic-float(ex['cubic_axis_residual']))<1e-12*max(1,abs(cubic)))
        far=reconstruct_far(cert,c)
        with mp.workdps(100):
            ferr={k:float(abs(mp.mpf(z)-mp.mpf(a['far_field'][-1][k]))/max(1,abs(mp.mpf(z))))for k,z in far['values'].items()}
            precisionerr={k:float(abs(mp.mpf(a['far_field'][0][k])-mp.mpf(a['far_field'][1][k])))for k in far['values']}
        check(tag+' independent exact-data far and moment',max(ferr.values())<1e-50,ferr);check(tag+' saved extra precision',max(precisionerr.values())<1e-50,precisionerr)
        check(tag+' full three inverse levels',[(z['order'],z['tail_order'],z['split'])for z in a['levels']]==[(32,96,16.),(48,160,64.),(64,192,128.)])
        item=dict(tag=tag,N=meta['N'],M=meta['M'],c=c,a=af,cH=chf,delta=df,b=b,e=e,E=E,axis_cubic_residual=cubic,origin_drift_diagonal=[c-chf,c+chf],origin_axis_R_Nf_limit=abs(df)/(abs(c+chf)+1),source_sha256=inp['sha256'],far=far,levels=[])
        for lev in a['levels']:
            label=tag+' order'+str(lev['order']);raw=lev['points'];check(label+' common774points',len(raw)==774 and [[p['x'],p['y']]for p in raw]==points);examine(raw,c,label)
            table=maxima(raw);check(label+' regions recomputed',table==lev['regions']);centererr=abs(lev['center']-chf)
            check(label+' center error record',abs(centererr-lev['center_error'])<1e-15)
            item['levels'].append(dict(order=lev['order'],tail_order=lev['tail_order'],split=lev['split'],center_error=centererr,regions=table))
        item['refinements']=[changes(a['levels'][i]['points'],a['levels'][i+1]['points'])for i in range(2)]
        for i,comp in enumerate(a['comparisons']):
            computed=item['refinements'][i]['pointwise_maximum_changes']
            check(tag+' pointwise refinement record '+str(i),all(abs(computed[k]['change'])==abs(comp['pointwise_maximum_changes'][k]['change'])for k in computed))
        w=a['witnesses'];examine(w['points'],c,tag+' witness88');needed=set()
        for lev in a['levels']:
            for region in lev['regions'].values():
                for key in ['R','R_Nf','R_Nv']:
                    if key in region:needed.add((region[key]['x'],region[key]['y']))
        check(tag+' every maximum witnessed',needed<={(p['x'],p['y'])for p in w['points']})
        item['witness_refinement']=changes(a['levels'][-1]['points'],w['points']);item['witness_count']=len(w['points']);item['witness_center_error']=abs(w['center']-chf)
        check(tag+' witness refinement record',all(abs(t['change'])==abs(a['witness_refinement'][k]['change'])for k,t in item['witness_refinement']['pointwise_maximum_changes'].items()))
        check(tag+' center finite polynomial quadrature',max(t['error']for t in a['center_finite_polynomial_quadrature'])<1e-9,a['center_finite_polynomial_quadrature'])
        check(tag+' two MP density levels',len(a['mp_jet_checks'])==10 and {t['target_digits']for t in a['mp_jet_checks']}=={70,100})
        item['MP_max_double_error']=max(z for t in a['mp_jet_checks']for z in t['absolute_double_errors']);check(tag+' MP density agreement',item['MP_max_double_error']<1e-8,item['MP_max_double_error'])
        with mp.workdps(110):
            mpdiff=max(float(abs(mp.mpf(x)-mp.mpf(y)))for u,w in zip(a['mp_jet_checks'][:5],a['mp_jet_checks'][5:])for x,y in zip(u['values'],w['values']))
        check(tag+' independent MP precision change',mpdiff<1e-60,mpdiff)
        item['finite_radius_identity']=a['finite_radius_identity'];check(tag+' four exact finite radius defects',len(item['finite_radius_identity'])==4 and max(t['error_from_exact']for t in item['finite_radius_identity'])<1e-8,item['finite_radius_identity'])
        item['axis_derivative_samples']=a['axis_derivative_samples'];check(tag+' axis grid scope',a['axis_derivative_samples']['count']==2001 and a['axis_derivative_samples']['range']==[1e-7,1e6])
        if 'convergent_moment_integral'in a:
            item['convergent_moment_integral']=a['convergent_moment_integral'];check(tag+' convergent moment integral',float(a['convergent_moment_integral']['difference'])<1e-45)
        item.update(extra_records(a,cert,far,tag));item['final_regions']=item['levels'][-1]['regions'];out.append(item)
    result=dict(status='PASS'if all(a['passed']for a in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),checks=checks,count=len(checks),states=out,proof_sha256=sha(ROOT/'SUMMARY_PROOF.md'),driver_sha256=sha(__file__),pipeline_sha256=sha(V/'PIPELINE.json'),scope='Finite auxiliary hydrostatic trials; empirical quadrature comparison. No full elliptic IPM candidate or uniform error bound.')
    (V/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
    lines=['# c=2 resolved-map hydrostatic checkpoint audit','',result['utc']+'; '+result['status']+'; '+str(len(checks))+' independent summary checks.','',result['scope'],'','All residual maxima below use the same774 physical points, with radii1e-5..1e4, the64/192/128 inverse rule and a separate88/256/512 witness check. Undefined0/0 ratios remain null.','', '| State | a | center defect | b | e/a | Q | B_log | M | Cp/K |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
    for a in out:
        ff=a['far']['values'];lines.append(f"| {a['tag']} | {a['a']:.9g} | {a['delta']:.9g} | {a['b']:.9g} | {a['E']:.9g} | {float(ff['Q']):.9g} | {float(ff['B_log']):.9g} | {float(ff['M']):.9g} | {float(a['cusp']['Cp_K']):.9g} |")
    for a in out:
        lines.extend(['','## '+a['tag'],'',f"Actual axis cubic residual coefficient {a['axis_cubic_residual']:.9g}; origin drift diagonal {a['origin_drift_diagonal']}; axis limiting normalized center defect {a['origin_axis_R_Nf_limit']:.9g}.",'','| Region | max abs R | max abs R/Nf | max abs R/Nv | R/Nf maximum location |','|---|---:|---:|---:|---|'])
        for name,_,_ in regions:
            t=a['final_regions'][name];p=t['R_Nf'];lines.append(f"| {name} | {abs(t['R']['R']):.9g} | {p['R_Nf']:.9g} | {t['R_Nv']['R_Nv']:.9g} | ({p['x']:.9g},{p['y']:.9g}) |")
        lines.append('\nCenter errors at orders32/48/64/88: '+', '.join(f'{z:.6g}'for z in [*[t['center_error']for t in a['levels']],a['witness_center_error']])+'.')
        for label,dif in [('32 to48',a['refinements'][0]),('48 to64',a['refinements'][1]),('64 to88 witness',a['witness_refinement'])]:
            lines.append('\n'+label+'; '+str(dif['common_points'])+' common points: '+', '.join(k+'='+format(abs(t['change']),'.6g')for k,t in dif['pointwise_maximum_changes'].items())+'.')
        lines.extend(['','| y | signed yR/Nf | three-term asymptotic | difference |','|---:|---:|---:|---:|']);lines.extend('| '+t['y']+' | '+format(float(t['y_signed_R_Nf']),'.12g')+' | '+format(float(t['asymptotic_prediction']),'.12g')+' | '+format(float(t['asymptotic_remainder']),'.9g')+' |'for t in a['axis_points'])
        lines.append('\nCartesian jets versus70/100-digit scalar differentiation: maximum double error '+format(a['MP_max_double_error'],'.6g')+'. Finite-axis signs are sampled diagnostics only: '+json.dumps(a['axis_derivative_samples'])+'.')
    lines.extend(['','All exact-data moment reconstructions, source hashes, separate maximizing records and pointwise changes are in SUMMARY.json. The independent positive-beta recurrence confirms the logarithmic finite constants of the saved polynomials. Here cp-1 is exactly zero. Nonzero r2 gives a sqrt(y) contribution and nonzero B_log gives a logarithmic contribution to the signed scaled axis residual. The constant normalization correction is retained. These finite trial sequences do not establish convergence or rule out other solutions. The principal endpoint remains UNRESOLVED.'])
    (V/'SUMMARY.md').write_text('\n'.join(lines)+'\n');print(result['status'],result['count']);print([a for a in checks if not a['passed']])
    if result['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
