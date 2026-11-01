# Necessary potential logarithms at the first period

Status: PROVED in V533 after exact polar/Cartesian agreement and the independent18:35Z review. Both periods have admitted convergent branches.

## Statement

Let Q be7 or8, delta=2/Q, c=Q/(Q-2), and let b be any real root of the irreducible degree2Q compatibility polynomial from253 or256. Set f_1=epsilon(sin(theta)+b sin(3theta)), with real epsilon nonzero, and take its uniquely tuned pure density and stream series whenever the hypotheses of131 hold. Write a_Q(b) for the sin(theta) coefficient of f_Q at unit amplitude.

If a_Q is a nonzero rational polynomial of degree at mostQ, then the common potential necessarily has a nonzero correction at orderQ of the form

    epsilon^Q r^2 log(r) [alpha_Q(b)+beta_Q(b)cos(2theta)].

At least one of alpha_Q and beta_Q is nonzero. No pure homogeneous potential coefficient at that order generates the required density. This assertion concerns the power and logarithmic expansion of132, with finite cosine coefficients and its usual gauges. It does not restrict more general representations of the same smooth exterior function.

## Density range at potential degree two

At n=Q the density exponent is-1 and the potential exponent is2. For an even cosine potential coefficient C=sum c_m cos(2m theta), direct differentiation gives

    -partial_y Delta [r^2 c_m cos(2m theta)]
      =4m(1-m^2)c_m r^-1
          [sin((2m+1)theta)+sin((2m-1)theta)].

The terms m=0 and m=1 vanish. Every m>=2 contributes only odd frequencies at least3. Consequently every pure degree-two cosine potential has zero sin(theta) density coefficient. A nonzero a_Q is therefore an obstruction to such a pure potential, independently of the free coefficient at order2Q or any later tuning choice.

The full logarithmic range follows from the exact identities

    -partial_y Delta(r^2 log r) = -4r^-1 sin(theta),
    -partial_y Delta(r^2 log r cos(2theta))
        =4r^-1[sin(theta)+sin(3theta)],
    partial_x partial_y(r^2 log r) = sin(2theta),
    partial_x partial_y(r^2 log r cos(2theta))
        =-sin(4theta)/2.

Eliminate every density frequency at least5 by descending through the pure columns m>=2. Let the residual be a_Q sin(theta)+d_Q sin(3theta). Then

    alpha_Q=(d_Q-a_Q)/4,   beta_Q=d_Q/4.

These are rational polynomials of degree at mostQ in b. They supply exactly the missing density. The stream agrees as well: both reconstructed and prescribed streams satisfy the same pure Poisson equation at P_Q=0, whose kernel on the even positive sine frequencies is trivial. Pure potential gauges at m=0,1 change neither density nor stream. The difference beta_Q-alpha_Q=a_Q/4 proves that the logarithmic correction cannot vanish when a_Q!=0.

## Nonvanishing at every compatibility root

The finite nonresonant density recurrence gives a_Q in Q[b] with degree at mostQ. If it is not the zero polynomial, it cannot vanish at a root of the irreducible compatibility polynomial of degree2Q. Otherwise that degree2Q minimal polynomial would divide a_Q, contradicting its smaller degree. Thus one exact nonzero coefficient of a_Q and the already certified irreducibility suffice for every real compatibility root. No rounded root substitution is used in this proof.

Homogeneity multiplies all order-Q coefficients by epsilon^Q. Since epsilon!=0, it preserves nonvanishing. The density and stream stay pure; the logarithm is confined to their common potential. The reconstruction and geometric bounds132 show that this finite correction does not change any sufficient exterior radius established in253 or256.

## Independent arithmetic protocol

Generate f_n and g_n through n=Q by a positive-frequency polar sine recurrence, with signed folding of both product frequencies. Compare every coefficient with the separately generated exact Cartesian prefix. Extract a_Q and check that it is nonzero and has degree at mostQ. Form the descending pure potential, compute alpha_Q and beta_Q, and verify its density and stream using the Cartesian derivative operators and the four logarithmic identities. Retain exact rational polynomials and all source hashes. The Q8 irreducibility and convergence inputs are admitted in V530 and V531.

Dependencies:01,121,131,132,253,256. The obstruction to a pure potential follows from the finite order alone; convergence is used only to identify an actual exterior solution carrying that logarithm.

## Completed independent verification

The positive-frequency polar recurrence agrees exactly with all112 retained coefficients at Q7 and144 at Q8. The a_Q polynomials have degrees7 and8. Their leading coefficients independently agree with the theory part calculation. Both are coprime to the irreducible compatibility polynomials. The descending pure potential plus the two logarithmic terms reproduces every prescribed density and stream coefficient exactly. The combined arithmetic took1.77seconds. All20 branches in253 and256 therefore require a nonzero first-period common-potential logarithm. No nonvanishing assertion about the second permitted logarithmic order follows from this check.
