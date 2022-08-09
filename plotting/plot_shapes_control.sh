source utils/setup_cvmfs_sft.sh
source utils/setup_python.sh
export PYTHONPATH=$PWD:$PYTHONPATH

ERA=$1
INPUT=$2
VAR=$3
CAT=$4
MATCH=$5
LABEL=$6
LATEX=$7
CHANNEL=$8
TAG=$9

python plotting/plot_shapes_control.py -l --era Run${ERA} --input ${INPUT} --variables ${VAR} --category-postfix ${CAT} --match-data ${MATCH} --lumi-label ${LABEL} --write-to-latex ${LATEX} --channels ${CHANNEL} --tag ${TAG}

