# arti

seed_job.dsl is DSL job for Jenkins

test_common.py is for storing common checks across all hosts

create new env
```
pip install -r requirements.txt
```

create new tests:

run all tests against new server

```
sh run_fantazja.sh -v >fantazja.out

grep PASS fantazja.out |sed -e 's/^.*:://g' -e 's/\[.*$//g'|sort -u |grep -v website > fantazja.in

reuse tests:
grep PASS qantms.out |sed -e 's/^.*:://g' -e 's/\[.*$//g'|sort -u |grep -v website > qantms.in
for i in `cat qantms.in `;do grep -n $i *py|head -1;done
```
