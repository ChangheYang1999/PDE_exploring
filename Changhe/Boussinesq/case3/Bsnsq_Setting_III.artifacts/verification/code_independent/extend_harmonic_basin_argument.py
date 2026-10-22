from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
now=datetime.now(timezone.utc).isoformat();r=Path('research/161_harmonic_local_outgoing_region');p=r/'PROOF.md';s=p.read_text()
(r/'verification/proof_before_global_basin_extension.md').write_text(s)
s=s.replace('Choose delta>0 much smaller than A-A0 and A-R0,', 'Choose delta>0 with delta<2/45 and much smaller than A-A0 and A-R0,')
s=s.replace('## 7. Dependencies and scope','''## 7. A global invariant outgoing set still has nonzero vorticity

This strengthens the scope statement by constructing, at each endpoint, a particular nonempty open invariant set O of endpoint orbits on which Omega is not identically zero. It does not claim that the locally harmonic region extends globally.

Consider the right endpoint. Section5 gives an open local outgoing neighborhood N containing a center-line point (u0,0) with0<u0<delta, all of whose backward orbits tend to p. Let O be its full flow-saturation, union over all real times t of phi_t N. The global vector field is smooth and at most linear at infinity, so this flow is complete. Thus O is nonempty, open, invariant in both time directions, and every orbit in O has backward limit p. The exact global thermal equation makes Theta=M throughout O.

The line Y=0 is invariant from u0 to u*=5delta/2, with W1(u,0)=f_+(u)>0 throughout0<u<3delta, including the radial correction annulus. This follows from the oddness of the stream correction in Y and its cancellation of Yv-H to first order along the positive real line: H_Y(u,0)=f_+(u)=v(u). Equivalently the exact formulas in section4 give the same center-line speed across the cutoff. The time integral int_(u0)^(u*) du/f_+(u) is finite because u0>0. The image of N at that finite time is an open neighborhood of (u*,0), contained in O.

Since u*>2delta, the correction vanishes in a neighborhood of (u*,0). For small nonzero Y in the last open neighborhood, section2 therefore gives

    Omega(u*,Y)=f_+''(u*) Y,
    f_+''(u)=exp(-1/sqrt(u)) (1-3sqrt(u))/(4u^3).

Our allowed choice delta<2/45 gives u*<1/9, so f_+''(u*)>0. Consequently Omega is nonzero at points in O. If(V) held identically on O, Theta=M there would make Omega(phi_(-t)X)=exp(t)Omega(X); boundedness at the backward limit p would force Omega=0 on O. This is a contradiction. Thus(V) does not hold identically on this chosen O. Reflection constructs the corresponding O at the left endpoint.

The conclusion is existential for the two constructed invariant open sets, each obtained from a local neighborhood containing a center-line point. No assertion about every arbitrarily selected invariant subset of the global basin is needed or made. In particular it is compatible with exact harmonicity on the local outgoing side established in section5.

## 8. Dependencies and scope''')
s+='\nExtension UTC '+now+': supplied the global flow-saturation argument and exact nonzero-vorticity witness at u*=5delta/2. No numerical premise, new PDE solution or full endpoint is claimed.\n';p.write_text(s)
manifest=r/'build_inputs.json';d=json.loads(manifest.read_text());d['utc']=now
seen=set()
for item in d['inputs']:
 f=Path(item['path']);item['sha256']=hashlib.sha256(f.read_bytes()).hexdigest();seen.add(str(f))
for f in [r/'verification/proof_before_global_basin_extension.md',Path(__file__)]:
 if str(f) not in seen:d['inputs'].append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
manifest.write_text(json.dumps(d,indent=2)+'\n')
# Repair exact local dependency names in164; no missing-file filtering in the manifest.
m=Path('research/164_finite_transverse_polynomial_endpoint/build_inputs.json');d=json.loads(m.read_text())
for f in [Path('research/73_local_affine_detachment/PROOF.md'),Path('research/53_beta2_endpoint_stable_geometry/PROOF.md')]:
 if f.exists():d['inputs'].append({'path':str(f),'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
m.write_text(json.dumps(d,indent=2)+'\n')
q=Path('verification/opus262_global_basin_witness');q.mkdir()
q.joinpath('question.md').write_text('''Audit this short extension of our explicit smooth beta2 nonprofile construction. Restrictions: no JavaScript/TypeScript, no servers/listeners, no RLScience cluster, no GPU, no Lean/Lake, no external posting. No tools requested.

Near p=(A,M/4), use u=x-A,Y=y-M/4. For0<u<3delta the old field is W=(f(u),(4-f\'(u))Y), f=e^(-1/sqrt(u)), Theta=M. A compact stream correction supported in r<2delta preserves exactly W1(u,0)=f(u),W2(u,0)=0 across the annulus. For r<delta the corrected outgoing side of a smooth strong unstable curve is harmonic, Theta=M, all sufficiently small outgoing-side backward orbits converge to p, and it contains (u0,0) for0<u0<delta. Globally W is smooth, grows at most linearly, and satisfies W.gradTheta=0. Choose delta<2/45. Let N be a small open outgoing neighborhood containing (u0,0), and O=union_{t in R}phi_t N. Complete flow makes O open,invariant,and all its backward limits equal p, hence Theta=M on O. The center-line orbit reaches u*=5delta/2 in finite time integral_(u0)^(u*)du/f(u). Its open-neighborhood image lies in O. The correction vanishes near(u*,0), so Omega=f''(u*)Y there, f''=f(1-3sqrt(u))/(4u^3)>0 at u*. Thus Omega is nonzero on O. If V:W.gradOmega+Omega=Theta_x held identically on O, boundedness at p would force Omega=0 on O, contradiction. Therefore V fails somewhere on this chosen invariant O, although it holds near p on the local outgoing side. Same by reflection left. We claim existence of these two chosen O, not a universal claim for arbitrary invariant subsets. Confirm or identify a gap; no full profile/no global endpoint asserted.
''');q.joinpath('options.json').write_text(json.dumps({'max_tokens':3500,'effort':'low'}))
with Path('WORKLOG.md').open('a') as f:f.write('\n'+now+' | Extended161completeproof: chosen globalflow-saturationOhasnonzeroOmegaoutsidecompactcorrection, fdoubleprimeexactwitness; originalproofpreserved,manifestupdated. PreparedactualOpus262. Readactuallead12:14xii/161/147entries; auditingfinalscopes.\n')
print(now)
