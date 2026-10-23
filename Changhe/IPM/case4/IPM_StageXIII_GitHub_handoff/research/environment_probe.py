from absolute_common import *
atomic(OUT/'environment.json',provenance())
print(json.dumps(provenance()))
