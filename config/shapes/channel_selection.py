from pickletools import float8
from ntuple_processor.utils import Selection

def channel_selection(channel, era):
    if "mmet" in channel:
        cuts = [
            ("(pt_1>25.)", "acceptance"),
            #("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_mu24_1)", "trg_matching"),
            ("extramuon_veto == 1", "lepton_veto"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
            #("(met_uncorrected>50.)", "met_cut"),
        ]
        return Selection(name="mmet", cuts=cuts)
    elif "emet" in channel:
        cuts = [
            ("(pt_1>33.)", "acceptance"),
    #        ("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_ele32_1)", "trg_matching"),
            ("extraelec_veto == 1", "lepton_veto"),
            ("((abs(etaSC_1) < 1.44) || (1.57 < abs(etaSC_1) < 2.5)) && ((abs(etaSC_2) < 1.44) || (1.57 < abs(etaSC_2) < 2.5))", "ECAL_cut"),
            #("(abs(eta_1) < 1.5)", "eta_cut"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
            #("(met_uncorrected>50.)", "met_cut"),
        ]
        return Selection(name="emet", cuts=cuts)
    elif "mm" in channel:
        cuts = [
            ("(pt_1>25. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("abs(eta_1) < 1.2 && abs(eta_2) < 1.2", "BB_cut"),
            #("(abs(eta_1) < 1.2 && abs(eta_2) > 1.2) || (abs(eta_2) < 1.2 && abs(eta_1) > 1.2)", "BE_cut"),
            #("(abs(eta_1) > 1.2 && abs(eta_2) > 1.2)", "EE_cut"),
            ("(m_vis > 60. && m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_mu24_1 || trg_single_mu24_2)", "trg_matching"),
        ]
        return Selection(name="mm", cuts=cuts)
    elif "ee" in channel:
        cuts = [
            ("(pt_1>33. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("((abs(eta_1 + deltaetaSC_1) < 1.44) || (1.57 < abs(eta_1 + deltaetaSC_1) < 2.5)) && ((abs(eta_2 + deltaetaSC_2) < 1.44) || (1.57 < abs(eta_2 + deltaetaSC_2) < 2.5))", "ECAL_cut"),
            #("abs(eta_1 + deltaetaSC_1) < 1.44 && abs(eta_2 + deltaetaSC_2) < 1.44", "BB_cut"),
            #("(abs(eta_1 + deltaetaSC_1) < 1.44 && abs(eta_2 + deltaetaSC_2) > 1.57) || (abs(eta_2 + deltaetaSC_2) < 1.44 && abs(eta_1 + deltaetaSC_1) > 1.57)", "BE_cut"),
            ("(abs(eta_1 + deltaetaSC_1) > 1.57 && abs(eta_2 + deltaetaSC_2) > 1.57)", "EE_cut"),
            #("(abs(eta_1) < 1.5 && abs(eta_2) < 1.5)", "eta_cut"),
            ("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_ele32_1)", "trg_matching"),
        ]
        return Selection(name="ee", cuts=cuts)
    ##need to fill in with appropriate cuts!!

    #data only since it has different trigger matching
def data_only_channel_selection(channel, era):
    if "mmet" in channel:
        cuts = [
            ("(pt_1>25.)", "acceptance"),
            ("(HLT_IsoMu24)", "trg_matching"),
            ("extramuon_veto == 1", "lepton_veto"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
        ]
        return Selection(name="mmet", cuts=cuts)
    if "emet" in channel:
        cuts = [
            ("(pt_1>29.)", "acceptance"),
            ("(trg_single_ele27_1)", "trg_matching"),
            ("extraelec_veto == 1", "lepton_veto"),
            ("(abs(eta_1) < 2.4)", "eta_cut"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
        ]
        return Selection(name="emet", cuts=cuts)
    elif "mm" in channel:
        run_list = {355443,355444,355445,355558,355559,355679,355680,355768,355769}
        cuts = [
            ("(pt_1>25. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("abs(eta_1) < 1.2 && abs(eta_2) < 1.2", "BB_cut"),
            #("(abs(eta_1) < 1.2 && abs(eta_2) > 1.2) || (abs(eta_2) < 1.2 && abs(eta_1) > 1.2)", "BE_cut"),
            #("(abs(eta_1) > 1.2 && abs(eta_2) > 1.2)", "EE_cut"),
            ("(run in run_list)", "run_cut"),
            ("(m_vis > 60. && m_vis < 120.)", "Z_mass_window"),
            ("(HLT_IsoMu24)", "trg_matching"),
        ]
        return Selection(name="mm", cuts=cuts)
    elif "ee" in channel:
        run_list = {355443,355444,355445,355558,355559,355679,355680,355768,355769}
        cuts = [
            ("(pt_1>29. && pt_2>29. && abs(eta_1)<2.4 && abs(eta_2)<2.4)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("((abs(eta_1 + deltaetaSC_1) < 1.44) || (1.57 < abs(eta_1 + deltaetaSC_1) < 2.5)) && ((abs(eta_2 + deltaetaSC_2) < 1.44) || (1.57 < abs(eta_2 + deltaetaSC_2) < 2.5))", "ECAL_cut"),
            #("abs(eta_1 + deltaetaSC_1) < 1.44 && abs(eta_2 + deltaetaSC_2) < 1.44", "BB_cut"),
            #("(abs(eta_1 + deltaetaSC_1) < 1.44 && abs(eta_2 + deltaetaSC_2) > 1.57) || (abs(eta_2 + deltaetaSC_2) < 1.44 && abs(eta_1 + deltaetaSC_1) > 1.57)", "BE_cut"),
            ("(abs(eta_1 + deltaetaSC_1) > 1.57 && abs(eta_2 + deltaetaSC_2) > 1.57)", "EE_cut"),
            ("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_ele27_1 || trg_single_ele27_2)", "trg_matching"),
        ]
        return Selection(name="ee", cuts=cuts)
