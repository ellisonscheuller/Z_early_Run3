#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Dumbledraw.dumbledraw as dd
import Dumbledraw.rootfile_parser_inputshapes as rootfile_parser
import Dumbledraw.styles as styles
import ROOT
import argparse
import copy
import yaml
import os

import logging

logger = logging.getLogger("")
from multiprocessing import Pool
from multiprocessing import Process
import multiprocessing

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Plot categories using Dumbledraw from shapes produced by shape-producer module."
    )
    parser.add_argument(
        "-l", "--linear", action="store_true", help="Enable linear x-axis"
    )
    parser.add_argument("-e", "--era", type=str, required=True, help="Era")
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="ROOT file with shapes of processes",
    )
    parser.add_argument(
        "--variables",
        type=str,
        default=None,
        help="Enable control plotting for given variable",
    )
    parser.add_argument(
        "--category-postfix",
        type=str,
        default=None,
        help="Enable control plotting for given category_postfix. Structure of a category: <variable>_<postfix>",
    )
    parser.add_argument(
        "--match_data", 
        type=str,
        default="True",
        help=""
    )
    parser.add_argument(
        "--run-plot",
        type=str,
        default="no",
        help="Makes a full run plot if it is true.",
    )
    parser.add_argument(
        "--channels",
        type=str,
        default=None,
        help="Enable control plotting for given variable",
    )
    parser.add_argument(
        "--normalize-by-bin-width",
        action="store_true",
        help="Normelize plots by bin width",
    )
    parser.add_argument(
        "--fake-factor", action="store_true", help="Fake factor estimation method used"
    )
    parser.add_argument(
        "--embedding", action="store_true", help="Fake factor estimation method used"
    )
    parser.add_argument(
        "--draw-jet-fake-variation",
        type=str,
        default=None,
        help="Draw variation of jetFakes or QCD in derivation region.",
    )
    parser.add_argument(
        "--blinded", action="store_true", help="if true, no data is plottet"
    )
    parser.add_argument(
        "--tag", type=str, default=None, help="plots are stored in plots/tag/"
    )

    return parser.parse_args()


