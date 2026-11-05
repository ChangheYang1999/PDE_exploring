#!/usr/bin/env python3
"""Assemble an actual rank-one A/B/operator-tail certificate for Candidate013."""
import json,hashlib
from pathlib import Path
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;ctx.prec=384
CR=HERE.parent/'coercivity_residual'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rbpath=HERE/'rank1_replay_bindings_v01.json';rb=json.loads(rbpath.read_text())
assert rb['status']=='ACTUAL_RANK1_REPLAY_COMPLETED_WITH_IMMUTABLE_DEPENDENCIES' and rb['before']==rb['after']
for path,digest in rb['before'].items():assert sha(Path(path))==digest
rankpath=HERE/rb['result_file'];assert sha(rankpath)==rb['result_sha256']
rank=json.loads(rankpath.read_text());assert rank['status']=='RIGOROUS_A11_AND_GRAM_ONLY'
hspath=CR/'L2_signed_far_v05'/'result.json';hs=json.loads(hspath.read_text())
assert hs['status']=='CERTIFIED_DIRECT_L2' and hs['theta_core_pass'] and hs['theta_exterior_pass'] and hs['theta_origin_pass']
assert hs['assembler_sha256']==sha(CR/'assemble_L2_signed_far_v05.py')
assert hs['far_cache_sha256']==sha(CR/'L2_signed_far_v05'/'far_expansion.cache.json')
for name,digest in hs['source_configuration']['code_hashes'].items():assert sha(CR/name)==digest
for name,digest in hs['used_chunk_sha256'].items():assert sha(CR/'L2_cert_v04'/name)==digest
assert hs['source_configuration']['source_hashes']['base007']=='ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21'
assert hs['source_configuration']['source_hashes']['phi013']=='a16e9d85d5362860c9772388be9d5ab9d4764ad53b729a70ead31ae6bcb32c2a'
A=arb(rank['A11']['midpoint'])+arb(0,arb(rank['A11']['radius']).abs_upper())
B=arb(rank['B11']['ball'])
kappa=arb(hs['kappa_HS_upper']).abs_upper()
assert A<0 and B>0
Alow=A.abs_lower();Aupper=A.abs_upper();Bupper=B.upper()
epsilon=(kappa*kappa-Alow*Alow).sqrt().upper()
CN=(Aupper*Bupper).upper()
assert epsilon<arb('0.7071') and CN<arb('5.236')
out={'status':'RIGOROUS_ACTUAL_RANK1_SOURCE_OPERATOR_CERTIFICATE',
     'source_hashes':hs['source_configuration']['source_hashes'],
     'basis':'phi_01(x,y)=sqrt(2/pi)*y*exp(-(x²+y²)/2), exact L2-normalized real S1 Schwartz function',
     'q':'21/10','dimension':1,
     'A_matrix':[[A.str(90)]],'B_matrix':[[B.str(90)]],
     'B_definition':'B11=||W2 J^q phi_01||_2², W2=sqrt(1+4r²)',
     'full_actual_HS_upper':kappa.str(90),'A11_absolute_lower':Alow.str(90),
     'operator_tail_epsilon_upper':epsilon.str(90),
     'adopted_rational_tail_epsilon':'7071/10000',
     'finite_rank_absolute_C_N_upper':CN.str(90),'adopted_rational_C_N':'1309/250',
     'operator_approximation':'K_N G=A11 <G,phi_01> phi_01; ||Cvs3-K_N||op <=epsilon on real S1',
     'inherited_N2_quadratic_form_bound':'|Cvs3[J^q(W2g)]| <=epsilon ||J^q(W2g)||²+C_N||g||²',
     'signed_finite_part':'A11<0, so Cvs3[G] <=epsilon ||G||² is also valid as a one-sided upper bound',
     'tail_proof':'T->PTP is an orthogonal projection in the Hilbert-Schmidt Hilbert space; ||K-PKP||HS²=||K||HS²-|A11|², and operator norm is at most HS norm',
     'scope_warning':'This is an actual finite-rank source-commutator certificate. Its displayed tail upper is too coarse to close the campaign invariant-ball budget. It proves no lower obstruction and no stationary existence. The finite C_N pairing uses inherited N2, not the different Qa Gram. The preferred local integer proof does not charge this decomposition.',
     'bindings':{str(p.relative_to(HERE.parent)):sha(p) for p in [Path(__file__),rbpath,rankpath,hspath]}}
(HERE/'actual_rank1_operator_tail_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
