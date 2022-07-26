common_files_2018 = {
    "DY": [
        # "DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8",
        "DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X",
        # "DY1JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
        # "DY2JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
        # "DY3JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
        # "DY4JetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8",
    ],
    "TT": [
        "TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X",
        "TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_RunIISummer20UL18NanoAODv9-106X",
    ],
    "W": [
        "WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X",
        "WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X",
        "WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8_RunIISummer20UL18NanoAODv9-106X",
    ],
    #"VV": [
     #   # "WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
      #  "WW_TuneCP5_13TeV-pythia8",
       # # "WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8",
        #"WZ_TuneCP5_13TeV-pythia8",
        # "ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8",
        # "ZZTo4L_TuneCP5_13TeV_powheg_pythia8",
        #"ZZ_TuneCP5_13TeV-pythia8",
        # "ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
        # "ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8",
        # "ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
        # "ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8",
    #],"""
}

files = {
    "2018": {
        "mm": dict(
            {
                "data": [
                    "SingleMuon_Run2018A-UL2018",
                    "SingleMuon_Run2018B-UL2018",
                    "SingleMuon_Run2018C-UL2018",
                    "SingleMuon_Run2018D-UL2018",
                ],
            },
            **common_files_2018
        ),
        "ee": dict(
            {
                "data": [
                    "EGamma_Run2018A-UL2018",
                    "EGamma_Run2018B-UL2018",
                    "EGamma_Run2018C-UL2018",
                    "EGamma_Run2018D-UL2018",
                ],
            },
            **common_files_2018
        ),
        "mmet": dict(
            {
                "data": [
                    "SingleMuon_Run2018A-UL2018",
                    "SingleMuon_Run2018B-UL2018",
                    "SingleMuon_Run2018C-UL2018",
                    "SingleMuon_Run2018D-UL2018",
                ],
            },
            **common_files_2018
        ),
        "emet": dict(
            {
                "data": [
                    "EGamma_Run2018A-UL2018",
                    "EGamma_Run2018B-UL2018",
                    "EGamma_Run2018C-UL2018",
                    "EGamma_Run2018D-UL2018",
                ],
            },
            **common_files_2018
        ),
    },
    
}
