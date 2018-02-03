#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Tkinter import *
import tkFileDialog
import ntpath
import os
import re
import copy
import sys
import math

try:
    from Tkinter import *
except ImportError:
    print("Tkinter library is not available.")
    exit(0)


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


path = os.path.dirname(sys.modules[__name__].__file__)
path = os.path.join(path, '..')
sys.path.insert(0, path)

def split_pages(src, dst, rotate=0, crop={"t":0,"r":0,"b":0,"l":0}, split=True):
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
	


	if any(i > 0 for i in crop):
		print "Cropping"
		t1, t2=p.mediaBox.lowerLeft
		t3, t4=p.mediaBox.upperRight

		prevrote=p.get('/Rotate')

		if prevrote==90:
	 		p.mediaBox.upperRight = (t3-crop["b"], t4-crop["r"])
	    		p.mediaBox.lowerLeft = (t1+crop["t"], t2+crop["l"])
		elif prevrote==180:
	 		p.mediaBox.upperRight = (t3-crop["l"], t4-crop["b"])
	    		p.mediaBox.lowerLeft = (t1+crop["r"], t2+crop["t"])
		elif prevrote==270:
	 		p.mediaBox.upperRight = (t3-crop["t"], t4-crop["l"])
	    		p.mediaBox.lowerLeft = (t1+crop["b"], t2+crop["r"])		
		else:
	 		p.mediaBox.upperRight = (t3-crop["r"], t4-crop["t"])
	    		p.mediaBox.lowerLeft = (t1+crop["l"], t2+crop["b"])
	
		print str(p.get('/Rotate'))

	if rotate>0:
	   	p.rotateClockwise(rotate)

	if split:
		print "splitting"		
		q = copy.copy(p)
		q.mediaBox = copy.copy(p.mediaBox)

		x1, x2 = p.mediaBox.lowerLeft
		x3, x4 = p.mediaBox.upperRight

		x1, x2 = math.floor(x1), math.floor(x2)
		x3, x4 = math.floor(x3), math.floor(x4)
		x5, x6 = math.floor((x3-x1)/2)+x1, math.floor((x4-x2)/2)+x2

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

	if split:
		output.addPage(q)

    output.write(dst_f)
    src_f.close()
    dst_f.close()
    
    return True



