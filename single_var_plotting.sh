#!/bin/sh

echo Please enter a variable:
read variable
echo Please enter a channel:
read channel
echo Are you making a single run graph?
read answer
export answer
filename='temp.txt'
run_list=$(cat temp.txt)
temp_str=""

if [ $answer == 'no' ]
then
    for rn_ber in $run_list
    do
        export rn_ber
        source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2022_"$channel"_"$rn_ber".root $variable $rn_ber $answer $channel earlyRun3$channel
    done
else
    source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2022_"$channel"_run.root $variable None $answer $channel earlyRun3$channel
fi
