# Independent checks of the four fixed-c_l trials

Date: 2026-10-20. Status: exact center exclusions for the specified interpolants, and independently recomputed numerical residuals. No assertion about a family of exact profiles follows.

## Data and interpretation

The four files in the numerics lane are fixclS_n120m48_d0.001.npz, fixclS_n120m48_d-0.001.npz, fixclSA_n120m48_d0.01.npz and fixclSA_n120m48_d-0.01.npz. Their parameters differ from c_l=5.574692542183549 by the indicated amounts. Each has N=120, M=48, L=8 and angular warp beta=0.9. Hashes, complete parameters and all observations are in verification/summary.json.

For statements about exact interpolants, the nodal numbers and parameters are their exact saved binary values. Radial nodes are the ideal Chebyshev-Lobatto nodes and angular nodes the ideal Gauss nodes, with the mathematical reciprocal k=1/c_l. The smooth first row is exactly one. The density is

    rho=x^2 y (1+r^2/L^2)^((k-3)/2) b(q,s),
    q=1-(1+r^2/L^2)^(-(1-k)/2),
    theta=s+(beta/2)sin(2s).

Here b is the tensor interpolant, a polynomial of degree120 in2q-1 and a cosine polynomial of degree47 in2s. At every fixed nonzero point it is smooth. The identity b(0,s)=1 makes rho/(x^2 y) continuous and equal to one at the center. It does not imply smoothness of this quotient there.

The evaluator uses independently reconstructed coefficients, logarithmic radial quadrature and polar principal-value subtraction for the canonical full-plane inverse, and eighth-order Cartesian finite differences for density and velocity derivatives. It does not execute the numerics lane's inverse, orbit integration or differentiation code. The inverse was checked against manufactured fields as documented in ../inverse/PROOF.md.

## Exact center obstruction

For any strong profile rho=x^2 y a with a smooth near zero,

    G_5(x)=partial_y^5 rho(x,0)/120
          =x^2 partial_y^4 a(x,0)/24

must tend to zero as x tends to zero. Differentiating the finite angular expansion and the radial expansion of the saved interpolant gives an explicit finite expression for this limit. The independently implemented ball calculation in ../center-regularity/code/axis_jet_balls.py bounds it away from zero for all four trials. The values are approximately256.0344,275.7834,116.5867,387.9119, in the above order. Thus none of these exact saved interpolants belongs to the strong class.

There is a separate transport obstruction, not just a representation problem. Write the degree-five angular density coefficient as P_5(theta)=sum p_m sin(m theta). In particular p_7,p_9,p_11 are finite expressions in the nodal values. For a velocity of class C^3 with the required parities, its linear part is(-cx,cy); its cubic part times grad(x^2 y) contributes only polynomial harmonics of degree at most5. The degree-five coefficient of harmonic m>=7 in the transport residual is therefore

    Q_m=(5c_l-1)p_m+(c/2)[(m-7)p_(m-2)-(m+7)p_(m+2)].

This follows by applying(-cx,cy).grad to r^5 P_5 and using sine product formulas. For m=7 and9, Q_7=Q_9=0 would imply

    p_7^2+7p_9^2-8p_7p_11=0,

provided c_l>1 and p_7!=0. Indeed Q_7=(5c_l-1)p_7-7cp_9, Q_9=(5c_l-1)p_9+c(p_7-8p_11); elimination gives(5c_l-1) times this determinant. If p_9=0 then Q_7 is already nonzero, so division by p_9 is unnecessary. The ball intervals exclude zero for this determinant in every file. Consequently none can solve exact transport with a C^3 velocity for any choice of the central strain c. With the prescribed identity c=3c_l-1, Q_7 itself is nonzero in every file. This argument is proved in full in ../center-regularity/PROOF.md and applied here to exact binary data.

The same nonzero p_7 also forces a resonant streamfunction term3p_7 x^5 log|x| in the x-axis velocity after taking the derivative. Thus a high-order polynomial fit of the axis cannot be used as an exact smooth-center certificate. The coefficient3p_7, the determinant and both Q tests are saved as enclosing ball intervals.

## Canonical inverse, parity, gauge and exterior tail

Evenness in x and oddness in y hold exactly by the formula and its reflection convention. They imply U_1 odd in x and even in y, U_2 even in x and odd in y, hence U(0)=0 exactly. Numerical parity tests at40 generic positive-quadrant points and their reflections give zero discrepancy to machine precision. The strain is independently evaluated by

    c=int_0^infinity rho_3(r) r^(-2) dr,

