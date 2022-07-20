from ntuple_processor import Histogram
import os 
import numpy as np

var_name = (os.environ["variable"])
str_list = os.environ["x"]
chnn = (os.environ["channel"])

def Convert(string):
  li = list(string.split(","))
  return li

histo_list = (Convert(str_list))
histo_list = list(map(float, histo_list))

minimal_control_plot_set = {var_name}

if var_name == "mt_uncorrected":
  var_name_1 = "sqrt(2.*pt_1*met_uncorrected*(1.-cos(phi_1 - metphi_uncorrected)))"
else:
  var_name_1 = var_name

control_binning = {
    chnn: {var_name:Histogram(var_name, var_name_1, histo_list)},
    #"mm": {
    #"eta_1": Histogram("eta_1", "eta_1", [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]),
    #"eta_2": Histogram("eta_2", "eta_2", [-2.5, -2.4, -2.3, -2.2, -2.1, -2.0, -1.9, -1.8, -1.7, -1.6, -1.5, -1.4, -1.3, -1.2, -1.1, -1.0, -0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]),
    #"phi_1": Histogram("phi_1", "phi_1", np.linspace(-np.pi, np.pi, 40)),
    #"phi_2": Histogram("phi_2", "phi_2", np.linspace(-np.pi, np.pi, 40)),
    #}
  }