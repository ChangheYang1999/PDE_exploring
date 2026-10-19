# Lead: run a lead script with pforward.velocity_p replaced by pforward2.velocity_p (exponential-integrator weights).
# Usage: python3 withpf2.py script.py [args...]
import sys, runpy
sys.path.insert(0, 'explore')
import pforward as PF, pforward2 as PF2
PF.velocity_p = PF2.velocity_p
script = sys.argv[1]; sys.argv = sys.argv[1:]
runpy.run_path(script, run_name='__main__')
