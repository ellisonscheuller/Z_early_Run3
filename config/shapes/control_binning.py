from ntuple_processor import Histogram
import os 

var_name = (os.environ["variable"])
str_list = os.environ["x"]

def Convert(string):
  li = list(string.split(","))
  return li

histo_list = (Convert(str_list))
histo_list = list(map(float, histo_list))


minimal_control_plot_set = {var_name}


control_binning = {
  "mmet": {var_name:Histogram(var_name, var_name, histo_list)},
  "emet": {var_name:Histogram(var_name, var_name, histo_list)},
  "mt": {var_name:Histogram(var_name, var_name, histo_list)},
  "em": {var_name:Histogram(var_name, var_name, histo_list)},
  "et": {var_name:Histogram(var_name, var_name, histo_list)},
  "tt": {var_name:Histogram(var_name, var_name, histo_list)},
  "mm": {var_name:Histogram(var_name, var_name, histo_list)},
  "me": {var_name:Histogram(var_name, var_name, histo_list)},
  "ee": {var_name:Histogram(var_name, var_name, histo_list)},
}
