#!/bin/sh

workpath=./build
distpath=./dist
specpath=./
icon=icon.ico
if [ "$1" == "macos" ]; then
	workpath="./macos/build"
	distpath="./macos/dist"
	specpath="./macos/"
	icon="icon.icns"
fi

pyinstaller --onefile --windowed --add-data "icon.png:." --icon="$icon" --clean pdf_kindle_gui.py --workpath "$workpath" --distpath "$distpath" --specpath "$specpath"

