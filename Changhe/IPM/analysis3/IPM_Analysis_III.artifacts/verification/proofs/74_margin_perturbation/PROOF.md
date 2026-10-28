# Quantitative stability of the anisotropic energy margin

## Exact setting and result

Let a>0 and let mu be a locally absolutely continuous function on R
with bounded derivative. Put

 w(X)=|cos(theta)|^(-2a)exp(mu(log|X|)).

Let V and W be globally Lipschitz vector fields on R2 with the IPM
parities: component1 is odd in x and even in y, component2 is even
in x and odd in y. Assume W(0)=0 and div W=2c/3 almost everywhere,
where c is a real constant. Set L=||DW||_L-infinity, using the Euclidean
operator norm. Let rho and h have bounded gradients. Define

 kappa_w(V)=1+(div V)/2+(V.grad log w)/2,
 bplus(rho)=(|grad rho|-partial_y rho)/2,
 m(V,rho)=essinf(kappa_w(V)-bplus(rho)).

Then

 ||kappa_w(V+W)-kappa_w(V)||_infinity
 <=|c|/3+(||mu'||_infinity/2+2a)L,                      (1)

 ||bplus(rho+h)-bplus(rho)||_infinity<=||grad h||_infinity,

 m(V+W,rho+h)>=m(V,rho)-|c|/3
                -(||mu'||_infinity/2+2a)L-||grad h||_infinity. (2)

All identities and bounds are almost everywhere; the axes have zero
Lebesgue measure and the weighted estimates use the same values away
from them. The angular quotients have bounded extensions where needed.
For a=17/4 and the piecewise radial derivative -17/2,-5/4, the exact
coefficient of L in (1) is51/4=12.75.

## Proof of the angular estimate

The Lipschitz condition and W(0)=0 give |W(X)|<=L|X|, hence

 |W_r/r|=|W.X|/r^2<=L.

Parity gives W1(0,y)=0 and W2(x,0)=0. Integrating each component on
its coordinate segment yields

 |W1(x,y)/x|<=L,   |W2(x,y)/y|<=L.

For x!=0 and r!=0, direct Cartesian computation gives

 tan(theta) W_theta/r
 =-y^2 W1/(xr^2)+y W2/r^2
 =(y^2/r^2)(-W1/x+W2/y).

Its absolute value is at most2L. Since

 (W.grad log w)/2=(mu'/2)W_r/r+a tan(theta)W_theta/r,

and div W/2=c/3, (1) follows. No derivative of mu' is required, so its
jump at t=0 causes no extra term.

For any g,z in R2, the triangle inequality gives

 | (|g+z|-(g_y+z_y))/2-(|g|-g_y)/2 |
 <=(|z|+|z_y|)/2<=|z|.

This proves the bplus bound and then (2) by taking essential infima.
The gradient term in (2) cannot simply be omitted: the Lipschitz
velocity norm and the density-gradient norm are different quantities.

## IPM application and explicit sufficient radius

For W=W[h]=U[h]+c[h]X/3, incompressibility of U gives div W=2c[h]/3.
The verified high spaces of topics63 and71 have the required parity,
W(0)=0, bounded DW and bounded grad h. If the constants satisfy

 |c[h]|<=C_c||h||_H,  ||DW[h]||_infinity<=C_W||h||_H,
 ||grad h||_infinity<=C_g||h||_H,

then a sufficient condition to retain half the margin m0>0 is

 ||h||_H<=m0/[2(C_c/3+(51/4)C_W+C_g)].

This is conditional on specified constants and a proved m0. It is not
a numerical radius until these quantities are enclosed. For a moving
tail, replace h here by the full background change; the same formula
then includes its gradient and induced field. A bound for only the
remainder h does not automatically include the tail change.

The positive-axis coefficient also obeys

 |(V2+W2)(0,y)/y-V2(0,y)/y|<=L.

Thus d>=d0>0 remains positive when L<d0. This alone proves neither the
endpoint asymptotics in(A) nor invertibility of a perturbed operator;
those are separate hypotheses. In particular it does not identify
maximal graph domains, which can change as shown in proof 73.