where rho_3 is the physical sin(3theta) coefficient. Adding a harmonic streamfunction term lambda xy would change c and U by lambda(-x,y), but is excluded by the canonical sublinear velocity law. No such adjustment is used in any residual evaluation.

The saved values obey max|b_nodes|<27. The coefficient bound proved in ../exterior-tail/PROOF.md gives, uniformly for these files, |rho(X)|<=2087424 |X|^(1/5) at sufficiently large radius. The reciprocal k is strictly between0 and1/5. At the inverse outer radius R=10^30, the same proved exterior expansion bounds the omitted velocity by5.21856e-13 for observers |X|<=10^5 and the omitted central strain by5.21856e-18. These bounds use exact rational arithmetic on the saved parameters. They bound the omitted exterior; they do not certify the interior floating-point quadrature.

## Numerical checks and their limits

The transport residual is R=(c_l X+U).grad rho-rho. In this topic's summary, the report notation is

    N_f=|rho|+|W_1 rho_x|+|W_2 rho_y|,
    N_v=|rho|+|X.grad rho|+|U.grad rho|.

The raw inverse JSON files use the historical reversed labels R_Nv and R_Nf respectively; the summary explicitly converts them. Comparisons in this proof use the report notation.

The two main points are X_1=(10cos(1),10sin(1)) and X_2=(10cos(1.55),10sin(1.55)). The canonical inverse is evaluated with1024,2048 and4096 angles, radial Gauss order24, panel size0.1 and outer radius10^30. At4096 angles, |R|/N_f at(X_1,X_2) is

    delta c_l=+0.001: (0.003514297294,0.002755305736),
    delta c_l=-0.001: (0.003723266472,0.002850471413),
    delta c_l=+0.010: (0.002535507673,0.003333454252),
    delta c_l=-0.010: (0.004591650899,0.002551250359).

The2048-to4096 change is below1.3e-9 at X_1 and7e-13 at X_2. These defects are therefore well resolved relative to their size. The seven-point2048 run also samples the center region, two points next to the first axis source and two far-field points. This sampling is not a supremum bound or a full-domain grid study.

For E=-partial_x U_2+partial_y U_1-rho_x, the2048-angle calculation with eighth-order step sizes0.005,0.0025,0.00125 stabilizes at about1e-6 in |E|/|rho_x| next to the source. Doubling the angular quadrature at step0.0025 reduces these values below3e-7. The stable differentiation sweep alone was therefore not an estimate of total inverse error. Both contributions are recorded separately. By definition the exact canonical inverse has E=0; these numerical E values check the independently implemented inverse and differentiation.

The central identity defects3c_l-1-c lie between-7.4e-7 and+4.91e-7. Small scalar defects and small E do not repair the transport residual or the exact center incompatibility. These four parameter trials cannot serve as YES_inf evidence, cannot establish a continuum family, and supply no nonexistence theorem for other profiles. They show that the tested fixed-c_l solves remain inadequate under a separately implemented physical evaluator.

Dependencies: elementary finite interpolation, the center expansion and elimination in ../center-regularity/PROOF.md, the canonical inverse and manufactured tests in ../inverse/PROOF.md, and the exact exterior expansion in ../exterior-tail/PROOF.md. No formal build was performed.


## Additional96x40 fixed-parameter trials

The same independent method is applied to the four exact files listed in verification96/inputs.json: stageA at +0.001, stageA at -0.001, the subsequent stageB at -0.001, and stageA at -0.01. The artifacts are frozen separately in data96/. The +0.01 log exists but no corresponding saved density was available at this audit's start; no numerical conclusion is inferred for that missing state. Distinguishing the two negative0.001 stages is essential because their auxiliary parameter and physical shape drift even with c_l fixed.

The analytic center tests, canonical strain formula, harmonic-gauge restriction and parity proof above apply unchanged to these finite representations. The rigorous envelope uses their own N=96,M=40 and exact maximum nodal value through the coefficient-norm bound in ../exterior-tail/PROOF.md, not the earlier120-grid constant. The new observer radius10^5 safely contains all evaluation points. Independent2048/4096 real-space velocity checks, two near-source elliptic tests, strain integration and256-bit center-ball expressions are performed on each frozen state. The summary must report actual outcomes and does not assume the120-grid values carry over. The orbit residual logs are not independently verified by this procedure.
