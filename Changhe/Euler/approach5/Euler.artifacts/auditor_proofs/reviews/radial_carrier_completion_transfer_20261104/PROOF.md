# Negative scalar completions of the original radial carrier families

Status: exact application of confirmed LIT309 to the original integrating-factor and Volterra radial carriers.

## 1. Statement and hypotheses

Fix 0<c<1/2 and finite real omega. Put Jx=e3 cross x, X=(cI-omega J)x, L=(1-c)I+omega J and b=2(1-c). Let sigma be the smooth transverse section through a nonzero point used in the confirmed C69, C71 or C72 construction. On a smaller finite flowbox, let V be that constructed carrier, so div V=0, X.V=0, DV X=-LV, and V is smooth, flat exactly on the central orbit Gamma and nonzero elsewhere.

For the original integrating-factor C69 and C71 construction retain its parameter hypothesis omega=0 or c=1/3. For the Volterra constructions, including C72 and the all-omega C69 extension, every finite omega is allowed. The radial factor f is the positive smooth flat factor used in the relevant construction.

None of these fields has a smooth scalar S on a neighbourhood of the central point satisfying all of

    X.grad S=-bS, W.grad S=0, W=curl V,
    P2=S+|V|^2/2, -Delta P2=tr((DV)^2),
    S=0 on Gamma, S<0 off Gamma.

No flatness assumption on S is needed. This is only an obstruction for the displayed scalar sign and zero set. The proof invokes the confirmed local theorem A2607-A2610 after checking its exact normalized one-form hypotheses.

## 2. Original integrating-factor fields

Use the checked section notation: beta_i=X.sigma_i/|X|^2, gQ_ij=sigma_i.sigma_j-|X|^2 beta_i beta_j, and j=|det(sigma_1,sigma_2,X)|. The matrix gQ is smooth positive definite and j is smooth positive after fixing orientation. The original construction is

    jv=exp(tau) f(r) e_theta,
    V(sigma)=sigma_i v_i-(beta.v)X,

where tau is smooth and d tau=(3c-1)beta. Its existence is part of the original parameter restriction: for omega=0, beta=d(log|sigma|)/c, and for c=1/3 the right side is zero.

Pulling back V.dx gives gQ v. Therefore

    sigma^*(V.dx)=f zeta_i dy_i,
    zeta=M(y)e_theta, M=exp(tau)gQ/j.

On a compact smaller disc M is smooth positive definite. If m is a positive lower eigenvalue bound, then zeta.e_theta>=m, |zeta|<=C and |D zeta|<=C+C/r. Also |V(sigma)| is bounded above and below by positive constants times f, by the invertibility of the section representation. The accumulated derivative integral is at most K0+K1 log(R/r). All LIT309 hypotheses hold. Its conclusion proves Section 1 for the original C69 and C71 fields, including omega=0, c!=1/3.

## 3. Volterra fields for every omega

Here the checked construction has v=(f e_theta+q e_r)/j. Its estimates are

    |q|<=C r f, |D(q e_r)|<=C f,
    r f'/f=Lambda(log(1/r)),
    Lambda(t)<=C(1+t).

The original logarithmic factor has Lambda(t)=log t+1 and also satisfies this last bound. With M=gQ/j the normalized form is zeta=M[e_theta+(q/f)e_r]. The perturbation has size at most Cr. Thus, after shrinking, zeta.e_theta>=m/2 and |zeta| is bounded. The same representation gives |V(sigma)| comparable to f.

The derivative of the normalized correction obeys

    |D[(q/f)e_r]|<=|D(q e_r)|/f+|q| f'/f^2
                       <=C[1+Lambda(log(1/r))].

It follows that |D zeta|<=C/r+C[1+log(1/r)]. The second term is integrable on (0,R), and the first has logarithmic accumulated integral. These are precisely the LIT309 assumptions. The flatness and isolated orbit were already established in the construction proofs. This proves the stated noncompletion for every finite omega in the Volterra families, for every envelope allowed by C72.

## 4. Dependencies, comparison and limits

The complete 23:50 Theory Agent C application note was read and its formulas rederived above. The relevant integrating-factor section of the confirmed independent C69 proof, the radial correction and factor sections of the confirmed C71/C72 proof, and the full eleven-item coordinator LIT309 comparison were reread. The latter independently checks normalization of the large radial derivative and its consistency with the section curl ratios. These are existing configured model agent comparisons through files; actual provider execution is independently unattested.

The argument extends the earlier radial-family completion obstruction to the original integrating-factor fields without using a trace sign. It does not change the original parameter restriction of the integrating-factor construction itself. General nonradial carriers, other scalar signs or zero sets, actual tails without these section forms and unrestricted rotating-profile nonexistence remain outside this result. No computation or formal build was performed.
