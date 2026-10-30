# Certified low-order lower bound on the sharpw forcing norm

Let F be the exact residual of C1-N1-007-d2w-j7-e2bal. For s>=0 define
J^s=(1-Delta)^(s/2) and

    X_(s,w)(F)^2 = ||omega D^2 J^s F||_2^2
                   +32768 ||D J^s F||_2^2+1048576 ||J^s F||_2^2,
    omega=(1+4r^2)^(2/5).

If this quantity is infinite, every finite smallness threshold fails.
Otherwise Plancherel and (1+|xi|^2)^s>=1 give

    X_(s,w)(F)>=sqrt(32768 G1^2+1048576 G0^2),
    G1=||D F||_2, G0=||F||_2.

The independently confirmed complete-plane component enclosures N4-139
and N4-153 imply the strict rational floors

    G0>3766893247/10^10, G1>34391037868/10^10.

Substitution proves X_(s,w)(F)>732.35 for every s>=0. In particular at
the sharpw theorem's s=1/5184, its sufficient threshold 0.00021035 is
missed by more than 3,480,000. The verification file retains the exact
rational comparison and a tighter ball for the resulting lower bound.

This is a failed sufficient residual condition. It is not a lower bound
on a correction or a nonexistence proof. The independently certified
fixed-c L2 correction distance >0.004769166867 is a different statement.
The weighted Hessian component was discarded, so no claim that a Bessel
multiplier increases that weighted component is used.

Dependencies: Plancherel, the norm definition, and the confirmed component
bounds. The component fields are not recomputed in this postprocessing.
