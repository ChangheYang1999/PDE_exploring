"""Run three short source checks with the ongoing numerical child held."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,os,signal,subprocess,sys,time,re
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/reference_b18s2_audit';PID=256524
STAGES=[('bridge',['research/legendre_exact_bridge/code/convert.py','--request','research/reference_b18s2_audit/verification/bridge_request_v01.json','--tag','reference_b18s2_v01']),
        ('constraints',['research/fitted_center_constraints/code/check.py','--request','research/legendre_exact_bridge/verification/reference_b18s2_v01/structural_request.json','--tag','reference_b18s2_v01','--bits','1024']),
        ('reduce_constraints',['research/fitted_center_constraints/code/reduce_v02.py','--record','research/fitted_center_constraints/verification/reference_b18s2_v01/result.json','--tag','reference_b18s2_reduction_v01'])]
def stamp():return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def clean(t):
    t=t.replace(str(ROOT)+'/', '').replace(str(ROOT),'.')
    return re.sub(r'File "(/(?:home|mnt|efs|tmp)/[^"]+)"',lambda m:'File "[external]/'+Path(m.group(1)).name+'"',t)
def main():
    assert sorted(os.sched_getaffinity(0))==[50]
    assert b'compact_annulus/code/compute_v01.py' in (Path('/proc')/str(PID)/'cmdline').read_bytes()
    hold_tick=time.monotonic();out={'started_utc':stamp(),'preserved_numerical_child':PID,'stages':[]};os.kill(PID,signal.SIGSTOP)
    try:
        while (Path('/proc')/str(PID)/'stat').read_text().rsplit(') ',1)[1].split()[0]!='T':time.sleep(.01)
        freeze_log=BASE/'verification/freeze_v01.log'
        with freeze_log.open('x') as f:
            frozen=subprocess.run([sys.executable,'-B','-X','int_max_str_digits=0','research/reference_b18s2_audit/code/freeze_v01.py'],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=120)
        freeze_log.write_text(clean(freeze_log.read_text()))
        assert frozen.returncode==0,freeze_log.read_text()
        for n,h in json.loads((BASE/'verification/freeze_v01.json').read_text())['files'].items():assert sha256((ROOT/n).read_bytes()).hexdigest()==h
        for name,args in STAGES:
            log=BASE/'verification'/(name+'_v01.log');start,tick=stamp(),time.monotonic()
            with log.open('x') as f:r=subprocess.run([sys.executable,'-B','-X','int_max_str_digits=0',*args],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=120)
            text=clean(log.read_text());log.write_text(text)
            out['stages'].append({'name':name,'started_utc':start,'finished_utc':stamp(),'elapsed_seconds':time.monotonic()-tick,'exit_code':r.returncode,'log':str(log.relative_to(ROOT))})
            print(name,r.returncode,text[-400:],flush=True)
            if r.returncode:break
    finally:
        os.kill(PID,signal.SIGCONT);out['finished_utc']=stamp();out['elapsed_hold_seconds']=time.monotonic()-hold_tick;out['scope']='Only one busy numerical worker. Long child held during short serial checks and resumed.'
        with (BASE/'verification/serial_pause_v01.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    assert len(out['stages'])==3 and all(row['exit_code']==0 for row in out['stages'])
if __name__=='__main__':main()
