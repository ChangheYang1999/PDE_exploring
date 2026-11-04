# Critical nonrotating Bernoulli criterion at C1 regularity

## Statement and scope

Let V be a C1 vector field on R3 with constant divergence kappa>0, complete flow Phi, and the following uniform backward confinement: for every compact D, the union of Phi_-t(D), t>=0, is bounded. If V cross curl V=0 everywhere, then curl V=0.

Consequently, let U,P be C1 on R3 and solve the nonrotating Euler profile equation with c=1/2, div U=0, and U=o(|y|) uniformly at infinity. Put

    V=y/2+U,
    H=|V|^2/2+P-|y|^2/8.

If H is constant, then U is constant. It is sufficient that H tends to one finite constant at infinity, or that H-h_infinity belongs to Lp(R3) for some 0<p<infinity. Under U tending to zero, U=0.

These are exactly the conditional critical results of Liu, Section 9, in the retained manuscript in the team records. They do not assert a general critical Liouville theorem, nor a theorem for nonzero rotation.

## 1. A scalar tail lemma

Suppose a measurable finite-almost-everywhere scalar f obeys

    f(Phi_-t x)=exp(kappa t)f(x)

outside an invariant null set, and for every bounded ball B,

    lim_{lambda->infinity} lambda |{x in B: |f(x)|>lambda}|=0.

Fix a compact ball D and delta>0. The backward image of E={x in D: |f(x)|>delta}, after deletion of the null set, lies in one fixed bounded ball B and in the superlevel at delta exp(kappa t). Its volume is exp(-kappa t)|E|. Therefore

    delta |E| <= lambda |{x in B: |f(x)|>lambda}|,
    lambda=delta exp(kappa t).

The right side tends to zero. Exhausting space and positive thresholds proves f=0 almost everywhere. Boundedness of the local weak-L1 tail alone would not suffice: V=(kappa x1,0,0), f=1/x1 off x1=0 has the exact transport and a nonzero bounded weak tail.

## 2. Aligned curl vanishes at zeros of the carrier

Write Omega=curl V and Z={V=0}. Suppose Omega_j(p)!=0 at some p in Z. Near p, alignment gives V=g Omega, with continuous g=V_j/Omega_j. Since V_j(p)=0 and Omega_j(p)!=0,

    g(p+h)=ell dot h+o(|h|),
    ell=grad V_j(p)/Omega_j(p).

Hence DV(p)=Omega(p) tensor ell. Taking its curl gives Omega(p)=ell cross Omega(p), whose scalar product with Omega(p) is impossible unless Omega(p)=0. This contradiction proves Omega=0 on Z without differentiating Omega.

## 3. The vanishing weak tail near zeros

Off Z put f=(Omega dot V)/|V|^2, so Omega=fV, and set f=0 on Z. At each p in Z, positive trace DV(p)=kappa guarantees one component V_i has a nonzero differential. Use s=V_i as a C1 coordinate in a product chart x=chi(s,z). The local zero set Z lies in s=0 and is null. A countable chart cover makes all of Z null.

On the entire local hyperplane s=0, Omega_i=0: at a point outside Z use Omega=fV, and at a point of Z use Section 2. On a compact coordinate box continuity yields a uniform modulus eta(r)->0 such that

    |Omega_i(chi(s,z))|<=eta(|s|),
    |f(chi(s,z))|<=eta(|s|)/|s|  for s!=0.

Given epsilon>0, choose rho with eta(r)<=epsilon for r<=rho. On the portion |s|>=rho the scalar is bounded. Thus, for sufficiently large lambda, its lambda-superlevel is contained, apart from the null hyperplane, in |s|<epsilon/lambda. Bounded coordinate Jacobians imply limsup lambda times this superlevel volume is at most C epsilon. Sending epsilon to zero proves the local vanishing weak tail. Finite charts cover the zeros in any fixed compact ball; f is bounded on the remaining compact part. This proves the tail hypothesis globally on bounded balls.

## 4. The scalar transport law at C1 regularity

On R3 minus Z, f is continuous and div(fV)=div Omega=0 in distributions. In a C1 flow box x=chi(t,z), its Jacobian is J(t,z)=exp(kappa t)J(0,z). Changing variables in the weak divergence identity gives

    partial_t(f(chi(t,z))J(t,z))=0

as a distribution. The continuous representative is independent of t, so f(Phi_t x)=exp(-kappa t)f(x). A nonstationary trajectory cannot reach Z in finite time by uniqueness of the C1 flow. Finitely many flow boxes cover every compact orbit segment. The transport therefore holds for every finite t off the invariant null set Z.

Section 1 forces f=0 almost everywhere. Hence Omega=0 almost everywhere, and continuity makes it zero everywhere.

## 5. Euler consequence and its exact limitation

At c=1/2 and omega=0, the exact Bernoulli identity is grad H=V cross Omega. Constant H gives the alignment hypothesis. Sublinearity supplies completeness and the uniform backward confinement, while div V=3/2. Sections 1-4 imply curl U=0. Together with div U=0 and harmonic Liouville under sublinear growth this makes U constant.

In general at this critical c, V dot grad H=0. A finite limit H->h_infinity makes each strict superlevel above h_infinity and strict sublevel below it bounded. The Lp alternative makes these sets finite-measure instead. Each is invariant under Phi and its volume is multiplied by exp(3t/2), so it has zero measure. Since it is open it is empty. Thus H=h_infinity and the preceding argument applies.

For nonzero rotation the carrier curl is curl B=Omega-2 omega e3. Alignment with Omega is not alignment with curl B. Section 2 cannot be transferred without proving its zero-set conclusion separately. No behavior of H at infinity follows here from velocity sublinearity or decay alone.

## Verification

This is a direct reconstruction of the actual manuscript Lemmas 9.1-9.2, Remark 9.3, Theorem 9.4 and Corollary 9.5. No external Beltrami rigidity theorem or numerical computation is used. Pressure has no normalization or growth requirement in the constant-H case beyond the explicitly stated Bernoulli condition.

Audited: 2026-11-02T21:29:33Z
