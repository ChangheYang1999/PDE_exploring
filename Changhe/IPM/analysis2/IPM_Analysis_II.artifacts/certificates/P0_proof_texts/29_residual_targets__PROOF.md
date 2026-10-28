# Necessary residual scales for the present weighted theorem

Status: proved by the two already verified general embeddings below. These are necessary consequences of the sufficient smallness condition, not sufficient tests for the full norm.

## Exact statement

Let R>=1 and0<s<=2^-12. Use the compact parity completion N_(s,R) of topics16 and18, with

    w_R=(1+r^2/R^2)^(-11/10), L_R(f)=||w_R f||_(dot H^-1),
    E_R(f)^2=||(1+4r^2)^(2/5)D2f||2^2
                +2^22||<r>^(-1/5)Df||2^2+2^53 L_R(f)^2,
    N_(s,R)(f)=E_R(J^s f), J=(1-Delta)^(1/2).

All derivatives are ordered Cartesian tensors, and f denotes the continuous representative supplied by the embedding. If N_(s,R)(f)<=2^-35, then

    L_R(f)<=6*2^(-123/2)<2^-58,
    |f(X)|<=2^-31 max(1,|X|^(1/5)) for every X.

These conclusions apply in particular to the actual unnormalized reference residual F in the current conditional nonlinear theorem, where R=2^31 and s=3*2^-31, if that theorem's sufficient residual hypothesis is met. Neither conclusion implies this sufficient hypothesis conversely. No sampled or normalized residual can replace F here.

## Proof

Put H=J^s f. The negative component of E_R gives L_R(H)<=2^(-53/2)N_(s,R)(f). The Bessel bound of topic16/SHARP_LOW_COMMUTATOR_PROOF.md, retained in topic18, gives L_R(J^-s H)<=6L_R(H). It is an inequality on the same canonical completion, so it applies to f=J^-s H. Consequently

    L_R(f)<=6*2^(-53/2)N_(s,R)(f)<=6*2^(-123/2).

The last number is less than2^-58 because6<2^(7/2), equivalently36<128.

The point embedding in topic18, equation(7), states

    |f(X)|<=16max(1,|X|)^(1/5)N_(s,R)(f).

Since max(1,|X|)^(1/5)=max(1,|X|^(1/5)) and16*2^-35=2^-31, the second conclusion follows for every point of the continuous representative. The strict bound on s in the current theorem lies in the stated interval. This proves the assertion.

## Dependencies and scope

18_fractional_constants/PROOF.md, equations(6)-(7) and section5, supplies the point embedding and its compatible low inclusion. 16_weighted_fractional/SHARP_LOW_COMMUTATOR_PROOF.md supplies the Bessel bound. 20_real_velocity/PROOF.md verifies transfer of the same theorem toR=2^31. The current matrix weakening in topic24 changes neither embedding.

The verification script checks the exact inequalities and parameters, and binds these dependencies. No numerical profile is asserted to meet either target. Passing them is weaker than bounding the whole fractional residual norm.
