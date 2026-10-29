#!/usr/bin/env python3
"""Passive /proc accounting for this lane. No server, GPU work, or process control."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, os, re, time

ROOT=Path(__file__).resolve().parent.parent
DEADLINE=datetime(2026,10,29,16,44,44,tzinfo=timezone.utc)
HZ=os.sysconf('SC_CLK_TCK')
PAGE=os.sysconf('SC_PAGE_SIZE')

def snapshot():
    rows=[]
    for proc in Path('/proc').iterdir():
        if not proc.name.isdigit():continue
        try:
            if proc.stat().st_uid != os.getuid():continue
            args=[x.decode(errors='replace') for x in (proc/'cmdline').read_bytes().split(b'\0') if x]
            if not args:continue
            exe=Path(args[0]).name
            if not (re.fullmatch(r'python[0-9.]*',exe) or exe in ('bash','sh')):continue
            cwd=(proc/'cwd').resolve()
            # Require a script file inside this lane; exclude unrelated Python/shell sessions.
            scripts=[]
            for x in args[1:]:
                if x.startswith('-') or '\n' in x or len(x)>1024:continue
                p=Path(x);p=p if p.is_absolute() else cwd/p
                if p.suffix in ('.py','.sh') and p.resolve().is_relative_to(ROOT):scripts.append(str(p.resolve()))
            if not scripts:continue
            raw=(proc/'stat').read_text();fields=raw[raw.rfind(')')+2:].split()
            status={}
            for line in (proc/'status').read_text().splitlines():
                if line.startswith(('Cpus_allowed_list:','Threads:')):
                    k,v=line.split(':',1);status[k]=v.strip()
            rows.append({'pid':int(proc.name),'ppid':int(fields[1]),'state':fields[0],
                         'start_ticks':int(fields[19]),'user_cpu_seconds':int(fields[11])/HZ,
                         'system_cpu_seconds':int(fields[12])/HZ,'resident_bytes':int(fields[21])*PAGE,
                         'nice':int(fields[16]),'last_processor':int(fields[36]),
                         'affinity':status.get('Cpus_allowed_list'),'threads':status.get('Threads'),
                         'command':args,'lane_scripts':scripts})
        except (FileNotFoundError,ProcessLookupError,PermissionError,IndexError,OSError):
            continue
    return {'recorded_utc':datetime.now(timezone.utc).isoformat(),'clock_ticks_per_second':HZ,'processes':rows}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True)
    ap.add_argument('--once',action='store_true');ap.add_argument('--interval',type=float,default=60.)
    a=ap.parse_args();out=a.output.resolve()
    if not out.is_relative_to(ROOT) or a.interval<10:raise ValueError('Lane output and interval >=10 required')
    out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists():raise FileExistsError('Fresh accounting stream required')
    with out.open('x') as f:
        while True:
            r=snapshot();f.write(json.dumps(r,separators=(',',':'))+'\n');f.flush()
            if a.once or datetime.now(timezone.utc)>=DEADLINE:break
            time.sleep(min(a.interval,max(0.,(DEADLINE-datetime.now(timezone.utc)).total_seconds())))
    print(json.dumps({'finished_utc':datetime.now(timezone.utc).isoformat(),'output':str(out)}),flush=True)

if __name__=='__main__':main()
