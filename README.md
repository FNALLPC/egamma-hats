EGamma exercise
---------------
This exercise provdes an introduction to CMS electron and photon objects. It is used as part of:
 - [CMSDAS CERN 2023](https://indico.cern.ch/event/1257234/)
 - [CMSDAS LPC 2023](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2023EGammaShortExercise)
 - [CMSDAS 2021](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2021EGammaExercise)
 - [LPC HATS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/EGammaHATSatLPC2020)
 - [CMSDAS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2020EGammaExercise)

To setup the exercise environment, choose a 3-digit number to replace the three instances of `xxx` below,
and execute:
```bash
# connect to lxplus with a port forward to access the jupyter notebook server
ssh USERNAME@lxplus8.cern.ch -L8xxx:localhost:8xxx

# create a working directory and clone the repo
mkdir workdir && cd workdir
git clone https://github.com/CERN-CMS-DAS-2023/short-ex-egm
cd short-ex-egm

# in case you do not already have this in your .bashrc (or equivalent) please run
source /cvmfs/cms.cern.ch/cmsset_default.sh

# this script sets up the python environment, only run once
# do not worry about pip's error message for coffea/numpy dependency
./setup.sh

# this enables the environment, run it each login (csh users: use activate.csh)
source egammaenv/bin/activate

# this gives you permission to read CMS data via xrootd
voms-proxy-init --voms cms --valid 192:00

jupyter notebook --no-browser --port 8xxx
```
There should be a link like `http://localhost:8xxx/?token=...` displayed in the output at this point, paste that into your browser.
You should see a jupyter notebook with a directory listing. Open `exercise.ipynb`.
