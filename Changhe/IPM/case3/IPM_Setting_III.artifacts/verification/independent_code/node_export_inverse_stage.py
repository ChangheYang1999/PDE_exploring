"""Instrumented finite rules and predeclared witness selection for auxiliary inverse.
No producer imports. See CANDIDATE_INVERSE_EXECUTION_PROOF.md and addenda.
"""
import numpy as np
from independent_hydrostatic import finite_rule,validate_inverse_options
from node_export_arithmetic_strict import residual,decomposition,exact

RULES={'A':dict(order=48,tail_order=160,split=64.,inner=.125,partition='dyadic'),
       'B':dict(order=64,tail_order=192,split=128.,inner=.125,partition='dyadic'),
       'C':dict(order=88,tail_order=256,split=512.,inner=.125,partition='ratio')}
REGIONS=['r<.1','.1<=r<1','1<=r<100','r>=100']
META=['R_split','inner_panels','outer_panels','inner_nodes','outer_nodes','tail_nodes','minimum_panel_width','rounded_endpoint_nodes','x_axis_imposed','y_axis_imposed']
RESIDUAL_COLUMNS=['R','Nf','Nv','Rf','Rv']
DECOMP_COLUMNS=['R_reference','R_producer','velocity_term','jet_term','difference','common_denominator','alternate_velocity_term','alternate_jet_term']

def physical_cuts(lo,hi,scale,partition):
    if hi<=lo:return np.array([float(lo)])
    cuts=[float(lo),float(hi)]
    if partition=='dyadic':
        for v in np.r_[0.,.015625,.03125,.0625,.125,.25,.5,1.,2.,4.]*scale:
            if lo<v<hi:cuts.append(float(v))
        v=max(4*scale,np.finfo(float).tiny);ratio=2.
    elif partition=='ratio':v=scale/64.;ratio=1.5
    else:raise ValueError('unknown physical partition')
    while v<hi:
        if lo<v:cuts.append(float(v))
        nxt=v*ratio
        if not nxt>v:raise ArithmeticError('nonincreasing physical cut')
        v=nxt
    return np.unique(cuts)

def panels(lo,hi,order,scale,partition):
    cuts=physical_cuts(lo,hi,scale,partition)
    if len(cuts)<2:return np.empty(0),np.empty(0),dict(count=0,nodes=0,min_width=None,endpoint_nodes=0)
    a,b=cuts[:-1],cuts[1:];width=b-a;z,w=finite_rule(order)
    zz=a[:,None]+width[:,None]*(z[None,:]+1)/2;ww=width[:,None]*w[None,:]/2
    info=dict(count=len(width),nodes=zz.size,min_width=float(min(width)),endpoint_nodes=int(np.count_nonzero((zz<=a[:,None])|(zz>=b[:,None]))))
    return zz.ravel(),ww.ravel(),info

def quadrature_parts(x,y,p,rule):
    validate_inverse_options(rule['order'],rule['tail_order'],rule['split'],rule['inner'])
    if not 0<p<1:raise ValueError('growth exponent must lie in (0,1)')
    xx,yy=abs(float(x)),abs(float(y));R=rule['split']*max(1.,xx,yy,rule['inner']);P=1/(1-p)
    a,aw,ai=panels(0.,yy,rule['order'],rule['inner'],rule['partition'])
    b,bw,bi=panels(yy,R,rule['order'],rule['inner'],rule['partition'])
    z,w=finite_rule(rule['tail_order']);u=(z+1)/2;t=R/u**P;tw=w/2*P*R*u**(-P-1)
    widths=[d['min_width']for d in [ai,bi]if d['min_width']is not None]
    meta=np.array([R,ai['count'],bi['count'],ai['nodes'],bi['nodes'],len(t),min(widths)if widths else np.nan,ai['endpoint_nodes']+bi['endpoint_nodes'],int(x==0),int(y==0)],float)
    return xx,yy,(a,aw),(b,bw),(t,tw),meta

def evaluate(jet,x,y,p,rule):
    xx,yy,a,b,t,meta=quadrature_parts(x,y,p,rule);sx=-1 if x<0 else 1;sy=-1 if y<0 else 1
    an,aw=a;bn,bw=b;tn,tw=t;ja,jb,jt=jet(xx,an),jet(xx,bn),jet(xx,tn)
    tx=float(tw@jt[:,1]);txx=float(tw@jt[:,3]);Ix=float(bw@jb[:,1])+tx;Ixx=float(bw@jb[:,3])+txx
    Jx=float((aw*an)@ja[:,1]);Jxx=float((aw*an)@ja[:,3]);V=[-sx*Ix,sy*(Jxx+yy*Ixx)];Phi=sx*sy*(Jx+yy*Ix)
    if x==0:V[0]=0.;Phi=0.
    if y==0:V[1]=0.;Phi=0.
    return dict(V=np.array(V),Phi=Phi,dV2_dy=Ixx,tail_V=np.array([-sx*tx,sy*yy*txx]),meta=meta)

def finite_arithmetic(j,jp,v,vm,vp,c,x,y):
    r=residual(j,v,c,x,y);rows=[]
    for velocity in [vm,vp]:
        d=decomposition(j,jp,v,velocity,c,x,y)
        if not d['identity']or not d['alternate_identity']:raise ArithmeticError('exact two-jet identity failed')
        rows.append([float(d[k])for k in DECOMP_COLUMNS])
    return np.array([float(r[k])if r[k]is not None else np.nan for k in RESIDUAL_COLUMNS]),np.array(rows)

