from common import *
import argparse
ap=argparse.ArgumentParser();ap.add_argument('mode',choices=MODES);args=ap.parse_args()
p=E/args.mode;p.mkdir(exist_ok=True);assert not (p/'inputs.json').exists()
x=extract(args.mode);write(p/'inputs.json',{'utc':now(),**x})
write(p/'input_freeze.json',{'utc':now(),'status':'IMMUTABLE_FINAL_PARENT_SCALARS_BEFORE_EVALUATION','inputs_sha256':sha(p/'inputs.json'),'source_freeze_sha256':sha(E/'source_freeze.json')})
print(json.dumps({'utc':now(),'mode':args.mode,'inputs_sha256':sha(p/'inputs.json'),'parents':x['parents']}))
