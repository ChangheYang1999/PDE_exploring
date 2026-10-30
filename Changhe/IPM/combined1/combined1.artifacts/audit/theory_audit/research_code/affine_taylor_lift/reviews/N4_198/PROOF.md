# Independent audit of the affine Taylor lift at candidate007

## Statement and scope

Fix the exact rational c of candidate007, so c>1, and put p=(3+1/c)/2.
Let chi be its even Cartesian potential, rho=-partial_y Delta chi,
u=(-chi_xyy,chi_xxy), F=(cX+u).grad rho-rho and a=rho_y(0).
Let C extract the coefficients of x^2,y^2,x^4,x^2y^2,y^4 from F/y.
The already audited candidate satisfies chi_xxyy(0)=1-c and
(a-4c+2)(a-8c+4)!=0. All jets below are ordinary Cartesian Taylor
polynomials; no floating fit is involved.

For the ordered pairs (2,1),(0,3),(3,1),(1,3),(0,4), put

e_ij=x^(2i)y^(2j)(1+r^2)^(p-i-j-2).

Let eta=alpha e_21+beta e_03+g e_31+d e_13+e e_04 be the unique
nonlinear repair already proved and independently computed in
../taylor_repair_audit/PROOF.md, so C(chi+eta)=0. Define K=60(a-8c+4)
and

    u0=-192 alpha^2/K,
    v0=18 alpha beta/c,
    w0=(a-4)v0/112,
    tau=u0 e_31+v0 e_13+w0 e_04, z=eta+tau.

Then C(chi)+DC(chi)[z]=0, but generally
C(chi+z)=(0,0,-192 alpha^2,-8640 alpha beta,0).
Within the five-dimensional correction space z is the unique affine
feasible step. Both eta and z preserve a, the strain, and the leading
and first-descendant tail moments of every affected branch. They belong
to the frozen007 span. This statement concerns that exact c and chart;
it is not a claim of membership at a different exponent.

## Proof

The potential degree-six part of eta is alpha x^4y^2+beta y^6.
Its density is -24alpha x^2y-120beta y^3 and its velocity is
(-8alpha x^3,24alpha x^2y). Their transport product is
-192alpha^2 x^4y-8640alpha beta x^2y^3. Any product involving a
potential term of degree eight or above has degree at least seven
in F. Thus it does not enter C. The exact quadratic expansion of F
and C(chi+eta)=0 imply

    C(chi)+DC(chi)[eta]=(0,0,192alpha^2,8640alpha beta,0).

For a homogeneous degree-eight potential M, the leading variation is

    ((2c-1)x partial_x+y partial_y-1)(-partial_y Delta M)
         +a M_xxy.

The linear fields used here are rho=ay+O(r^3),
u=((c-1)x,(1-c)y)+O(r^3), forced by the audited strain identity.
Substitution of M=x^6y^2,x^2y^6,y^8 gives, in the last three rows,

    [K  0          0]
    [0 -480c       0]
    [0 12(a-4) -1344].

Multiplication by (u0,v0,w0) cancels the displayed affine defect.
The five-by-five differential has block lower triangular form with
diagonal 24(a-4c+2),-240,K,-480c,-1344, all nonzero. This proves
uniqueness. Since tau begins at degree eight, the quadratic transport
of z is the same as that of eta through degree five, proving the
remaining nonlinear defect. The corrections begin at degree six,
so neither origin quantity changes.

For tail preservation, decompose each even monomial into the finite
homogeneous harmonics. In block(0,m), e_ij gives a constant multiple
of t^(i+j-m)(1-t)^2. Both its value and first derivative vanish at
t=1. The independently confirmed finite membership table in
../constraint_rank/verification/candidate007.json places all of these
polynomials in the frozen007 basis. Linear combinations preserve those
identities, which are checked again for tau and z.

Let B_ij=||-partial_y Delta e_ij||2. The independently computed exact
positive rational values of B_ij^2/pi from the nonlinear-repair audit
are inputs. They follow from direct Leibniz differentiation and exact
whole-plane beta moments, with all endpoint hypotheses already checked.
The triangle inequality proves

    ||rho[tau]||2 <= |u0|B_31+|v0|B_13+|w0|B_04,
    ||rho[z]||2 <= sum_ij |coefficient_ij(z)|B_ij.

Outward square roots and rational threshold comparisons certify these
upper bounds. They concern perturbation size, not residual smallness.

## Independent verification

Reconstruct chi and each correction from the canonical source with
ordinary Cartesian jets. Compute DC independently as both the analytic
linearized field and the exact centered difference of the quadratic
residual. Verify the five equations, the exact quadratic defect, the
origin invariants, the full canonical correction map and both tail
moments. Compare the exact parameters and correction coordinates to the
frozen T4-251 record. Use only own code for computation; foreign code
is retained for inspection and source binding. No snapshot is modified.
The general real-c theorem awaits its separate Opus review. This audit
is an independent arithmetic and hypothesis check at candidate007.
