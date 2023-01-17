from random import randint
import re
import argparse
#domain
domain = "@popolton.ac.uk"
#using regex to filter non alphabetic characters
pattern = r'[^A-Za-z0-9]+'
#generates n digits random numbers 
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))
#genereates email
def make_email(fnames,surnames,random_num):
    emails = fnames + '.' + surnames +random_num+domain
    return emails
#read file
parser = argparse.ArgumentParser()
parser.add_argument('filename')

try:
    args = parser.parse_args()
    details = []
    file = open(args.filename, "r")  # The file opened
    with file as fh:
        lines = fh.readlines()
        for line in lines:
            student_id = fname = line.split(',')[0].split()[0]
            fnames = line.split(',')[0].split()[1]
            surnames = line.split(',')[1]
            random_num = random_with_N_digits(4)
            surnames = re.sub(pattern, '', surnames)
            emails = make_email(fnames,surnames,random_num)
            students_details = student_id + ' ' + emails
            details.append(students_details)

    with open("output.txt","w") as file:
        for detail in details:
            file.write(detail+"\n")   
    print("Output.txt is Created")     


except Exception as err:
    print("Error: Missing command-line argument.")
