# Closure with a low semigroup that allows transient growth

## 1. Why a separate theorem is needed

The finite-rank proposal TM-17b correctly gives a conditional L2 inverse by removing a compact self-adjoint part and applying the stationary finite-rank lemma. It does not, by itself, justify replacing condition (B) in T4-019. Equation (7) of that proof is used twice: first to obtain the L2 inverse, and then directly in the high energy matrix in Section 3. The matrix includes the term 2 w2 ||h||2^2 from low dissipativity. An inverse inequality ||h||2<=K||A_k h||2 does not give that signed quadratic term.

This is a limitation of that proposed transfer, not a claim that a resolvent-based replacement is impossible. The theorem below supplies one precise replacement using a low semigroup bound that may have a prefactor greater than one. A stationary Woodbury certificate alone does not establish its new hypothesis. A dynamic finite-rank certificate could establish it, but none is supplied here.

## 2. Spaces and explicit hypotheses

All functions are real and S1, meaning even in x and odd in y. Let Rj have symbol i xi_j/|xi|, U[h]=(-R1R2 h,R1^2 h), J=(1-Delta)^(1/2), omega=(1+4r^2)^(2/5), and v=omega^2. Define

    E(h)^2=||omega D^2h||2^2+2^14||Dh||2^2+2^18||h||2^2,
    X_s(h)=E(J^s h).

The spaces are the completions of compact smooth S1 functions. All derivatives use ordered Cartesian Frobenius tensors. Thus X_s controls H^(2+s). Set

    s=2^-17, R=2^-14, eta=1/196608=R/12,
    c_s=(4 pi s(1+s))^(-1/2).

Let rho be a smooth S1 reference, u=U[rho] its canonical velocity, V=cX+u, and a0=rho_y(0)>0. Require the following hypotheses.

(A) Structure. 9/5<c<37/20, c+partial_y u2(0)=1, and u is smooth, divergence free and sublinear. The fields D rho, <r>D^2rho, <r>^2D^3rho, <r>^2D^4rho, Du, <r>D^2u, and <r>D^3u are bounded. For some gamma<1, |D^j rho|=O(r^(gamma-j)) for j=0,1,2 outside a ball. These assumptions give a complete globally Lipschitz background flow.

(C) Derivative energies. Define

    A=[[rho_y,-rho_x/2],[-rho_x/2,0]],
    M1=I-sym Du+A,
    M2=(1+c+V.grad log omega)I-2sym DV+A,
    S=(v_xy rho_x-v_xx rho_y-v_x rho_xy+v_y rho_xx)/2.

Require M1>=(9/10)I, M2>=(1/2)I, and

    (||D^2rho||infinity, ||omega D^2rho||infinity,
     ||omega D^3rho||infinity, ||omega D^2u||infinity,
     ||D(v D rho)/omega||infinity, ||S||infinity)
        <=(3,8,10,3,28,40).

(D) Fractional coefficient bounds. With each ordered component's supremum taken before summation,

    (|c|,||Du||S,||omega D^2u||S,||omega D^3u||S,
     ||D rho||S,||omega D^2rho||S,
     ||omega D^3rho||S,||omega D^4rho||S)
        <=(2,6,24,160,22,32,80,2048).

(L) Uniform low stability allowing transient growth. For every

    k in B={k in X_s: X_s(k)<=R, c[k]=partial_y U2[k](0)=0},

let A_k=V.grad-1+U[.].grad rho+U[k].grad have its maximal distributional L2 realization. Require the certified bound

    ||exp(t A_k)||L2->L2 <= 2 exp(-t),  for every t>=0.       (5)

The existence of this L2 semigroup follows from (A) and k in X_s by the complete Lipschitz flow and bounded perturbation. Its numerical bound (5) is an additional, unverified hypothesis. It replaces the signed condition c+1-theta-kappa>=2; that condition is not assumed here. The hypothesis must hold uniformly for rough k throughout the normalized ball, not just k=0 or a finite-dimensional truncation.

