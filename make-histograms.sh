#!/bin/sh

   #enter which channel you want (mm/ee/mmet/emet)
   channel='mm'

   #if 0 then it sums the runs, if 1 you get a run by run plot
   runPlot=0

   #input the max luminosity you want runs to be grouped by (if 0 it will not group runs)
   groupRuns=0

   #luminosity of the summed runs (if you use runPlot it will not matter what number it here because it will be weighted to 1 pb-1)
   totalLuminosity=0.088645086184

   #Run numbers and correspoding luminosities you want to plot
   run_list="355443,355444,355445,355558,355559,355679,355680,355768,355769"
   lumi_list="1.971790835,1.243983634,1.537414347,11.7548517,6.878012741,1.078718626,46.78980232,1.222612315,16.16789967"

   #variables by channel (this can be changed to fit what variables you want plotted)
   if [ $channel == 'mm' ]
   then
      #variable_list='pt_1'
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,nTrackerLayers_1_barrel,nTrackerLayers_1_endcap,nTrackerLayers_2_barrel,nTrackerLayers_2_endcap,nStations_1_barrel,nStations_2_barrel,nStations_1_endcap,nStations_2_endcap,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'mmet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,\
      nTrackerLayers_1_barrel_pos,nTrackerLayers_1_barrel_neg,nTrackerLayers_1_endcap_pos,nTrackerLayers_1_endcap_neg,nStations_1_barrel_pos,nStations_1_barrel_neg,nStations_1_endcap_pos,nStations_1_endcap_neg,\
      met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"

   elif [ $channel == 'ee' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,\
      deltaetaSC_1_barrel_nv015,deltaetaSC_2_barrel_nv015,deltaetaSC_1_endcap_nv015,deltaetaSC_2_endcap_nv015,\
      eInvMinusPInv_1_barrel_nv015,eInvMinusPInv_2_barrel_nv015,eInvMinusPInv_1_endcap_nv015,eInvMinusPInv_2_endcap_nv015,\
      hoe_1_barrel_nv015,hoe_2_barrel_nv015,hoe_1_endcap_nv015,hoe_2_endcap_nv015,\
      scEtOverPt_1_barrel_nv015,scEtOverPt_2_barrel_nv015,scEtOverPt_1_endcap_nv015,scEtOverPt_2_endcap_nv015,\
      sieie_1_barrel_nv015,sieie_2_barrel_nv015,sieie_1_endcap_nv015,sieie_2_endcap_nv015,\
      lostHits_1_barrel_nv015,lostHits_2_barrel_nv015,lostHits_1_endcap_nv015,lostHits_2_endcap_nv015,\
      deltaetaSC_1_barrel_nv1530,deltaetaSC_2_barrel_nv1530,deltaetaSC_1_endcap_nv1530,deltaetaSC_2_endcap_nv1530,\
      eInvMinusPInv_1_barrel_nv1530,eInvMinusPInv_2_barrel_nv1530,eInvMinusPInv_1_endcap_nv1530,eInvMinusPInv_2_endcap_nv1530,\
      hoe_1_barrel_nv1530,hoe_2_barrel_nv1530,hoe_1_endcap_nv1530,hoe_2_endcap_nv1530,\
      scEtOverPt_1_barrel_nv1530,scEtOverPt_2_barrel_nv1530,scEtOverPt_1_endcap_nv1530,scEtOverPt_2_endcap_nv1530,\
      sieie_1_barrel_nv1530,sieie_2_barrel_nv1530,sieie_1_endcap_nv1530,sieie_2_endcap_nv1530,\
      lostHits_1_barrel_nv1530,lostHits_2_barrel_nv1530,lostHits_1_endcap_nv1530,lostHits_2_endcap_nv1530,\
      deltaetaSC_1_barrel_nv3045,deltaetaSC_2_barrel_nv3045,deltaetaSC_1_endcap_nv3045,deltaetaSC_2_endcap_nv3045,\
      eInvMinusPInv_1_barrel_nv3045,eInvMinusPInv_2_barrel_nv3045,eInvMinusPInv_1_endcap_nv3045,eInvMinusPInv_2_endcap_nv3045,\
      hoe_1_barrel_nv3045,hoe_2_barrel_nv3045,hoe_1_endcap_nv3045,hoe_2_endcap_nv3045,\
      scEtOverPt_1_barrel_nv3045,scEtOverPt_2_barrel_nv3045,scEtOverPt_1_endcap_nv3045,scEtOverPt_2_endcap_nv3045,\
      sieie_1_barrel_nv3045,sieie_2_barrel_nv3045,sieie_1_endcap_nv3045,sieie_2_endcap_nv3045,\
      lostHits_1_barrel_nv3045,lostHits_2_barrel_nv3045,lostHits_1_endcap_nv3045,lostHits_2_endcap_nv3045,\
      met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'emet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,\
      deltaetaSC_1_barrel_pos_nv015,deltaetaSC_1_barrel_neg_nv015,deltaetaSC_1_endcap_pos_nv015,deltaetaSC_1_endcap_neg_nv015,\
      eInvMinusPInv_1_barrel_pos_nv015,eInvMinusPInv_1_barrel_neg_nv015,eInvMinusPInv_1_endcap_pos_nv015,eInvMinusPInv_1_endcap_neg_nv015,\
      hoe_1_barrel_pos_nv015,hoe_1_barrel_neg_nv015,hoe_1_endcap_pos_nv015,hoe_1_endcap_neg_nv015,\
      scEtOverPt_1_barrel_pos_nv015,scEtOverPt_1_barrel_neg_nv015,scEtOverPt_1_endcap_pos_nv015,scEtOverPt_1_endcap_neg_nv015,\
      sieie_1_barrel_pos_nv015,sieie_1_barrel_neg_nv015,sieie_1_endcap_pos_nv015,sieie_1_endcap_neg_nv015,\
      lostHits_1_barrel_pos_nv015,lostHits_1_barrel_neg_nv015,lostHits_1_endcap_pos_nv015,lostHits_1_endcap_neg_nv015,\
      deltaetaSC_1_barrel_pos_nv1530,deltaetaSC_1_barrel_neg_nv1530,deltaetaSC_1_endcap_pos_nv1530,deltaetaSC_1_endcap_neg_nv1530,\
      eInvMinusPInv_1_barrel_pos_nv1530,eInvMinusPInv_1_barrel_neg_nv1530,eInvMinusPInv_1_endcap_pos_nv1530,eInvMinusPInv_1_endcap_neg_nv1530,\
      hoe_1_barrel_pos_nv1530,hoe_1_barrel_neg_nv1530,hoe_1_endcap_pos_nv1530,hoe_1_endcap_neg_nv1530,\
      scEtOverPt_1_barrel_pos_nv1530,scEtOverPt_1_barrel_neg_nv1530,scEtOverPt_1_endcap_pos_nv1530,scEtOverPt_1_endcap_neg_nv1530,\
      sieie_1_barrel_pos_nv1530,sieie_1_barrel_neg_nv1530,sieie_1_endcap_pos_nv1530,sieie_1_endcap_neg_nv1530,\
      lostHits_1_barrel_pos_nv1530,lostHits_1_barrel_neg_nv1530,lostHits_1_endcap_pos_nv1530,lostHits_1_endcap_neg_nv1530,\
      deltaetaSC_1_barrel_pos_nv3045,deltaetaSC_1_barrel_neg_nv3045,deltaetaSC_1_endcap_pos_nv3045,deltaetaSC_1_endcap_neg_nv3045,\
      eInvMinusPInv_1_barrel_pos_nv3045,eInvMinusPInv_1_barrel_neg_nv3045,eInvMinusPInv_1_endcap_pos_nv3045,eInvMinusPInv_1_endcap_neg_nv3045,\
      hoe_1_barrel_pos_nv3045,hoe_1_barrel_neg_nv3045,hoe_1_endcap_pos_nv3045,hoe_1_endcap_neg_nv3045,\
      scEtOverPt_1_barrel_pos_nv3045,scEtOverPt_1_barrel_neg_nv3045,scEtOverPt_1_endcap_pos_nv3045,scEtOverPt_1_endcap_neg_nv3045,\
      sieie_1_barrel_pos_nv3045,sieie_1_barrel_neg_nv3045,sieie_1_endcap_pos_nv3045,sieie_1_endcap_neg_nv3045,\
      lostHits_1_barrel_pos_nv3045,lostHits_1_barrel_neg_nv3045,lostHits_1_endcap_pos_nv3045,lostHits_1_endcap_neg_nv3045,\
      met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"
   fi

   #exported to use in control binning
   export channel
   export variable_list

   python shapes/produce_shapes.py --channels $channel --output-file output/earlyRun3_crown_2022_"$channel"\
   --directory /ceph/moh/CROWN_samples/EarlyRun3_V11/ntuples\
   --$channel-friend-directory /ceph/moh/CROWN_samples/EarlyRun3_V11/friends/crosssection\
   --era 2018 --num-processes 16 --num-threads 16 --optimization-level 1 --control-plots --run-plot $runPlot --group-runs $groupRuns\
   --control-plot-set $variable_list --total-lumi $totalLuminosity --run-list $run_list --lumi-list $lumi_list --ntuple_type crown --skip-systematic-variations

   