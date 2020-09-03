EGamma exercise
---------------
This exercise provdes an introduction to CMS electron and photon objects. It is used as part of:
 - [CMSDAS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2020EGammaExercise)
 - [LPC HATS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/EGammaHATSatLPC2020)

To setup the exercise environment, choose a 3-digit number to replace the three instances of `xxx` below,
and execute:
```bash
# connect to LPC with a port forward to access the jupyter notebook server
ssh cmslpc-sl7.fnal.gov -L8xxx:localhost:8xxx

# create a working directory and clone the repo
cd nobackup # if this symlink does not exist, look for /uscms_data/d1/$USER
git clone git@github.com:nsmith-/CMSDAS_EGamma.git
cd CMSDAS_EGamma

# this script sets up the python environment, only run once
./setup.sh

# this enables the environment, run it each login (csh users: use activate.csh)
source egammaenv/bin/activate

# this gives you permission to read CMS data via xrootd
voms-proxy-init --voms cms --valid 100:00

# in case you do not already have this in your .bashrc (or equivalent) please run
source /cvmfs/cms.cern.ch/cmsset_default.sh

jupyter notebook --no-browser --port 8xxx
```
There should be a link like `http://localhost:8xxx/?token=...` displayed in the output at this point, paste that into your browser.
You should see a jupyter notebook with a directory listing. Open `exercise.ipynb`.
