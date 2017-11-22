#!/usr/bin/env python#
#Script to grab stock data and display
from __future__ import print_function
import json
import requests
import prettytable
import time
import sys

def getCompanyList():
    #return hard dumb list for now
    return ['NFLX', 'NVDA']

def main():
    #Read interest file or user input
    company_list = getCompanyList()

    if company_list:
        tbl = prettytable.PrettyTable(["Company", "Last Price", "Opening", "Change"])
    #iterate through list and get stock data
    for company in company_list:
        request = 'https://finance.google.com/finance?q='+company+'&output=json'
        rsp = requests.get(request)

        if rsp.status_code in (200,0):
            fin_data = json.loads(rsp.content[6:-2].decode('unicode_escape'))
            tbl.add_row([fin_data['name'], fin_data['l'], fin_data['op'], fin_data['c']])
    print(tbl)

main()
