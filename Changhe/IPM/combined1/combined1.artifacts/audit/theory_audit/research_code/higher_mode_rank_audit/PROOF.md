# Independent audit of the higher angular radius25 extension

## Exact statement and dependencies

Set c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
p_j=(3+gamma-j delta)/2, S=1+x^2+y^2, r^2=x^2+y^2,
v=1/S and H_m=Re(x+iy)^(2m). Let the old potential space have the
1922 selected generators in data/old_basis.json. Its exact independence
is the accepted T4-195/T4-230 dependency; its fixed-c basis is also bound
by T4-348 and the independently reviewed density-injectivity proof.
Adjoin, for each N=0,...,11 and each block

    (j,m) in ({1} x {9,...,19}) union ({2,3} x {9,...,23}),

    H_m S^(p_j-m) [625/(625+r^2)]^4
        P_N(2r^2/(625+r^2)-1).

Here P_N is the Legendre polynomial with P_N(1)=1. All2414 potentials
are independent and chi -> -partial_y Delta chi is injective on their
span. The density space therefore also has dimension2414. The240
functions additional to candidate016 have density angular support
contained in {31,33,...,47}; the frequency31 coefficient occurs in at
least one of these functions. This is a theorem about the abstract list,
not a conditioning estimate, fitted-candidate identity or PDE inverse.

## Complete independence argument

Angular orthogonality separates cos(2m theta). In each block a potential
relation is sum_j v^(-p_j) Q_j(v)=0, with rational Q_j analytic at zero.
The exact values of all p_j, j=0,...,7, and all28 distinct differences
are nonintegers. If any Q_j is nonzero, its first nonzero Taylor term
has integer order e_j. All leading exponents e_j-p_j are distinct.
Dividing by the unique smallest power and letting v decrease to zero
leaves one nonzero coefficient, a contradiction. Thus all Q_j vanish.
The same argument separates these powers from an integer Laurent class.

Within a separated (j,m), set a=624 and v0=-1/a. The new radial factor is

    A_mN(v)=625^4 v^4 (1-v)^m
       P_N(2(1-v)/(1+a v)-1)/(1+a v)^4.

It has pole order4+N at v0. Its highest Laurent coefficient is

    C_mN=625^4 v0^4 binom(2N,N)(1-v0)^(m+N)/a^(4+N),

which is nonzero. To see this, the leading term of P_N is
2^(-N)binom(2N,N)z^N, while the numerator of its argument at v0 is
2(1-v0). Every other term has smaller pole order. Old radial polynomials
are analytic at v0. A greatest N with nonzero coefficient in any
relation therefore has an uncancellable pole. Descend in N and remove
all new coefficients; the accepted old independence removes the rest.
There are41 blocks with12 functions each, so1922+492=2414. The pole
argument is used on rational identities after the fractional branches
have separated; it does not continue a noninteger power across a pole.

## Density injectivity

All generators are smooth and separately even in x and y, with
|D^k chi|=O(r^(3+gamma-k)) for0<=k<=4 at infinity. The new factors have
an extra r^-8 decay and preserve these bounds. As gamma<1, fourth
derivatives tend to zero. If partial_y Delta chi=0, then Delta chi=f(x).
For any fixed x, f''(x)=partial_xx Delta chi(x,y) tends to zero as
|y| tends to infinity, so f''=0. Evenness forces f=K constant.
Then h=chi-Kr^2/4 is entire harmonic and grows as O(1+r^(3+gamma)).
The harmonic derivative bound on disks of radius L about an arbitrary
point gives |D^4 h|<=C L^-4 sup|h|=O(L^(gamma-1)). Let L tend to
infinity: D^4 h=0. Thus h is a polynomial of degree at most3. Separate
evenness and harmonicity leave h=A+B(x^2-y^2). Consequently
chi=A+B(x^2-y^2)+Kr^2/4. At each angular frequency the right hand side
is an integer Laurent polynomial in v. Fractional branch separation,
including that integer class, forces it and each Q_j to vanish.
Potential independence then forces every coefficient to vanish.

## Frequencies and exact implementation check

The Laplacian preserves cos(2m theta); -partial_y shifts only to the
sines2m-1 and2m+1. The240 added functions have m=16,...,23, giving the
stated support. The function j=1,m=16,N=0 has origin expansion
H_16[1+(p_1-16-4/625)r^2+O(r^4)]. Since Delta(r^2 H_16)=4*33 H_16
and -partial_y H_16=32 Im(x+iy)^31, its density coefficient is
4*33*32*(p_1-16-4/625), a nonzero rational number. Higher origin orders
cannot cancel this term, establishing the actual frequency31 endpoint.

The checker independently reconstructs the proposed list from the old
basis and the complete016 shape list. It verifies that the stated
launch's existing-block rule adds exactly j=1,m=16..19 and j=2,3,m=16..23.
It constructs the entire Legendre polynomial numerator by the three-term
recurrence, evaluates the normalized numerator at v0, and checks all180
Laurent coefficients against the closed formula and the peer record.
The84 previously accepted radius25 coefficients are checked again as
calibration. Exact branch conditions, growth, cardinalities and the
origin coefficient are retained. Sources are copied before execution;
no publisher code is executed. A future candidate requires a new exact
shape and hash binding. The finite checks support this full informal
proof and do not replace it.
