import sys, os, string
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form( QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.resize(300,75)
        self.lineedit1 = QLineEdit('Enter File Name')
        self.pbutton1 = QPushButton('Load File')
        self.lineedit2 = QLineEdit('Character Count')
        self.pbutton2 = QPushButton('Count Total Characters')
        self.lineedit3 = QLineEdit('Word Count')
        self.pbutton3 = QPushButton('Count Total Words')
        self.lineedit4 = QLineEdit('Line Count')
        self.pbutton4 = QPushButton('Count Total Lines')
        self.lineedit5 = QLineEdit('What Word Would You Like to Count?')
        self.pbutton5 = QPushButton('Count Specific Word')
        self.lineedit6 = QLineEdit('Average Characters per Word')
        self.pbutton6 = QPushButton('Determine Average')
        self.lineedit7 = QLineEdit('Average Words per Line')
        self.pbutton7 = QPushButton('Determine Average')
        self.lineedit8 = QLineEdit('Enter First Word')
        self.lineedit9 = QLineEdit('Enter Second Word')
        self.lineedit10 = QLineEdit('Frequency')
        self.pbutton8 = QPushButton('Determine Frequency')
        self.lineedit11 = QLineEdit('Word Order')
        self.pbutton9 = QPushButton('Second Word Follows the First Word')
        self.pbutton10 = QPushButton('First Word Follows the Second Word')
        self.pbuttonQuit = QPushButton('Quit')
        layout = QVBoxLayout()
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit5)
        layout.addWidget(self.pbutton5)
        layout.addWidget(self.lineedit6)
        layout.addWidget(self.pbutton6)
        layout.addWidget(self.lineedit7)
        layout.addWidget(self.pbutton7)
        layout.addWidget(self.lineedit8)
        layout.addWidget(self.lineedit9)
        layout.addWidget(self.lineedit10)
        layout.addWidget(self.pbutton8)
        layout.addWidget(self.lineedit11)
        layout.addWidget(self.pbutton9)
        layout.addWidget(self.pbutton10)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        self.lineedit1.setFocus()
        self.connect(self.pbutton1, SIGNAL('clicked()'),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL('clicked()'),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL('clicked()'),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL('clicked()'),self.button4Pressed)
        self.connect(self.pbutton5, SIGNAL('clicked()'),self.button5Pressed)
        self.connect(self.pbutton6, SIGNAL('clicked()'),self.button6Pressed)
        self.connect(self.pbutton7, SIGNAL('clicked()'),self.button7Pressed)
        self.connect(self.pbutton8, SIGNAL('clicked()'),self.button8Pressed)
        self.connect(self.pbutton9, SIGNAL('clicked()'),self.button9Pressed)
        self.connect(self.pbutton10, SIGNAL('clicked()'),self.button10Pressed)
        self.connect(self.pbuttonQuit, SIGNAL('clicked()'),self.buttonQuitPressed)
        self.setWindowTitle('Python File Processor')
    #Total Character Count
    def charcount(self):
        charcount = 0
        for line in self.lines:
            line = line.strip() #help received from a student (Stephen Ross??)
            charcount = charcount + len(line)
        return charcount
    #Total Word Count
    def wordcount(self):
        wordcount = 0
        for line in self.lines:
            line = line.translate(None, string.punctuation)
            line = line.lower()
            words = line.split()
            for word in words:
                wordcount = wordcount + 1
        return wordcount
    #Total Line Count
    def linecount(self):
        linecount = 0
        for line in self.lines:
            linecount = linecount + 1
        return linecount
    #Count a Specific Word
    def specificword(self, word):
        count = 0
        for line in self.lines:
            line = line.translate(None, string.punctuation)
            line = line.lower()
            linelist = line.split()
            for w in linelist:
                if w == word:
                    count = count + 1
                else:
                    count = count + 0
        return count
    def w2followsw1(self, word1, word2):
        count = 0
        for line in self.lines:
            line = line.translate(None, string.punctuation)
            line = line.lower()
            if word1 + ' ' + word2 in line:
                count = count + 1
            else:
                count = count + 0
        return count
    def w1followsw2(self, word1, word2):
        count = 0
        for line in self.lines:
            line = line.translate(None, string.punctuation)
            line = line.lower()
            if word2 + ' ' + word1 in line:
                count = count + 1
            else:
                count = count + 0
        return count
    #Button Execution Methods
    def button1Pressed(self):
        #For Windows -- Update variable f to the correct directory 'C:/Users/**INSERT FULL DIRECTORY HERE**' + g
        #For Mac -- Update variable f to the correct directory
        g = str(self.lineedit1.text())
        f = '/Users/christianhoward/Documents/Python/' + g
        try:
            with open(f) as load: #opens file, sets load.readlines = self.lines, then closes program
                self.lines = load.readlines()
            outtext = 'The file ' + str(g) + ' has been loaded.'
            self.lineedit1.setText(outtext)
        except (ValueError, TypeError, IOError):
            outtext = 'Error: could not read file ' + g + '.'
            self.lineedit1.setText(outtext)
            self.lines = []
    def button2Pressed(self): #charcount cc = charcount variable
        cc = self.charcount()
        outtext = str(cc) + ' characters in the file.'
        self.lineedit2.setText(outtext)
    def button3Pressed(self): #wordcount wc = wordcount variable
        wc = self.wordcount()
        outtext = str(wc) + ' words in the file.'
        self.lineedit3.setText(outtext)
    def button4Pressed(self): #linecount lc = linecount variable
        lc = self.linecount()
        outtext = str(lc) + ' lines in the file.'
        self.lineedit4.setText(outtext)
    def button5Pressed(self): #specificword sw = specificword variable swo = num of times variable
        sw = self.lineedit5.text()
        sw = str(sw).lower()
        swo = self.specificword(sw)
        outtext =  str(sw) + ' appears ' + str(swo) + ' times in the file.'
        self.lineedit5.setText(outtext)
    def button6Pressed(self): #avgcharword avgcw = average characters per word variable
        avgcw = self.lineedit6.text()
        avgcw = round(float(self.charcount())/float(self.wordcount()), 1)
        outtext = 'Average Characters per Word: ' + str(avgcw)
        self.lineedit6.setText(outtext)
    def button7Pressed(self): #avgwordline avgwl = average words per line variable
        avgwl = self.lineedit7.text()
        avgwl = round(float(self.wordcount())/float(self.linecount()), 1)
        outtext = 'Average Words per Line: ' + str(avgwl)
        self.lineedit7.setText(outtext)
    def button8Pressed(self): #freqword1word2 freq1 = word1 freq2 = word2
        freq1 = self.lineedit8.text()
        freq1 = str(freq1).lower()
        freq1o = self.specificword(freq1)
        freq2 = self.lineedit9.text()
        freq2 = str(freq2).lower()
        freq2o = self.specificword(freq2)
        if freq1o > freq2o:
            outtext = str(freq1) + ' appears more times than ' + str(freq2) + '.'
        elif freq2o > freq1o:
            outtext = str(freq2) + ' appears more times than ' + str(freq1) + '.'
        else:
            outtext = str(freq1) + ' and ' + str(freq2) + ' appear the same number of times.'
        self.lineedit10.setText(outtext)
    def button9Pressed(self):
        w1 = self.lineedit8.text()
        w1 = str(w1).lower()
        w2 = self.lineedit9.text()
        w2 = str(w2).lower()
        w2f1 = self.w2followsw1(w1, w2)
        outtext = str(w2) + ' follows ' + str(w1) + ' ' + str(w2f1) + ' times.'
        self.lineedit11.setText(outtext)
    def button10Pressed(self):
        w1 = self.lineedit8.text()
        w1 = str(w1).lower()
        w2 = self.lineedit9.text()
        w2 = str(w2).lower()
        w1f2 = self.w1followsw2(w1, w2)
        outtext = str(w1) + ' follows ' + str(w2) + ' ' + str(w1f2) + ' times.'
        self.lineedit11.setText(outtext)
    def buttonQuitPressed(self):
        quit()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()