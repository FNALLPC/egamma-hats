#!/usr/bin/env bash

NAME=egammaenv
LCG=/cvmfs/sft.cern.ch/lcg/views/LCG_102/x86_64-centos7-gcc11-opt #as of Dec 2022, most recent LCG

if [[ -f $NAME/bin/activate ]]; then
  echo "egammaenv already installed. Run \`source $NAME/bin/activate\` to activate"
  exit 1
fi
source $LCG/setup.sh
python -m venv --copies $NAME
source $NAME/bin/activate
LOCALPATH=$(python -c 'import sys; print(f"{sys.prefix}/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages")')
export PYTHONPATH=${LOCALPATH}:$PYTHONPATH
python -m pip install git+https://github.com/cms-nanoAOD/correctionlib.git
sed -i "2a source ${LCG}/setup.sh" $NAME/bin/activate
sed -i "3a export PYTHONPATH=${LOCALPATH}:\$PYTHONPATH" $NAME/bin/activate
sed -i "4a source ${LCG}/setup.csh" $NAME/bin/activate.csh
sed -i "5a setenv PYTHONPATH ${LOCALPATH}:\$PYTHONPATH" $NAME/bin/activate.csh
ipython kernel install --user --name=$NAME
