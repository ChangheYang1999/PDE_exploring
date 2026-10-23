# Locations and regional maxima of the independently re-evaluated residuals of the six 4.2 states
# (reads the checker's JSON evidence, read-only).
import json, math, glob
base='verification/evidence/residuals/'
states=['res_cl1.5_N72M16','res_cl1.5_N144M32','res_cl1.5_N192M48','res_cl3.0_N72M16','res_cl3.0_N144M32','res_cl3.0_N192M48']
regions=[(0,1e-2),(1e-2,1),(1,1e2),(1e2,1e30)]
for s in states:
    d=json.load(open(base+s+'_fixed_q3.json'))
    pts=[]
    for p in d['points']:
        th=math.atan2(p['y'],p['x'])
        if abs(p['y'])<=1e-300: continue
        r=min(p['residuals'],key=lambda q:q['relative_step'])
        pts.append((p['radius'],th,abs(r['R']),r['abs_R_over_Nf'],r['abs_R_over_Nv'],r['Nf']))
    print(s, 'points off axis', len(pts), 'of', len(d['points']))
    for k,name in [(2,'|R|'),(3,'|R|/Nf'),(4,'|R|/Nv')]:
        m=max(pts,key=lambda q:q[k])
        print('  max %-7s %.3g at r=%.3g th=%.4f (Nf %.3g)'%(name,m[k],m[0],m[1],m[5]))
    for a,b in regions:
        sub=[q for q in pts if a<=q[0]<b]
        if not sub: continue
        print('  region [%g,%g) n=%d max|R| %.2g  max|R|/Nf %.2g  max|R|/Nv %.2g'%(a,b,len(sub),max(q[2] for q in sub),max(q[3] for q in sub),max(q[4] for q in sub)))
