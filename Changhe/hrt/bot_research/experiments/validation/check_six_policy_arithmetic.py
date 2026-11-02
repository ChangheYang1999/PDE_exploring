"""Six-dimensional checks for the reused exact rational certificate solver."""
from datetime import datetime,timezone
from fractions import Fraction
from pathlib import Path
import hashlib,json
from bot_research.experiments.validation.publish_extended_counter_game import exact_certificate
from bot_research.experiments.validation.artifact_io import atomic_json

def main():
    matrices={
        'zero':[[0]*6 for _ in range(6)],
        'pure_first':[[0 if i==j else 1 if i==0 else -1 if j==0 else 0 for j in range(6)] for i in range(6)],
        'duplicated_cycle':[[[[0,1,-1],[-1,0,1],[1,-1,0]][i//2][j//2] for j in range(6)] for i in range(6)]}
    cases=[]
    for name,m in matrices.items():
        c=exact_certificate(m);assert c is not None
        p=list(map(Fraction,c['weights']));assert sum(p)==1 and min(p)>=0
        payoff=[sum(p[i]*m[i][j] for i in range(6)) for j in range(6)]
        assert min(payoff)>=0 and c['checked_active_sets']==792
        if name=='pure_first':assert p==[1,0,0,0,0,0]
        if name=='duplicated_cycle':assert [sum(p[i:i+2]) for i in (0,2,4)]==[Fraction(1,3)]*3
        cases.append(dict(name=name,matrix=m,certificate=c))
    root=Path('bot_research/experiments/validation')
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,cases=cases,
        input_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [root/'publish_extended_counter_game.py',Path(__file__).relative_to(Path.cwd())]})
    atomic_json(root/'analysis/six_policy_game/verification/arithmetic_components.json',result,exclusive=True)
    print(json.dumps(dict(all_passed=True,cases=len(cases),active_sets_per_case=792)),flush=True)
if __name__=='__main__':main()
