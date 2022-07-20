from pickletools import float8
from ntuple_processor.utils import Selection

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

run_lumi = {run_list[i]: lumi_list[i] for i in range(len(run_list))}

def run_group_selection(initial_run, final_run):
    cuts = [
            ("run >= {} && run <= {}".format(initial_run, final_run), "run_{}_{}".format(initial_run, final_run)),
        ]
    return Selection(name=initial_run + "-" + final_run, cuts=cuts)

def run_selection(_run):
    return Selection(name=_run, cuts=[("run == {}".format(_run), _run)])