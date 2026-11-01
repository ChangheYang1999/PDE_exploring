"""Execute one local research script with compact, path-safe failure evidence."""
from pathlib import Path
from datetime import datetime,timezone
import runpy,sys,traceback,json
sys.dont_write_bytecode=True
script,fail=sys.argv[1:3];sys.argv=[script]+sys.argv[3:]
try:runpy.run_path(script,run_name='__main__')
except SystemExit:raise
except Exception as exc:
    record={'checked_at_utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'error_type':type(exc).__name__,'error':str(exc),'frames':[{'file':Path(x.filename).name,'line':x.lineno} for x in traceback.extract_tb(exc.__traceback__)]}
    Path(fail).write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record),flush=True);raise SystemExit(1)
