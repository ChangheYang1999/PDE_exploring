from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
now=datetime.now(timezone.utc).isoformat()
entry=f'''
## Further checked boundary-operator statements ({now})

Juan Jose Marin, Jose Maria Martell, Dorina Mitrea and Marius Mitrea,
*Characterizations of Lyapunov domains in terms of Riesz transforms and
the Plemelj-Privalov theorem*, arXiv:2604.19143v1, April2026.
Primary PDF: https://arxiv.org/pdf/2604.19143 . Theorem1.3(i), pages5-6,
was read in full. It assumes an Ahlfors regular domain in R^n, n>=2,
with compact boundary, a bounded doubling nondecreasing Dini modulus
omega vanishing at zero, and an odd C^2 divergence-free vector kernel
homogeneous of degree1-n. The generalized double-layer principal value
maps C^omega(boundary) boundedly into C^omega_Z(boundary), where
omega_Z(t)=integral_0^t omega(s)ds/s+t integral_t^diam omega(s)ds/s^2.
If omega_Z<=C omega it maps into C^omega. The theorem gives no numerical
operator norm. Its operators are on domain boundaries and have different
kernels and measures from the whole-plane second-order Riesz transforms.
It is a qualitative modulus-of-continuity comparison, not a value for
C_alpha or D_alpha. Local source: sources/marin_martell_mitrea_mitrea_2026.pdf.

Yifei Pan and Yuan Zhang, *Cauchy singular integral operator with parameters
in Log-Holder spaces*, arXiv:2001.03778v1, January2020.
Primary PDF: https://arxiv.org/pdf/2001.03778 . Definition1.1 and
Theorem1.2, pages1-2, were read. The slice Cauchy operator on D times a
parameter domain sends the stated C^(k,L^alpha Log^nu L) space into
C^(k,L^alpha Log^(nu+1)L), with C depending on the domain and indices.
The norm includes suprema of derivatives and the joint-variable modulus
|h|^alpha |log|h||^nu. The introduction assumes disjoint C^(1,alpha)
Jordan boundary components; the displayed Theorem1.2 uses C^(k,alpha)
boundary, k>=0. No attempt is made here to resolve that boundary-notation
issue at k=0, and no result from this source is used in our proof.
The claimed sharpness concerns the additional logarithmic regularity
loss under parameter dependence; its numerical constant is unspecified.
It is not a sharp Holder operator-norm result for the planar Beurling
transform. Only the singular-integral statement was investigated.
Local source: sources/pan_zhang_2020.pdf.
'''
with Path('04_literature/README.md').open('a') as f:f.write(entry)
with Path('VERIFY_REPORT.md').open('a') as f:
 f.write(f'''\n## V062: Two further primary-source boundary-operator checks\n\nDate: {now}\n\nClaim: The cited Marin-Martell-Mitrea-Mitrea2026 and Pan-Zhang2020 statements do not supply an exact numerical norm for the whole-plane operators of this project.\n\nMethod: Downloaded the primary arXiv PDFs, read Theorem1.3(i) and its hypotheses in the first, and Definition1.1/Theorem1.2 in the second. Checked the domains, kernels, moduli and unspecified constants directly.\n\nResult: The first gives a qualitative generalized double-layer bound with the Zygmund-transformed modulus; the second gives a sharp logarithmic regularity loss for a parameter-dependent Cauchy operator. Neither evaluates our norm. Full scope notes and local sources are in04_literature/README.md. The minor k=0 boundary-notation issue in the second is not resolved or used.\n\nVerdict: **CONFIRMED**.\n''')
paths=['04_literature/sources/marin_martell_mitrea_mitrea_2026.pdf','04_literature/sources/pan_zhang_2020.pdf']
Path('04_literature/additional_source_manifest.json').write_text(json.dumps(dict(time_utc=now,sha256={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in paths}),indent=2)+'\n')
print(now)
