# Created by: William Winslade
# 20 April 2022
#
# PURPOSE: Run a simulation executable with arguments to test a range of values for a variable of choice
# 
# USAGE: Currently, this program is only written to change two variables when calling the simulation executable
#        If you are wanting to change more than two variables at once, the script will have to be adjusted accordingly
#        Currently, the 'vars_in.txt' file is used for inputting your variable settings. It is a comma delimited structure with
#        file in the format: variable1_input, variable2_input
#

import csv
import os
import shutil
import subprocess as sp
import sys

# Prevent erroneus execution of this script and potential for overwriting needed data files
userInput = input("Proceed with AFINES execution?\n(y/n) >> ")
if userInput != 'y':
    sys.exit('ERROR: User Aborted Execution')


# Clean Terminal
sp.call('clear')

# Use in sp.call(afines....) if you want to supress stdout from AFINES executable:
FNULL = open(os.devnull, 'w')


inFile = open('/Users/williamwinslade/Documents/GitHub/PersonalScripts/build_vars_in.txt', 'r', newline= '')
inData=[x.strip().split(',') for x in inFile]
#print(inData[0][1])
#print(range(len(inData)))


# Creates needed directories if they don't already exist
for j in range(len(inData)):
    if os.path.exists('/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/out/apr21_2/{}'.format(inData[j][0])):
        shutil.rmtree('/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/out/apr21_2/{}'.format(inData[j][0]))
    os.mkdir('/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/out/apr21_2/{}'.format(inData[j][0]))
    
    #print('DEGUG: Dir Imported: '+ (str(inData[j][1])))

# Executes simulations
for i in range(len(inData)):
    modulusIn = inData[i][0]
    dirIn = inData[i][1]
    print("\nStarting new sim with link stiffness {} and output directory ...{}".format(modulusIn, dirIn[-40:]))

    # Note: if you want to change a different variable, you'll need to change the following string accordingly:
    afines = '/Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/bin/AFINES --c /Users/williamwinslade/Documents/Xcode/researchMaster/AFINES/in/casesForApril7/april_7_in_2.cfg --polymer_bending_modulus 1 --p_motor_stiffness ' + modulusIn +' --dir ' + dirIn
    # print("DEBUG: Command determined: {}".format(afines))

    # Calls executable with specified inputs from array
    sp.call(afines, shell=True, stdout=FNULL, stderr=FNULL)

    print("\nCompleted Simulation {} of {}".format((i+1), len(inData)))

print('\n >> Program completed, see user-defined output directories for sim data\n')