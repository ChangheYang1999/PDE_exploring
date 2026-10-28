# The exact content of the archived finite-section columns

## Scope and sources

This topic audits the files `numerics/src/c2_fminus.py`, `c2_gram2.py`, `lin_assembly.py`, and `lin_fast.py` from the copied Analysis I artifacts, with the binary64 input `numerics/data/trial_v2_h0.008.npz` interpreted exactly. It does not certify a singular value. The background coefficient `Aout[259,0]` is unchanged by the exact scalar repair of proof 04, which modifies only `Aout[0,0]` and the matching outer correction.

## The tail direction is truncated

For an integer M>=3, let

    Theta_0(theta)=sum_(m=0)^(M-1) A_m cos(2m theta).

The elementary product identity `2 cos u cos v=cos(u+v)+cos(u-v)` gives

    Theta_0 cos(2theta)=sum_(m=0)^M B_m cos(2m theta),
    B_0=A_1/2,
    B_1=A_0+A_2/2,
    B_m=(A_(m-1)+A_(m+1))/2, 2<=m<=M-2,
    B_(M-1)=A_(M-2)/2,
    B_M=A_(M-1)/2.                                      (1)

The archived code allocates a vector of length M+1, initially zero. It fills B_0, B_1 and B_m for 2<=m<M, but never fills B_M. It also assembles the TAU column only over m<M. Its Gram-side angular vector uses the same truncation. Therefore the stored TAU direction is internally the truncated one

    Theta_TAU=Theta_0 cos(2theta)-(A_(M-1)/2)cos(2M theta), (2)

apart from its separate radial rounding. The comment identifying it with the full product is false when A_(M-1) is nonzero.

For the prescribed input M=260 and

    A_259=-8059128652303703/10384593717069655257060992658440192.

Thus the omitted coefficient is exactly

    B_260=-8059128652303703/20769187434139310514121985316880384.

It is about -3.8803292992852125e-19. Smallness does not make (1) an identity for the stored vector. Formula (2), on the other hand, is an exact and usable angular definition. Multiplication by x^2 y does not eliminate this difference on any open angular set. If the full product is intended in a new construction, mode 260 must be admitted in both the density and Green representation, and every resulting output mode must be included or enclosed.

## The actual linearization contains the normalization term

The header of `c2_fminus.py` calls the operator unnormalized. Its imported class is `FastAssembler`, a subclass of `LinAssembler` which overrides Green integration but not `column`. The inherited `column` computes `ch=c_of(m,basis)` and adds `(ch/3) Rt` to the output, where Rt is the background's derivative with respect to log radius. Since Rt=X dot grad rho, this is exactly the normalization term `(c[h]/3) X dot grad rho` from proof 01.

The actual archived matrix therefore includes that term. The word "unnormalized" is an inaccurate description of the operator it assembles. This audit does not establish that its rounded background is exactly normalized, or that the sampled matrix is a continuum realization. Those are different questions.

## Radial measure and omitted tails

Write u=r/L and

    m(r)=u^3(1+u^2)^((k-3)/2).

The intended H1m column norm is the spatial integral with weight

    w_X(r)=m(r)^(-2)(1+u^2)^(-3/2).

By proof 12 its exact log-radius Gram density is `e^(8t) w_X(e^t)` multiplying the value and derivative angular matrices. The H1q output rows approximate instead a log-radius integral with squared weight

    w_Y(t)^2=(1+u)/m(e^t)^2.

These are different continuum measures. The row expression lacks the spatial Jacobian and the column's outer factor. A theorem may deliberately use different X and Y, but cannot identify this row norm with the H1m spatial norm without a comparison with explicit hypotheses. The finite-difference derivative is a further approximation which needs its own error bound.

The archived Gram quadrature integrates over finite log-radius endpoints generated from `tmin-25` to `t0+45` and the finite piece endpoints. Several columns have genuine inner or outer half-line pieces. The omitted half-line contributions are not zero. For example the J reference equals x^2 y all the way to the origin, so its positive Gram density has a strictly positive integral below tmin-25. Likewise a nonzero pure outer tail has a positive Gram density above t0+45. Agreement of 24- and 48-point finite-interval quadratures does not bound either omitted tail. A new certificate must integrate these half-lines analytically or enclose them explicitly.

## What is and is not refuted

The full-product description of TAU and the word "unnormalized" are refuted for these archived files. Their actual truncated angular definition and normalized coupling can be recovered exactly as above. The tail omission and sampled row measure prevent treating the reported floating singular values as rigorous continuum singular values by themselves. They do not imply that every such singular value is numerically inaccurate, and do not refute a newly defined exactly conforming section with certified half-line integrals.
