 #!/bin/sh
    
 if [ $1 == 'q' ]
 then
    echo Please enter a variable:
    read variable
    echo Please enter a lower bound:
    read lower_bound
    echo Please enter an upper bound:
    read upper_bound   

    list=""
   for ((i=0; i<=39; i++))
   do
      var=$(printf %.4f $(echo "($lower_bound+$i*($upper_bound-$lower_bound)/40)" | bc -l));
      list+="$var,"
   done
   var=$(printf %.4f $(echo "($lower_bound+$i*($upper_bound-$lower_bound)/40)" | bc -l));
   list+="$var"
   export variable
   export x="$list"
   echo $list
   python shapes/produce_shapes.py --channels mm --output-file output/earlyRun3_crown_2018_mm --directory /storage/gridka-nrg/moh/CROWN_samples/EarlyRun3_V00/CROWNRun --mm-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V00/friends/crosssection --era 2018 --num-processes 4 --num-threads 4 --optimization-level 1 --control-plots --control-plot-set $variable --ntuple_type crown --skip-systematic-variations
 else
    echo try again
fi

source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2018_mm.root m_vis mm earlyRun3
source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2018_ee.root m_vis ee earlyRun3
