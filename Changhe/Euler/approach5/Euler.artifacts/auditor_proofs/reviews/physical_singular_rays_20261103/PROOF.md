# Twisted rays and the physical meaning of derivative decay

Status: CONFIRMED by A475 after full independent reconstruction, repeated postwrite inspection and the focused configured-model A15 review. This is a scaling theorem. It excludes no Euler profile and asserts no example of an Euler singularity.

## 1. Exact statement

Let 0<c<1, omega in R, T in R and U in C1(R3;R3). Set J(x,y,z)=(-y,x,0), A=cI-omega J, Q_s=e^(omega sJ), and for t<T put

    s=-log(T-t), y=e^(sA)x,
    u(x,t)=e^((1-c)s)Q_s U(y).                           (1)

A rotation-invariant matrix norm is used for derivatives. Define three subsets of R3 minus{0}, with all limits below taken as (x,t)->(x_*,T), t<T:

    Sigma_v={x_*: limsup (T-t)^(1-c)|u(x,t)|>0},
    Sigma_I={x_*: limsup (T-t)|Du(x,t)|>0},
    Sigma_L={x_*: Du is unbounded on N times(T-tau,T)
                     for every neighborhood N of x_* and tau>0}.

The sets are invariant under e^(sigma A) for every real sigma, and Sigma_I is contained in Sigma_L. Each nonempty set contains a complete twisted dilation ray {e^(sigma A)x_*:sigma in R}, which approaches0 at one end and infinity at the other, crossing every sphere. On the rotation axis this curve is straight; off the axis it rotates when omega!=0.

Moreover,

    Sigma_v empty iff U(y)->0 uniformly at infinity,
    Sigma_I empty iff DU(y)->0 uniformly at infinity,
    Sigma_L empty iff |DU(y)|<=C(1+|y|)^(-1/c)
                              for some finite C.        (2)

The last condition implies

    (D): integral_1^infinity m(r) dr/r<infinity,
         m(r)=sup_(|y|>=r)|DU(y)|.                       (3)

Conversely (D) implies Sigma_I is empty, but this scaling argument gives no converse from Sigma_I empty to(D), or from(D) to Sigma_L empty. The terminology concerning Sigma_L refers specifically to uniform local bounds for the spatial gradient up to T; it does not assert existence of a spacetime Lipschitz extension.

No Euler equation, pressure, incompressibility or nonzero-profile assumption is needed for(1)-(3).

## 2. Exact scaling and invariance

Since e^(sA)=e^(cs)Q_s^T, the chain rule gives

    Du(x,t)=e^s Q_s DU(y)Q_s^T.                          (4)

