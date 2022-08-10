
Framework to produce Control Plots

Before cloning the early Run3 analysis framework start the ssh agent:
```bash
eval $(ssh-agent)
ssh-add
```
Àfterwards checkout the early Run3 analysis framework:
```bash
git clone --recursive git@github.com:KIT-CMS/Z_early_Run3.git
```
1. setup the environment
```bash
source utils/setup_root.sh
```
2. Go to 'make-histograms.sh' and make your changes according to your histogramming desires (comments to guide in the script)
    - To define new variables not in the ntuple go to control_binning.py
    - To change the binning/bounds go to control_binning.py
    - To change the cuts go to channel_selection.py
    - To change the MC weights go to process_selection.py
    - To change the data weights (such as lumi scaling) go to data_selection.py
    - To specify new file names for each sample go to file_names.py
    - Everything else should be able to be modified in the bash script but if you want to add new features a good place to start is produce_shapes.py

3. Run the histogramming code
```bash
. make-histograms.sh
```
4. Open up a new terminal for the plotting

5. Go to 'make-plots.sh' and make your changes according to your plotting desires (comments to guide in the script)
    - To change your pdf slideshow go to presentation/control-plots-slides.tex
    - To add logos for your pdf slideshow go to /logos
    - To get your chi square data for each plot go to /chi_square_data

6. Run the plotting code
```bash
. make-plots.sh
```
