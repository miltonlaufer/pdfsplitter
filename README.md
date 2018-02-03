# PDF Splitter, Rotate and Crop for kindle 
## (or any other eBook reader):

# Description:

A PDF page splitter (based on http://stackoverflow.com/a/15741856/1301753), with rotation and cropping. 


** Python (of course) has to be installed: https://www.python.org/downloads/ ** 


# Option 1: Graphical User Interface:

* Download the files on the "pdf_kindle_gui" folder.
* Open a terminal (*Ubuntu*: 'ctrl+alt+t'; *Windows*: 'Windows+R' and then write 'cmd, press 'enter';Mac... Applications, maybe?), go to the folder where you put the files and:
    python pdf_kindle_gui
* From there, it's pretty intuitive. 

(There's also a one-file executable file on /pdf_kindle_gui/dist, but it only works on linux, as far as I tested it.)

# Option 2: Terminal
## (Good for batch jobs).

* Download the files on the "pdf_kindle" folder.
* Open a terminal (*Ubuntu*: 'ctrl+alt+t'; *Windows*: 'Windows+R' and then write 'cmd, press 'enter';Mac... Applications, maybe?), go to the folder where you put the files and choose one of the following options

USAGE:

    python pdfkindle ORIGINAL.pdf

or

    python pdfkindle ORIGINAL.pdf FINAL.pdf

or

    python pdfkindle ORIGINAL.pdf rotateClockwiseINTEGER

or

    python pdfkindle ORIGINAL.pdf FINAL.pdf rotateClockwiseINTEGER

(you can ommit the "python" if the file has execute permissions --i.e., "chmod +x pdfkindle")

Please remember the paths are relative, so if you have your script on "/home/myuser/", you'll need to execute this way:

    python /home/myuser/pdfkindle ORIGINAL.pdf

or

    python /home/myuser/pdfkindle /home/myuser/somepdfs/ORIGINAL.pdf

the output file will be saved on the current folder.

##BATCH JOBS:

     for i in *.pdf; do python pdfkindle $i; done
