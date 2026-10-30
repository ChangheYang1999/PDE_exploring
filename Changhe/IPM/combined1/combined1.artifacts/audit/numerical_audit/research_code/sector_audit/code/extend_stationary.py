"""Independent finite homogeneous recursion, using previously verified exact orders."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import argparse,json,sys,time
from flint import fmpq as Q,arb,ctx
from sectors_flint import dx,dy,add,product_cs,aq
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/sector_audit'

def digest(p):return sha256(Path(p).read_bytes()).hexdigest()
def density(C,s):return {n:-v for n,v in dy({n:(s*s-n*n)*v for n,v in C.items()},s-2,'c').items()}
def inverse(G,s):
    todo=G.copy();C={}
    for n in range(max(G)-1,-1,-2):
        image=density({n:Q(1)},s);assert image.get(n+1,0)!=0
        coefficient=todo.get(n+1,Q(0))/image[n+1]
        if coefficient:C[n]=coefficient
        todo=add(todo,image,-coefficient)
    assert not todo
    return C

def fields(C,a):
    s=a+3;G=density(C,s);stream=dy(dx(C,s,'c'),s-1,'c')
    return G,{n:-v for n,v in dy(stream,s-2,'s').items()},dx(stream,s-2,'s'),dx(G,a,'s'),dy(G,a,'s')

def parse(d):return {int(n):Q(v) for n,v in d.items() if Q(v)}
def dump(d):return {str(n):str(v) for n,v in sorted(d.items())}

def run(nmax):
    ctx.prec=512;start=time.monotonic();checkpoint=BASE/'verification/stationary_principal.json'
    original=json.loads(checkpoint.read_text());c=Q(original['cl']);gamma=1/c;delta=1-gamma
    target=BASE/f'verification/stationary_extension_{nmax}.json'
    records=original['branches'];potentials=[parse(original['leading_potential'])]+[parse(r['potential_cos']) for r in records]
    FF=[fields(C,gamma-j*delta) for j,C in enumerate(potentials)]
    for j,row in enumerate(records,1):
        assert FF[j][0]==parse(row['stationary_density_sin'])
        assert {n:j*(c-1)*v for n,v in FF[j][0].items()}==parse(row['forcing_sin'])
    peerfile=BASE/'peer_data/N1_orders_0_12.json';peer=json.loads(peerfile.read_text())
    if target.exists():
        prior=json.loads(target.read_text());assert prior['code_sha256']==digest(__file__)
        for row in prior['additional_orders']:
            j=row['index'];assert j==len(FF)
            C=parse(row['potential_cos']);FF.append(fields(C,gamma-j*delta));potentials.append(C)
    else:prior={'additional_orders':[]}
    print('prepared checkpoint through',len(FF)-1,'elapsed',time.monotonic()-start,flush=True)
    for j in range(len(FF),nmax+1):
        force={}
        for i in range(j):
            k=j-1-i
            force=add(force,product_cs(FF[i][1],FF[k][3]))
            force=add(force,product_cs(FF[k][4],FF[i][2]))
        Gj={n:v/(j*(c-1)) for n,v in force.items()};alpha=gamma-j*delta
        C=inverse(Gj,alpha+3);ff=fields(C,alpha);assert ff[0]==Gj
        norm=(arb.pi()*aq(sum((v*v for v in force.values()),Q(0)))).sqrt()
        FF.append(ff);potentials.append(C)
        prior['additional_orders'].append({'index':j,'residual_exponent':str(alpha),'forcing_full_circle_norm':norm.str(80),
            'stationary_density_sin':dump(Gj),'potential_cos':dump(C),'forcing_sin':dump(force),'max_density_harmonic':max(Gj)})
        checks=[]
        for k in range(min(len(FF),13)):
            row=peer['orders'][str(k)]
            matches={'index':k,'exponent':Q(row['alpha'])==gamma-k*delta,'density':parse(row['G'])==FF[k][0],
                     'potential':parse(row['C'])==potentials[k]}
            assert all(v for key,v in matches.items() if key!='index'),matches
            checks.append(matches)
        prior.update({'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'cl':str(c),
            'checkpoint_sha256':digest(checkpoint),'peer_sha256':digest(peerfile),'code_sha256':digest(__file__),
            'checks':checks,'elapsed_seconds':time.monotonic()-start,'scope':'Finite exact recurrence only; no convergence or full residual bound.'})
        temp=target.with_suffix('.pending');temp.write_text(json.dumps(prior,indent=2)+'\n');temp.replace(target)
        print('order',j,'forcing norm',norm.str(30),'exact peer matches',len(checks),'seconds',time.monotonic()-start,flush=True)
    print('done',time.monotonic()-start,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--order',type=int,default=12);a=p.parse_args();run(a.order)
