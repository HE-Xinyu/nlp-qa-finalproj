import gzip
import random
import json
from  tqdm import tqdm

with gzip.open("datasets/bioasq.jsonl.gz", "rb") as f:
    elems = [
        json.loads(l.rstrip())
        for l in tqdm(f, desc=f'loading ', leave=False)
    ]
    meta, samples = elems[0], elems[1:]

train = []
dev = []

for sample in samples:
    if random.random() < 0.5:
        train.append(sample)
    else:
        dev.append(sample)

s = ""
with gzip.open("datasets\BioASQ-train.gz", "wb") as f:
    s += json.dumps(meta)
    s += "\n"
    for sample in train:
        s += json.dumps(sample)
        s += "\n"
    
    f.write(s.encode())

s = ""
with gzip.open("datasets\BioASQ-dev.gz", "wb") as f:
    s += json.dumps(meta)
    s += "\n"
    for sample in dev:
        s += json.dumps(sample)
        s += "\n"
    
    f.write(s.encode())