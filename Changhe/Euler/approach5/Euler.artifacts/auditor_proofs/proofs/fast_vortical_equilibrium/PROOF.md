# Exact affine profiles with arbitrarily fast vortical equilibrium growth

## Statement and scope

For every 0<c<1/2, every real omega and every L>0 there is an entire polynomial divergence-free solution of the rotating profile equation with a vortical carrier equilibrium at zero whose largest backward Lyapunov exponent exceeds max(L,2(1-2c)). The velocity has linear growth and no backward absorbing ball. It is neither sublinear nor decaying and is not helicity-free. Thus the result tests proposed local identities only; it does not refute an estimate using the global hypotheses of A399.

Write Jy=(-y2,y1,0), A=cI-omega J, B=Ay+U, W=curl U, a=1-2c and kappa=1+c. All solutions below are C-infinity on R3. No external theorem or numerical calculation is needed.

## Exact solution and pressure

For real s and nonzero q put

    N = [[s,-q,0],[q,-1-s,0],[0,0,1]],
    D=s(s+1)-q^2,
    U(y)=Ny,
    P(y)=-D(y1^2+y2^2)/2-omega(1+2s)y1 y2-y3^2.

The trace of N is zero. Direct multiplication gives

    (1-c)U+(B.grad)U+omega JU
       =[N+N^2+omega(JN-NJ)]y,
    N+N^2=diag(D,D,2),
    JN-NJ=[[0,1+2s,0],[1+2s,0,0],[0,0,0]].

The last two matrices are symmetric and their sum has negative gradient exactly grad P. This verifies the full momentum equation, including pressure, for every c and omega. Also

    W=2q e3,
    DB=[[c+s,omega-q,0],[q-omega,c-1-s,0],[0,0,kappa]].

Thus B(0)=0, W(0)!=0, DB W=kappa W and [B,W]=-kappa W.

## Backward spectrum

Let R>0 satisfy R^2=(s+1/2)^2-(q-omega)^2. The horizontal block of -DB has trace a and eigenvalues a/2+R and a/2-R; its third eigenvalue is -kappa. Since Psi_t is a linear flow with derivative exp(-t DB), the Lyapunov exponents at delta_0 equal these eigenvalues.

Choose q=1,

    R>max(a/2,L-a/2,3a/2),
    s=-1/2+sqrt(R^2+(1-omega)^2).

This realizes the chosen R, gives one positive and two negative eigenvalues, and makes the largest exponent a/2+R exceed both L and 2a. The invariant full-flow-ergodic measure delta_0 has entropy zero. Its basin is the stable plane: a nonzero unstable component grows exponentially and eventually leaves each compact set, whereas points in the stable plane tend to zero. Thus the basin has spatial measure zero. No SRB conclusion is made.

## Limitations of the countertest

A positive backward eigenvalue gives escaping backward trajectories and excludes any ball absorbing all bounded sets. Therefore this example does not have the compact core required by A398-A399. It only shows that the complete local Euler equation and all its differentiated identities cannot by themselves bound the exponent of a vortical equilibrium by 2a: every jet of this exact polynomial solution satisfies those identities.

Moreover

    U.W=2q y3,        W.grad(U.W)=4q^2=|W|^2.

The example is not locally helicity-free. Its velocity is unbounded and not o(|y|), has infinite energy, and its pressure is quadratic. Its vortex flow is translation by 2qt e3 and is nonrecurrent, consistently with the failed sublinearity premise of the vortex recurrence theorem. This supplies no gluing to a decaying exterior and no target counterexample. A theorem excluding only positive-entropy measures on the zero stratum cannot exclude this entropy-zero local test.

## Verification

Every asserted identity was independently multiplied and differentiated above. The source snapshot and hash are retained in verification. No computation was needed. The connection with finite-regularity coverage is only the previously conditional A400 criterion; this proof does not promote that criterion.
