import argparse
import csv
import json
import sys
import os

def Main():
    #Adding input arguments
    parser = argparse.ArgumentParser(description='Interview solution for Thermistor data set')
    parser.add_argument('-c', '--CSV', metavar='', required=True, help="Indicates that the following name is of the input .csv file", type=str)
    arg = parser.parse_args()

    #Checking if the second argument to a script call has a .csv extension
    if(sys.argv[2][-1]=='v' and sys.argv[2][-2]=='s' and sys.argv[2][-3]=='c'):
        csv_start_file = sys.argv[2]
        #Making the same name to a .json file as it is for .csv file using slices
        json_name = csv_start_file[:(len(csv_start_file)-4):1]

    #Checking if there is a .csv file with a name entered as a argument to a script call
    if(not os.path.isfile('./csv_start_file')):
        #Checking if there is a .csv in input file name
        if('.csv' in sys.argv[2]):
            #Open .csv file for reading
            with open(csv_start_file, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=';')
                #Making a output dictionary for storing output temperature-resistance pairs
                output = {}
                #What few next lines of code do is they check first if a row from .csv file is a digit, check if it is in required range and divisible by 5
                # and stores those members in a dictionary called output
                for line in csv_reader:
                    if (line[0].isdigit()):
                        if((int(line[0])>=0)and(int(line[0])<=100)):
                            if(int(line[0])%5==0):
                                temp = float(line[0])
                                temp1 = float(line[2])
                                #output[temp] = line[2]
                                output[temp] = temp1
                #Using json.dump() method next lines of code is making output .json file with members that satisfies above mentioned terms
                s = json.dumps(output, indent=4, sort_keys=True)
                print(s)
            with open(json_name+'.json', 'w') as json_file:
                json.dump(output, json_file, indent=4)
        else:
            print("Not a .csv file")
        

if __name__ == '__main__':
    Main()
