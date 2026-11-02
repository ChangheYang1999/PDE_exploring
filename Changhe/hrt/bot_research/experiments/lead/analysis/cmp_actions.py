import json,sys
def acts(f):
    out={}
    for l in open(f):
        d=json.loads(l)
        a=[(e.get('accepted'),json.dumps(e['action'],sort_keys=True)) for e in d['event'] if e.get('kind')=='action']
        out[(d['round'],d['player'])]=a
    return out
A=acts(sys.argv[1]); B=acts(sys.argv[2])
for r in range(1,int(sys.argv[3])+1):
    for p in (0,1):
        print(r,p,'same' if A.get((r,p))==B.get((r,p)) else 'DIFF')
