# Pointwise failures of the signed low-energy sufficient condition

## Statement

Let rho be a C1 real density, c>1, and kappa>=0. Define

    theta=sup_X (sqrt(rho_x(X)^2+rho_y(X)^2)-rho_y(X))/2.

If at a single point X0 the displayed expression is greater than c-1, then the sufficient condition

    c+1-theta-kappa>=2

fails for every kappa>=0. This is a failure of that sufficient energy hypothesis, not a nonexistence theorem and not a proof that the actual generator lacks a positive decay rate.

The claim follows because theta is at least its value at X0. Continuity implies the same lower bound for the essential supremum. The matrix [[rho_y,-rho_x/2],[-rho_x/2,0]] has smallest eigenvalue (rho_y-sqrt(rho_x^2+rho_y^2))/2, which also proves the stated connection to the signed principal form.

## Independent evaluation

For the exact canonical potentials of candidates002,003,004, the conversion from the original immutable generator data was checked coefficient by coefficient in T4-037 and T4-038. The copied canonical inputs retain those hashes. The present computation uses the independent rational polar construction from those proofs, also stated fully in ../weak_probe_audit/PROOF.md. It does not import N4 code.

Write t=r^2/(1+r^2), u=1-t, delta=1-1/c and a_j=(j+1)delta/2. That construction gives

    rho=r sum_(j,n) u^(a_j) R_(j,n)(t) sin(n theta).

For T_(a,1)R=(1-2at)R+2t(1-t)R', differentiation yields

    rho_r=sum u^a T_(a,1)R sin(n theta),
    rho_theta/r=sum u^a nR cos(n theta).

Then rho_x=cos(theta)rho_r-sin(theta)rho_theta/r and rho_y=sin(theta)rho_r+cos(theta)rho_theta/r. At a nonzero rational point, t and u are rational and every polynomial evaluation is exact. Arb encloses the square root r, powers u^a, trigonometric addition recurrences, and the final eigenvalue formula. A strictly positive enclosure for theta_X0-(c-1) proves the claimed failure. No finite scan is used as a global upper bound.

The code checks the particular rational point selected in each N4 scan. Agreement of the point value and failure gap gives independent reproduction of that witness, without any claim to reproduce all scan rows. Numerical outputs and hashes are in verification/. This argument and method were written before execution. No Lean build is performed.
