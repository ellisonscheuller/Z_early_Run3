from ntuple_processor import Histogram
import os 
import numpy as np

variable_list = os.environ["variable_list"].split(",")
channel = os.environ["channel"]
control_binning = {channel:dict()}

#corresponding lists are in the order [lower_bound, upper_bound, number_of_bins]
uniformBinningDict = {
  'pt': [25, 200, 40], 
  'eta': [(-2.4), 2.4, 40], 
  'phi': [(-np.pi), (np.pi), 40], 
  'm_vis': [60, 120, 40],
  'pt_vis': [0, 200, 40],
  'mt_uncorrected': [40, 200, 40],
  'nStations': [0, 6, 6],
  'nTrackerLayers': [0, 20, 20],
  'deltaetaSC': [(-0.05), 0.05, 40],
  'eInvMinusPInv': [(-0.005), (0.005), 40],
  'hoe': [0, 0.05, 40],
  'scEtOverPt': [(-0.2), 0.05, 40],
  'sieie': [],
  'lostHits': [0,2,2],
  'met_uncorrected': [0, 200, 40],
  'metphi_uncorrected': [(-np.pi), (np.pi), 40],
  'pfmet_uncorrected': [0, 200, 40],
  'pfmetphi_uncorrected':  [(-np.pi), (np.pi), 40]
  }

#function which allows you to add new variables not in the ntuple
def renamingVariable(var):
    out = None
    base = var.replace("_barrel", "").replace("_endcap", "").replace("_pos", "").replace("_neg", "").replace("_nv015", "").replace("_nv1530", "").replace("_nv3045", "")
    idx = "1" if ("_1" in var) else "2"
    npv015 = "(0 < npvGood && npvGood <= 15)"
    npv1530 = "(15 < npvGood && npvGood <= 30)"
    npv3045 = "(30 < npvGood && npvGood < 45)"
    #ee
    if channel == "ee":
      #number of vertices
      if "_nv015" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv015)
      elif "_nv1530" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv1530)
      elif "_nv3045" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv3045)
      #barrel or endcap
      if "_barrel" in var:
          out = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.44) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.44)".format(base=base, idx=idx)
      elif "_endcap" in var:
          out = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.57) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.57)".format(base=base, idx=idx)
      else: out = variable_list[i]
    #mm
    elif channel == "mm":
      if "_barrel" in var:
          out = "{base}*(abs(eta_{idx}) < 1.2) -1e9*(abs(eta_{idx}) > 1.2)".format(base=base, idx=idx)
      elif "_endcap" in var:
          out = "{base}*(abs(eta_{idx}) > 1.2) -1e9*(abs(eta_{idx}) < 1.2)".format(base=base, idx=idx)
      else: out = variable_list[i]
    #emet
    elif channel == "emet":
      if "mt_uncorrected" in var:
        base = "sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))"
      elif "_barrel" in var:
          base = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.44) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.44)".format(base=base, idx=idx)
      elif "_endcap" in var:
          base = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.57) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.57)".format(base=base, idx=idx)
      #number of vertices
      if "_nv015" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv015)
      elif "_nv1530" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv1530)
      elif "_nv3045" in var:
        base = "{base}*({npvsel}) -1e9*(!{npvsel})".format(base=base, npvsel=npv3045)
      #charge
      if "_pos" in var:
        out = "{base}*(q_1 > 0) -1e9*(q_1 < 0)".format(base=base)
      elif "_neg" in var:
        out = "{base}*(q_1 < 0) -1e9*(q_1 > 0)".format(base=base)
    #mmet
    elif channel == "mmet":
      if "mt_uncorrected" in var:
        base = "sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))"
      elif "_barrel" in var:
          base = "{base}*(abs(eta_{idx}) < 1.2) -1e9*(abs(eta_{idx}) > 1.2)".format(base=base, idx=idx)
      elif "_endcap" in var:
          base = "{base}*(abs(eta_{idx}) > 1.2) -1e9*(abs(eta_{idx}) < 1.2)".format(base=base, idx=idx)
      #charge
      if "_pos" in var:
        out = "{base}*(q_1 > 0) -1e9*(q_1 < 0)".format(base=base)
      elif "_neg" in var:
        out = "{base}*(q_1 < 0) -1e9*(q_1 > 0)".format(base=base)

    assert out != None
    return out

for i in range(len(variable_list)):
  var_name = renamingVariable(variable_list[i])
  histo_bin_list=list()
  minimal_control_plot_set = {variable_list[i]}

  #makes the bins and bounds
  binning_base = variable_list[i].replace("_1", "").replace("_2", "").replace("_barrel", "").replace("_endcap", "").replace("_pos", "").replace("_neg", "").replace("_nv015", "").replace("_nv1530", "").replace("_nv3045", "")
  
  for k in range(0, uniformBinningDict[binning_base][2]):
    var_bin_list=uniformBinningDict[binning_base][0]+k*(uniformBinningDict[binning_base][1]- uniformBinningDict[binning_base][0])/(uniformBinningDict[binning_base][2])
    histo_bin_list.append(var_bin_list)
  
  #control binning
  control_binning[channel][variable_list[i]]=Histogram(variable_list[i], var_name, histo_bin_list)
