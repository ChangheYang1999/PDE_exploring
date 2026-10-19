# Lead: adir.py with pforward2.velocity_p (exponential-integrator weights). Usage: python3 adir2.py state.npz [m1]
import sys, runpy
sys.path.insert(0, 'explore')
import pforward as PF, pforward2 as PF2
PF.velocity_p = PF2.velocity_p
runpy.run_path('explore/adir.py', run_name='__main__')
