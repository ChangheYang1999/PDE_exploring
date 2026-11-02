"""Retained fault-injection fixtures for the logical policy-value comparator."""
from datetime import datetime,timezone
from pathlib import Path
import hashlib,json
from bot_research.bots.counters.wall_prefix_selector import WallPrefixSelector
from bot_research.experiments.validation.policy_value_snapshot import freeze_state
from bot_research.experiments.validation.source_closure import static_closure
from bot_research.experiments.validation.artifact_io import atomic_json

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
    roots={'bot_research.experiments.validation.check_policy_value_snapshot'}
    inputs={str(p):sha(p) for p in sorted(static_closure(roots))}
    data=Path('bot_research/bots/counters/data/early_wall_guard_001.json');inputs[str(data)]=sha(data)
    tests=[]
    def require(name,condition):
        assert condition,name
        tests.append(dict(name=name,passed=True))
    a,b=WallPrefixSelector(),WallPrefixSelector()
    require('fresh_G_logical_values_equal',freeze_state(vars(a.g))==freeze_state(vars(b.g)))
    require('fresh_L_logical_values_equal',freeze_state(vars(a.l))==freeze_state(vars(b.l)))
    b.l.model.last_round+=1
    require('nested_model_round_mutation_detected',freeze_state(vars(a.l))!=freeze_state(vars(b.l)))
    b=WallPrefixSelector()
    # H is held as a bound method by the persistent model.
    bound_methods=[value for value in vars(b.l.model).values() if hasattr(value,'__self__')]
    require('one_bound_model_method',len(bound_methods)==1)
    owner=bound_methods[0].__self__
    require('handoff_switch_field_exists',hasattr(owner,'switched'))
    owner.switched=not owner.switched
    require('bound_model_owner_mutation_detected',freeze_state(vars(a.l))!=freeze_state(vars(b.l)))
    b=WallPrefixSelector();b.g.trace.append(dict(round=99))
    require('G_trace_mutation_detected',freeze_state(vars(a.g))!=freeze_state(vars(b.g)))
    def closure_factory():
        value=[]
        def policy():return value
        return policy,value
    left,lv=closure_factory();right,rv=closure_factory()
    require('equal_closure_values_equal',freeze_state(left)==freeze_state(right))
    rv.append(7)
    require('closure_cell_mutation_detected',freeze_state(left)!=freeze_state(right))
    cyclic=[];cyclic.append(cyclic)
    try:freeze_state(cyclic)
    except ValueError:tests.append(dict(name='cycle_rejected',passed=True))
    else:raise AssertionError('Cycle was accepted.')
    try:freeze_state(object())
    except TypeError:tests.append(dict(name='unsupported_value_rejected',passed=True))
    else:raise AssertionError('Unsupported object was accepted.')
    shared=[]
    require('documented_alias_identity_exclusion',freeze_state([shared,shared])==freeze_state([[],[]]))
    require('documented_dict_order_exclusion',freeze_state({'a':1,'b':2})==freeze_state({'b':2,'a':1}))
    assert all(sha(p)==h for p,h in inputs.items())
    result=dict(time_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,tests=tests,
        policy_decision_calls=0,new_games=0,input_sha256=inputs,
        scope='Post-run reproduction and fault injection of constructor/value fixtures; not a pre-call timestamp attestation or universal Python-state equivalence proof.')
    atomic_json(Path('bot_research/experiments/validation/analysis/wall_prefix_selector/verification/value_fixtures.json'),result,exclusive=True)
    print(json.dumps(dict(time_utc=result['time_utc'],all_passed=True,fixtures=len(tests),policy_decision_calls=0)),flush=True)
if __name__=='__main__':main()
