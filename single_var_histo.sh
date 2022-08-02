#!/bin/sh
   echo Please enter a variable:
   read variable
   echo Please enter a channel:
   read channel
   echo Please enter an lower bound:
   read lower_bound
   echo Please enter a upper bound:
   read upper_bound
   echo Please enter a bin size:
   read bin_size
   echo Are you making a single run plot?:
   read answer

   #creating the run list
   run_list="355443 355444 355445 355558 355559 355679 355680 355768 355769 done"
   #run_list="355680 done"
   lumi_list="1.971790835 1.243983634 1.537414347 11.7548517 6.878012741 1.078718626 46.78980232 1.222612315 16.16789967 done"
   #lumi_list="46.78980232 done"
   echo Your run list has these numbers: $run_list
   echo Your lumi list has these numbers: $lumi_list
   export channel
   export answer
   echo "${run_list}" > ./temp.txt
   echo "${lumi_list}" > ./lumi.txt

   list=""
   for ((i=0; i<=($bin_size-1); i++))
   do
      var=$(printf %.4f $(echo "($lower_bound+$i*($upper_bound-$lower_bound)/$bin_size)" | bc -l));
      list+="$var,"
   done
   var=$(printf %.4f $(echo "($lower_bound+$i*($upper_bound-$lower_bound)/$bin_size)" | bc -l));
   list+="$var"
   export variable
   export x="$list"
   echo $list

   #boolean for histogramming type
   single_var="True"
   export single_var

   #run by run versus single run plot
   if [ $answer == 'no' ]
   then
      for rn_number in $run_list
      do
         export rn_number
         python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"_$rn_number --directory /ceph/moh/CROWN_samples/EarlyRun3_V11/ntuples --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection --era 2018 --num-processes 4 --num-threads 4 --optimization-level 1 --control-plots --control-plot-set $variable --ntuple_type crown --skip-systematic-variations
      done
   else
      python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"_run --directory /ceph/moh/CROWN_samples/EarlyRun3_V11/ntuples --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection --era 2018 --num-processes 4 --num-threads 4 --optimization-level 1 --control-plots --control-plot-set $variable --ntuple_type crown --skip-systematic-variations
   fi