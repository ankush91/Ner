
import os
import re

true = 1
false = 0
delimiter = "/"

def preProcess():
  readPath = r"data/TE3-platinum-test"
  writePath = r"stanford-ner-2015-12-09/data/TE3-platinum-test-text"
  
  inExt = "tml.TE3input.xml"
  outExt = "txt"
  forceWriteFolder = true
  overwriteFlag = true
  ignoreExtMismatch = false
  
  success = doPreProcessing(readPath, writePath, forceWriteFolder, overwriteFlag, inExt, outExt, ignoreExtMismatch)
  return success

def checkReadPath(readPath):
  if os.path.exists(readPath):
    return true
  else:
    print "Directory ", readPath, " does not exist or is inaccessible."
    return false
    
def checkWritePath(writePath, forceWrite):
  if os.path.exists(writePath):
    return true
  elif forceWrite == true:
    print "Directory ", writePath, " does not exist. Attempting to create"
    os.makedirs(writePath)
    if os.path.exists(writePath):
      print "Creation successful."
      return true
    else:
      print "Coult not create directory ", writePath
      return false
  else:
      print "Could find directory ", writePath
      return false

def stripTags(content):
  if ("<TEXT>" not in content) or ("</TEXT>" not in content):
    return ""
  
  textStart = content.find("<TEXT>") + 6
  textEnd = content.find("</TEXT>")
  
  content  = content [textStart : textEnd]
  content = content.strip()
  return content

def doPreProcessing(readPath, writePath, forceWriteFolder, overwriteFlag, inExt, outExt, ignoreExtMismatch):
  if (checkReadPath(readPath) == false or checkWritePath(writePath, forceWriteFolder) == false):
    return false

  fileList = os.listdir(readPath)
  fileCount = len(fileList)
  
  if(fileCount == 0):
    print "Empty folder."
    return false

  print fileCount, " files found in directory ", readPath
  print "Writing output files to directory ", writePath, "\n"

  for i in range(0, fileCount):
    if inExt not in fileList[i] and ignoreExtMismatch == false:
      continue
    
    ofPath = readPath + delimiter + fileList[i]
    currFile = open(ofPath, 'r')
    content = currFile.read()
    plainContent = stripTags(content)
    
    if (plainContent == ""):
      print "\tFile ID: " , i , "\t\tName: " , fileList[i], "\t\tInput badly formed. Cannot process."
    
    newFile = re.sub(inExt, outExt, fileList[i])
    nfPath = writePath + delimiter + newFile
    
    if not (os.path.exists(nfPath)):
      print "\tFile ID: " , i , "\t\tName: " , fileList[i], "\t\tWriting to:", newFile
      outFile = open(nfPath,"w")
      outFile.write(plainContent)
      outFile.close()
      
    else:
      if (overwriteFlag == true):
        print "\tFile ID: " , i , "\t\tName: " , fileList[i], "\t\tOverwriting:", newFile
        outFile = open(nfPath,"w")
        outFile.write(plainContent)
        outFile.close()
      
      else:
        print "\tFile ID: " , i , "\t\tName: " , fileList[i], "\t\tOutput file exists. Skipping."

    currFile.close()
    
  return true

