"""Nonzero-radius exact modewise error checks, distinct from aggregate evaluation."""
import sys,json,math
sys.dont_write_bytecode=True
from fractions import Fraction as F
import numpy as np
import kernels,bounds

def main():
    P=np.zeros((261,13));R=np.zeros_like(P);T=np.zeros((8,260))
    for n,l,v in [(0,0,2),(134,2,-3),(260,1,5)]:P[n,l]=v
    for n,l,v in [(0,1,-2),(134,0,3),(260,2,-1)]:R[n,l]=v
    T[0,0]=8;T[1,1]=-3;T[2,259]=2
    pr=np.zeros_like(P);rr=np.zeros_like(R);tr=np.zeros_like(T);prem=np.zeros(261);rrem=np.zeros(261)
    pr[0,1]=1/16;pr[260,0]=1/32;rr[134,2]=1/64;tr[0,0]=1/128;tr[1,259]=1/256;prem[134]=1/512;rrem[260]=1/1024
    arrays=dict(P_mid=P,R_mid=R,T_mid=T,P_rad=pr,R_rad=rr,T_rad=tr,P_rem=prem,R_rem=rrem)
    model=kernels.build(arrays);linear=kernels.validate_actual_linear_maps(model);inputs=kernels.error_inputs(arrays,model);h=F(1,2048)
    def polynomial(a):return sum((F(float(v))*h**l for l,v in enumerate(a)),F(0))
    def scaledpoly(row,e,absolute=True):return sum((F(abs(v) if absolute else v)*F(2)**e*h**l for l,v in enumerate(row)),F(0))
    expected={}
    for p in range(3):
        expected['A'+str(p)]=sum((scaledpoly(row,model['ep']) for row in model['Aj'][p]),F(0));expected['B'+str(p)]=sum((scaledpoly(row,model['ep']) for row in model['Bj'][p]),F(0))
        expected['eA'+str(p)]=F(0);expected['eB'+str(p)]=F(0)
    for n in range(261):
        m=2*(n+1);ep=polynomial(pr[n])+F(float(prem[n]));er=polynomial(rr[n])+F(float(rrem[n]))
        for p,a,b in [(0,ep,er),(1,2*ep+m*er,m*ep+2*er),(2,(4+m*m)*ep+4*m*er,4*m*ep+(4+m*m)*er)]:expected['eA'+str(p)]+=a;expected['eB'+str(p)]+=b
    # Independent collected angular map for each original radius coefficient.
    hr=[[F(0)]*8 for _ in range(262)]
    for m in range(260):
        w={}
        for q in [1+2*m,1-2*m,3+2*m,3-2*m]:w[abs(q)]=w.get(abs(q),0)+(1 if q>0 else -1)
        for q,coef in w.items():
            for l in range(8):hr[(q-1)//2][l]+=abs(F(coef,8))*F(float(tr[l,m]))
    def derivative(rows):return [[(l+1)*row[l+1] if l<7 else F(0) for l in range(8)] for row in rows]
    hj=[hr]
    for p in range(3):hj.append([[3*v+w for v,w in zip(row,dr)] for row,dr in zip(hj[-1],derivative(hj[-1]))])
    for p in range(4):
        expected['H'+str(p)]=sum((scaledpoly(row,model['eh']) for row in model['Hp'][p]),F(0));expected['TH'+str(p)]=sum(((2*j+1)*scaledpoly(row,model['eh']) for j,row in enumerate(model['Hp'][p])),F(0))
        expected['eH'+str(p)]=sum((sum((v*h**l for l,v in enumerate(row)),F(0)) for row in hj[p]),F(0));expected['eTH'+str(p)]=sum(((2*j+1)*sum((v*h**l for l,v in enumerate(row)),F(0)) for j,row in enumerate(hj[p])),F(0))
    hdr=derivative(hr);fr=[]
    for n in range(1,262):fr.append([(abs(4-2*n)*hr[n-1][l]+(4+2*n)*hr[n][l]+hdr[n-1][l]+hdr[n][l])/2 for l in range(8)])
    fpr=derivative(fr)
    for name,rows,e in [('F',model['F'],model['ef']),('Fp',model['Fp'],model['ef'])]:expected[name]=sum((scaledpoly(row,e) for row in rows),F(0))
    expected['mF']=sum((2*n*scaledpoly(row,model['ef']) for n,row in enumerate(model['F'],1)),F(0))
    for name,rows in [('eF',fr),('eFp',fpr)]:expected[name]=sum((sum((v*h**l for l,v in enumerate(row)),F(0)) for row in rows),F(0))
    expected['emF']=sum((2*n*sum((v*h**l for l,v in enumerate(row)),F(0)) for n,row in enumerate(fr,1)),F(0))
    # Compare exact positive aggregates with the distinct mode-by-mode sums.
    for name,target in expected.items():
        v=inputs[name];got=sum((F(c)*h**l for l,c in enumerate(v['coeff'])),F(0))*F(2)**v['power']/v['denominator']
        if name.startswith(('eA','eB')):
            z=inputs['rem'+name[1:]];got+=F(z['coeff'][0])*F(2)**z['power']
        assert got==target,('aggregate radius or center',name,got,target)
    def pe(a,b):return expected['e'+a]*(expected[b]+expected['e'+b])+expected[a]*expected['e'+b]
    dv=[]
    for p in range(3):
        v=F(1,bounds.K)*expected['eH'+str(p+1)]+expected['eH'+str(p)]
        for l in range(p+1):v+=math.comb(p,l)*(pe('A'+str(l),'H'+str(p-l+1))+pe('B'+str(l),'TH'+str(p-l)))
        dv.append(v)
    dw=[F(0),pe('F','TH0'),pe('mF','H1')+2*pe('F','TH1')+pe('Fp','TH0')]
    c={'a':F(0),'b':h,'h':h,'elo':F(1),'ehi':F(1)};co=kernels.combine(model,F(1),F(1));outputs={};tests=0
    for name in ['arb512','iv200']:
        _,out=bounds.Engine(name).cell(c,model,co,inputs);outputs[name]=out
        for key,vals in [('dV',dv),('dW',dw)]:
            for val,box in zip(vals,out[key]):assert F(box['lower_exact'])<=val<=F(box['upper_exact']);tests+=1
    for key in outputs['arb512']:
        for a,b in zip(outputs['arb512'][key],outputs['iv200'][key]):assert max(F(a['lower_exact']),F(b['lower_exact']))<=min(F(a['upper_exact']),F(b['upper_exact']));tests+=1
    assert any(v>0 for v in dv) and dw[1]>0 and dw[2]>0
    print(json.dumps({'status':'PASS_NONZERO_RADII_MODEWISE_EXACT_ERRORS_AND_DUAL_ENGINES','modewise_aggregate_equalities':len(expected),'actual_linear_identity_checks':linear,'exact_dV_dW_and_interval_overlap_checks':tests,'dV_exact':[str(v) for v in dv],'dW_exact':[str(v) for v in dw]}),flush=True)
if __name__=='__main__':main()
