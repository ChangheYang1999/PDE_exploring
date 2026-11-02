"""Check the two inactive gates and sampled equal-name gameplay prefixes."""
from copy import deepcopy
from datetime import datetime,timezone
from pathlib import Path
from urllib.parse import parse_qs
import argparse,ast,hashlib,json,time
from td_game.config import balanced_config
from td_game.engine import Engine
from bot_research.experiments.validation.isolated_match import resolve
from bot_research.experiments.validation.artifact_io import atomic_json
from bot_research.experiments.validation.source_closure import static_closure

class InactiveGates(ast.NodeTransformer):
    def visit_Assign(self,node):
        if len(node.targets)==1 and isinstance(node.targets[0],ast.Name) and node.targets[0].id in ('struck','passive_mid'):
            return None
        return self.generic_visit(node)
    def visit_Name(self,node):
        if isinstance(node.ctx,ast.Load) and node.id in ('struck','passive_mid'):
            return ast.Constant(value=False)
        return node
    def visit_UnaryOp(self,node):
        node=self.generic_visit(node)
        if isinstance(node.op,ast.Not) and isinstance(node.operand,ast.Constant) and isinstance(node.operand.value,bool):
            return ast.Constant(value=not node.operand.value)
        return node
    def visit_BoolOp(self,node):
        node=self.generic_visit(node)
        # Only eliminate true conjuncts. Do not erase evaluation of false suffixes.
        if isinstance(node.op,ast.And):
            node.values=[v for v in node.values if not (isinstance(v,ast.Constant) and v.value is True)]
            if not node.values:return ast.Constant(value=True)
            if len(node.values)==1:return node.values[0]
        return node
    def visit_If(self,node):
        node=self.generic_visit(node)
        if isinstance(node.test,ast.Constant) and node.test.value is False:return node.orelse
        return node
    def visit_FunctionDef(self,node):
        if node.name=='_quiet':return None
        return self.generic_visit(node)
    def visit_keyword(self,node):
        if node.arg in ('strike_until','passive_mid_from'):
            assert isinstance(node.value,ast.Constant) and node.value.value is None
            return None
        return self.generic_visit(node)

class StripDocstrings(ast.NodeTransformer):
    def generic_visit(self,node):
        node=super().generic_visit(node)
        if isinstance(node,(ast.Module,ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)):
            if node.body and isinstance(node.body[0],ast.Expr) and isinstance(node.body[0].value,ast.Constant) and isinstance(node.body[0].value.value,str):
                node.body=node.body[1:]
        return node

def dump(node):return ast.dump(node,include_attributes=False)
def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def parameters(spec):return {k:json.loads(v[0]) for k,v in parse_qs(spec.partition('?')[2]).items()}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',required=True);args=p.parse_args();start=time.perf_counter()
    manifest=Path('bot_research/experiments/validation/nominee-handoff-001.json');m=json.loads(manifest.read_text())
    candidates=m['candidates'];assert [c['id'] for c in candidates]==['P4TNUB','P5TNUBM']
    paths=[Path(c['spec'].partition(':')[0].replace('.','/')+'.py') for c in candidates]
    for path in paths:assert digest(path)==m['input_sha256'][str(path)]
    old,new=[ast.parse(p.read_text()) for p in paths]
    assert dump(StripDocstrings().visit(old))==dump(StripDocstrings().visit(InactiveGates().visit(new)))
    instances=[resolve(c).decide.__self__ if hasattr(resolve(c).decide,'__self__') else None for c in []]
    from bot_research.experiments.lead.v28 import Insurer as A
    from bot_research.experiments.lead.v30 import Insurer as B
    aa,bb=A(**parameters(candidates[0]['spec'])),B(**parameters(candidates[1]['spec']))
    pa,pb=dict(aa.p),dict(bb.p)
    assert pa.pop('passive_until')==4 and pb.pop('passive_until')==5
    assert pb.pop('strike_until') is None and pb.pop('passive_mid_from')==5
    assert pa==pb
    opponents=list(json.loads(Path('bot_research/experiments/validation/triggered-budget-a001.json').read_text())['opponents'])
    opponents += [dict(id='idle',spec='td_bots.protocol:idle'),dict(id='timing',spec='bot_research.bots.economy.timing:@make')]
    roots={x['spec'].partition(':')[0] for x in candidates+opponents}|{'bot_research.experiments.validation.check_nominee_prefix_equivalence'}
    hashes={str(p):digest(p) for p in static_closure(roots)}
    for path,sha in m['input_sha256'].items():
        if '/data/' in path:
            assert digest(path)==sha;hashes[path]=sha
    hashes[str(manifest)]=digest(manifest)
    proof=Path('bot_research/experiments/validation/analysis/nominee_prefix_equivalence/PROOF.md');hashes[str(proof)]=digest(proof)
    cases=[]
    for opponent in opponents:
        for side in (0,1):
            games=[Engine(balanced_config(),('equal-name-0','equal-name-1')) for _ in candidates]
            policies=[]
            for candidate in candidates:
                cs=[resolve(candidate).decide,resolve(opponent).decide]
                if side:cs.reverse()
                policies.append(cs)
            rows=[]
            for rnd in range(1,5):
                observations=[[g.observation(s) for s in (0,1)] for g in games]
                assert observations[0]==observations[1]
                saved=deepcopy(observations)
                actions=[[policies[i][s](observations[i][s]) for s in (0,1)] for i in (0,1)]
                assert observations==saved and actions[0]==actions[1]
                records=[games[i].play_round(actions[i]) for i in (0,1)]
                assert records[0]==records[1]
                assert all(e['accepted'] for row in records[0] for e in row['event'] if e['kind']=='action')
                rows.append(dict(round=rnd,actions=actions[0],snapshots=[games[0].snapshot(s) for s in (0,1)]))
                if games[0].result is not None:break
            assert games[0].observation(1-side)==games[1].observation(1-side)
            cases.append(dict(opponent=opponent,target_side=side,rounds=rows,equal_next_observation=True))
    assert len(cases)==12 and all(digest(p)==h for p,h in hashes.items())
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),runtime_seconds=time.perf_counter()-start,
        all_passed=True,source_specialization_ast_equal=True,shared_parameters_equal=True,input_sha256=hashes,
        cases=cases,scope='Four-round equal-name prefix equivalence. Public labels in named benchmarks may reveal identity immediately.')
    atomic_json(args.output,out,exclusive=True);print(json.dumps({k:out[k] for k in ('time_utc','runtime_seconds','all_passed')}))
if __name__=='__main__':main()
