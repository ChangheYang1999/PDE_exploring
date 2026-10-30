# Audit of the sharpened weighted weak test

The analytic proposition T2-W4 is CONFIRMED. Its candidate-specific arithmetic still needs an independent field reconstruction. The published scalar decimal fields are not all downward bounds of their own displayed component formula.

## Statement, hypotheses and proof

Let w=(1+|X|^2)^(-a/2), 0<a<2, and let rho+h solve the fixed-c stationary equation. Assume all hypotheses of the audited T4-081 weak identity, including the canonical divergence-free velocity, its cutoff admissibility conditions and ||w U[h]||_2<=C_U||wh||_2. Put m=||wh||_2. For a real polynomial P set t=r^2/(1+r^2), W=1-t and phi=y W^2 P(t). Define

    I=integral F phi,
    M=(2c+1)phi+V.grad phi,
    D=||M/w||_2+C_U||phi |grad rho|/w||_2,
    H=sup |grad phi|/w^2.

Then |I|<=Dm+C_U Hm^2. For nonzero I this yields

    m >= 2|I|/[D+sqrt(D^2+4 C_U H |I|)].

For the zero probe or vanishing numerator, use the trivial lower bound zero rather than evaluate 0/0.

Indeed divergence-free integration by parts gives

    I=integral h M - integral phi U[h].grad rho
                         +integral h U[h].grad phi.

Weighted Cauchy-Schwarz bounds these terms by m||M/w||, C_U m||phi |grad rho|/w||, and C_U Hm^2 respectively. The audited cutoff argument applies because every fixed polynomial P gives phi=O(r^-3), grad phi=O(r^-4), with smooth behavior at zero. Solving the increasing quadratic yields the claim. This is a necessary correction-size test, not an existence result.

## Exact polar formulas

For phi=rW^2P(t)sin(theta), define T P=(1-4t)P+2t(1-t)P'. Its radial and angular gradient components are W^2 T P sin(theta) and W^2 P cos(theta). Therefore

    H=sup_(0<=t<=1) W^(2-a) max(|P|,|T P|).

The angular maximization is exact. With rho=r sum W^a_j R_(j,n)(t)sin(n theta), its gradient is the sum of W^a_j T_(a_j,1)R sin(n theta) and W^a_j n R cos(n theta). The angular products needed for phi^2|grad rho|^2 are

    integral sin^2(theta)sin(n theta)sin(m theta)
       =pi/4(2[n=m]-[|n-m|=2]+[n+m=2]),
    integral sin^2(theta)cos(n theta)cos(m theta)
       =pi/4(2[n=m]-[|n-m|=2]-[n+m=2]).

These follow directly from product-to-sum and trigonometric orthogonality. The radial Jacobian is r dr=dt/(2W^2), so the full gradient norm squared has radial factor t W^(1-a+a_i+a_j)/2 times P^2 and these angular coefficients. The transport norm is obtained by collecting all sine modes of (2c+1)phi+V.grad phi before squaring. This retains all cross terms and removes the earlier triangle bound. Expanding the resulting rational polynomials gives beta moments. These are the formulas in the frozen T2 note and script.

Choosing P by floating-point optimization is harmless only after freezing exact rational coefficients and reevaluating the full expression rigorously. No claim that the chosen P globally maximizes the test follows.

## Decimal output audit

The frozen script uses m.lower().str(12,radius=False). The conversion to a limited decimal string is not a directed floor. Reconstructing the quadratic formula at 512 bits from each row's certified component balls shows that 20 of the 34 stored m_lower decimal values exceed the upper endpoint of that formula's enclosure. Fourteen are below its lower endpoint.

For example, the d2, a=1, k=288 row stores 0.0142312059075, while its component formula is enclosed near 0.01423120590745775517679. The Markdown table calls 0.014231206 a rounded-down lower bound, but this is larger still. The span Mpen2, a=1 row has formula near 0.04395530670478614688602 and prints 0.043955307 in the table.

This disproves the assertion that these outputs are downward-rounded versions of the certified formula. It does not prove that the true optimal correction distance is below those decimals; it means those decimals lack the claimed justification. Retain the full ball or explicitly floor a chosen decimal grid below its lower endpoint. The rounding error is tiny and changes no present closure row, but printed strict lower bounds require correction.

The reconstruction is not an independent PDE-field evaluation. All new candidate-specific values remain OPEN pending that second path. The exact polynomial coefficient vectors are frozen in the source JSON for the next audit stage.

## Independent general-polynomial reconstruction

For the independent arithmetic path, construct the density and stream function from the canonical potential coefficients by the separate T4 polar loader. Write rho=r sum W^a_j R_(j,n) sin(n theta) and psi=r^2 sum W^a_j S_(j,m) sin(m theta). Put Q=(1-4t)P+2t(1-t)P' and A=(2c+1)P+cQ. The sine-mode coefficients of M/(rW^2) are A in mode1, together with W^a_j (T_j S P - m S Q)/2 in mode m+1 and W^a_j (T_j S P + m S Q)/2 in mode m-1, where T_j S=(2-2a_j t)S+2t(1-t)S'. Squaring the combined coefficients before integration gives the transport norm, including every radial and angular cross term.

The weak pairing is -pi/2 times the sum over density mode1 of integral t W^(a_j-1) R A, plus pi/4 times the sum over |n-m|=1 of integral t W^(a_i+a_j-1) R[sign(n-m)m S Q-(T_j S)P]. The density-gradient term uses the two exact angular products stated above and the radial factor t W^(1-a+a_i+a_j)P^2/8 times pi. All integrals extend over0<t<1. Exact rational polynomial construction followed by Arb evaluation in the variable W supplies a second arithmetic path.

The polynomial gradient supremum is independently bounded by adaptive rational interval subdivision. On each t interval, a Bernstein enclosure of P and Q is multiplied by the maximum of W^(2-a). Subdivide until a chosen rational H target is certified on every interval. The target may exceed the peer upper bound; it still gives a valid independent correction-distance lower bound. This check does not presume the peer grid or its chosen optimum.

## Independently reproduced candidate005 span

At 2026-10-29T02:36:49.127840+00:00, the direct polynomial reconstruction at2048bits reproduced the peer's pairing, combined transport norm M, and angular gradient norm C: all three enclosures overlap. The independently subdivided supremum uses H<=1999843/100000000 with 34 accepted cells. The resulting necessary bound is

    ||(1+r^2)^(-3/5) h||_2 > 6091157959/250000000000

for the fixed-c correction class of T2-W4. This is approximately0.024364631836. The weaker safe decimal0.02436463 is therefore independently certified. The test is normalized by the exact frozen rational coefficient vector; it does not prove global optimality of that vector. Runtime was99.978011 real seconds. Output SHA256 3704c54dae47583889ae23f95454805b1ccd96138e81cccf5f5098ff81890924.
