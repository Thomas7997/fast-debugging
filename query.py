import argparse
import requests
from os import getcwd

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--question", help="The question related to the error.")
args = parser.parse_args()

qcontent = ""

if args.question :
    qcontent = args.question
else :
    print("Waiting for the question content ...")

x = requests.get(f'https://www.google.com/search?q={qcontent}')

p = f"{getcwd()}/pages"

f = open(f"{p}/index.html", "w")
f.write(x.text)
f.close()