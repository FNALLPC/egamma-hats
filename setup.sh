#!/usr/bin/env bash

NAME=egammaenv
LCG=/cvmfs/sft.cern.ch/lcg/views/LCG_96python3/x86_64-centos7-gcc8-opt/setup.sh

if [[ -f $NAME/bin/activate ]]; then
  echo "egammaenv already installed. Run \`source $NAME/bin/activate\` to activate"
  exit 1
fi
source $LCG
python -m venv --copies $NAME
source $NAME/bin/activate
python -m pip install setuptools pip --upgrade
python -m pip install "coffea>=0.6.27"
sed -i "2a source ${LCG}" $NAME/bin/activate
ipython kernel install --user --name=$NAME
