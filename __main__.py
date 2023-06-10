import argparse
import requests
from os import getcwd

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--question", help="The question related to the error.")
parser.add_argument("question_content")
args = parser.parse_args()

qcontent = ""

if args.question and args.question_content :
    qcontent = args.question_content
else :
    print("Waiting for the question content ...")

x = requests.get(f'https://www.google.com?q={qcontent}')

p = f"{getcwd()}/pages"

f = open(f"{p}/index.html", "w")
f.write(x.content)
f.close()