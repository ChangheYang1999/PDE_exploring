# Report assembly 32c9fd3c at cutoff A3160

## 1. Exact object and retained evidence

This audit concerns the front matter, main Sections0-10 and AppendixA of report SHA25632c9fd3c52988244c9dad13d8ed6e39c25e24a025ab00218a719b6855670b589, with8012newline-terminated lines and1272869bytes, assembled at10:19Z. Its verdict cutoff is A3160. The prior report324d99cfda6302ce8a0545392c4638651e58fc6e335058e32a344db1f1c6f5b2 was cumulatively approved in A3160 at cutoff A3156.

The full prior and submitted bytes, the declared70-line normal diff57bb1210962614cee0a067fe9b68879060ede5941de1a1ec7c18f329ea7b8cf9 and an independently computed unified diff6c730fe2b1337e5a469201ef6ed26d7e7a226a4e596b657ea5990685cbdc4091 are retained in `verification`. The added and deleted text sequences agree exactly. All declared changes, including the entire new table row, were read. Unchanged mathematics inherits only the prior approved scope; historical AppendicesB/C are not collectively certified.

## 2. LIT384 transfers and their exact scope

The new paragraph in Theorem8(o) and the table row correctly transfer A3157-A3158. For0<beta<1, L>0, t=(beta-3)/2, k=(beta+1)/2 and m=2-beta, the aligned, normalized degree-one poloidal/toroidal family is indexed by rho in[0,1]. Its smooth completion has exact centered energy LR^beta for R>=2, translated error O_a(R^(beta-2)), all integer derivative orders O(r^(t-h)), and a smooth Poisson pressure. It fails the full Euler equation for every c and omega.

Its normalized logarithmic tangential, gradient and positive spherical-source coefficients are respectively

    tau=1-2rho/(k^2+2),
    M=rho H+(1-rho)(t^2+2),
    S=m[1-2beta rho/(k^2+2)].

The identity S=m[(1-beta)+beta tau] proves leading equality in the cited J lower bound for every rho. The interval

    (k^2+2)/(k^2+2+3t^2)<=rho<=(k^2+2)/(2(k+1))

is exactly the exterior pointwise q>=0 range. Its interior gives strict exterior positivity; a parameter in it makes the exterior source radial. In this range I and J have equal leading coefficients. This is not a statement about the core, where q<0.

At rho=1 the field is the pure poloidal Hardy endpoint with D=D_* and both source signs. The distinct parameter

    rho_d=(t^2-1)(k^2+2)/(7t^2-k^2-2)

makes the gradient norm constant on each exterior sphere and gives D^2=beta L M_d/(4pi), with H<M_d and D_H<D<D_*. It minimizes D only in the stated aligned one-parameter family without a source-positivity restriction. The report says "over the family" and does not claim a full-mode optimum. The endpoint premise is absent at rho_d because M_d>H. Neither the positive-source interval nor the radial-source choice is asserted to coincide with rho_d.

The Section5 bullet therefore correctly says D_* is not an energy-ratio-only lower bound, while the strict general bound D>D_H remains. The wording "a positive exterior source is compatible with it" is read as compatibility with the energy-ratio class, as established by the explicit following construction. Replacing "it" with "the energy ratio" would remove that avoidable pronoun ambiguity, but the displayed statements are precise.

## 3. Version, cutoff and mechanical checks

The report cites source2a4a7fb8 and comparison77697f3e, the versions checked for A3157-A3158. The current source e322fa7780ed903cfde7e58278627ebc53f91a3fb2bb2bd04e2bdd0fb2b511a7 differs only in its status sentence, now recording A3157-A3158 and the open scope A3159. The full difference is retained and read; it changes no hypothesis, formula, proof or construction.

The front matter correctly records A3160 as approval of the10:08Z assembly at cutoff3156. The new history records A3157-A3160. The not-known list and the closing Theorem8(o) sentence retain A3159. The phrase "No explicit gap above D_H is proved here" is accurate at this report's cutoff3160; LIT385 is still pending. Later conditional or unconditional results are not silently imported.

The submitted bytes have zero NUL bytes, zero em-dash characters and zero occurrences of the prohibited absolute local path prefixes. The complete new table row has the intended six delimiter characters. These are mechanical checks of this object, not evidence for the mathematical claims. No report outside this agent was modified.

## 4. Cumulative conclusion and remaining boundaries

At the stated cutoff, the new transfers are faithful and the previous approved mathematics is unchanged. Cumulative approval applies to the front matter, main Sections0-10 and AppendixA of exactly32c9fd3c. It does not approve later edits or historical AppendicesB/C as a whole.

The arbitrary-omega target remains open. The smooth source-positive and constant-gradient controls are not Euler solutions. The actual-profile amplitude optimum, a general kinematic optimum, global source positivity and automatic Hardy endpoint remain unresolved. The status-only source revision preserves the A3157-A3159 scopes. No numerical diagnostic or formal build was used in this review.