Let F=V.grad rho-rho. If F belongs to X_s and X_s(F)<=eta, then exactly one h in B solves the stationary equation F(rho+h;c)=0. Its origin slope is positive and its leading sublinear profile agrees with that of rho. The low-metric Picard contraction is less than 0.012467.

This is a new conditional theorem, CLAIMED pending independent review. No present candidate is asserted to satisfy (L) or the residual hypothesis.

## 3. The fractional L2 component needs no new semigroup hypothesis

For 0<s<=1, concavity gives t^s-1<=s(t-1) for t>=1. Also sqrt(1+|xi|^2)-1<=|xi|. Therefore, by Fourier multiplication and Plancherel,

    ||(J^s-I)h||2<=s||Dh||2,
    b_s:=||J^s h||2 <= b+s a,                              (6)

where b=||h||2 and a=||DJ^s h||2. The last inequality uses ||Dh||2<=a. This estimate transfers the low bound on the original function to the fractional component without assuming that J^s commutes with A_k.

## 4. Derivative estimates and a high semigroup

Put P=||omega D^2J^s h||2, a=||DJ^s h||2, b_s=||J^s h||2. For X_s(k)<=R define the fixed constants

    nu=R/sqrt(s),
    A_s=127/50+(653/5)s,  B_s=(9/5)(1+44s),
    m1=9/10-4290s-(13/10)nu,  q=6+1360s,
    alpha=m1-s q,
    m2=1/2-4708s-(A_s+B_s)nu,
    u1=347/5+5440s+B_s nu,  v1=10+34816s,
    k1=u1+s v1.

The exact derivative identities under (C), the first two component rows of the fractional commutator bound under (D), and the rough transport estimates give, on smooth orbits h'=A_k h,

    a' <= -m1 a+q b_s,
    (P^2)'/2 <= -m2 P^2+(u1 a+v1 b_s)P+40a^2.             (7)

The inequality for a can be interpreted as an upper Dini derivative at a=0. These are the same component estimates audited in T4-013 and T4-039. Specifically the smooth fractional rows are s(4708P+5440a+34816b_s)P and s(4290a+1360b_s)a. The rough rows cost at most nu[(A_s+B_s)P^2+B_s aP] and (13/10)nu a^2. None uses a low dissipative term or a negative norm.

Using (6), (7) becomes

    a' <= -alpha a+q b,
    (P^2)'/2 <= -m2 P^2+(k1 a+v1 b)P+40a^2.               (8)

The parameter certificate gives alpha>0.83849 and m2>0.36814. By (L), b(t)<=2e^-t b(0). Variation of constants in the first inequality proves exponential decay of a at every rate below min(alpha,1). For the second inequality, Young's inequality gives

    (P^2)' <= -m2 P^2+(2k1^2/m2+80)a^2
                                  +(2v1^2/m2)b^2.        (9)

Consequently P decays at every rate below min(m2/2,alpha,1), with a finite constant depending only on the displayed parameters. Equation (6) gives the same conclusion for b_s. Thus the high semigroup decays exponentially, with a possible prefactor. No assertion of high contractivity is made.

For completeness, the high realization can be constructed before assuming any decay. On the smooth core, the ordinary L2 energy is bounded above by a fixed constant times b_s^2, because D rho is bounded; (7) then bounds the derivative of E(J^s h)^2 by a constant times itself on any fixed X_s ball. Smooth approximations of k give high semigroups with this uniform finite-time bound. The complete-flow L2 construction gives convergence in C([0,T];L2), since U[k_m]-U[k_l] tends uniformly to zero and the uniform high bounds control Dh. Weak compactness, uniqueness of the low limit and lower semicontinuity give a high semigroup. Strong continuity follows from weak continuity and the finite-time upper norm bound at t=0. This is the construction used in T4-019, with a finite growth bound in place of the high decay estimate. For the resulting fixed-k semigroup, (L) and (8)-(9) then give the asserted high decay.

