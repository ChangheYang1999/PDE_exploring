# The residual jet dependency is larger than the P/R value-model audit

This note is part of the conditional hypothesis list. The source
cert_resid.py1911be775730931d0753099ec74272a08cb10945f33d2183fe37c9d08f2e6053
constructs the five radial residual jets at lines393-475, with nder=4.
They contain523 angular sine coefficients each, of radial degree12:
65 models across13 parents,441935 coefficient boxes and33995 scalar
remainders. Topic118 saved a contemporary replay of these objects and
checked its angular reductions. It did not certify these objects as
physical derivatives of the residual.

The source constructs exponential-polynomial density derivatives Rd
through order5, ODE derivatives A,B through order4, and velocity-derived
Pt,Qt through order4. It combines them in the exact intended identity

 d_t^i eps = c_l d_t^(i+1) rho - d_t^i rho
   + sum_{l=0}^i binom(i,l) [Pt^(l) * rho_t^(i-l)
                            + Qt^(l) * rho_theta^(i-l)],

where each product includes the angular sine/cosine product identity and
the scalar factors embodied in Pt,Qt. The source implements these through
conv_scatter, not by differentiating a previously bounded residual
remainder. A separate verification must identify those coefficient
conventions, derivatives, products, remainders and scalar point inputs
with the physical residual.

Topic101's stated full finite result concerns function-value Taylor
models for the P and R solutions of its ODE system. It does not certify
all five jets of the nonlinear residual. Therefore completion of
98,99,101 would not alone establish H1 or the radial part of H2.
The additional residual-jet construction, followed by full angular
assembly, Cartesian conversion, recentering, cutoff composition and
Bernstein suprema, remains required. A C0 Taylor remainder cannot be
differentiated to obtain any of these missing derivative enclosures.

The numbers441935 and33995 describe a potential finite audit of the
13 parent jets, not a completed audit and not proof that the new v2.2
historical run used the contemporary topic118 arrays. Only source and
saved-scalar linkage asserted elsewhere has been checked for v2.2.
