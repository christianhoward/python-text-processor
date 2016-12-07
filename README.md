# Python Text Processor

A .txt processor built using Python 2.7 and PyQt4.

## Requirements
- Python 2.7
- PyQt4

## To Run
This program can be launched through command line or IDLE. In your terminal, navigate to the directory where the textprocessor.py file is located and enter the following command to run it:
```sh
python textprocessor.py
```

## Overview
Prior to launching the program, please check lines 125-129 to update the file path to the directory where the .txt files can be found. A relative file path has been set for Mac users and there are comments within lines 125 and 129 that address absolute path and relative path for Windows and Mac users alike.

In the Graphic User Interface (GUI), you'll find a file loader at the top. In this first box, you'll enter the file name. It should be noted that there is placeholder text in each line edit in the program. For any line edit where an input is required, in this case Count Specific Word and Frequency/Word Order, you will need to clear the lines out before adding an input.

All “functions” in this program are actually methods within the defined Form class. Thus, all methods can be found below the initialization method. The Count Total Characters, Count Total Words, Count Total Lines, Average Characters per Word, and Average Words per Line methods are executed by pushing their respective buttons. No text entry is needed in their respective line edits. For the Count Specific Word, Frequency, and Word Order methods, you will need to enter words in their respective line edits. Please note that the Frequency and Word Order methods both use the "Enter First Word" and "Enter Second Word" line edits and have their own line edits above their respective buttons for the returned results. All results will be returned in the GUI. 

## Project Description
In this instance, the text processor program can be used to analyze character, word, and line counts as well as averages, frequency, and word order within a .txt file.

## Questions??
If you have any questions, please feel free to contact me.
