![Logo](https://raw.githubusercontent.com/miltonlaufer/pythonscripts/master/pdf_kindle_gui/icon.png)

# PDF Splitter, Rotate and Crop for Kindle 
### (or any other eBook reader)

# Description:

A PDF page splitter (based on http://stackoverflow.com/a/15741856/1301753), with rotation and cropping. 

## Before
![BEFORE](https://raw.githubusercontent.com/miltonlaufer/pythonscripts/master/pdf_kindle_gui/screenshots/Before.png)
## After
![AFTER](https://raw.githubusercontent.com/miltonlaufer/pythonscripts/master/pdf_kindle_gui/screenshots/after02.png)


~~Python (of course) has to be installed:** https://www.python.org/downloads/~~ 
**Not python mandatory for GUI versions** (See below, ["UPDATE"](https://github.com/miltonlaufer/pythonscripts#update-gui-standalone-distributions) ) 


# Option 1: Graphical User Interface

### Screenshots

![Screenshot 1](https://raw.githubusercontent.com/miltonlaufer/pythonscripts/master/pdf_kindle_gui/screenshots/pdf_kindle_01.png)
![Screenshot 2](https://raw.githubusercontent.com/miltonlaufer/pythonscripts/master/pdf_kindle_gui/screenshots/pdf_splitterWithPreview.png)

### Installation and use

* Download the files from the [/pdf_kindle_gui](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle_gui/) folder.
* Open a terminal (*Ubuntu*: 'ctrl+alt+t'; *Windows*: 'Windows+R' and then write 'cmd', press 'enter'; *Mac*... applications, maybe?), go to the folder where you put the files and:
    python pdf_kindle_gui
* From there, it's pretty intuitive. 

(There's also a one-file standalone executable release on [/pdf_kindle_gui/dist](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle_gui/dist), but it only works on linux, as far as I tested it.)

### UPDATE: GUI standalone distributions

##### There are now working GUI standalone versions for Mac OS, Windows and Linux.

*Mac*: Get the +pdf_kindle_gui.app+ file from [/pdf_kindle_gui/macos/macos/dist/](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle_gui/macos/macos/dist/).

*Windows*: Get +pdf_kindle_gui.exe+ file from [/pdf_kindle_gui/dist_windows/](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle_gui/dist_windows/).

*Linux*: Get +pdf_kindle_gui+ file from [/pdf_kindle_gui/dist/](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle_gui/dist/).

##### Mac OS Screenshots (by Osk)

![First screen](https://user-images.githubusercontent.com/746152/35768578-9ccd6b74-08dc-11e8-971f-0e1649547921.png)
![File selected](https://user-images.githubusercontent.com/746152/35768577-9c312b4c-08dc-11e8-8ec0-54059ae70d69.png)
![File splitted](https://user-images.githubusercontent.com/746152/35768576-9bf65a6c-08dc-11e8-9398-d8fb9cdb1bdc.png)

# Option 2: Terminal
## (Good for batch jobs).

* Download the files from the [/pdf_kindle/](https://github.com/miltonlaufer/pythonscripts/tree/master/pdf_kindle) folder.
* Open a terminal (*Ubuntu*: 'ctrl+alt+t'; *Windows*: 'Windows+R' and then write 'cmd, press 'enter';Mac... Applications, maybe?), go to the folder where you put the files and choose one of the following options

USAGE:

    python pdfkindle.py ORIGINAL.pdf

or

    python pdfkindle.py ORIGINAL.pdf FINAL.pdf

or

    python pdfkindle.py ORIGINAL.pdf rotateClockwiseINTEGER

or

    python pdfkindle.py ORIGINAL.pdf FINAL.pdf rotateClockwiseINTEGER

(you can ommit the "python" if the file has execute permissions --i.e., "chmod +x pdfkindle")

Please remember the paths are relative, so if you have your script on "/home/myuser/", you'll need to execute this way:

    python /home/myuser/pdfkindle.py ORIGINAL.pdf

or

    python /home/myuser/pdfkindle.py /home/myuser/somepdfs/ORIGINAL.pdf

the output file will be saved on the current folder.

## BATCH JOBS:

The following splits all the PDFs on the current dir. You can add to this command any of the options from above.  

     for i in *.pdf; do python pdfkindle.py $i; done

For instance, if you want to rotate all the files 90º clockwise,

     for i in *.pdf; do python pdfkindle.py $i 90; done
