# pythonscripts

***********
PDF for kindle:

Description:

A PDF page splitter (based on http://stackoverflow.com/a/15741856/1301753).



Python (of course) has to be installed: https://www.python.org/downloads/ 



USAGE:

$ python pdfkindle ORIGINAL.pdf

or

$ python pdfkindle ORIGINAL.pdf FINAL.pdf

or

$ python pdfkindle ORIGINAL.pdf rotateClockwiseINTEGER

or

$ python pdfkindle ORIGINAL.pdf FINAL.pdf rotateClockwiseINTEGER

(you can ommit the "python" if the file has execute permissions --i.e., "chmod +x pdfkindle")

Please remember the paths are relative, so if you have your script on "/home/myuser/", you'll need to execute this way:

$ python /home/myuser/pdfkindle ORIGINAL.pdf

or

$ python /home/myuser/pdfkindle /home/myuser/somepdfs/ORIGINAL.pdf

the output file will be saved on the current folder.