For real sigma set x'=e^(-sigma A)x and t'=T-e^(-sigma)(T-t). Then s'=s+sigma and y'=y. Orthogonality of the rotations implies

    (T-t')^(1-c)|u(x',t')|=(T-t)^(1-c)|u(x,t)|,
    (T-t')|Du(x',t')|=(T-t)|Du(x,t)|,
    |Du(x',t')|=e^sigma|Du(x,t)|.                        (5)

The transformation is a homeomorphism and maps neighborhoods approaching (x_*,T) to neighborhoods approaching (e^(-sigma A)x_*,T). Both sigma and -sigma are allowed. The two limsup sets and the local unboundedness set are therefore invariant. A uniform gradient bound near a terminal point makes its normalized gradient tend to0, proving Sigma_I subset Sigma_L. Finally |e^(sigma A)x_*|=e^(c sigma)|x_*|, which proves the ray assertion. In the off-axis case this is a rotating ray on a fixed polar cone; no planar-spiral assertion is needed.

## 3. The velocity and normalized-gradient equivalences

If U tends to0 uniformly, then as (x,t)->(x_*,T) with x_*!=0,

    |y|=e^(cs)|x|->infinity,
    (T-t)^(1-c)|u(x,t)|=|U(y)|->0.

The identical argument using(4) proves the DU implication. Conversely, if U does not tend to0, there exist epsilon>0 and y_n with |y_n|->infinity and |U(y_n)|>=epsilon. Set

    s_n=c^(-1)log|y_n|, t_n=T-e^(-s_n),
    x_n=e^(-s_n A)y_n.

Then |x_n|=1. Along a subsequence x_n tends to some x_* on the unit sphere, and the normalized velocity at (x_n,t_n) is at least epsilon. Hence x_* belongs to Sigma_v. Replacing U by DU proves the normalized-gradient converse. This argument allows infinite limsups and needs no boundedness at infinity.

## 4. Uniform local gradient bounds give the exact power rate

If |DU(y)|<=C(1+|y|)^(-1/c), then(4) gives

    |Du(x,t)|<=C e^s(e^(cs)|x|)^(-1/c)=C|x|^(-1/c)

for x!=0. This is uniformly bounded near every x_*!=0, so Sigma_L is empty.

For the converse, assume Sigma_L is empty. Each point of the unit sphere has a neighborhood and a terminal time interval on which Du is bounded. A finite subcover gives one bound M and one tau>0 valid on the entire sphere for T-t<tau. For sufficiently large |y| choose s=c^(-1)log|y| and x=e^(-sA)y, so |x|=1 and e^(-s)<tau. Equation(4) implies

    |DU(y)|=e^(-s)|Du(x,T-e^(-s))|<=M|y|^(-1/c).

Continuity of DU bounds it on the remaining compact ball and gives the global(1+|y|) formulation. This proves the third equivalence in(2). The resulting bound m(r)<=C r^(-1/c) is integrable in(3), because c>0.

If(D) holds, m is nonincreasing and cannot have a positive limiting value, since integral dr/r diverges. It is finite for all sufficiently large r by integrability; continuity of DU on compact sets then makes it finite for all positive r. Thus m(r)->0, so Sigma_I is empty by Section3.

## 5. A locally self-similar physical field

Suppose instead that formula(1) is only assumed for |x|<rho and T-t<tau0, with the same globally defined C1 profile U. It is enough that Du be locally bounded up to T near every point of one sphere |x|=b, where0<b<rho. Compactness gives a uniform M and terminal interval there. Given large y, take

    s=c^(-1)log(|y|/b), x=e^(-sA)y.

Then |x|=b and the formula applies. Hence |DU(y)|<=M b^(1/c)|y|^(-1/c), giving(D) as before. No claim about a global physical symmetry outside the ball is used. An annulus containing this sphere is more than sufficient. This proves the local formulation at explicit domains without importing an unchecked literature definition of local self-similarity.

## 6. The meaning and limit of the Dini implication

For rho>0, a change of variables using(4) gives the extended-real identity

    integral_(T-1)^T sup_(|x|>=rho)|Du(x,t)| dt
       =c^(-1) integral_rho^infinity m(r) dr/r.           (6)

Indeed dt=e^(-s)ds, the factor e^s in(4) cancels it, and r=rho e^(cs). Thus(D) is a time-integrated gradient bound outside every fixed ball. If(D) fails, Sigma_L must be nonempty by Section4 and therefore contains a whole twisted ray. This is a conditional implication, not an exclusion of such rays for Euler.

The strictness of the gradient-power condition relative to(D) can be seen kinematically. Fix0<p<(1-c)/c and define the smooth divergence-free field

    U(y)=(1+|y|^2)^(-(p+1)/2) J y.

Its divergence is zero because Jy is orthogonal to y. It tends to0 and satisfies |DU(y)|=O(|y|^(-p-1)), so(D) holds. On the rotation axis DU=(1+|y|^2)^(-(p+1)/2)J; after(4), at a fixed nonzero axis point its norm grows like e^((1-c(p+1))s), which diverges. Thus Sigma_L is nonempty. This field is not asserted to solve Euler. The example separates the raw scaling hypotheses and does not construct an Euler profile satisfying one but not the other.

For a nontrivial decaying smooth Euler profile, spatially isolated gradient blowup at T would therefore imply(D). The remaining question is whether decay alone prohibits these ray-shaped sets of local gradient unboundedness. Nothing in this theorem answers it. Existing far-field theorems remain conditional on their full original hypotheses. No computation is needed.

Review record: the exact statements and all proofs were independently checked. The full A15 review is pinned in verification; it found no mathematical error and its scaling and local-domain checks were verified here. The later C35 and C36 additions to the source dictionary are separate claims and are not imported by A475. No computation was used.
