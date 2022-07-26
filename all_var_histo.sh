#!/bin/sh
   echo Please enter a channel:
   read channel
   echo Are you making a single run plot?:
   read answer

   #creating the run list
   run_list="355443 355444 355445 355558 355559 355679 355680 355768 355769 done"
   lumi_list="1.971790835 1.243983634 1.537414347 11.7548517 6.878012741 1.078718626 46.78980232 1.222612315 16.16789967 done"
   echo Your run list has these numbers: $run_list
   echo Your lumi list has these numbers: $lumi_list
   export channel
   export answer
   echo "${run_list}" > ./temp.txt
   echo "${lumi_list}" > ./lumi.txt

   #variables by channel
   if [ $channel == 'mm' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,nTrackerLayers_1_barrel,nTrackerLayers_1_endcap,nTrackerLayers_2_barrel,nTrackerLayers_2_endcap,nStations_1_barrel,nStations_2_barrel,nStations_1_endcap,nStations_2_endcap,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'mmet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,nTrackerLayers_1_barrel_pos,nTrackerLayers_1_barrel_neg,nTrackerLayers_1_endcap_pos,nTrackerLayers_1_endcap_neg,nStations_1_barrel_pos,nStations_1_barrel_neg,nStations_1_endcap_pos,nStations_1_endcap_neg,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"

   elif [ $channel == 'ee' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,deltaetaSC_1_barrel,deltaetaSC_2_barrel,eInvMinusPInv_1_barrel,eInvMinusPInv_2_barrel,hoe_1_barrel,hoe_2_barrel,scEtOverPt_1_barrel,scEtOverPt_2_barrel,sieie_1_barrel,sieie_2_barrel,lostHits_1_barrel,lostHits_2_barrel,deltaetaSC_1_endcap,deltaetaSC_2_endcap,eInvMinusPInv_1_endcap,eInvMinusPInv_2_endcap,hoe_1_endcap,hoe_2_endcap,scEtOverPt_1_endcap,scEtOverPt_2_endcap,sieie_1_endcap,sieie_2_endcap,lostHits_1_endcap,lostHits_2_endcap,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'emet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,deltaetaSC_1_barrel_pos,deltaetaSC_1_barrel_neg,eInvMinusPInv_1_barrel_pos,eInvMinusPInv_1_barrel_neg,hoe_1_barrel_pos,hoe_1_barrel_neg,scEtOverPt_1_barrel_pos,scEtOverPt_1_barrel_neg,sieie_1_barrel_pos,sieie_1_barrel_neg,lostHits_1_barrel_pos,lostHits_1_barrel_neg,deltaetaSC_1_endcap_pos,deltaetaSC_1_endcap_neg,eInvMinusPInv_1_endcap_pos,eInvMinusPInv_1_endcap_neg,hoe_1_endcap_pos,hoe_1_endcap_neg,scEtOverPt_1_endcap_pos,scEtOverPt_1_endcap_neg,sieie_1_endcap_pos,sieie_1_endcap_neg,lostHits_1_endcap_pos,lostHits_1_endcap_neg,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"
   fi

   #boolean for histogramming type
   single_var="False"
   export single_var

   export variable_list
   #run by run versus single run plot
   if [ $answer == 'no' ]
   then
      for rn_number in $run_list
      do
         export rn_number
         python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"_$rn_number --directory /ceph/moh/CROWN_samples/EarlyRun3_V11/ntuples --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection --era 2018 --num-processes 4 --num-threads 4 --optimization-level 1 --control-plots --control-plot-set $variable_list --ntuple_type crown --skip-systematic-variations
      done
   else
      python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"_run --directory /ceph/jheitkoetter/for_ellison/ntuples_small --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection --era 2018 --num-processes 4 --num-threads 4 --optimization-level 1 --control-plots --control-plot-set $variable_list --ntuple_type crown --skip-systematic-variations
   fi