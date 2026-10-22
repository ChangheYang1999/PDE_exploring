"""Replay the explicit local criterion using registered exact inputs."""
import os
for name in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
os.environ['PYTHONDONTWRITEBYTECODE'] = '1'
import argparse, datetime, hashlib, json, resource, time
from fractions import Fraction
from pathlib import Path
import flint
from flint import arb, ctx
from certified_eval import LocalInverse, read_compiled, rational, store, upper_abs
resource.setrlimit(resource.RLIMIT_AS, (4*1024**3,4*1024**3))
resource.setrlimit(resource.RLIMIT_CPU, (530,540))
HERE = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()


def frac_ball(s):
    f = Fraction(s)
    return rational(f.numerator, f.denominator)


def frobenius(entries):
    return sum((upper_abs(v)**2 for v in entries),arb(0)).sqrt().upper()


def run(bits, params):
    ctx.prec=bits
    ctx.threads=1
    start=time.process_time()
    source=HERE/params['compiled']['path']
    assert sha(source)==params['compiled']['sha256']
    if sha(HERE/params['raw_source']['path'])!=params['raw_source']['sha256']:print('note: raw state bytes differ from the frozen copy; the compiled coefficient file hash is still enforced')
    comp=read_compiled(source)
    assert comp['M']==52 and comp['N']==208 and comp['beta']==2
    inv=LocalInverse(comp,*params['taylor_center_rational'])
    x,y=map(frac_ball,params['center'])
    r=frac_ball(params['radius'])
    middle=inv.evaluate(x,y)
    # The proposed preconditioner is a rational matrix, never an asserted inverse Jacobian.
    if 'matrix_A' in params:
        A=[[Fraction(c) for c in row] for row in params['matrix_A']]
    else:
        A=[[Fraction(format(float(middle['DW'+str(i)+str(j)].mid()),'.10f'))
            for j in range(2)] for i in range(2)]
    determinant=A[0][0]*A[1][1]-A[0][1]*A[1][0]
    assert determinant!=0
    Ai=[[A[1][1]/determinant,-A[0][1]/determinant],
        [-A[1][0]/determinant,A[0][0]/determinant]]
    ai=[[rational(v.numerator,v.denominator) for v in row] for row in Ai]
    K=frobenius([v for row in ai for v in row])
    square=inv.evaluate(x+arb(0,r.upper()),y+arb(0,r.upper()))
    jac=[[square['DW'+str(i)+str(j)] for j in range(2)] for i in range(2)]
    error=[[(1 if i==j else 0)-sum((ai[i][l]*jac[l][j]for l in range(2)),arb(0))
            for j in range(2)] for i in range(2)]
    k=frobenius([v for row in error for v in row])
    e=frobenius([middle['W1'],middle['W2']])
    d0,d1,dtheta=[frac_ball(params[name]) for name in ('d0','d1','dtheta')]
    gradient=square['Theta_y']
    if gradient>0:gamma=gradient.lower()
    elif gradient<0:gamma=(-gradient).lower()
    else:gamma=arb(0)
    c=k+K*d1
    motion=K*(e+d0)
    margin=(1-c)*r
    values={'K':K,'k':k,'e':e,'gamma':gamma,'c':c,
            'center_displacement_bound':motion,'available_radius':margin,
            'd0':d0,'d1':d1,'dtheta':dtheta,'radius':r}
    gates={'contractive':c<1,'strict_self_map':motion<margin,
           'nonzero_gradient':dtheta<gamma,
           'center_elliptic_identity_contains_zero':middle['elliptic_identity_interval'].contains(0),
           'square_elliptic_identity_contains_zero':square['elliptic_identity_interval'].contains(0)}
    out={'precision_bits':bits,'matrix_A':[[str(v)for v in row]for row in A],
         'matrix_A_inverse':[[str(v)for v in row]for row in Ai],
         'bounds':{key:store(v)for key,v in values.items()},
         'point':{key:store(v)for key,v in middle.items()},
         'square':{key:store(v)for key,v in square.items()},
         'gates':gates,'all_gates_pass':all(gates.values()),
         'cpu_seconds':time.process_time()-start,
         'scope':'Strict gates concern this exact trial and this local ball; independent code audit required.'}
    return out

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--bits',type=int,default=2048)
    parser.add_argument('--params',type=Path,default=HERE/'data/parameters.json')
    parser.add_argument('--output',type=Path,default=HERE/'verification/certificate_2048.json')
    a=parser.parse_args()
    params=json.loads(a.params.read_text())
    record={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'parameters_sha256':sha(a.params),'script_sha256':sha(__file__),
            'evaluator_sha256':sha(HERE/'certified_eval.py'),'proof_sha256':(sha(HERE/'PROOF.md') if (HERE/'PROOF.md').exists() else None),
            'python_flint_version':flint.__version__,'parameters':params}
    record['result']=run(a.bits,params)
    record['completed_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    a.output.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'completed_utc':record['completed_utc'],'matrix_A':record['result']['matrix_A'],
                     'bounds':{k:v['display']for k,v in record['result']['bounds'].items()},
                     'point':{k:record['result']['point'][k]['display']for k in ('W1','W2','Theta_x','Theta_y','DW00','DW01','DW10','DW11')},
                     'gates':record['result']['gates'],'cpu_seconds':record['result']['cpu_seconds']},indent=2))