class Application(Frame):

    def set_message(self, text):
	self.label_message["text"] = text
	self.label_message.config(fg="red")


    def action_open(self):
	"""Triggers open file diaglog, reading file."""
	tmp_in_file = tkFileDialog.askopenfilename(**self.open_options)
	if not tmp_in_file:
	   self.in_file=""
	   self.size["text"]= ""
	   return
	self.in_file = tmp_in_file

	self.set_message("Current PDF file: %s" % ntpath.basename(self.in_file))
	self.getSize()

	

    def getSize(self):
	src_f = file(self.in_file, 'r+b')
 
    	try:
    		inputf = pPDF.PdfFileReader(src_f, strict=False)
    	except: 
		self.size["text"]= "There was a problem reading your PDF file. Try printing the original file as a new pdf\n(using system's pdf reader, for instance) and using that output here."
	   	self.in_file=""
	    	return False
	try:
		p = inputf.getPage(1)
    	except: 
		self.size["text"]= "There was a problem reading the first page of your document. Try printing the original file as a new pdf\n(using system's pdf reader, for instance) and using that output here."
	   	self.in_file=""    		
		return False
	t1, t2=p.mediaBox.lowerLeft
	t3, t4=p.mediaBox.upperRight
	
	points=[t1,t2,t3,t4]

	size=self.calSize(self.pos(points,p.get('/Rotate')/90))
	
	self.size["text"]= "First page dimensions of current document: "+str(size[0])+"x"+str(size[1])

    def calSize(self,t):
	return [t[0]+t[2],t[1]+t[3]]
	
    def pos(self,t,i):
	return t[i:]+t[0:i]

    def split_pdf(self):
	if self.in_file=="":
		self.set_message("Can't split, no PDF selected. Click 'Select file' and select one.") 
		return
	reg = re.compile(re.escape('.pdf'), re.IGNORECASE)
	output_file=reg.sub('', self.in_file)+"_splitted.pdf"

	if split_pages(self.in_file, output_file, int(self.rotate), {"t":self.nCT,  "r":self.nCR, "b":self.nCB,"l":self.nCL}, (self.var_split.get()==1))==True:
		self.set_message("FILE SPLITTED! Check the folder where the original file is")
	else:
		self.set_message("ERROR: There was a problem splitting your PDF.\nTry printing it as a new PDF using your \nsystem's PDF reader and try again with that new file")

    def rotate_selection(self, value):
	self.rotate=value
	print "Rotation set to: "+str(value)

    def updateC(self, *args):
	print "Updating crop values"
	self.nCL=self.crop_left.get()
	print "L: "+str(self.nCL)
	self.nCB=self.crop_bottom.get()
	print "B: "+str(self.nCB)
	self.nCT=self.crop_top.get()
	print "T: "+str(self.nCT)
	self.nCR=self.crop_right.get()
	print "R: "+str(self.nCR)

    def createWidgets(self):
	"""Sets up GUI contents."""
	self.winfo_toplevel().title("PDF Splitter by Milton Läufer".decode("utf-8"))

	row = 0
	column = 0

	PAD_X = 10

	row = row + 1
	column = 0

	self.title = Label(self)
	self.title["text"] = "PDF Splitter".decode("utf-8")
	self.title["font"]=("Helvetica", 16)
	self.title.grid(row=row, column=column, rowspan=1,
				columnspan=2, padx=PAD_X, pady=10, sticky=W)

	row = row + 1
	column = 0
	self.label_message = Label(self, anchor="w")
	self.label_message["text"] = "Click 'Select file' to open a PDF file"
	self.label_message.grid(row=row, column=column, rowspan=1,
				columnspan=2, padx=PAD_X, pady=10, sticky=W)

	row = row + 1
	separator = Frame(self, relief=GROOVE, bd=1, height=2, bg="white")
	separator.grid(columnspan=2, padx=PAD_X, pady=4, sticky=N+E+S+W)
        row = row + 1


        self.label_split = Label(self, anchor=W)
        self.label_split["text"] = "Split PDF pages?"
        self.label_split.grid(row=row, column=0, padx=PAD_X, pady=7, sticky=W)

        self.var_split = IntVar()
        self.checkbox_split = Checkbutton(self, variable=self.var_split)
        self.checkbox_split.grid(row=row, column=1, padx=PAD_X, pady=2)
	self.var_split.set(1)

	row = row + 1
	separator = Frame(self, relief=GROOVE, bd=1, height=2, bg="white")
	separator.grid(columnspan=2, padx=PAD_X, pady=4, sticky=N+E+S+W)

	row += 1
	self.label_rotate = Label(self, anchor=E,bd=1)
	self.label_rotate["text"] = "Clockwise rotation"
	self.label_rotate.grid(row=row, column=column, padx=PAD_X, pady=7, sticky=E)
	
	column += 1	
        optionList = [0,90,180,270]
        self.rotate_value=StringVar()
        self.rotate_value.set(0) # default choice
        self.rotation_object = OptionMenu(self, self.rotate_value, *optionList, command=self.rotate_selection)
        self.rotation_object.grid(column=column,row=row,padx=PAD_X, pady=7, sticky=W)

	row = row + 1
	separator2 = Frame(self, relief=GROOVE, bd=1, height=2, bg="white")
	separator2.grid(columnspan=2, padx=PAD_X, pady=4, sticky=N+E+S+W)

	column = 0
	row = row + 1
	cropping_frame = Frame(self)
	cropping_frame.grid(row=row, column=0, columnspan=2, sticky=E,padx=PAD_X, pady=10)

	self.label_crop = Label(cropping_frame, anchor=W)
	self.label_crop["text"] = "Crop from top"
	self.label_crop.grid(row=1, column=1, padx=PAD_X, pady=7)
	
   	self.crop_top = IntVar()
	self.o_crop_top = Entry(cropping_frame,textvariable=self.crop_top,width=5)
        self.crop_top.trace("w", self.updateC)
	self.o_crop_top.grid(row=1, column=2, padx=PAD_X, pady=7)

	self.label_crop = Label(cropping_frame, anchor=E)
	self.label_crop["text"] = "Crop from bottom"
	self.label_crop.grid(row=3, column=3, padx=PAD_X, pady=7)

   	self.crop_bottom = IntVar()
	self.o_crop_bottom = Entry(cropping_frame,textvariable=self.crop_bottom,width=5)
	self.crop_bottom.trace("w", self.updateC)
	self.o_crop_bottom.grid(row=3, column=2, padx=PAD_X, pady=7)

	self.label_crop = Label(cropping_frame, anchor=E)
	self.label_crop["text"] = "Crop from right"
	self.label_crop.grid(row=2, column=4, padx=PAD_X, pady=7, sticky=E)

   	self.crop_right = IntVar()
	self.o_crop_right = Entry(cropping_frame,textvariable=self.crop_right,width=5)
	self.crop_right.trace("w", self.updateC)
	self.o_crop_right.grid(row=2, column=3, padx=PAD_X, pady=7)

	
	self.label_crop = Label(cropping_frame, anchor=W)
	self.label_crop["text"] = "Crop from left"
	self.label_crop.grid(row=2, column=0, padx=PAD_X, pady=7)

   	self.crop_left = IntVar()
	self.o_crop_left = Entry(cropping_frame,textvariable=self.crop_left,width=5)
	self.crop_left.trace("w", self.updateC)
	self.o_crop_left.grid(row=2, column=1, padx=PAD_X, pady=7)

	self.size = Label(cropping_frame, anchor=W)
	self.size["text"] = "First page dimensions of current document: NO DOCUMENT SELECTED"
	self.size["font"]=("Helvetica", 10)
	self.size.grid(row=4, column=0,
				columnspan=4, padx=PAD_X, pady=10, sticky=E)

	row = row + 1
	separator3 = Frame(self, relief=GROOVE, bd=1, height=2, bg="white")
	separator3.grid(columnspan=2, padx=PAD_X, pady=4, sticky=N+E+S+W)



	column = 0
	row = row + 1
	buttons_frame = Frame(self)
	buttons_frame.grid(row=row, column=0, columnspan=2, sticky=E,padx=PAD_X, pady=10)

	self.button_open = Button(buttons_frame)
	self.button_open["text"] = "Select file"
	self.button_open["fg"] = "black"
	self.button_open["command"] = self.action_open
	self.button_open.grid(row=0, column=0, padx=14, pady=2)

	self.button_split = Button(buttons_frame)
	self.button_split["text"] = "Split PDF"
	self.button_split["fg"] = "black"
	self.button_split["command"] = self.split_pdf
	self.button_split.grid(row=0, column=1, padx=14, pady=2)


	self.button_quit = Button(buttons_frame)
	self.button_quit["text"] = "QUIT"
	self.button_quit["fg"] = "red"
	self.button_quit["command"] = self.quit 
	self.button_quit.grid(row=1, column=1, padx=14, pady=2, sticky=E)

	row = row + 1
	separator3 = Frame(self, relief=GROOVE, bd=1, height=2, bg="white")
	separator3.grid(columnspan=2, padx=PAD_X, pady=4, sticky=N+E+S+W)
	row = row + 1


	self.title = Label(self, anchor=W)
	self.title["text"] = "by Milton Läufer - based on http://stackoverflow.com/a/15741856/1301753".decode("utf-8")
	self.title["text"] += "\n http://www.miltonlaufer.com.ar".decode("utf-8")	
	self.title["font"]=("Helvetica", 10)
	self.title.grid(row=row, column=0, rowspan=1,
				columnspan=2, padx=PAD_X, pady=10, sticky=E)

    def __init__(self, master=None):
	Frame.__init__(self, master)
	self.open_options = {}
	self.open_options['initialdir']=os.path.expanduser('~')
	self.open_options["filetypes"] = [("PDF Documents", ("*.pdf"))]
	self.in_file=""
	self.rotate=0
	self.b_split=True
	self.nCL=self.nCB=self.nCR=self.nCT=0
	self.pack()
	self.createWidgets()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)




def main():
	root = Tk()
	try:
		imgicon = PhotoImage(file=resource_path("icon.png")) #'os.path.join(os.path.dirname(os.path.realpath(__file__)),'icon.png'))
		root.tk.call('wm', 'iconphoto', root._w, imgicon)  
	except:
		print "no anduvo"
	
	#root.geometry("450x340")
	
	app = Application(master=root)
	app.mainloop()
	root.destroy()

if __name__ == "__main__":
    main()