Its generator is the maximal distributional high realization: if h and A_k h lie in X_s, the maximal L2 identity S(t)h-h=integral_0^t S(v)A_kh dv has a strongly continuous X_s integrand, and division by t identifies the high generator derivative. The reverse inclusion follows from the low restriction. The exponentially convergent high semigroup integral now proves high bijectivity. The high and low inverses agree by low uniqueness. In particular ||A_k^-1||L2->L2<=2 follows from (5).

## 5. Quantitative stationary inverse

For f in X_s put

    f2=||omega D^2J^s f||2,
    f1=||DJ^s f||2,
    f0=||f||2.

Let h=A_k^-1 f. The just-proved high regularity permits the stationary energy inequalities. They give

    b<=2f0,
    a<=(f1+2q f0)/alpha=:G1,
    b_s<=2f0+sG1=:G0,
    m2 P^2<=(f2+k1 G1+2v1 f0)P+40G1^2.

For nonnegative P, B and C, mP^2<=BP+C implies P<=B/m+sqrt(C/m). Thus

    P <= (f2+k1 G1+2v1 f0)/m2+sqrt(40/m2)G1=:G2.           (10)

If X_s(f)<=epsilon, then f2<=epsilon, f1<=epsilon/128, and f0<=epsilon/512. Substitution into (10) gives

    X_s(h)<=sqrt(G2^2+2^14G1^2+2^18G0^2)
           <11.490384 epsilon<12epsilon.                  (11)

The constants are checked with outward Arb arithmetic; no sampled spectral information is used in this calculation. The low estimate (L) remains an explicit hypothesis.

## 6. Normalized nonlinear closure

For k in B let T(k)=-A_k^-1F. Equation (11) and X_s(F)<=R/12 give X_s(T(k))<R. The X_s embedding controls c[h], Dh and DU[h], with the latter two bounded by c_s X_s(h). The canonical contact formula is

    c[h]=-h_y(0)/4+(1/pi)PV integral sin(3theta)h(X)r^-3 dX.

For normalized k, the first-order origin identity for A_kh=f is f_y(0)=a0 c[h]. The actual residual has F_y(0)=0 by c+partial_yu2(0)=1. Therefore c[T(k)]=0. These identities use high regularity after inversion and do not impose a trace on arbitrary low inputs.

The ball B is complete in L2 by weak compactness in X_s, distributional uniqueness of the limit, lower semicontinuity and continuity of c on X_s. For k,l in B, maximal low domains and the product bound yield

    A_k(T(k)-T(l))=U[l-k].grad T(l),
    ||T(k)-T(l)||2<=2c_s R||k-l||2.

The certificate gives 2c_sR<0.012467<1, so the contraction theorem proves existence and uniqueness in B. Every stationary correction in B lies in the maximal domain and is a fixed point. Condition M1>=(9/10)I and normalization imply a0>7/10, while c_sR<0.006234, so the corrected origin slope stays positive. Fourier integrability implies h and Dh tend to zero at infinity, preserving a specified nonzero growing leading profile.

## 7. Interpretation and audit status

The source of the finite-rank proposal is frozen in source/T1_TRANSFER_MATRIX.md. Its stationary lemma is already independently audited in T4-039. This result checks the previously open high-low transfer and supplies a different sufficient hypothesis. It does not claim that finite-rank corrections cannot improve a high inverse, or that the top rate imposes a universal threshold. It also does not show that a candidate satisfying the principal energy obstruction fails (L): a semigroup may have transient growth and still satisfy (5).

The component estimates and domain construction are the audited ones in T4-013, T4-019 and T4-039. The new steps are (6), the stable triangular differential comparison, and its quantified stationary consequence. This proof and its scalar parameter certificate require independent review before the new framework can be registered as AUDITED. No candidate existence has been closed, and no formal proof-assistant run is supplied.
