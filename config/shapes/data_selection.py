from ntuple_processor.utils import Selection
import os


"""Base processes

List of base processes, mostly containing only weights:
    - triggerweight
    - triggerweight_emb
    - tau_by_iso_id_weight
    - ele_hlt_Z_vtx_weight
    - ele_reco_weight
    - aiso_muon_correction
    - lumi_weight
    - MC_base_process_selection
    - DY_base_process_selection
    - TT_process_selection
    - VV_process_selection
    - W_process_selection
    - HTT_base_process_selection
    - HTT_process_selection
    - HWW_process_selection
"""

file_name = "temp.txt"
lumi_file_name = "lumi.txt"
text = open(file_name, "r")
text_1 = open(lumi_file_name, "r")
run_listy = text.read()
lumi_listy = text_1.read()
text.close()
text_1.close()
print(run_listy)
print(type(run_listy))

def Convert(string):
    li = list(string.split(" "))
    return li

run_list = (Convert(run_listy))
run_list = run_list[:-1]
print(run_list)
print(type(run_list))

def Convert(string):
    li = list(string.split(" "))
    return li

lumi_list = (Convert(lumi_listy))
lumi_list = lumi_list[:-1]

run_lumi = {run_list[i]: float(lumi_list[i]) for i in range(len(run_list))}

def lumi_weight(era, run_numb):
    return ("{}".format(1./(run_lumi[run_numb])), "lumi")

def group_lumi_weight(era, run_list):
    sum_lumi = 0
    print(run_list)
    for run_numb in run_list:
        sum_lumi+=run_lumi[run_numb]
    print("HERE IS THE SUM LUMI: ", sum_lumi)
    return ("{}".format(1./sum_lumi), "lumi")

def data_base_process_selection(channel, era, run_numb):
    if channel in ["mmet"]:
        data_base_process_weights = [
            lumi_weight(era, run_numb),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["emet"]:
        data_base_process_weights = [
            lumi_weight(era, run_numb),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["mm"]:
        data_base_process_weights = [
            lumi_weight(era, run_numb),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["ee"]:
        data_base_process_weights = [
            lumi_weight(era, run_numb),
        ]
        return Selection(name="data base", weights=data_base_process_weights)

def data_base_group_process_selection(channel, era, run_list):
    if channel in ["mmet"]:
        data_base_process_weights = [
            group_lumi_weight(era, run_list),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["emet"]:
        data_base_process_weights = [
            group_lumi_weight(era, run_list),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["mm"]:
        data_base_process_weights = [
            group_lumi_weight(era, run_list),
        ]
        return Selection(name="data base", weights=data_base_process_weights)
    elif channel in ["ee"]:
        data_base_process_weights = [
            group_lumi_weight(era, run_list),
        ]
        return Selection(name="data base", weights=data_base_process_weights)

def data_process_selection(channel, era, run_numb):
    data_process_weights = data_base_process_selection(channel, era, run_numb).weights
    return Selection(name="scale_1_pb", weights=data_process_weights)

def data_group_process_selection(channel, era, run_list):
    data_process_weights = data_base_group_process_selection(channel, era, run_list).weights
    return Selection(name="scale_1_pb", weights=data_process_weights)

