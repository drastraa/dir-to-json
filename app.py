import json, os

allFolders = []
allFiles = []

def checkForFolder(path=''):
  sPath = ''
  if len(path) > 0:
    sPath = path+'/'
  else:
    sPath = ''

  newPath = ''
  files = os.listdir('./'+path)
  folders = []
  for file in files:
    if os.path.isdir(sPath+file):
      folders.append(file)
    else:
      if file != 'app.py' and file != 'data.json':
        allFolders.append(sPath)
        allFiles.append(file)
      elif not len(path) == 0:
        allFolders.append(sPath)
        allFiles.append(file)

  if len(folders) == 0:
    return False
  else:
    for folder in folders:
      newPath = sPath+folder
      checkForFolder(newPath)
    return True


checkForFolder()

allDict = {'path': allFolders, 'filename': allFiles}

with open('data.json', 'w') as jFile:
  jFile.write(json.dumps(allDict, indent=1))

print('"data.json" created\n\t' + str(len(allFolders)) + ' Paths,\n\t' + str(len(allFiles)) + ' Files')