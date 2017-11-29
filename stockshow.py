#!/usr/bin/env python#
#Script to grab stock data and display
from __future__ import print_function
import curses
from curses import wrapper
import json
import requests
import prettytable
import os.path
#import sys
import argparse
import pdb
import time
import datetime
from alpha_vantage.timeseries import TimeSeries

#Sleep time in seconds
SLEEP_TIME = 1.7
API_KEY = ' '

ts = TimeSeries(key=API_KEY)
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d")
source = 'GOOGLE'

def getCompanyList(args):
    if args.file is not None:
        if os.path.exists(args.file):
            with open(args.file) as f:
                content = f.readlines()
            content = [company.strip() for company in content]
            return content
        else:
            #return example list
            return ['NFLX', 'NVDA']
    elif args.list is not None:
        return args.list
    else:
        return ['NFLX', 'NVDA']

def parseArgs():
    parser=argparse.ArgumentParser(
            description='''Script to print stock data using google finance''',
            epilog="""Happy Trading"""
    )
    parser.add_argument('-f', '--file', type=str, help='provide filename with list of stock symbols')
    parser.add_argument('-l', '--list', nargs='+', help='provide list of stock symbols on the terminal')
    return parser.parse_args()

def getAlphaData(fin_data):
    cl = fin_data[date]['4. close']
    op = fin_data[date]['1. open']
    ch = float(cl) - float(op)
    chp = (ch / float(op) ) * 100
    return str(cl), str(op), str(ch), str(round(chp,2))

def getTable():
    args = parseArgs()

    company_list = getCompanyList(args)

    if company_list:
        tbl = prettytable.PrettyTable(["Company", "Last Price", "Opening", "Change(%)"])

    #iterate through list and get stock data
    for company in company_list:
        if source == 'GOOGLE':
            request = 'https://finance.google.com/finance?q='+company+'&output=json'
            rsp = requests.get(request)

            if rsp.status_code in (200,0):
                if "iid" in rsp.content:
                    fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
                    tbl.add_row([fin_data['name'], fin_data['l'], fin_data['op'], str(fin_data['c']+'('+fin_data['cp']+')')])
        elif source == 'ALPHA':
            fin_data, _ = ts.get_daily(company, outputsize='compact')
            cl, op, ch, chp = getAlphaData(fin_data)
            tbl.add_row([company, cl, op, str(ch+'('+chp+')')])

    return str(tbl)

def main(stdscr):
    win = curses.initscr()
    win.nodelay(1)
    while(True):
        if (win.getch() == curses.KEY_F1):
            curses.endwin()
            return
        win.clear()
        win.addstr(getTable())
        win.refresh()
        time.sleep(SLEEP_TIME)

wrapper(main)
