# Sharper closed-form upper bound for $C_\alpha$ (Theorem 3.7 remainders)

`PROOF.md` states and proves $C_\alpha\le F^{**}(\alpha)=\frac{4\cdot2^{-\alpha/2}}{\pi\alpha(\alpha+2)}+\frac{0.418}{1-\alpha}+0.5412$ for every
$0<\alpha<1$. This lowers the constant of the closed form of Theorem 9.3 by $0.0348$. Commands (single-threaded, python-flint):

```
bash code/run37.sh
bash code/run37_g7.sh
python3 code/nodes37.py
python3 code/check_closed_form37.py 209/500 1353/2500 4000 200
```

Outputs: the chunk certificates in `local/`, `mid/`, `local7/`, `mid7/`, then `data/remainders37.json` and
`results/closed_form37_check_209_500_1353_2500.json`. `SHA256SUMS.txt` lists the hashes of all files.
