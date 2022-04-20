#
# Created by: William Winslade
# 20 April 2022
#
# PURPOSE: Run a simulation executable with arguments to test a range of values for a variable of choice
#

import csv
import subprocess as sp

# Use if you want to supress stdout from AFINES executable:
#FNULL = open(os.devnull, 'w')

inFile = open('vars_in.txt', 'r', newline='')
dataIn = csv.reader(inFile, delimiter='\t')
for lines in dataIn:
    print(lines)

inFile.close()
# argsIn =
# dirIn =

# for lines in inFile

# afines = '/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/bin/AFINES -polymer_bending_modulus ' + argsIn +' -dir ' +dirIn

# sp.call(afines, stdout=FNULL, stderr=FNULL, shell=False)