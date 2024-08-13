EGamma HATS 2024
---------------
This exercise provides an introduction to CMS electron and photon objects.

This exercise is designed to be run to any cluster with a jupyterlab interface and a software stack close to LCG 105a. You mainly need a `coffea 0.7.x` environment and the data files. Pick your favorite one: SWAN, Purdue AF, coffea-casa etc.
If your cluster doesn't have the files, you can query DAS for them and read them via xrootd like it was done in the previous version of the exercise in https://github.com/gracecummings/CMSDAS_EGamma/blob/master/exercise.ipynb.
You will only need to change the events reading at the beginning of the notebooks and everything else should run fine.
Currently, SWAN and Purdue AF have the files locally. For SWAN, use `/eos/user/c/cmsdas/2024/short-ex-egm/datasets/` as `base_directory` in the notebooks and for Purdue, use `/work/projects/hats2024/egamma/datasets/`.

Just start a new session on the cluster, open a new terminal and clone the exercise material with the following command:

>`git clone https://github.com/FNALLPC/egamma-hats.git`

Then, open the jupyterlab interface and navigate to the folder `egamma-hats`.

We will start with `exercise-1.ipynb` and then move to `exercise-2.ipynb` and `exercise-3.ipynb`.

Some references:
 - [CMSDAS CERN 2024](https://indico.cern.ch/event/1388937/)
 - [CMSDAS CERN 2023](https://indico.cern.ch/event/1257234/)
 - [CMSDAS LPC 2023](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2023EGammaShortExercise)
 - [CMSDAS 2021](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2021EGammaExercise)
 - [LPC HATS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/EGammaHATSatLPC2020)
 - [CMSDAS 2020](https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCMSDataAnalysisSchoolLPC2020EGammaExercise)
