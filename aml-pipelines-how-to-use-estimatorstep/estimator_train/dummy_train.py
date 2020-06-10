# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import argparse
import os

print("*********************************************************")
print("Hello Azure ML!")

parser = argparse.ArgumentParser()
parser.add_argument('--datadir', type=str, help="data directory")
parser.add_argument('--output', type=str, help="output")
args = parser.parse_args()

print("Argument 1: %s" % args.datadir)
print("Argument 2: %s" % args.output)

if not (args.output is None):
    os.makedirs(args.output, exist_ok=True)
    print("%s created" % args.output)
    
with open(args.datadir, 'r') as f:
    content = f.read()
    with open(os.path.join(args.output, 'output.csv'), 'w') as fw:
        fw.write(content)