def setup_logging(output_file, level=logging.DEBUG):
    logger.setLevel(level)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    file_handler = logging.FileHandler(output_file, "w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

file_name = "run_group.txt"
text = open(file_name, "r")
run_listy = text.read()
text.close()
print(run_listy)
print(type(run_listy))

def Convert(string):
  li = list(string.split(" "))
  return li

run_list = (Convert(run_listy))
run_list = run_list[:-1]

print("THIS IS THE LIST: ", run_list)

def main(info):
    args = info["args"]
    variable = info["variable"]
    channel = info["channel"]
    channel_dict = {
        "ee": "#font[42]{#scale[0.85]{ee}}",
        "emet": "#scale[0.85]{e} met",
        "mmet": "#mu met",
        "em": "#scale[0.85]{e}#mu",
        "et": "#font[42]{#scale[0.85]{e}}#tau_{#font[42]{h}}",
        "mm": "#mu#mu",
        "mt": "#mu#tau_{#font[42]{h}}",
        "tt": "#tau_{#font[42]{h}}#tau_{#font[42]{h}}",
    }
    if args.run_plot == "no":
        run_numb = (os.environ["rn_ber"])
        print(run_numb)
        print(type(run_numb))
    if args.linear == True:
        split_value = 0.1
    else:
        if args.normalize_by_bin_width:
            split_value = 10001
        else:
            split_value = 101

    split_dict = {c: split_value for c in ["et", "mt", "tt", "em", "mm", "mmet", "emet", "ee"]}

    bkg_processes = [
        "VVL",
        "TTL",
        "ZL",
        "jetFakesEMB",
        "EMB",
        "HTT",
    ]  # "ggH125", "qqH125"

    if not args.fake_factor and args.embedding:
        bkg_processes = ["QCDEMB", "VVL", "VVJ", "W", "TTL", "TTJ", "ZJ", "ZL", "EMB"]
    if not args.embedding and args.fake_factor:
        bkg_processes = ["VVT", "VVL", "TTT", "TTL", "ZL", "jetFakes", "ZTT"]
    if not args.embedding and not args.fake_factor:
        bkg_processes = [
            # "VVL",
            "W",
            "TTL",
            "ZL",
        ]
    if args.draw_jet_fake_variation is not None:
        bkg_processes = ["VVL", "TTL", "ZL", "EMB"]
        if not args.fake_factor and args.embedding:
            bkg_processes = ["VVL", "VVJ", "W", "TTL", "TTJ", "ZJ", "ZL", "EMB"]
        if not args.embedding and args.fake_factor:
            bkg_processes = ["VVT", "VVL", "TTT", "TTL", "ZL", "ZTT"]
        if not args.embedding and not args.fake_factor:
            bkg_processes = [
                "VV",
                "W",
                "TTT",
                "TTL",
                "TTJ",
                "ZJ",
                "ZL",
                "ZTT",
            ]
    all_bkg_processes = [b for b in bkg_processes]
    legend_bkg_processes = copy.deepcopy(bkg_processes)
    legend_bkg_processes.reverse()
    if "2016" in args.era:
        era = "Run2016"
    elif "2017" in args.era:
        era = "Run2017"
    elif "2018" in args.era:
        era = "Run2018"
    else:
        logger.critical("Era {} is not implemented.".format(args.era))
        raise Exception

    category = "_".join([channel, variable])
    if args.category_postfix is not None:
        category += "_%s" % args.category_postfix
    rootfile = rootfile_parser.Rootfile_parser(args.input, variable)
    bkg_processes = [b for b in all_bkg_processes]
    if "em" in channel:
        if not args.embedding:
            bkg_processes = ["QCD", "VVT", "VVL", "W", "TTT", "TTL", "ZL", "ZTT"]
        if args.embedding:
            bkg_processes = ["QCDEMB", "VVL", "W", "TTL", "ZL", "EMB"]
        if args.draw_jet_fake_variation is not None:
            if not args.embedding:
                bkg_processes = ["VVT", "VVL", "W", "TTT", "TTL", "ZL", "ZTT"]
            if args.embedding:
                bkg_processes = ["VVL", "W", "TTL", "ZL", "EMB"]

    if "mmet" in channel:
        #bkg_processes = ["ZL", "TTL"]
        bkg_processes = ["ZL", "TTL", "W"]
        # bkg_processes = ["VVL", "W", "TTL", "ZL"]
    elif "emet" in channel:
        bkg_processes = ["ZL", "TTL", "W"]
        # bkg_processes = ["VVL", "W", "TTL", "ZL"]
    elif "mm" in channel:
        bkg_processes = ["TTL", "ZL"]
        #bkg_processes = ["W", "TTL", "ZL"]
        # bkg_processes = ["VVL", "W", "TTL", "ZL"]
    elif "ee" in channel:
        bkg_processes = ["W", "TTL", "ZL"]
        # bkg_processes = ["VVL", "W", "TTL", "ZL"]

    legend_bkg_processes = copy.deepcopy(bkg_processes)
    legend_bkg_processes.reverse()

    # create plot
    width = 600
    if args.linear == True:
        plot = dd.Plot([0.3, [0.3, 0.28]], "ModTDR", r=0.04, l=0.14, width=width)
    else:
        plot = dd.Plot([0.5, [0.3, 0.28]], "ModTDR", r=0.04, l=0.14, width=width)

    # get background histograms
    total_bkg = None
    if args.draw_jet_fake_variation is None:
        stype = "Nominal"
    else:
        stype = args.draw_jet_fake_variation
    for index, process in enumerate(bkg_processes):
        if index == 0:
            total_bkg = rootfile.get(
                channel, process, args.category_postfix, shape_type=stype
            ).Clone()
            plot.add_hist(
                rootfile.get(channel, process, args.category_postfix, shape_type=stype),
                process,
                "bkg",
            )
        else:
            if process == "HTT":
                HTT = rootfile.get(
                    channel, "ggH125", args.category_postfix, shape_type=stype
                ).Clone()
                HTT.Add(
                    rootfile.get(
                        channel, "qqH125", args.category_postfix, shape_type=stype
                    )
                )
                total_bkg.Add(HTT)
                plot.add_hist(HTT, "HTT", "bkg")
            else:
                total_bkg.Add(
                    rootfile.get(
                        channel, process, args.category_postfix, shape_type=stype
                    )
                )
                plot.add_hist(
                    rootfile.get(
                        channel, process, args.category_postfix, shape_type=stype
                    ),
                    process,
                    "bkg",
                )

        plot.setGraphStyle(process, "hist", fillcolor=styles.color_dict[process])

    plot.add_hist(total_bkg, "total_bkg")

    if args.run_plot == "yes":
        for index, category in enumerate(run_list):
            print("PROCESS VALUES: ", category)
            plot.add_hist(
                rootfile.get(channel, "data", category + "-scale_1_pb", shape_type=stype),
                category,
            )
            #plot.setGraphStyle(category, "hist", markercolor=styles.color_dict[category])
            
        #plot.create_stack(run_list, "data_stack")

        draw_list = list()

        for i in run_list:
            if args.match_data == "True":
                data_norm = plot.subplot(0).get_hist(i).Integral()
                entry_number = plot.subplot(0).get_hist(i).GetEntries()
                if entry_number > 50:
                    print(str(entry_number) + " " + i)
                    draw_list.append(i)
                mc_norm = plot.subplot(0).get_hist("total_bkg").Integral()
                assert mc_norm > 0.
                plot.subplot(0).get_hist("total_bkg").Scale(1/mc_norm)
                plot.subplot(1).get_hist("total_bkg").Scale(1/mc_norm)
                plot.subplot(2).get_hist("total_bkg").Scale(1/mc_norm)
                if data_norm != 0:
                    plot.subplot(0).get_hist(i).Scale(1/data_norm)
                    plot.subplot(1).get_hist(i).Scale(1/data_norm)
                    plot.subplot(2).get_hist(i).Scale(1/data_norm)
                for _proc in bkg_processes:
                    plot.subplot(0).get_hist(_proc).Scale(1/mc_norm)
                    plot.subplot(1).get_hist(_proc).Scale(1/mc_norm)
                    plot.subplot(2).get_hist(_proc).Scale(1/mc_norm)
            else:
                #data_norm = plot.subplot(0).get_hist(i).Integral()
                plot.subplot(0).get_hist(i).GetXaxis().SetMaxDigits(4) 
                entry_number = plot.subplot(0).get_hist(i).GetEntries()
                if entry_number > 50:
                    print(str(entry_number) + " " + i)
                    draw_list.append(i)
            if args.blinded:
                plot.subplot(0).setGraphStyle(i, "e0", markercolor=styles.color_dict[i], markersize=0, linewidth=0)
                plot.subplot(0).setGraphStyle(i, "e0", markercolor=styles.color_dict[i], markersize=0, linewidth=0)
            else:
                plot.subplot(0).setGraphStyle(i, "e0", markercolor=styles.color_dict[i])
                plot.subplot(0).setGraphStyle(i, "e0", markercolor=styles.color_dict[i])
            if args.linear:
                pass
            else:
                if args.blinded:
                    plot.subplot(1).setGraphStyle(i, "e0", markersize=0, linewidth=0)
                else:
                    plot.subplot(1).setGraphStyle(i, "e0")

            plot.subplot(2).normalize([i], "total_bkg")
            plot.subplot(2).setGraphStyle(i, "e0", markercolor=styles.color_dict[i])
            plot.subplot(2).setGraphStyle(i, "e0", markercolor=styles.color_dict[i])

            # set axes limits and labels
            plot.subplot(0).setYlims(
                split_dict[channel],
                max(
                    2 * plot.subplot(0).get_hist(i).GetMaximum(),
                    split_dict[channel] * 2,
                ),
            )

    plot.subplot(2).normalize(["total_bkg"], "total_bkg")
    plot.setGraphStyle(
        "total_bkg", "e2", markersize=0, fillcolor=styles.color_dict["unc"], linecolor=0
    )
    if args.run_plot == "no":
        plot.add_hist(
            rootfile.get(channel, "data", args.category_postfix, shape_type=stype),
            "data_obs",
        )
        data_norm = plot.subplot(0).get_hist("data_obs").Integral()
        plot.subplot(0).get_hist("data_obs").GetXaxis().SetMaxDigits(4)
        if args.blinded:
            plot.subplot(0).setGraphStyle("data_obs", "e0", markersize=0, linewidth=0)
            plot.subplot(0).setGraphStyle("data_obs", "e0", markersize=0, linewidth=0)
        else:
            plot.subplot(0).setGraphStyle("data_obs", "e0")
            plot.subplot(0).setGraphStyle("data_obs", "e0")
        if args.linear:
            pass
        else:
            if args.blinded:
                plot.subplot(1).setGraphStyle("data_obs", "e0", markersize=0, linewidth=0)
            else:
                plot.subplot(1).setGraphStyle("data_obs", "e0")

        plot.subplot(2).normalize(["total_bkg", "data_obs"], "total_bkg")

        # set axes limits and labels
        plot.subplot(0).setYlims(
            split_dict[channel],
            max(
                2 * plot.subplot(0).get_hist("data_obs").GetMaximum(),
                split_dict[channel] * 2,
            ),
        )

    # stack background processes
    plot.create_stack(bkg_processes, "stack")

    # normalize stacks by bin-width
    if args.normalize_by_bin_width:
        plot.subplot(0).normalizeByBinWidth()
        plot.subplot(1).normalizeByBinWidth()

    # plot.subplot(2).setYlims(0.75, 1.55)
    plot.subplot(2).setYlims(0.00, 2)
    if channel == "mmet":
        #plot.subplot(0).setLogY()
        #ymax = plot.subplot(0).get_hist("355206").GetMaximum()
        #plot.subplot(0).setYlims(0, ymax*1.5)
        ymax_list = list()
        for i in run_list:
            ymax_list.append(plot.subplot(0).get_hist(i).GetMaximum())
        ymax = max(ymax_list)
        plot.subplot(0).setYlims(0, ymax*1.7)
        # plot.subplot(0).setXlims(50, 150)
        # plot.subplot(1).setXlims(50, 150)
        # plot.subplot(2).setXlims(50, 150)
    elif channel == "emet":
        #plot.subplot(0).setLogY()
        ymax_list = list()
        for i in run_list:
            ymax_list.append(plot.subplot(0).get_hist(i).GetMaximum())
        ymax = max(ymax_list)
        plot.subplot(0).setYlims(0, ymax*1.7)
        # plot.subplot(0).setXlims(50, 150)
        # plot.subplot(1).setXlims(50, 150)
        # plot.subplot(2).setXlims(50, 150)
    elif channel == "mm":
        #plot.subplot(0).setLogY()
        ymax_list = list()
        for i in run_list:
            ymax_list.append(plot.subplot(0).get_hist(i).GetMaximum())
        ymax = max(ymax_list)
        plot.subplot(0).setYlims(0, ymax*1.7)
        #plot.subplot(0).setYlims(0, 1)
        # plot.subplot(0).setXlims(50, 150)
        # plot.subplot(1).setXlims(50, 150)
        # plot.subplot(2).setXlims(50, 150)
    elif channel == "ee":
        #plot.subplot(0).setLogY()
        ymax_list = list()
        for i in run_list:
            ymax_list.append(plot.subplot(0).get_hist(i).GetMaximum())
        ymax = max(ymax_list)
        plot.subplot(0).setYlims(0, ymax*1.7)
        # plot.subplot(0).setXlims(50, 150)
        # plot.subplot(1).setXlims(50, 150)
        # plot.subplot(2).setXlims(50, 150)

    if args.linear != True:
        plot.subplot(1).setYlims(0.1, split_dict[channel])
        plot.subplot(1).setYlabel("")  # otherwise number labels are not drawn on axis
        #plot.subplot(1).setLogY()
    if variable != None:
        if variable in styles.x_label_dict[channel]:
            x_label = styles.x_label_dict[channel][variable]
        else:
            x_label = variable
        plot.subplot(2).setXlabel(x_label)
    else:
        plot.subplot(2).setXlabel("NN output")
    if args.normalize_by_bin_width:
        plot.subplot(0).setYlabel("dN/d(NN output)")
    else:
        plot.subplot(0).setYlabel("a.u.")

    plot.subplot(2).setYlabel("Data/MC")
    plot.subplot(2).setGrid()
    plot.scaleYLabelSize(0.8)
    plot.scaleYTitleOffset(0.8)
    plot.scaleXTitleSize(0.8)

    # draw subplots. Argument contains names of objects to be drawn in corresponding order.

    if args.run_plot == "no":
        procs_to_draw = (
            ["stack", "total_bkg", "data_obs"]
            if args.linear
            else ["stack", "total_bkg", "data_obs"]
        )
        plot.subplot(0).Draw(procs_to_draw)
        if args.linear != True:
            plot.subplot(1).Draw(["stack", "total_bkg", "data_obs"])
        plot.subplot(2).Draw(["total_bkg", "data_obs"])
    elif args.run_plot == "yes":
        path = "chi_square_data/data_outfile.csv"
        procs_to_draw = ["stack", "total_bkg"]
        for i in draw_list:
            procs_to_draw.append(i)
            print("HELLO MY NAME IS ELDER PRICE")
            print(procs_to_draw)
            plot.subplot(0).Draw(procs_to_draw)
            if args.linear != True:
                plot.subplot(1).Draw(procs_to_draw)
        plot.subplot(2).Draw(procs_to_draw[1:])
        for i in draw_list:
            #chi square 
            print("\n Run " + i + ":")
            plot.subplot(2).get_hist(i).Fit("pol0","0")

            channelname = channel
            run = i
            variablename = variable
            chi2 = str(plot.subplot(2).get_hist(i).GetFunction("pol0").GetChisquare())
            num_dof = str(plot.subplot(2).get_hist(i).GetFunction("pol0").GetNDF())
            p_0 = str(plot.subplot(2).get_hist(i).GetFunction("pol0").GetParameter(0)) + " +/- " + str(plot.subplot(2).get_hist(i).GetFunction("pol0").GetParError(0))
            str_to_write = variablename + "," + run + "," + channelname + "," + chi2 + "," + num_dof +"," + p_0 + "\n"
            if os.path.exists(path): 
                with open(path , 'a') as f:
                    f.write(str_to_write)
            else:
                with open(path , 'w') as f:
                    f.write("variable,run,channel,chi2,dof,p_0\n")
                    f.write(str_to_write)
            

    # create legends
    suffix = ["", "_top"]
    for i in range(2):
        if channel == "mmet":
            plot.add_legend(width=0.5, height=0.12)
        else:
            plot.add_legend(width=0.625, height=0.15)
        for process in legend_bkg_processes:
            plot.legend(i).add_entry(
                0,
                process,
                styles.legend_label_dict[
                    process.replace("TTL", "TT").replace("VVL", "VV").replace("NLO", "")
                ],
                "f",
            )
        plot.legend(i).add_entry(0, "total_bkg", "Bkg. stat. unc.", "f")
        if args.run_plot == "no":
            plot.legend(i).add_entry(0, "data_obs", "Observed", "PE2L")
        elif args.run_plot == "yes":
            for index in run_list:
                plot.legend(i).add_entry(0, index, "Run "+index, "PE2L")
        print("THIS CODE WORKED THIS LONG")
        plot.legend(i).setNColumns(2)
    plot.legend(0).Draw()
    plot.legend(1).setAlpha(0.0)
    plot.legend(1).Draw()

    """for i in range(2):
        plot.add_legend(reference_subplot=2, pos=1, width=0.8, height=0.06)
        if args.run_plot == "yes":
            for index in run_list:
                plot.legend(i + 2).add_entry(0, index, "Run "+ index, "PE2L")
        else:
            plot.legend(i + 2).add_entry(0, "total_bkg", "Bkg. stat. unc.", "f")
        plot.legend(i + 2).setNColumns(4)
    plot.legend(2).Draw()
    plot.legend(3).setAlpha(0.0)
    plot.legend(3).Draw()"""
    # draw additional labels
    plot.DrawCMS()
    if "2016" in args.era:
        plot.DrawLumi("35.9 fb^{-1} (2016, 13 TeV)")
    elif "2017" in args.era:
        plot.DrawLumi("41.5 fb^{-1} (2017, 13 TeV)")
    elif "2018" in args.era:
        # plot.DrawLumi("XYZ fb^{-1} (2018, 13 TeV)")
        #plot.DrawLumi( str(run_lumi[run_numb]) + " fb^{-1} (2018, 13 TeV)")
        plot.DrawLumi( "1 pb^{-1} (2022, 13.6 TeV)")
    else:
        logger.critical("Era {} is not implemented.".format(args.era))
        raise Exception

    posChannelCategoryLabelLeft = None
    plot.DrawChannelCategoryLabel(
        "%s, %s" % (channel_dict[channel], "{cat}".format(cat=args.category_postfix)),
        begin_left=posChannelCategoryLabelLeft,
    )
    # save plot
    if not args.embedding and not args.fake_factor:
        postfix = "fully_classic"
    if args.embedding and not args.fake_factor:
        postfix = "emb_classic"
    if not args.embedding and args.fake_factor:
        postfix = "classic_ff"
    if args.embedding and args.fake_factor:
        postfix = "emb_ff"
    if args.draw_jet_fake_variation is not None:
        postfix = postfix + "_" + args.draw_jet_fake_variation

    if not os.path.exists("plots/%s" % (args.tag)):
        os.makedirs("plots/%s/%s_plots_%s/%s" % (args.tag, args.era, postfix, channel))

    if args.run_plot == "yes":
        plot.save(
            "plots/%s/%s_plots_%s/%s/%s_%s_%s_%s.%s"
            % (
                args.tag,
                args.era,
                postfix,
                channel,
                args.era,
                channel,
                variable,
                "run",
                "pdf",
            )
        )
        plot.save(
            "plots/%s/%s_plots_%s/%s/%s_%s_%s_%s.%s"
            % (
                args.tag,
                args.era,
                postfix,
                channel,
                args.era,
                channel,
                variable,
                "run",
                "png",
            )
        )

    else:

        plot.save(
            "plots/%s/%s_plots_%s/%s/%s_%s_%s_%s.%s"
            % (
                args.tag,
                args.era,
                postfix,
                channel,
                args.era,
                channel,
                variable,
                args.category_postfix,
                "pdf",
            )
        )
        plot.save(
            "plots/%s/%s_plots_%s/%s/%s_%s_%s_%s.%s"
            % (
                args.tag,
                args.era,
                postfix,
                channel,
                args.era,
                channel,
                variable,
                args.category_postfix,
                "png",
            )
        )


if __name__ == "__main__":
    args = parse_arguments()
    setup_logging("{}_plot_shapes.log".format(args.era), logging.DEBUG)
    variables = args.variables.split(",")
    channels = args.channels.split(",")
    infolist = []

    if not args.embedding and not args.fake_factor:
        postfix = "fully_classic"
    if args.embedding and not args.fake_factor:
        postfix = "emb_classic"
    if not args.embedding and args.fake_factor:
        postfix = "classic_ff"
    if args.embedding and args.fake_factor:
        postfix = "emb_ff"
    for ch in channels:
        for v in variables:
            infolist.append({"args": args, "channel": ch, "variable": v})
    pool = Pool(1)
    pool.map(main, infolist)
    # for info in infolist:
    #     main(info)
