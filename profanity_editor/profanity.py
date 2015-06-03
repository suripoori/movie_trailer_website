__author__ = 'Suraj'
import urllib.request

def read_text(textfile):
    with open(textfile) as f:
        content = f.read()
        check_profanity(content)


def check_profanity(text_to_check):
    with urllib.request.urlopen("http://www.wdyl.com/profanity?q=" + text_to_check) as response:
        output = response.read()
        output_string = output.decode('ascii')
    if "true" in output_string:
        print("Profanity Alert!!!")
    elif "false" in output_string:
        print("This document has no swear words")
    else:
        print("Something went wrong... could not scan properly")
