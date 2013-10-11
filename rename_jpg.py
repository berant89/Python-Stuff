import os
import re

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

def getjpgfiles(files):
	dirList = os.listdir(".")
	for fname in dirList:
		if ".jpg" in fname:
			files.append(fname)

def rename_files(files, name):
    number = 1
    for filename in files:
        os.rename(filename, name+str(number)+".jpg")
        number += 1

def print_files(files):
    for fname in files:
        print fname

if __name__ == '__main__':
	files = []
	message = "Type a new name then hit enter or just hit enter (no .jpg)"
	getjpgfiles(files)
	sort_nicely(files)
	print_files(files)
	name = str(raw_input(message))
	rename_files(files, name)
