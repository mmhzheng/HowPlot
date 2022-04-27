#! /usr/bin/python
# -*- coding:utf8 -*-

import os,sys 
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
sys.path.insert(0,parentdir)  
import json
from howplot import *

rcParams.update(cdf_params)


def s2d(d):
    #convert string key to tuple.
    for key in d.keys():
        try:
            d[eval(key)] = d[key]
            del d[key]
        except Exception:
            raise

def tuplize_keys(d):
    s2d(d['flow_set_ip_pair'])
    s2d(d['flow_set_5_tuple'])
    s2d(d['ip_pair_pkt_cnt_table'])
    s2d(d['5_tuple_pkt_cnt_table'])
    s2d(d['ip_pair_flow_size_table'])
    s2d(d['5_tuple_flow_size_table'])
    return d

def loadJsonToDict(js_file):
    js_dict = dict()
    with open(js_file) as js:
        js_dict = json.load(js)
    # return tuplize_keys(js_dict)
    return js_dict

if __name__ == "__main__":
    pcap_statistics = loadJsonToDict( "examples/univ1.json" )
    # for ip_pair in pcap_statistics['ip_pair_pkt_cnt_table']:
    #     ip_src = ip_pair[1]
    #     ip_dst = ip_pair[0]
    fsd = [0] * 100000
    max_size = 0
    for ftuple in pcap_statistics['5_tuple_pkt_cnt_table']:
        fsize = int(pcap_statistics['5_tuple_pkt_cnt_table'][ftuple])
        fsd[fsize] += 1
        max_size = max(max_size, fsize)
    

    summ = sum(fsd)
    x = range(max_size+1)
    # plot(x, fsd[:max_size+1], label="flow size distribution")
    for i in range(len(fsd)):
        fsd[i] = fsd[i]/summ
    y = cumsum(fsd[:max_size+1])
    plot(x, y, label="flow size distribution")
    xlabel("Flow Size")
    ylabel("Flow Num")
    # xscale("log")
    legend(loc='best')
    # Make the minor ticks and gridlines show.
    minorticks_on()
    savefig('figs/examples/cdf.pdf')

