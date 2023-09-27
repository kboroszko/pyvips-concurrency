#!/bin/bash
set -euo pipefail

# single process
docker run \
  -v `pwd`:/app \
  --cpus=2 \
  -e VIPS_CONCURRENCY=1 \
  --entrypoint /usr/bin/python3 \
  pyvips-test single.py -i data/2.jpeg >> results_no_c.csv


# two processes
docker run \
  -v `pwd`:/app \
  --cpus=2 \
  -e VIPS_CONCURRENCY=1 \
  --entrypoint /usr/bin/python3 \
  pyvips-test multiple.py -n 2 -i data/2.jpeg >> results_no_c.csv
