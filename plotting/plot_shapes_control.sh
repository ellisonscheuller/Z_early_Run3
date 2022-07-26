source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh
export PYTHONPATH=$PWD:$PYTHONPATH

ERA=$1
INPUT=$2
VAR=$3
CAT=$4
MATCH=$5
RUN=$6
CHANNEL=$7
TAG=$8

python plotting/plot_shapes_control.py -l --era Run${ERA} --input ${INPUT} --variables ${VAR} --category-postfix ${CAT} --match_data ${MATCH} --run-plot ${RUN} --channels ${CHANNEL} --tag ${TAG}

