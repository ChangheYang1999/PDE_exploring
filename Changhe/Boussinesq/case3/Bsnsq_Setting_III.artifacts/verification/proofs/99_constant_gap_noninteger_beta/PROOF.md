# A missing fractional exponent forces C=0 for noninteger beta>2

Written UTC: 2026-10-21T01:03:46.299360+00:00. Restricted asymptotic theorem, not a full B2 exclusion.

## Exact statement

Let beta>2 be noninteger, N=floor(beta), s=1/beta. Let Omega,Theta be smooth full-plane fields with the prompt's x-reflection parities. Let V be the canonical relative whole-plane inverse of Omega, V(0)=0. Suppose the vorticity profile equation
(beta X+V).grad Omega+Omega=Theta_x
holds, and suppose the following spatially differentiated expansions hold uniformly in angle:

Omega(r,theta)=sum_(k=1)^(N+1) r^(-ks) a_k(theta)+O_C1(r^(-(N+2)s)),
Theta(r,theta)=sum_(j=0)^(N-1) r^(1-(j+2)s) f_j(theta)+O_C1(r^(1-(N+2)s)).

Here O_C1(r^p) means a value bounded by Mr^p and Cartesian gradient bounded by Mr^(p-1). The angular coefficients are smooth, and a_1 is not identically zero. No temperature transport equation or sign condition is needed for this conditional statement.

For k=1,...,N, let u_(k-1) be the canonical homogeneous velocity of r^(-ks)a_k(theta) on all r>0, with no cutoff. Then
V=sum_(k=1)^N u_(k-1)+C+O(r^(1-(N+1)s)),
and necessarily C=0. Reflection already makes C horizontal component zero. Thus a nonzero source constant after subtraction of N homogeneous terms rules out an exact profile having these particular expansions.

## Inverse expansion

Each ks lies in (0,1), so the homogeneous stream degree2-ks lies strictly between1 and2. The angular Poisson equation is invertible on smooth periodic coefficients: its degree is noninteger and its Fourier eigenvalues do not vanish. The resulting velocity has degree1-ks, vanishes at0, and is the canonical homogeneous inverse. The parity is inherited.

Set eta=Omega-sum_(k=1)^N r^(-ks)a_k. At infinity eta=O(r^(-d)) with d=(N+1)s in (1,2). At0 its homogeneous subtractions have powers strictly less than1. Its ordinary velocity U_eta exists absolutely, including at0. At large |X|=r, split the integral into |Y|<r/2, |Y-X|<r/2 and the remaining region; further split the latter at |Y|=2r. Bounds |K|<=C/|X-Y| and |eta(Y)|<=C|Y|^(-d) at large radii give U_eta(X)=O(r^(1-d)): the core mass contributes r^(-1)*O(r^(2-d)), the near-X kernel is locally integrable, and the far tail gives int_r^infinity rho^(-d)d rho. A fixed neighborhood of0 contributes O(1/r), which is smaller. These estimates are uniform in angle. To justify the identity, let H=sum u_(k-1)+U_eta. Each homogeneous stream has degree greater than1, so its distributional Laplacian has no point mass at0; its velocity is continuous there. The eta inverse is continuous at0 because its local singular exponent is less than1. In distributions div H=0 and curl H=-Omega, with the kernel convention of packet03. Hence H-V is harmonic on the entire plane, including0, by distributional elliptic regularity. H is sublinear by the displayed homogeneous degrees and the estimate for U_eta; V is sublinear by packet03 applied to the smooth Omega=O(r^-s). The harmonic gradient estimate on expanding disks makes H-V constant. Evaluating at0, where every homogeneous velocity vanishes, proves
V=sum u_(k-1)+U_eta-U_eta(0), C=-U_eta(0),
with the asserted remainder. The ordinary center velocity has horizontal component zero by x-reflection.

## The vorticity residual at the missing power

For brevity write A_k(X)=r^(-ks)a_k(theta). The linear transport beta X.grad A_k+A_k and Theta_x have only integer-multiple powers r^(-ls) through l=N+1. Every product u_(j-1).grad A_k has degree -(j+k)s, again an integer multiple, since u_(j-1) has degree1-js. Terms with j+k>=N+2 are O(r^(-(N+2)s)). The inverse remainder times grad Omega is also O(r^(-(N+2)s)); the differentiated source remainders have the same or smaller size in the residual. The contribution of C is
C.grad A_1 + O(r^(-1-2s)).
Both error exponents (N+2)s and1+2s exceed1+s. Consequently the exact vorticity residual admits
0=sum_(l=1)^(N+1) r^(-ls) P_l(theta)+C.grad A_1+o(r^(-1-s)).
All displayed integer powers precede the C term, since N+1<beta+1<N+2. Successively multiply by r^s,r^(2s),... and take r->infinity to obtain P_l=0. Multiplying what remains by r^(1+s) gives C.grad A_1=0 on every ray, hence on the punctured plane by homogeneity.

If C=(0,C_2) with C_2 nonzero, then partial_y A_1=0. On each half-plane x>0 or x<0 it is a function of x alone. Homogeneity gives A_1=c_+ x^(-s) on x>0 and c_- |x|^(-s) on x<0. Smoothness across the points (0,1) and (0,-1), which belong to the punctured plane, forces c_+=c_-=0. This contradicts a_1 nonzero. Therefore C=0.

## Dependencies and scope

The inverse convention and sublinear uniqueness are packet03's. Packet98 is a separate application for computing serialized first-mode constants, not a dependency of this proof. The argument extends packet90's missing-exponent mechanism to all noninteger beta>2 under the explicitly stated differentiated expansions. These expansions exclude the additional C-dependent fractional terms of a general profile. The theorem therefore does not exclude the broad prompt class. At integer beta the missing power joins the integer ladder and this proof gives no C obstruction; logarithmic compatibility must be analyzed separately. Finite angular support is not assumed. No numerical evidence is a proof of existence or of full nonexistence.

## Audit amendment 2026-10-21T01:06:19.303827+00:00
Actual Claude Opus5.5 review119 correctly requested the distributional uniqueness justification, now supplied above. Its suggested parity correction is false: an odd source has an odd canonical stream, so U=(-Psi_y,Psi_x) has odd horizontal and even vertical components, as follows directly from packet03. The existing parity conclusion is retained. A direction-free alternative also proves the final step: C.grad A_1=0 with C nonzero forces A_1=c_±|Cperp.X|^-s on the two half-planes, contradicting continuity across the line parallel to C. No broader asymptotic class is excluded.
