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

def Convert(string):
  li = list(string.split(" "))
  return li

lumi_list = (Convert(lumi_listy))
lumi_list = lumi_list[:-1]

"""run_lumi = {
    "323775": 0.046767743,
    "323778": 0.270935867,
    "323790": 0.276737455,
    "323794": 0.016056603,
    "323841": 0.155038205,
    "323857": 0.095513180,
    "323940": 0.426706208,
    "323954": 0.015140930,
}"""

print("HEEE", len(run_list))
print(run_list)
print("HEEE",len(lumi_list))
run_lumi = {run_list[i]: lumi_list[i] for i in range(len(run_list))}

def lumi_weight(era):
    if era == "2016":
        lumi = "35.87"
    elif era == "2017":
        lumi = "41.529"
    elif era == "2018":
        # FIXME: testing with Run2018D only
        # lumi = "31.75"
        # lumi = "13.98"  # Run2018A
        lumi = "0.001"
        #lumi = run_lumi[run_numb]
    else:
        raise ValueError("Given era {} not defined.".format(era))
    return ("{} * 1000.0".format(lumi), "lumi")


def MC_base_process_selection(channel, era):
    if channel in ["mmet"]:
        MC_base_process_weights = [
            ("genweight*sumwWeight*crossSectionPerEventWeight", "normWeight"),
            #("puweight", "puweight"),
            #("id_wgt_mu_1", "idweight"),
            #("iso_wgt_mu_1", "isoweight"),
           # ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
            lumi_weight(era),
        ]
        return Selection(name="MC base", weights=MC_base_process_weights)
    elif channel in ["emet"]:
        MC_base_process_weights = [
            ("genweight*sumwWeight*crossSectionPerEventWeight", "normWeight"),
            #("puweight", "puweight"),
            #("id_wgt_ele_wpmedium_1", "idweight"),
            # ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
            lumi_weight(era),
        ]
        return Selection(name="MC base", weights=MC_base_process_weights)
    elif channel in ["mm"]:
        MC_base_process_weights = [
            ("genweight*sumwWeight*crossSectionPerEventWeight", "normWeight"),
            #("puweight", "puweight"),
            #("id_wgt_mu_1*id_wgt_mu_2", "idweight"),
            #("iso_wgt_mu_1*iso_wgt_mu_2", "isoweight"),
            # ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
            lumi_weight(era),
        ]
        return Selection(name="MC base", weights=MC_base_process_weights)
    elif channel in ["ee"]:
        MC_base_process_weights = [
            ("genweight*sumwWeight*crossSectionPerEventWeight", "normWeight"),
            ("puweight", "puweight"),
            ("id_wgt_ele_wpmedium_1*id_wgt_ele_wpmedium_2", "idweight"),
            # ("numberGeneratedEventsWeight", "numberGeneratedEventsWeight"),
            lumi_weight(era),
        ]
        return Selection(name="MC base", weights=MC_base_process_weights)


def DY_process_selection(channel, era):
    DY_process_weights = MC_base_process_selection(channel, era).weights
    DY_process_weights.append(
        ("6372.24/6077.22", "XS13p6TeV")
    )
    cuts = None
    if channel in ["mm", "ee"]:
        cuts = [
            ("(gen_match_1 != 15 && gen_match_2 != 15)", "tautauFilter")
        ]
    return Selection(name="DY", cuts=cuts, weights=DY_process_weights)


def TT_process_selection(channel, era):
    TT_process_weights = MC_base_process_selection(channel, era).weights
    TT_process_weights.append(
        ("920.92/831.76", "XS13p6TeV")
    )
    return Selection(name="TT", weights=TT_process_weights)


def VV_process_selection(channel, era):
    VV_process_weights = MC_base_process_selection(channel, era).weights
    return Selection(name="VV", weights=VV_process_weights)


def W_process_selection(channel, era):
    W_process_weights = MC_base_process_selection(channel, era).weights
    return Selection(name="W", weights=W_process_weights)


def ZL_process_selection(channel):
    return Selection(name="ZL", weights=[("1.0", "zl_weight")])


def TTL_process_selection(channel):
    return Selection(name="TTL", weights=[("1.0", "ttl_weight")])


def VVL_process_selection(channel):
    return Selection(name="VVL", weights=[("1.0", "vvl_weight")])
