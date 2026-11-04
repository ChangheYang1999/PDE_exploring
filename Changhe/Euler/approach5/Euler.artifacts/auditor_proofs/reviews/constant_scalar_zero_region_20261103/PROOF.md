# Zeros on a region with constant Bernoulli deficit

Status: independently proved. This confirms CO53 at its local scope and gives a stronger elementary replacement for its sublevel argument. The whole coordinator note was read; its nested sources are not certified here. Read after the C1 pressure-minimum lemma A1202.

## 1. Local pressure theorem and notation

Let G be a connected open subset of R3. Let v be C1 and divergence free there, and let pi be C1 with the distributional equation

    -Delta pi=tr((Dv)^2).

Suppose s=pi-|v|^2/2 is constant on G. Then exactly one of the following holds: v=0 on G, or at every point z of {v=0} the matrix Dv(z) is nonzero and skew symmetric.

For the further tail assertions, let0<c<1, let omega be any finite real number, let J be the fixed skew rotation matrix, and set A=cI-omega J, X(x)=Ax. Suppose G lies in R3 minus{0}, is invariant under the local flow of X, v and pi are smooth, and

    X.grad v=-Lv, X.v=0

for the fixed matrix L of the tail equation. Only the homogeneity consequence Dv(z)X(z)=0 at a zero is used. Let Y(w)=(I-w tensor w)v(w) be the tangential projection on G intersect S2. On every nontrivial connected such cone, all zeros of Y are simple zeros of v with index+1. The implication Y=0 iff v=0 follows because X.v=0 and X.w=c on the sphere.

## 2. The C1 minimum lemma, with its required identity

We use the following already checked local lemma A1202: if v is C1, pi is C1, the pressure equation above holds, v(z)=curl v(z)=0, and pi-|v|^2/2 has a local minimum at z, then v vanishes on a neighborhood of z. Here is the argument to specify every dependency.

Translate z to0 and let bars denote unit-sphere averages at radius r. Set E=bar|v|^2, F=bar(v.nu)^2, and Y0=bar(pi-pi(0))+F. The pressure equation, div v=0 and the divergence theorem give

    Y0'=(E-3F)/r.                                     (2.1)

For C1 data, this follows first after local convolution of the divergence form Delta pi=-partial_i partial_j(v_i v_j), followed by integration on spheres and the C1 limit; equivalently the distributional radial identity integrates from0 with its zero integration constant. The complete C1 justification is in the cited proof, Section2. It uses no second derivative of v.

Let M=Dv(0). Curl v(0)=0 makes M symmetric, and div v=0 makes its trace zero. Sphere moments give E=r^2|M|^2/3+o(r^2), F=2r^2|M|^2/15+o(r^2). Therefore(2.1) and Y0(0)=0 give Y0=-r^2|M|^2/30+o(r^2). The minimum gives Y0>=E/2+F>=0, so M=0. Now Y0=o(r^2) and(2.1) gives Y0'<=E/r<=2Y0/r. Thus r^(-2)Y0 is nonnegative and nonincreasing, with limit zero at0. It is identically zero, which makes E=0 and hence v=0 near0.

## 3. Every nontrivial zero has a nonzero skew derivative

At any zero z, put M=Dv(z). In the smooth setting, the constant-s identity pi=s+|v|^2/2 and the pressure equation evaluated at z immediately give

    |M|^2+tr(M^2)=0.

For C1 data the same equality follows by quadratic sphere averages: E=r^2|M|^2/3+o(r^2) and F=r^2[(tr M)^2+tr(M^2)+|M|^2]/15+o(r^2), while Y0=E/2+F because s is constant. Substitution in(2.1), with tr M=0, again yields |M|^2+tr(M^2)=0. Since this sum is2|sym M|^2, M is skew symmetric.

If M=0, then curl v(z)=0, and Section2 applies to the constant scalar s to make v zero nearby. Let O be the set where v vanishes on a neighborhood. It is open. If z is an ambient boundary point of O in G, C1 continuity gives v(z)=Dv(z)=0 from points in O; Section2 makes z interior to O, a contradiction. Thus O is also closed in G. Connectedness implies that either O is empty or v=0 throughout G. In the nontrivial case, every zero consequently has a nonzero skew derivative. This proves the first theorem.

