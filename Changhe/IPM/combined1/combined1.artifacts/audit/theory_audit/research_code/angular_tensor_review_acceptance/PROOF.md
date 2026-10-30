# Acceptance of the full-tensor angular quadrature review

Let M>=0 be an integer and chi=sum_(m=0)^M a_m(r)cos(2m theta),
with real C6 radial functions on an open annulus. Set
rho=-partial_y Delta chi, psi=partial_x partial_y chi,
u=(-partial_y psi,partial_x psi), and F=(cX+u).grad rho-rho,
with real c. At fixed r>0, exact quadrant midpoint quadrature with
N>=2M+2 integrates F^2, |grad F|^2, |D2F|_F^2 and (Delta F)^2.
Separate Cartesian derivative squares of order at most two are
integrated exactly when N>=2M+3. Any radial multiplier preserves
these fixed-radius identities. All nodes and function values here
are exact real numbers.

Proof. The Laplacian preserves angular frequency, and each Cartesian
derivative shifts it by at most one. Thus rho has odd sine frequencies
at most2M+1 and psi even sine frequencies at most2M+2. The polar
Jacobian u.grad rho=(psi_r rho_theta-psi_theta rho_r)/r gives odd
sine frequencies of F at most d=4M+3. Radial derivatives preserve
this degree. Polar gradient components are F_r and F_theta/r.
The orthonormal polar Hessian entries are F_rr,
F_rtheta/r-F_theta/r^2, and F_r/r+F_thetatheta/r^2. Their squares
sum, with multiplicity two on the middle entry, to the Cartesian
Frobenius square; their trace is Delta F. Each component has only
odd sine or only odd cosine frequencies at most d.

Every such square contains only the constant and cos(2q theta)
with 1<=q<=d. The N quadrant midpoint values of cos(2q theta)
sum to zero when 0<q<2N, by telescoping
2sin(q pi/(2N))cos((i+1/2)q pi/N). The integral is also zero.
Since d<2N at N>=2M+2, all full-tensor assertions follow.
For a separate derivative of order j<=2, coordinate parity keeps
a single sine/cosine type with one frequency parity, and the largest
frequency is at most d+j. Its square obeys the same cosine test
when d+2<2N, as ensured by N>=2M+3.

The complete independent N4-307 proof in source/N4_PROOF.md establishes
these same claims. Its symbolic tensor and trace derivations, all168
exact cyclotomic moments and the M79 product indices agree. I read
its code and its corrected polynomial-domain comparison; no failed
mathematical identity was concealed. Every bound source hash and the
peer374 result are checked in verification/manifest.json.

Verdict: CONFIRMED; T4-374 Section5 is independently reviewed. For
M79,160/161 nodes suffice respectively and180 passes both. This
acceptance covers no other section of374. It bounds no floating
node or evaluation error, radial quadrature error, omitted region,
whole-plane norm, inverse or existence claim. A proposed basis still
needs its actual candidate binding. No foreign code is executed.
