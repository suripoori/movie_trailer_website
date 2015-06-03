__author__ = 'Suraj'
import urllib

def read_text(textfile):
    with open(textfile) as f:
        content = f.read()
        check_profanity(content)


def check_profanity(text_to_check):
    conn = urllib.open("http://www.wdyl.com/profanity?q=" + text_to_check)
    output = conn.read()
    conn.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no swear words")
    else:
        print("Something went wrong... could not scan properly")
