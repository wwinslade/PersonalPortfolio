#
# Created by: William Winslade
# 20 April 2022
#
# PURPOSE: Run a simulation executable with arguments to test a range of values for a variable of choice
#

import csv
import os
import subprocess as sp
import time

# Clean Terminal
sp.call('clear')

# Use in sp.call(afines....) if you want to supress stdout from AFINES executable:
FNULL = open(os.devnull, 'w')


inFile = open('vars_in.txt', 'r', newline= '')
inData=[x.strip().split(',') for x in inFile]
#print(inData[0][0])
#print(range(len(inData)))

for i in range(len(inData)):
    modulusIn = inData[i][0]
    dirIn = inData[i][1]
    print("\nStarting new sim with modulus {} and output directory {}".format(modulusIn, dirIn))

    # Note: if you want to change a different variable, you'll need to change the following string accordingly:
    afines = '/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/bin/AFINES --c /Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/in/casesForApril7/april_7_in_2.cfg --polymer_bending_modulus ' + modulusIn +' --dir ' +dirIn
    # print("DEBUG: Command determined: {}".format(afines))

    # Calls executable with specified inputs from array
    sp.call(afines, stdout=FNULL, stderr=FNULL, shell=True)
   
    # Waits for AFINES sim to finish execution to prevent computer overload
    time.sleep(20)
    
    print("\nCompleted Simulation {} of {}".format((i+1), len(inData)))

print('\n >> Program completed, see user-defined output directories for sim data\n')