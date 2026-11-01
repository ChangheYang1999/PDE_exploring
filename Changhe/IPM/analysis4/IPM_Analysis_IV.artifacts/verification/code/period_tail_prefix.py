"""Run the retained Cartesian prefix implementation in topic262."""
from pathlib import Path
import argparse,sys
sys.dont_write_bytecode=True
import period_high_prefix as core
p=argparse.ArgumentParser();p.add_argument('--Q',type=int,required=True);a=p.parse_args();assert a.Q in [7,8]
core.ROOT=Path('research/262_tail_response_prefix')
core.one(a.Q,3,140 if a.Q==7 else 96,2048)
(core.ROOT/'sources/period_tail_prefix.py').write_bytes(Path(__file__).read_bytes())
