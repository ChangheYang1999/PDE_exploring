#!/usr/bin/env python3
"""Exact rational counterexample; no NumPy, device or network use."""
from fractions import Fraction as Q
from pathlib import Path
import datetime, hashlib, json
ROOT=Path(__file__).resolve().parents[3]
tau=Q(1,1000000); a=3*tau/4
norm_squared=1+a*a; error_squared=4*a*a
checks={
    'positive_tau':tau>0,
    'group_condition_squared':a*a<tau*tau*norm_squared,
    'whole_relative_error_exceeds_threshold_squared':error_squared>tau*tau*norm_squared,
    'error_exceeds_one_tau_squared':error_squared>tau*tau*norm_squared,
    'error_below_two_tau_squared':error_squared<4*tau*tau*norm_squared,
    'equal_full_norms':1+(-a)**2==norm_squared,
}
proof=ROOT/'research/group_exclusion_bound/PROOF.md'
spec=ROOT/'artifacts/specifications/SPEC_v1.16.md'
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'tau':str(tau),'a':str(a),'d':['1',str(a)],'D':['1',str(-a)],'group_indices':[1],'d_norm_squared':str(norm_squared),'error_norm_squared':str(error_squared),'checks':checks,'all_passed':all(checks.values()),'spec_sha256':hashlib.sha256(spec.read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact rational counterexample to the explanatory bound; not an Euler derivative or full-gate acceptance counterexample.'}
out=ROOT/'research/group_exclusion_bound/verification/counterexample_v1.json'
if out.exists():raise FileExistsError(out)
out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
assert result['all_passed']
