# stockshow
Show tabular stock data pulled from google finance

# installing prettytable:
    sudo easy_install prettytable
    
# Usage
usage: stockshow.py [-h] [-f FILE] [-l LIST [LIST ...]]

Script to print stock data using google finance

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  provide filename with list of stock symbols
  -l LIST [LIST ...], --list LIST [LIST ...]
                        provide list of stock symbols on the terminal

Happy Trading

# Example Output
stockshow $./stockshow.py -f company_list.txt 
+------------------------------+------------+---------+--------+
|           Company            | Last Price | Opening | Change |
+------------------------------+------------+---------+--------+
|          Apple Inc.          |   174.96   |  173.36 | +1.82  |
|         Twitter Inc          |   22.27    |  21.90  | +0.39  |
|      NVIDIA Corporation      |   214.93   |  217.00 | -0.97  |
|        Netflix, Inc.         |   196.32   |  196.58 | +0.09  |
|        Ambarella Inc         |   57.71    |  57.00  | +0.73  |
| Advanced Micro Devices, Inc. |   11.37    |  11.41  | -0.03  |
|          Tesla Inc           |   312.60   |  316.77 | -5.21  |
|     Cisco Systems, Inc.      |   36.45    |  36.70  | -0.20  |
+------------------------------+------------+---------+--------+
stockshow $


