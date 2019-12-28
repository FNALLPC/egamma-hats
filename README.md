EGamma short exercise
---------------------
To start the exercise environment, follow this recipe, substituting your favorite 3-digit number
for the three instances of `xxx` below:
```bash
ssh cmslpc-sl7.fnal.gov -L8xxx:localhost:8xxx
# ...
mkdir -p nobackup/cmsdas2020 & cd nobackup/cmsdas2020
git clone THIS
cd THIS
source setup.sh
voms_proxy_init --voms cms --valid 100:00
jupyter notebook --no-browser --port 8xxx
```
