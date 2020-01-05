EGamma short exercise
---------------------
To setup the exercise environment, choose a 3-digit number to replace the three instances of `xxx` below,
and execute:
```bash
# connect to LPC with a port forward to access the jupyter notebook server
ssh cmslpc-sl7.fnal.gov -L8xxx:localhost:8xxx

# create a working directory and clone the repo
mkdir -p nobackup/cmsdas2020 & cd nobackup/cmsdas2020
git clone git@github.com:nsmith-/CMSDAS_EGamma.git
cd CMSDAS_EGamma

# this script sets up the python environment, only run once
./setup.sh

# this enables the environment, run it each login (csh users: use activate.csh)
source egammaenv/bin/activate

# this gives you permission to read CMS data via xrootd
voms-proxy-init --voms cms --valid 100:00

jupyter notebook --no-browser --port 8xxx
```
There should be a link like `http://localhost:8123/?token=...` displayed in the output at this point, paste that into your browser.
Then open `exercise.ipynb`.
