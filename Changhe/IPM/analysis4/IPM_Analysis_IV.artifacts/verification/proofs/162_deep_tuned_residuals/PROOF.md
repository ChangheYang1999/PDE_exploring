# Direct residual certificates through truncation order 320

Status: CONFIRMED finite continuum certificates (V315). The infinite convergence theorem and its conservative radius are those of119 and126. This audit makes no smaller infinite-radius claim.

## Statement and hypotheses

Fix delta=2/3, c=3 and the smaller tuned algebraic root b of119. Use f1=sin(theta)+b sin(3 theta), with every resonant stream constant fixed by the next compatibility condition. The complete coefficient prefix through401 has been independently audited in141. For N in{40,80,160,320}, define rho_N and psi_N by truncating their pure radial series, and u_N=(-partial_y psi_N,partial_x psi_N).

At each fixed positive R in{1/5,1/4,1/2,1}, this audit encloses the full-circle uniform norms of the weighted stationary residual

    S_N(R,theta)=R^(-1/3)[(3X+u_N).grad rho_N-rho_N],

its first two angular derivatives, and the next density increment R^(-1/3)(rho_(N+1)-rho_N). At N=320 it also bounds R^(j-1/3) partial_R^j of the unweighted stationary residual for j=1,2. The claims are finite and refer to the exact algebraic profile enclosed by the retained coefficients.

## Independent polynomial construction

Put z=R^(-2/3), p_n=1-2n/3. Represent a sine polynomial by one half of its coefficients at positive signed Laurent frequencies and their negatives at the opposite frequencies. The Cartesian X and Y operators are those derived in01 and128. Let F_n and G_n be these Laurent representatives. The weighted residual is represented exactly by

    S_N = -2 sum_(n<=N) (n-1) z^(n-1) F_n
          +z [(sum z^(i-1) XG_i)(sum z^(j-1) YF_j)
               -(sum z^(i-1) YG_i)(sum z^(j-1) XF_j)].

This includes the linear and nonlinear parts before cancellation. It uses Cartesian derivatives and full polynomial products, independently of the numerical experiments' truncated angular convolution. No nonlinear term is omitted. The next increment is z^N F_(N+1).

For radial derivatives let E=z partial_z. Compute E and E^2 of this polynomial expression by assigning the integer factor(n-1)^k to each weighted summand and applying the product rule. Since the unweighted residual is R^(1/3) S_N,

    R^(2/3) partial_R residual = (1/3-2E/3) S_N,
    R^(5/3) partial_R^2 residual
        =[(1/3-2E/3)(-2/3-2E/3)] S_N.

These formulas involve no numerical differentiation.

## A continuum bound from interval samples

For a real trigonometric polynomial H with sine coefficients a_m, its kth angular derivative has second derivative bounded by sum_m |a_m| m^(k+2). On a uniform grid of spacing h=pi/M in[0,pi], linear interpolation has error at most h^2 ||H''||_infinity/8. This follows from the scalar interpolation remainder on each grid interval. The absolute value of a linear interpolant is bounded by the larger absolute endpoint value. Therefore the largest interval-sampled absolute upper bound plus that error bounds the continuum supremum. The largest sampled absolute lower bound bounds it from below. S1 parity supplies the same supremum on the full circle. All coefficients, samples and error estimates use outward-rounded complex or real ball arithmetic.

Finite strict decreases of the upper bound below the preceding lower bound certify decreases of the corresponding true norms. They do not control every subsequent truncation or prove a new infinite convergence radius. The source's binary64 grid estimates are compared separately and retain their empirical status.

## Evidence

The input is reconstructed from the frozen150-order base128 and151..401 extension141, with their recorded hashes. Their exact root containment, nonlinear recurrence and common-potential consistency are already independently checked. No new full checkpoint is needed. The evaluation report and its source program are retained read-only copies. Every numerical enclosure and actual elapsed time is recorded in verification.

## Completed finite certificates

All 72 strict decreases pass, for truncations 40, 80, 160, 320; radii
1/5, 1/4, 1/2, 1; the residual and next density increment; and angular
derivatives of orders zero, one and two. At each comparison the later
certified upper bound is below the earlier certified lower bound.

At truncation 320 the following rounded-up bounds hold on the full circle.
The columns concern the weighted residual and its angular derivatives.

| Radius | Residual | First angular derivative | Second angular derivative |
|---|---:|---:|---:|
| 1/5 | 8.853e-41 | 1.174e-38 | 2.459e-36 |
| 1/4 | 1.345e-61 | 2.616e-59 | 5.474e-57 |
| 1/2 | 8.424e-126 | 1.776e-123 | 3.717e-121 |
| 1 | 5.488e-190 | 1.157e-187 | 2.423e-185 |

At radius 1/5, the next weighted density increment is below 1.285e-43.
The first and second weighted radial derivatives of the unweighted
residual are below 1.903e-38 and 4.109e-36. The retained certificate gives
both lower and upper bounds for all quantities at every tested radius.

The computation used 1536-bit ball arithmetic and 4096 intervals on
[0,pi], with a proved interpolation error. Its actual arithmetic elapsed
time was 1413.6595467273146 seconds. All 96 reported floating grid values
lie between 0.99 times the corresponding certified lower bound and 1.01
times its upper bound. These comparisons do not replace the continuum
certificates. The small tested radii remain finite observations; the
proved infinite-series radius is unchanged.

The initial attempt stopped because an imported display helper was
missing. Its failure and log are retained. The repaired calculation
recomputed every row and completed successfully.
