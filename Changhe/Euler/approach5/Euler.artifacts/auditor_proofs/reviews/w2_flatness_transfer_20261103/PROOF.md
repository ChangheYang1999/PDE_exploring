# Vorticity size flatness transferred to a scattering orbit

## 1. Exact statement and assumptions

Let B=Ax+U be the complete carrier of a smooth profile, with A=cI-omega J, c>0 and div U=0. Let z(t)=Phi_t z0 be an escaping lower-window trace of a flat periodic witness, at the exact scope of the confirmed W2.13 result A889-A890. In particular

    D^j Omega(z(t))=0 for every integer j>=0 and every real t,
    Omega=curl U,

and z(t) approaches a compact periodic orbit backward and escapes to infinity forward. Assume on a neighborhood of z0 the confirmed scattering relations

    Xi(Phi_t y)=exp(tA)Xi(y),
    Xi is C^1, DXi(y)=lim_(t->infinity) exp(-tA)DPhi_t(y),
    W(Xi y)=DXi(y)Omega(y), Xi(z0)!=0.

The natural profile class used in B57 supplies these relations by the previously verified C^1 scattering theorem. Then det DXi=1, Xi is a local C^1 diffeomorphism, and for each integer N>=1 there is a neighborhood of x0=Xi(z0) and C_N<infinity such that

    |W(x)|<=C_N dist(x, Z)^N,
    Z={exp(tA)x0: t in R}.

The same conclusion holds near every point of Z, with constants depending on the point or a fixed compact orbit segment. This is a size-flatness assertion; it does not assert that W is smooth on a neighborhood.

## 2. Determinant and local inverse

Liouville's determinant identity follows by differentiating det DPhi_t and using div B=tr A=3c:

    det DPhi_t(y)=exp(3ct).

Since det exp(-tA)=exp(-3ct), the matrix exp(-tA)DPhi_t(y) has determinant1 for every t. The assumed derivative limit and continuity of the determinant give det DXi(y)=1. The C^1 inverse function theorem gives local inverse charts. On smaller compact charts both DXi and D(Xi inverse) are bounded, and both maps are Lipschitz.

No global inverse theorem is needed for this local transfer. The full natural-class scattering theorem supplies a global inverse as well, but that stronger fact is not being inferred from determinant1 alone.

## 3. Why nearest points may be chosen locally

The source invokes Taylor's formula at a nearest trace point. Its local justification is as follows. The image orbit Z has radius |exp(tA)x0|=exp(ct)|x0|, strictly increasing in t. Thus it is a smooth embedded curve, and outside a fixed small parameter interval about0 it remains a positive distance from x0. On a sufficiently small ball about x0, a nearest point of Z lies on the corresponding compact local arc and is attained there.

For the original trace, the backward limit periodic orbit is disjoint from z0, and the forward trace escapes. On the remaining compact parameter intervals, injectivity of a nonperiodic orbit separates z0 from the complement of a small local arc. Since B(z0) maps under DXi to Ax0!=0, the local trace is a regular embedded curve. It has a smaller tubular neighborhood whose relevant nearest points lie on a fixed compact local arc. This supplies the uniform local derivative bounds required below. No assertion that the entire original trace is closed in R^3 is used.

## 4. Uniform Taylor estimates and the distance bound

Fix N. Choose nested small compact neighborhoods of the local original trace arc, with all straight segments used below staying in the larger one. Smoothness bounds D^N Omega there by a finite constant. Taylor's integral formula about any point q on the compact arc, together with vanishing of every lower jet there, gives

    |Omega(y)|<=C_N |y-q|^N.

Minimizing over its nearest local point proves the source estimate |Omega(y)|<=C_N dist(y,z(R))^N near z0.

Alternatively, for the desired image estimate choose directly a nearest q_x in Z to x. By Section3 both x and q_x lie in the same smaller inverse chart. Put y=Xi^(-1)x and q=Xi^(-1)q_x. Then q lies on the original trace and

    |y-q|<=Lip(Xi^(-1))|x-q_x|.

The push-forward gives

    |W(x)|<=sup|DXi| |Omega(y)|
           <=sup|DXi| C_N Lip(Xi^(-1))^N dist(x,Z)^N.

This proves the exact assertion. Applying the same argument at z(t0) proves it at any other image point. Finite covers give uniform constants on a fixed compact orbit segment when needed.

## 5. What flatness has and has not transferred

The argument preserves arbitrary size orders using only a C^1 change of variables and a bounded multiplier. It does not differentiate that multiplier beyond order0. Therefore it proves neither higher differentiability of W nearby nor classical neighborhood derivative bounds. If W is independently known smooth, its jets at the orbit points vanish; without that extra regularity the size statement is the correct conclusion.

Nor does it make V flat. Curl can vanish to every size order while the velocity retains a nonzero harmonic derivative. Thus it is compatible with the transverse nonflat W2 geometry in A1254-A1259, and it supplies no exclusion of that supported configuration.

In the globally smooth, helicity-free, decaying original class, the earlier global theorem A309 already excludes nonzero profiles. B57 is a valid geometric transfer consequence and does not enlarge that global nonexistence class. The transfer lemma itself is useful whenever its separately stated smooth-flatness and scattering hypotheses are available.

## 6. Verification

The complete B57 paragraph, its claim entry and the W2.13 dependency proof were read. The latter is already confirmed A889-A890: differentiating the Cauchy law after lower jets vanish gives a linear law for the next jet, and exponential approach to the flat periodic orbit defeats every finite derivative growth rate. The new determinant, local inverse, nearest-point justification and uniform Taylor transfer have been proved above. No computation or formal build was used. The immutable source excerpt and capture hash are retained in the team records.
