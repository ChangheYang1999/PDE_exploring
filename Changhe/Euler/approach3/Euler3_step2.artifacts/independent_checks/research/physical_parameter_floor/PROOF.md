# Physical derivatives, relative steps and a fixed error floor

Date: 2026-10-29. Status: proved elementary identity and exact counterexample.

## Statement and notation

Let n be a positive integer, let d and D belong to R^n, and use the Euclidean norm. Let F>0 and s>0. Define

    E_F(d,D) = ||D-d|| / max(||d||, ||D||, F).

Then

    E_F(s d,s D) = E_(F/s)(d,D).

Thus multiplying a derivative and its difference estimate by s while keeping F fixed changes the effective floor in the original derivative units from F to F/s. If 0<s<1, this can make a failed test pass. Without the floor, the relative error is invariant under simultaneous nonzero scaling, provided at least one of d and D is nonzero.

A relative physical step h s, with difference quotient

    [f(p+h s)-f(p-h s)]/(2h s),

is still an estimate of the physical derivative f'(p). Changing that step does not by itself change the derivative coordinate. If u=p/s, with s fixed at the base point, then the derivative with respect to u is s f'(p). Comparing in u units therefore requires an explicit coordinate convention for the floor.

## Proof

By homogeneity, ||s(D-d)||=s||D-d|| and

    max(s||d||,s||D||,F) = s max(||d||,||D||,F/s).

Cancel s. This proves the identity. If F=0 and max(||d||,||D||)>0, the same cancellation proves relative-error invariance. The claim about the relative step follows directly from the definition of a derivative along the physical coordinate. The coordinate-conversion claim follows from the chain rule applied to f(su).

For a strict example take n=2, d=(10^-20,10^-20), D=d+(2*10^-16,0), F=sqrt(2)*10^-10, s=3/10 and tolerance tau=10^-6. Both ||d|| and ||D|| are less than F, as are their scaled values. Therefore

    E_F(d,D) = sqrt(2)*10^-6 > tau,
    E_F(s d,s D) = (3 sqrt(2)/10)*10^-6 < tau.

The first inequality follows from sqrt(2)>1, and the second from 18<100 after squaring positive quantities. The same discrepancy can persist at every ladder step if the difference estimates are constant, so additional passing-pair requirements do not remove it.

## Dependencies and scope

Only homogeneity of the Euclidean norm, elementary inequalities and the chain rule are used. No Euler field or production derivative is asserted to have this error. The result identifies a change in the test normalization. specification v1.17 section 3.0(b) prescribes relative steps at small omega; section 3.0(b')(1) separately prescribes scaled derivative coordinates for coefficient columns. The exact identity above allows these two operations to be checked separately.

## Verification evidence

`verification/README.md` points to the captured v4 source controls. No formalization or Lean/Lake execution is performed.
