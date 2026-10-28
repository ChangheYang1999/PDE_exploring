# Direct Theorem 3.7 certificates for C_alpha at six exponents

Statement and proof: `PROOF.md`. Result: `results/table37.json` (upper bounds for C_alpha at alpha = 1/1000, 1/100, 1/20,
1/10, 1/5, 99/100, rounded up at ten decimals).

- `code/run_table37.sh`: runs all chunks (exterior `far/`, local `local/`, middle `mid/`), sequential and single-threaded.
- `code/table37.py`: merges the chunks with exact coverage and hash checks, adds the small disk term, writes `results/table37.json`.
- `code/*.py` (other files): certification programs, see `PROOF.md` for their provenance.
- `SHA256SUMS.txt`: hashes of all files in this folder except itself.
