"""Isolated long-prefix construction and independent polar replay for root five."""
from pathlib import Path
import argparse,sys
sys.dont_write_bytecode=True
ROOT=Path('research/294_q10_tail_prefix')
p=argparse.ArgumentParser();p.add_argument('stage',choices=['cartesian','polar']);a=p.parse_args()
if a.stage=='cartesian':
 import period_ten_prefix as implementation
 implementation.ROOT=ROOT
 implementation.one(10,5,120,2048)
else:
 import period_ten_polar_replay as implementation
 implementation.ROOT=ROOT
 sys.argv=[sys.argv[0],'--Q','10','--root','5','--bits','3072']
 implementation.main()
(ROOT/'sources/q10_tail_prefix.py').write_bytes(Path(__file__).read_bytes())
