# performance comparison when running multiple pyvips programs

to run it:
```
for i in {1..10} ; do echo $i ; ./run_docker.sh ; done
```

to view the results:
```
python3 show_results.py -i results.csv
```

to view results for pyvips using `VIPS_CONCURRENCY=1`
```
python3 show_results.py -i results_no_c.csv
```
