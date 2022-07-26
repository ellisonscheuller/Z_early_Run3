#!/bin/sh
echo Please enter a channel:
read channel
echo Are you making a single run graph?
read answer
export answer
filename='temp.txt'
run_list=$(cat temp.txt)
temp_str=""

#variables by channel
   if [ $channel == 'mm' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,nTrackerLayers_1_endcap,nTrackerLayers_2_endcap,nStations_1_endcap,nStations_2_endcap,nTrackerLayers_1_barrel,nTrackerLayers_2_barrel,nStations_1_barrel,nStations_2_barrel,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   elif [ $channel == 'mmet' ]
   then
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,nTrackerLayers_1_barrel_pos,nTrackerLayers_1_barrel_neg,nTrackerLayers_1_endcap_pos,nTrackerLayers_1_endcap_neg,nStations_1_barrel_pos,nStations_1_barrel_neg,nStations_1_endcap_pos,nStations_1_endcap_neg,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"

   elif [ $channel == 'ee' ]
   then
      variable_list="pt_1,pt_2,eta_1,eta_2,phi_1,phi_2,m_vis,pt_vis,deltaetaSC_1_barrel,deltaetaSC_2_barrel,eInvMinusPInv_1_barrel,eInvMinusPInv_2_barrel,hoe_1_barrel,hoe_2_barrel,scEtOverPt_1_barrel,scEtOverPt_2_barrel,sieie_1_barrel,sieie_2_barrel,lostHits_1_barrel,lostHits_2_barrel,deltaetaSC_1_endcap,deltaetaSC_2_endcap,eInvMinusPInv_1_endcap,eInvMinusPInv_2_endcap,hoe_1_endcap,hoe_2_endcap,scEtOverPt_1_endcap,scEtOverPt_2_endcap,sieie_1_endcap,sieie_2_endcap,lostHits_1_endcap,lostHits_2_endcap,met_uncorrected,metphi_uncorrected,pfmet_uncorrected,pfmetphi_uncorrected"

   else
      variable_list="pt_1_pos,pt_1_neg,eta_1_pos,eta_1_neg,phi_1_pos,phi_1_neg,mt_uncorrected_pos,mt_uncorrected_neg,deltaetaSC_1_barrel_pos,deltaetaSC_1_barrel_neg,eInvMinusPInv_1_barrel_pos,eInvMinusPInv_1_barrel_neg,hoe_1_barrel_pos,hoe_1_barrel_neg,scEtOverPt_1_barrel_pos,scEtOverPt_1_barrel_neg,sieie_1_barrel_pos,sieie_1_barrel_neg,lostHits_1_barrel_pos,lostHits_1_barrel_neg,deltaetaSC_1_endcap_pos,deltaetaSC_1_endcap_neg,eInvMinusPInv_1_endcap_pos,eInvMinusPInv_1_endcap_neg,hoe_1_endcap_pos,hoe_1_endcap_neg,scEtOverPt_1_endcap_pos,scEtOverPt_1_endcap_neg,sieie_1_endcap_pos,sieie_1_endcap_neg,lostHits_1_endcap_pos,lostHits_1_endcap_neg,met_uncorrected_pos,met_uncorrected_neg,metphi_uncorrected_pos,metphi_uncorrected_neg,pfmet_uncorrected_pos,pfmet_uncorrected_neg,pfmetphi_uncorrected_pos,pfmetphi_uncorrected_neg"
   fi

if [ $answer == 'no' ]
then
    for rn_ber in $run_list
    do
        export rn_ber
        source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2022_"$channel"_"$rn_ber".root $variable_list $rn_ber $answer $channel earlyRun3$channel
    done
else
    source plotting/plot_shapes_control.sh 2018 output/earlyRun3_crown_2022_"$channel"_run.root $variable_list None "True" $answer $channel earlyRun3$channel
fi