def masks(x,y):
    r=np.hypot(x,y)
    return [r<.1,(r>=.1)&(r<1),(r>=1)&(r<100),r>=100]

def discrepancy(a,b):
    ab=abs(a-b);den=np.maximum(abs(a),abs(b));pure=np.divide(ab,den,out=np.zeros_like(ab),where=den!=0)
    return dict(absolute=ab,pure_relative=pure,floored=ab/np.maximum(den,1e-5)),int(np.count_nonzero(den==0))

def maxima(x,y,rr):
    out=[]
    for name,mask in zip(REGIONS,masks(x,y)):
        ids=np.flatnonzero(mask);row=dict(region=name,count=len(ids),metrics={})
        for namez,col in [('absR',0),('Rf',3),('Rv',4)]:
            values=abs(rr[:,col]);valid=ids[np.isfinite(values[ids])];i=int(valid[np.argmax(values[valid])])if len(valid)else None
            row['metrics'][namez]=dict(index=i,value=float(values[i])if i is not None else None,x=float(x[i])if i is not None else None,y=float(y[i])if i is not None else None,defined_count=len(valid),undefined_count=len(ids)-len(valid))
        out.append(row)
    return out

def select_witnesses(x,y,own,prod,vm,vp,A,B,prior,fdproxy):
    reasons={}
    def add(i,reason):
        if i is not None:reasons.setdefault(int(i),[]).append(reason)
    def arg(values,reason):
        ids=np.flatnonzero(np.isfinite(values))
        if len(ids):add(int(ids[np.argmax(values[ids])]),reason)
    for i in prior:add(i,'previous local MP witness')
    for i in [1139,2294,2296]:add(i,'predeclared cancellation/second-derivative witness')
    for label,q in [('A',A),('B',B)]:
        for row in maxima(x,y,q['residual']):
            for metric,z in row['metrics'].items():add(z['index'],label+' '+row['region']+' '+metric)
    for comp in range(2):
        for metric,z in discrepancy(A['velocity'][:,comp],B['velocity'][:,comp])[0].items():arg(z,'A-B V'+str(comp+1)+' '+metric)
    for label,q in [('A',A),('B',B)]:
        for ref,v in [('Vm',vm),('Vp',vp)]:
            for comp in range(2):
                dd,_=discrepancy(q['velocity'][:,comp],v[:,comp])
                for metric in ['absolute','pure_relative']:arg(dd[metric],label+'-'+ref+' V'+str(comp+1)+' '+metric)
    arg(abs(own[:,3]),'absolute gxx');arg(fdproxy,'gxx versus five-point FD proxy')
    jet_delta=[];relative=[];signs=0;zeros=0
    for i in range(len(x)):
        a=residual(own[i],vm[i],2,x[i],y[i])['R'];b=residual(prod[i],vm[i],2,x[i],y[i])['R'];d=abs(a-b);den=max(abs(a),abs(b));jet_delta.append(d);relative.append(d/den if den else exact(0));signs+=int(a*b<0);zeros+=int(den==0)
    add(max(range(len(x)),key=lambda i:jet_delta[i]),'exact absolute map-jet residual contribution')
    add(max(range(len(x)),key=lambda i:relative[i]),'exact relative map-jet residual contribution')
    return dict(indices=sorted(reasons),reasons={str(i):reasons[i]for i in sorted(reasons)},map_residual_sign_disagreement_count=signs,map_residual_both_zero_count=zeros,absolute_jet_argmax=max(range(len(x)),key=lambda i:jet_delta[i]),relative_jet_argmax=max(range(len(x)),key=lambda i:relative[i]))

def stability(j,vm,velocities,c,x,y):
    rr=[residual(j,v,c,x,y)for v in velocities];spread=max(z['R']for z in rr)-min(z['R']for z in rr)
    terms=[(exact(v[0])-exact(vm[0]))*exact(j[1])+(exact(v[1])-exact(vm[1]))*exact(j[2])for v in velocities];D=max(map(abs,terms));nf=rr[1]['Nf'];relative=spread/D if D else None;normalized=spread/nf if nf else None
    stable=(spread<=D/100 if D else spread==0)and nf>0 and spread<=nf/100000000
    components=[]
    for k in range(2):
        for a,b in [(2,1),(2,0),(0,1)]:
            u,v=exact(velocities[a][k]),exact(velocities[b][k]);d=abs(u-v);den=max(abs(u),abs(v));components.append(dict(component=k+1,pair=['ABC'[a],'ABC'[b]],absolute=float(d),pure_relative=float(d/den)if den else None,both_zero=not bool(den)))
    rb=abs(rr[1]['R']);residual_relative=spread/rb if rb else None
    return dict(criterion_label='map-discrepancy-relative only',component_spreads=components,spread_over_abs_R_B=float(residual_relative)if residual_relative is not None else None,within_one_percent_of_abs_R_B=bool(spread<=rb/100)if rb else None,zero_R_B=not bool(rb),S=float(spread),D=float(D),Nf_B=float(nf),spread_over_velocity_term=float(relative)if relative is not None else None,spread_over_Nf_B=float(normalized)if normalized is not None else None,empirical_stable=bool(stable),zero_D=not bool(D),zero_Nf=not bool(nf),exact_operands=[str(spread),str(D),str(nf)])
