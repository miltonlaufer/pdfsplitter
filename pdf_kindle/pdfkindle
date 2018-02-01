#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Based on http://stackoverflow.com/a/15741856/1301753

import copy
import sys
import math
import os
import re

try:
	import PyPDF2 as pPDF
except: 
	print "Package PyPDF2 not installed, try 'pip install PyPDF2' or 'sudo apt-get install python-pypdf2'"
	print "Trying with pyPDF..."
	try: 
		import pyPdf as pPDF
	except:
		print "Package pyPDF not installed either. Please install it in order to use this script"
		quit()


def split_pages(src, dst, rotate=0):
    src_f = file(src, 'r+b')
    dst_f = file(dst, 'w+b')

    try:
    	inputf = pPDF.PdfFileReader(src_f, strict=False)
    except: 
	print "There was a problem reading your PDF file. Try printing the original file as a new pdf (using system's pdf reader, for instance) and using that output here."
    	return False

    output = pPDF.PdfFileWriter()

    for i in range(inputf.getNumPages()):
	try:
        	p = inputf.getPage(i)
    	except: 
		print "There was a problem reading your PDF file. Try printing the original file as a new pdf (using system's pdf reader, for instance) and using its output again here."
    		return False
	
	if rotate>0:
	    	p.rotateClockwise(rotate)
        
	q = copy.copy(p)
        q.mediaBox = copy.copy(p.mediaBox)

        x1, x2 = p.mediaBox.lowerLeft
        x3, x4 = p.mediaBox.upperRight

        x1, x2 = math.floor(x1), math.floor(x2)
        x3, x4 = math.floor(x3), math.floor(x4)
        x5, x6 = math.floor(x3/2), math.floor(x4/2)

        if x3 > x4:
            # horizontal
            p.mediaBox.upperRight = (x5, x4)
            p.mediaBox.lowerLeft = (x1, x2)

            q.mediaBox.upperRight = (x3, x4)
            q.mediaBox.lowerLeft = (x5, x2)
        else:
            # vertical
            p.mediaBox.upperRight = (x3, x4)
            p.mediaBox.lowerLeft = (x1, x6)

            q.mediaBox.upperRight = (x3, x6)
            q.mediaBox.lowerLeft = (x1, x2)

        output.addPage(p)
        output.addPage(q)

    output.write(dst_f)
    src_f.close()
    dst_f.close()
    
    return True


input_file=""
output_file=""

print "Help: "
print "$ pdfkindle ORIGINAL.pdf"
print "or"
print "$ pdfkindle ORIGINAL.pdf FINAL.pdf"
print "or"
print "$ pdfkindle ORIGINAL.pdf rotateClockwiseINTEGER"
print "or"
print "$ pdfkindle ORIGINAL.pdf FINAL.pdf rotateClockwiseINTEGER"

print; print
print "--------------------------------------"
print "--- Verifying files ------------------"
print "--------------------------------------"

rotate=0

if len(sys.argv)==2:
	input_file=sys.argv[1]
elif len(sys.argv)==3:
	input_file=sys.argv[1]
	try:
		rotate=int(sys.argv[2])
	except:
		rotate="none"
		output_file=sys.argv[2]

elif len(sys.argv)==4:
	input_file=sys.argv[1]
	output_file=sys.argv[2]
	rotate=sys.argv[3]
else:
	input_file=raw_input("Enter the original PDF file name: ")
	output_file=raw_input("Enter the splitted PDF file name [default original_filename+'_splitted']: ")
	rotate=raw_input("OPTIONAL, if you want to rotate the PDF, enter an integer of how many degrees clockwise [default 0|90|180|270]: ")
	try:
		rotate=int(rotate)
	except:
		print;print "Only integers are accepted for the rotation value, setting it to default [0]";print
		rotate=0


while(os.path.isfile(input_file)==False):
	input_file=raw_input("Input file doesn't exist. Please, enter the original PDF file name:")



while(not isinstance(output_file,str)):
	output_file=raw_input("Please, enter a valid splitted PDF file name:")





if isinstance(rotate, int) and rotate%90!=0:
	myList=[0,90,180,270]
	rotate=min(myList, key=lambda x:abs(x-rotate))
	print "Rotation value not multiple of 90, setting to closest: "+str(rotate)


if output_file=="":
	reg = re.compile(re.escape('.pdf'), re.IGNORECASE)
	output_file=reg.sub('', input_file)+"_splitted.pdf"


if split_pages(input_file,output_file, int(rotate))==True:
	print;print
	print "--------------------------------------"
	print "--- Success! -------------------------"
	print "--------------------------------------"
else:
	print;print
	print "**************************************"
	print "*** There was an error, check    *****"
	print "*** the messsages and try again  *****"
	print "**************************************"
