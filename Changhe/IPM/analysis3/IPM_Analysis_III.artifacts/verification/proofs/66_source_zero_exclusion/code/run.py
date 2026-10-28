from pathlib import Path
import subprocess,sys
p=Path(__file__).with_name("certify.py")
subprocess.run([sys.executable,"-B",str(p),"prepare","--bits","512"],check=True)
subprocess.run([sys.executable,"-B",str(p),"evaluate","--bits","512","--radial","4","--angular","24","--tag","wide"],check=True)
