# The integer scalar target does not match a higher fractional remainder target

## Statement

Let V be the actual normalized modal transport field, let d(t)=V_2(0,e^t)/e^t, and put q(t,theta)=V(X).X/r^2. For a radial cofactor beta, E beta=x^2 y beta(log r), the transport splitting is

 (V.grad-1)E beta=E(A beta)+Err beta,
 Err beta=x^2 y[(q-d) beta'+b_0(t,theta) beta],             (1)

where b_0 is the fixed smooth coefficient on any open annulus avoiding modal knots. Let B_6={beta in B:A beta in H_g^6}, with its graph norm. Let Y_H be any remainder target whose norm controls ordinary local H^(25/4) on a fixed open patch where q-d is nonzero. Then the block

 X beta=Err beta+C_R E beta

does not map B_6 boundedly into Y_H. In particular choosing Gamma_H=H_g^6 solely because of the integer compactness theorem does not satisfy J1 for such a remainder target.

This is a failure of this particular mismatch of orders. It is not a counterexample to the abstract block continuation theorem or to a compatible choice such as Gamma_H of order25/4.

## An actual patch with a nonzero derivative coefficient

Near the origin the verified expansion is V=(-A x,D y)+O(r^3), with A=2ell-1, D=4ell-1 and Sigma=A+D>0. Thus

 q-d=-Sigma cos(theta)^2+O(r^2).                          (2)

Choose a closed angular interval strictly between the two axes, as close to the vertical axis as needed to lie in its high-order region. Its cos(theta)^2 has a positive lower bound. A sufficiently small fixed annulus, below the first modal knot, makes q-d bounded away from zero on this patch. All background coefficients there are analytic. The test functions below have compact support in that annulus, so endpoint weights cause no issue.

## Oscillatory sequence

Choose a nonzero smooth compactly supported radial cutoff chi(t) in that annulus and set

 beta_n(t)=n^(-7) chi(t) cos(nt).                          (3)

The scalar first-order expression A beta_n has H_g^6 norm bounded uniformly in n, and its low B norm is bounded. Hence ||beta_n||_(B_6)<=C. On the chosen patch the leading part of Err beta_n is

 -n^(-6) x^2 y(q-d)chi(t) sin(nt).                        (4)

Its local H^(25/4) norm is bounded below by c n^(1/4) for large n. One way to verify the estimate is to pass to the smooth coordinates (t,theta), localize further inside the patch, and use the Fourier identity for a compact amplitude times exp(int): after translating the Fourier variable by n, the H^s norm divided by n^s tends to the amplitude's L2 norm. The two real oscillatory branches separate in frequency. The remaining transport term in (1) has local H^(25/4) norm O(n^(-3/4)).

The coupling cannot cancel (4). On this fixed patch the canonical velocity is an operator of order zero. More directly, the global unweighted H^s norm of E beta_n, whose support is in a fixed physical annulus, is O(n^(s-7)); the Riesz multipliers have absolute value at most1, so the same bound holds for U[E beta_n]. Multiplication by a smooth background gradient and localization preserves this bound. The strain coefficient c[E beta_n] is an integral against a smooth compactly supported radial amplitude and therefore decreases faster than every inverse power of n by repeated integration by parts. Finally the subtracted axis row has the exact moment formulas of proof 110: its local H^s norm is no larger than O(n^(s-7)), and in fact has an extra derivative gain. Its lift is smooth in theta and has the same bound. For s=25/4 all these contributions are O(n^(-3/4)).

The remainder norm thus grows at least as c n^(1/4), while the B_6 norm stays bounded. This proves the assertion.

## General order rule and scope

The same construction with amplitude n^(-(N+1)) proves the general rule: B_N supplies at most order N for a nonzero first-derivative jet lift. A target that demands local order s>N cannot satisfy J1 on that scalar domain. This does not preclude an order-s scalar target, an appropriately weighted stronger scalar domain, or a weaker remainder target. Their remaining coefficient and endpoint mapping conditions must still be checked.