## 4. Tail zeros are simple with positive index for every omega

At a zero z in the tail setting, homogeneity gives MX(z)=0. A nonzero real skew3by3 matrix has a one-dimensional kernel and can be written M h=beta e cross h, where e=X(z)/|X(z)| and beta!=0. Restrict to a sphere point w=z with |w|=1. For a tangent vector h, the derivative of the projected field Y is

    D_S Y(w)h=(I-w tensor w)M h
             =beta(e.w) w cross h.

The second equality follows by decomposing e into its normal and tangential parts: the cross product of its tangential part with h is normal and is projected out. Here e.w=c/|X(w)|>0. Thus D_S Y is a nonzero planar rotation, is invertible, and has positive determinant. The zero is simple and has local index+1. Its velocity also has a transverse linear lower bound.

This argument is valid for every finite omega, with constants allowed to depend on it. It uses no nonrotating sphere identity, no invariant measure and no actual-profile scattering premise.

## 5. The enclosed sublevel estimate

Let Omega be a closed smooth coordinate disk on the sphere whose twisted cone lies in G, and suppose v is nonzero on its boundary. The connected component containing that cone is nontrivial. Section4 makes each zero in Omega isolated. The zeros form a closed subset of a compact set and cannot accumulate at the boundary, so they are finite.

Near each zero w_j, invertibility of D_S Y gives |Y(w)|>=c_j dist(w,w_j) after shrinking a coordinate disk. Since |v|>=|Y|, the same lower bound applies to |v|. Outside these finitely many disks |v| has a positive minimum. Therefore, for all sufficiently small epsilon>0,

    area{w in Omega: |v(w)|^2<epsilon}<=C epsilon.

Smooth positive area densities are equivalent on the compact disk, so the statement holds for either the usual sphere measure or any fixed smooth metric used in the source. This improves CO53(b)'s unspecified positive exponent to exponent1. It excludes every zero of infinite order. If no zero exists, the sublevel set is empty for small epsilon.

The boundary degree of Y equals the sum of its finitely many local indices, hence the number of zeros. If a zero exists it is strictly positive, for every omega. One can verify this usual degree addition by removing disjoint small disks around the zeros and integrating the angular one-form of the normalized field; its exterior derivative is zero where the field is nonzero. Thus CO53(c)'s omega=0 conclusion extends to all omega at this same local constant-s scope.

## 6. CO53(a), what was checked, and what remains open

CO53(a) assumes k=X.v=0 on an open cone, v(z)=Dv(z)=0, s(z)=0 and finite smooth velocity order. Its repeated-stream-factor conclusion is the already confirmed LIT212 argument A1147-A1149 at this stronger local scope. At a repeated factor of multiplicity j>=2, scalar transport forces scalar multiplicity q(j-1), whereas the pressure equation forces2(j-1); q>2 contradicts equality. The leading stream gradient is therefore isolated. The one-sign and index arguments A1115-A1117 give index at most zero. The coefficient calculation in the coordinator note agrees with the complete proof in auditor_proofs/reviews/repeated_stream_factor_20261103/PROOF.md, and no new assumption is removed here.

For CO53(b)-(c), Sections1-5 provide an independent stronger proof using constant s. The source's longer metric sublevel and Rellich calculations are not needed for these verdicts and are not separately certified here. No statement about a point where s is merely flat, or where s has a nonzero harmonic leading term but varies, follows from constant s. In particular this does not settle general T0 points or the main Euler conjecture.

Dependencies: the complete C1 pressure-minimum proof in auditor_proofs/reviews/high_order_pressure_deficit_20261103/PROOF.md, Section2-4; finite-factor proof A1147-A1149 for CO53(a); elementary linear algebra, compactness and planar degree for the new conclusions. Exact source and postread evidence are retained alongside this proof. No numerical calculation or formal build is used.
