#!/bin/sh

workpath=./build
distpath=./dist
specpath=./
if [ "$1" == "macos" ]; then
	workpath="./macos/build"
	distpath="./macos/dist"
	specpath="./macos/"
fi

pyinstaller --onefile --windowed --add-data 'icon.png:.' --icon=icon.ico --clean pdf_kindle_gui.py --workpath "$workpath" --distpath "$distpath" --specpath "$specpath"

