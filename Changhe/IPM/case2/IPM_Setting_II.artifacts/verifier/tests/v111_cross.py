# V111: m1 = 1/2 crossing in eta13 at a_2 = -1.228 for t_min -14 and -17 (quadratic through the three states), D there
import numpy as np
c=np.array([0.0744,0.0773,0.0802])
data={'t14':{'m1':[0.496726,0.503051,0.50543],'div_sp':[-0.239,-0.2434,-0.251],'div_fd1':[-0.2383,-0.2428,-0.2504],'dir_fd1':[-0.2544,-0.2494,-0.2487]},
      't17':{'m1':[0.496214,0.503102,0.506319],'div_sp':[-0.2204,-0.224,-0.2321],'div_fd1':[-0.2197,-0.2233,-0.2314],'dir_fd1':[-0.2374,-0.2339,-0.2336]}}
for k,d in data.items():
    pm=np.polyfit(c,d['m1'],2); r=np.roots(pm-np.array([0,0,0.5])); r=[float(x.real) for x in r if abs(x.imag)<1e-12 and 0.07<x.real<0.081]
    lin=float(c[0]+(0.5-d['m1'][0])*(c[1]-c[0])/(d['m1'][1]-d['m1'][0]))
    out={'c_cross_quad':round(r[0],5),'c_cross_lin01':round(lin,5)}
    for q in ('div_sp','div_fd1','dir_fd1'):
        pq=np.polyfit(c,d[q],2); out[q+'_quad']=round(float(np.polyval(pq,r[0])),4)
        out[q+'_lin01']=round(float(np.interp(lin,c[:2],d[q][:2])),4)
    out['dm1_dc_at_cross']=round(float(np.polyval(np.polyder(pm),r[0])),3)
    print(k,out)
for q in ('m1','div_sp','div_fd1','dir_fd1'):
    print('shift t14->t17',q,[round(b-a,4) for a,b in zip(data['t14'][q],data['t17'][q])])
