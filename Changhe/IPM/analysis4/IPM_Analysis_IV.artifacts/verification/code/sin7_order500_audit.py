"""Specialize the independently reviewed single-harmonic audit to new sin7 data."""
from pathlib import Path
import sys
sys.dont_write_bytecode=True
import single_harmonic_finite_audit as audit
audit.ROOT=Path('research/293_sin7_order500')
audit.CASES[7]=(2,5,'single_sin7_45_p1024_N500')
audit.one(7,20,2048,[400,500])
(audit.ROOT/'sources/sin7_order500_audit.py').write_bytes(Path(__file__).read_bytes())
