#!/bin/sh
   #answers like mm,ee,mmet,emet
   echo Please enter a channel:
   read channel

   #answer is yes or no
   echo Are you making a single run plot?:
   read answer

   #creating the run list
   run_list="355443 355444 355445 355558 355559 355679 355680 355768 355769 done"
   lumi_list="1.971790835 1.243983634 1.537414347 11.7548517 6.878012741 1.078718626 46.78980232 1.222612315 16.16789967 done"
   echo Your run list has these numbers: $run_list
   echo Your lumi list has these numbers: $lumi_list

   #to use these variables in python
   export channel
   export answer

   #puts the lists into a temporary text file so both histogramming and plotting can see them
   echo "${run_list}" > ./run_list.txt
   echo "${lumi_list}" > ./lumi_list.txt

   #variables by channel (this can be changed to fit what variables you want plotted)
   if [ $channel == 'mm' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,nTrackerLayers_1_barrel,nTrackerLayers_1_endcap,nTrackerLayers_2_barrel,nTrackerLayers_2_endcap,nStations_1_barrel,nStations_2_barrel,nStations_1_endcap,nStations_2_endcap,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'mmet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,nTrackerLayers_1_barrel_pos,nTrackerLayers_1_barrel_neg,nTrackerLayers_1_endcap_pos,nTrackerLayers_1_endcap_neg,nStations_1_barrel_pos,nStations_1_barrel_neg,nStations_1_endcap_pos,nStations_1_endcap_neg,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"

   elif [ $channel == 'ee' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,deltaetaSC_1_barrel_nv015,deltaetaSC_2_barrel_nv015,deltaetaSC_1_endcap_nv015,deltaetaSC_2_endcap_nv015,eInvMinusPInv_1_barrel_nv015,eInvMinusPInv_2_barrel_nv015,eInvMinusPInv_1_endcap_nv015,eInvMinusPInv_2_endcap_nv015,hoe_1_barrel_nv015,hoe_2_barrel_nv015,hoe_1_endcap_nv015,hoe_2_endcap_nv015,scEtOverPt_1_barrel_nv015,scEtOverPt_2_barrel_nv015,scEtOverPt_1_endcap_nv015,scEtOverPt_2_endcap_nv015,sieie_1_barrel_nv015,sieie_2_barrel_nv015,sieie_1_endcap_nv015,sieie_2_endcap_nv015,lostHits_1_barrel_nv015,lostHits_2_barrel_nv015,lostHits_1_endcap_nv015,lostHits_2_endcap_nv015,deltaetaSC_1_barrel_nv1530,deltaetaSC_2_barrel_nv1530,deltaetaSC_1_endcap_nv1530,deltaetaSC_2_endcap_nv1530,eInvMinusPInv_1_barrel_nv1530,eInvMinusPInv_2_barrel_nv1530,eInvMinusPInv_1_endcap_nv1530,eInvMinusPInv_2_endcap_nv1530,hoe_1_barrel_nv1530,hoe_2_barrel_nv1530,hoe_1_endcap_nv1530,hoe_2_endcap_nv1530,scEtOverPt_1_barrel_nv1530,scEtOverPt_2_barrel_nv1530,scEtOverPt_1_endcap_nv1530,scEtOverPt_2_endcap_nv1530,sieie_1_barrel_nv1530,sieie_2_barrel_nv1530,sieie_1_endcap_nv1530,sieie_2_endcap_nv1530,lostHits_1_barrel_nv1530,lostHits_2_barrel_nv1530,lostHits_1_endcap_nv1530,lostHits_2_endcap_nv1530,deltaetaSC_1_barrel_nv3045,deltaetaSC_2_barrel_nv3045,deltaetaSC_1_endcap_nv3045,deltaetaSC_2_endcap_nv3045,eInvMinusPInv_1_barrel_nv3045,eInvMinusPInv_2_barrel_nv3045,eInvMinusPInv_1_endcap_nv3045,eInvMinusPInv_2_endcap_nv3045,hoe_1_barrel_nv3045,hoe_2_barrel_nv3045,hoe_1_endcap_nv3045,hoe_2_endcap_nv3045,scEtOverPt_1_barrel_nv3045,scEtOverPt_2_barrel_nv3045,scEtOverPt_1_endcap_nv3045,scEtOverPt_2_endcap_nv3045,sieie_1_barrel_nv3045,sieie_2_barrel_nv3045,sieie_1_endcap_nv3045,sieie_2_endcap_nv3045,lostHits_1_barrel_nv3045,lostHits_2_barrel_nv3045,lostHits_1_endcap_nv3045,lostHits_2_endcap_nv3045,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'emet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,deltaetaSC_1_barrel_pos_nv015,deltaetaSC_1_barrel_neg_nv015,eInvMinusPInv_1_barrel_pos_nv015,eInvMinusPInv_1_barrel_neg_nv015,hoe_1_barrel_pos_nv015,hoe_1_barrel_neg_nv015,scEtOverPt_1_barrel_pos_nv015,scEtOverPt_1_barrel_neg_nv015,sieie_1_barrel_pos_nv015,sieie_1_barrel_neg_nv015,lostHits_1_barrel_pos_nv015,lostHits_1_barrel_neg_nv015,deltaetaSC_1_barrel_pos_nv1530,deltaetaSC_1_barrel_neg_nv1530,eInvMinusPInv_1_barrel_pos_nv1530,eInvMinusPInv_1_barrel_neg_nv1530,hoe_1_barrel_pos_nv1530,hoe_1_barrel_neg_nv1530,scEtOverPt_1_barrel_pos_nv1530,scEtOverPt_1_barrel_neg_nv1530,sieie_1_barrel_pos_nv1530,sieie_1_barrel_neg_nv1530,lostHits_1_barrel_pos_nv1530,lostHits_1_barrel_neg_nv1530,deltaetaSC_1_barrel_pos_nv3045,deltaetaSC_1_barrel_neg_nv3045,eInvMinusPInv_1_barrel_pos_nv3045,eInvMinusPInv_1_barrel_neg_nv3045,hoe_1_barrel_pos_nv3045,hoe_1_barrel_neg_nv3045,scEtOverPt_1_barrel_pos_nv3045,scEtOverPt_1_barrel_neg_nv3045,sieie_1_barrel_pos_nv3045,sieie_1_barrel_neg_nv3045,lostHits_1_barrel_pos_nv3045,lostHits_1_barrel_neg_nv3045,deltaetaSC_1_endcap_pos_nv015,deltaetaSC_1_endcap_neg_nv015,eInvMinusPInv_1_endcap_pos_nv015,eInvMinusPInv_1_endcap_neg_nv015,hoe_1_endcap_pos_nv015,hoe_1_endcap_neg_nv015,scEtOverPt_1_endcap_pos_nv015,scEtOverPt_1_endcap_neg_nv015,sieie_1_endcap_pos_nv015,sieie_1_endcap_neg_nv015,lostHits_1_endcap_pos_nv015,lostHits_1_endcap_neg_nv015,deltaetaSC_1_endcap_pos_nv1530,deltaetaSC_1_endcap_neg_nv1530,eInvMinusPInv_1_endcap_pos_nv1530,eInvMinusPInv_1_endcap_neg_nv1530,hoe_1_endcap_pos_nv1530,hoe_1_endcap_neg_nv1530,scEtOverPt_1_endcap_pos_nv1530,scEtOverPt_1_endcap_neg_nv1530,sieie_1_endcap_pos_nv1530,sieie_1_endcap_neg_nv1530,lostHits_1_endcap_pos_nv1530,lostHits_1_endcap_neg_nv1530,deltaetaSC_1_endcap_pos_nv3045,deltaetaSC_1_endcap_neg_nv3045,eInvMinusPInv_1_endcap_pos_nv3045,eInvMinusPInv_1_endcap_neg_nv3045,hoe_1_endcap_pos_nv3045,hoe_1_endcap_neg_nv3045,scEtOverPt_1_endcap_pos_nv3045,scEtOverPt_1_endcap_neg_nv3045,sieie_1_endcap_pos_nv3045,sieie_1_endcap_neg_nv3045,lostHits_1_endcap_pos_nv3045,lostHits_1_endcap_neg_nv3045,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"
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
      python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"_run --directory /ceph/moh/CROWN_samples/EarlyRun3_V11/ntuples --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection --era 2018 --num-processes 30 --num-threads 30 --optimization-level 1 --control-plots --control-plot-set $variable_list --ntuple_type crown --skip-systematic-variations
   fi