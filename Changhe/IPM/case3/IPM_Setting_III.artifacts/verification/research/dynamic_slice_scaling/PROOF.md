# The fixed positive axis ratio is a spatial gauge slice

Status: exact conditional scaling statement. Dependencies: the canonical spatial scaling and the proved axis asymptotic K/a>0 for an admissible primary profile, recorded in SPEC.md and the earlier verifier scaling audit. This result does not prove profile existence or slope positivity.

Let an admissible profile have ell>1, nonzero slope a, and nonzero axis coefficient K of the same sign as a. Set delta=1-1/ell>0. Under the allowed spatial scaling rho_lambda(X)=lambda*rho(X/lambda), its slope stays a and its axis coefficient becomes lambda^delta K. Hence K_lambda/a=lambda^delta K/a. For every prescribed q>0, the unique choice lambda=(q*a/K)^(1/delta)>0 attains K_lambda/a=q. This preserves ell, the PDE, symmetry, smoothness, sublinear growth, and the canonical inverse by the already verified scaling law.

In particular, the frozen positive ratio K/a=1/2 of the constant-start DR evolution is not an extra restriction on spatial scaling orbits of primary profiles with the stated axis asymptotic. It is a choice of representative. It must not be counted as a second invariant parameter condition in an existence obstruction. This does not claim that the DR trajectory reaches every profile on that slice.

More explicitly, suppose a_star>0 and rho_star is any profile at ell=C. First scale it spatially to K_star/a_star=1/2. Let q=1/a_star and set rho=q*rho_star. Its DR slope is1 and axis coefficient1/2. Its strain is q(1-C), so variantA gives cw=q and cx=Cq. Linearity of the inverse then proves cw*rho-(cx*X+U[rho]).grad rho=0. Thus every positive-slope profile at C has a stationary DR representative with exactly the two constant-start normalizations. This is a correspondence of stationary fields; no basin-of-attraction or convergence claim follows.

The positivity qualification matters for conversion to slope1 with cw>0. This argument makes no assertion about negative-slope profiles or whether they are already excluded by a separate theorem. It also depends on the nonzero same-sign axis asymptotic, rather than silently discarding a hypothetical profile for which that premise had not been established.
