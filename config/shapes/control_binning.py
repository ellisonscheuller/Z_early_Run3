from ntuple_processor import Histogram
import os 
import numpy as np

single_var_str = (os.environ["single_var"])
single_var_bool = True

chnn = (os.environ["channel"])

def Convert(string):
  li = list(string.split(","))
  return li

if single_var_str == "False": single_var_bool = False

if single_var_bool:
  single_var_name = (os.environ["variable"])
  sin_bin_list = os.environ["x"]
  single_bin_list = (Convert(sin_bin_list))
  single_bin_list = list(map(float, single_bin_list))

  minimal_control_plot_set = {single_var_name}

  control_binning = {chnn: {single_var_name:Histogram(single_var_name, single_var_name, single_bin_list)}}

else:
  var_list = (os.environ["variable_list"])

  variable_list = (Convert(var_list))

  if chnn == "mm":
    lower_bound_list= [25,25,(-2.4),(-2.4),(-3.14),(-3.14),60,0,0,0,0,0,0,0,0,0,0,(-3.14),0,(-3.14)]
    upper_bound_list=[200,200,2.4,2.4,3.14,3.14,120,200,20,20,20,20,6,6,6,6,200,3.14,200,3.14]
    bin_size_list=[40,40,40,40,40,40,40,40,20,20,20,20,6,6,6,6,40,40,40,40]
  elif chnn == "ee":
    lower_bound_list= [29,29,(-2.4),(-2.4),(-3.14),(-3.14),60,0,(-0.3),(-0.1),(-0.3),(-0.1),(-0.1),(-0.1),(-0.1),(-0.1),0,0,0,0,(-0.2),(-0.2),(-0.2),(-0.2),0,0,0,0,0,0,0,0,0,(-3.14),0,(-3.14)]
    upper_bound_list=[200,200,2.4,2.4,3.14,3.14,120,200,0.3,0.1,0.3,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.2,0.2,0.2,(30*10**(-3)),(30*10**(-3)),(30*10**(-3)),(30*10**(-3)),2,2,2,2,200,3.14,200,3.14]
    bin_size_list=[40,40,40,40,40,40,40,40,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,2,2,2,2,40,40,40,40]
  elif chnn == "mmet":
    lower_bound_list= [25,25,(-2.4),(-2.4),(-3.14),(-3.14),40,40,0,0,0,0,0,0,0,0,0,0,(-3.14),(-3.14),0,0,(-3.14),(-3.14)]
    upper_bound_list=[200,200,2.4,2.4,3.14,3.14,200,200,20,20,20,20,6,6,6,6,200,200,3.14,3.14,200,200,3.14,3.14]
    bin_size_list=[40,40,40,40,40,40,40,40,20,20,20,20,6,6,6,6,40,40,40,40,40,40,40,40]
  elif chnn == "emet":
    lower_bound_list= [25,25,(-2.4),(-2.4),(-3.14),(-3.14),40,40,(-0.3),(-0.3),(-0.1),(-0.1),0,0,(-0.2),(-0.2),0,0,0,0,(-0.3),(-0.3),(-0.1),(-0.1),0,0,(-0.2),(-0.2),0,0,0,0,0,0,(-3.14),(-3.14),0,0,(-3.14),(-3.14)]
    upper_bound_list=[200,200,2.4,2.4,3.14,3.14,200,200,0.3,0.3,0.1,0.1,0.1,0.1,0.2,0.2,(30*10**(-3)),(30*10**(-3)),2,2,0.3,0.3,0.1,0.1,0.1,0.1,0.2,0.2,(30*10**(-3)),(30*10**(-3)),2,2,200,200,3.14,3.14,200,200,3.14,3.14]
    bin_size_list=[40,40,40,40,40,40,40,40,20,20,20,20,20,20,20,20,20,20,2,2,20,20,20,20,20,20,20,20,20,20,2,2,40,40,40,40,40,40,40,40]

  channel_dict = dict()
  control_binning = dict()
  control_binning[chnn] = {}
  for i in range(len(variable_list)):
    histo_list=list()
    minimal_control_plot_set = {variable_list[i]}

    def renaming(var):
      out = None
      base = var.replace("_barrel", "").replace("_endcap", "").replace("_pos", "").replace("_neg", "")
      idx = "1" if ("_1" in var) else "2"
      #ee
      if chnn == "ee":
        if "_barrel" in var:
            out = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.44) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.44)".format(base=base, idx=idx)
        elif "_endcap" in var:
            out = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.57) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.57)".format(base=base, idx=idx)
        else: out = variable_list[i]
      #mm
      elif chnn == "mm":
        if "_barrel" in var:
            out = "{base}*(abs(eta_{idx}) < 1.2) -1e9*(abs(eta_{idx}) > 1.2)".format(base=base, idx=idx)
        elif "_endcap" in var:
            out = "{base}*(abs(eta_{idx}) > 1.2) -1e9*(abs(eta_{idx}) < 1.2)".format(base=base, idx=idx)
        else: out = variable_list[i]
      #emet
      elif chnn == "emet":
        if "mt_uncorrected" in var:
          base = "sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))"
        elif "_barrel" in var:
            base = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.44) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.44)".format(base=base, idx=idx)
        elif "_endcap" in var:
            base = "{base}*(abs(eta_{idx} + deltaetaSC_{idx}) > 1.57) -1e9*(abs(eta_{idx} + deltaetaSC_{idx}) < 1.57)".format(base=base, idx=idx)
        #charge
        if "_pos" in var:
          out = "{base}*(q_1 > 0) -1e9*(q_1 < 0)".format(base=base)
        elif "_neg" in var:
          out = "{base}*(q_1 < 0) -1e9*(q_1 > 0)".format(base=base)
      #mmet
      elif chnn == "mmet":
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

    #new variables not in the ntuples
    var_name = renaming(variable_list[i])

    #makes the bins and bounds
    for k in range(0, bin_size_list[i]+1):
      var=lower_bound_list[i]+k*(upper_bound_list[i]- lower_bound_list[i])/(bin_size_list[i])
      histo_list.append(var)

    print(var_name)
    
    #control binning
    control_binning[chnn][variable_list[i]]=Histogram(variable_list[i], var_name, histo_list)