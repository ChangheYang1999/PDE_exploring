# Classification of zeroth-order formal Lyapunov functions

## Exact theorem

Let V be a connected open subset of R^3, c and omega real, c!=1/2, and
Psi in C^1(V x R^3 x R). For y in V let a pointwise jet be u in R^3,
M a trace-free real 3 by 3 matrix, and p in R, with

    b=cy-omega Jy+u,
    g=-(1-c)u-Mb-omega Ju.

Suppose, for every such jet,

    Psi_y.b+Psi_u.(Mb)+Psi_p(g.b) <= 0.

If omega=0, then and only then Psi=f(H), where

    H=p+|cy+u|^2/2+c(c-1)|y|^2/2,
    f in C^1(R), (1-2c)f' >= 0.

If omega!=0, Psi is constant. In particular f'>=0 in the target range
0<c<1/2. The extension with f'>=0 for c>1/2 is false.

## Proof

After substituting g, the coefficient of M is
(Psi_u-Psi_p b).Mb. Since M is arbitrary in the trace-free subspace and may be
multiplied by any real scalar, this coefficient vanishes. For b!=0 the only
vector v for which v b^T is orthogonal to every trace-free matrix is v=0:
such a matrix must be a scalar multiple of I, while v b^T has rank at most one.
Continuity extends Psi_u=Psi_p b across b=0.

For fixed y set s=p+|b|^2/2. The map
G(y,u,s)=Psi(y,u,s-|b|^2/2) is C^1 and has G_u=0, so G=F(y,s).
Writing

    H_omega=p+|cy+u|^2/2+c(c-1)|y|^2/2-omega Jy.u,
    s=H_omega-c(c-1)|y|^2/2+omega^2r^2/2,

gives Psi=f(y,H_omega) with f C^1. Put a=1-2c, X=cy+u, w=omega Jy.
The pointwise Bernoulli calculation reduces the inequality to

    -a f_h |X|^2+(f_y+a f_h w).X-f_y.w <= 0

for every X in R^3 and every h in R. Therefore A=a f_h>=0. If A=0,
variation of X forces f_y=0. If A>0, the maximum over X equals

    |f_y-Aw|^2/(4A),

so f_y=A w. In all cases

    f_y=a omega f_h Jy,   a f_h>=0.

For omega=0, f_y=0. A connected open set is path connected, so f depends only
on h, giving the stated classification and sign. Conversely the derivative
is -a f'|X|^2, which is nonpositive.

For omega!=0 put k=a omega, which is nonzero. The last identity says that f
is constant along the C^infinity vector fields

    Y1=d_y1+k y2 d_h, Y2=d_y2-k y1 d_h, Y3=d_y3.

A small rectangular composition of the Y1 and Y2 flows, staying inside V,
returns y to itself and translates h by a nonzero multiple of its area.
Interchanging the order gives the opposite sign. Since f is constant along
each constituent flow, it is invariant under all sufficiently small positive
and negative h-translations. Thus f_h=0; the identity gives f_y=0, and
connectedness gives constancy. This flow argument only needs f C^1, not
second derivatives or a formal commutator applied to f.

## Counterexample to the overextended sign and limits of the theorem

For c>1/2, omega=0, Psi=-H has derivative (1-2c)|X|^2<=0 and f'=-1. Thus the
submission's phrase 'any c!=1/2 works' is correct only with the amended sign.
No actual global solution need realize each test jet: this is intentionally a
formal, pointwise algebraic theorem with arbitrary admissible first jets.
It does not exclude higher-derivative, nonlocal, or solution-specific Lyapunov
functions. In particular it does not prove the target Liouville conjecture.

Dependency: the directly checked rotating Bernoulli identity. No pressure
normalization, decay, completeness, source theorem or numerical computation
enters this proof.

Audit recorded: 2026-11-02T18:42:51Z
