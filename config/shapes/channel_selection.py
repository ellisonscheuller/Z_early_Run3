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
            ("(abs(eta_1) < 1.5)", "eta_cut"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
            #("(met_uncorrected>50.)", "met_cut"),
        ]
        return Selection(name="emet", cuts=cuts)
    elif "mm" in channel:
        cuts = [
            ("(pt_1>25. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("(m_vis > 60. && m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_mu24_1 || trg_single_mu24_2)", "trg_matching"),
        ]
        return Selection(name="mm", cuts=cuts)
    elif "ee" in channel:
        cuts = [
            ("(pt_1>33. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("(abs(eta_1) < 1.5 && abs(eta_2) < 1.5)", "eta_cut"),
            ("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(trg_single_ele32_1)", "trg_matching"),
        ]
        return Selection(name="ee", cuts=cuts)
    ##need to fill in with appropriate cuts!!   

def data_only_channel_selection(channel, era):
    if "mmet" in channel:
        cuts = [
            ("(pt_1>25.)", "acceptance"),
            #("(m_vis > 60. &&  m_vis < 120.)", "Z_mass_window"),
            ("(HLT_IsoMu24)", "trg_matching"),
            ("extramuon_veto == 1", "lepton_veto"),
            ("(sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))>40.)", "mt_cut"),
        ]
        return Selection(name="mmet", cuts=cuts)
    if "mm" in channel:
        cuts = [
            ("(pt_1>25. && pt_2>25.)", "acceptance"),
            ("(q_1*q_2 < 0)", "opposite_charge"),
            ("(m_vis > 60. && m_vis < 120.)", "Z_mass_window"),
            ("(HLT_IsoMu24)", "trg_matching"),
        ]
        return Selection(name="mm", cuts=cuts)