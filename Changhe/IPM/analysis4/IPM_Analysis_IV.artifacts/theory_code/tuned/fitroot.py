import re,sys,numpy as np
for fn in sys.argv[1:]:
    ns=[];ls=[]
    for line in open(fn):
        m=re.match(r'\s*(\d+) l1=(\S+)',line)
        if m: ns.append(int(m.group(1))); ls.append(float(m.group(2)))
    ns=np.array(ns);ll=np.log(ls)
    for lo in (60,120):
        s=ns>=lo
        X=np.vstack([ns[s],np.log(ns[s]),np.ones(s.sum())]).T
        co,*_=np.linalg.lstsq(X,ll[s],rcond=None)
        print(fn,'fit n>=%d: log l1 = n*log A + beta*log n + c : A=%.4f beta=%.3f'%(lo,np.exp(co[0]),co[1]))
