import hashlib
import argparse

usage = '''Usage examples:

        + Basic: 
            md5hashcracker.py -hashes hashes.txt -p passwordlist.txt 

        + With Output File:
            md5hashcracker.py -hashes hashes.txt -p passwordlist.txt -o 

                                            '''
parser = argparse.ArgumentParser(
    description="This script will create the hash of each password in the -p file and find the matches with the hashes provided in the -hashes file. The results with the original password of each hash will be showed once finished. ",
    epilog=usage, formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument("-hashes", dest="hashes", help="List of hashes to crack (Ex. hashes.txt)")
parser.add_argument("-p", dest="passwords", help="List of possible passwords (Ex. passwordlist.txt)")
parser.add_argument("-o", dest="output", help="Store the results in a txt file (Ex. results.txt)", default=False,
                    action="store_true")
myparams = parser.parse_args()

hashesFile = open(myparams.hashes, 'r')
passwordsFile = open(myparams.passwords, 'r')
hashes_list = hashesFile.read().splitlines()
passwords_list = passwordsFile.read().splitlines()

results = []

if myparams.output:
    resultsFile = open('results.txt', 'w')
    for hash in hashes_list:
        for password in passwords_list:
            md5password = hashlib.md5(password.encode('utf-8')).hexdigest()
            print(password + ' = ' + md5password)
            if md5password == hash:
                print(" --------------------------- PASSWORD FOUND! -----------------------------------")
                resultsFile.write(md5password + " = " + password + "\n")
                results.append(md5password + " = " + password)
                break
    print("\n[*] Cracked Hashes: \n")
    for x in results:
        print("     " + x + "\n")

    print("\n [*] All the cracked hashes have been stored in the results.txt output file!")
else:
    for hash in hashes_list:
        for password in passwords_list:
            md5password = hashlib.md5(password.encode('utf-8')).hexdigest()
            print(password + ' = ' + md5password)
            if md5password == hash:
                print(" --------------------------- PASSWORD FOUND! -----------------------------------")
                results.append(md5password + " = " + password)
                break
    print("\n[*] Cracked Hashes: \n")
    for x in results:
        print("     " + x + "\n")

