from xml.dom import minidom
import os

xmlFile = "xyz.xml"
dirPath = "xyz"
with open(xmlFile) as xmlF:
    xmldoc = minidom.parse(xmlF)
    actions = xmldoc.getElementsByTagName('action')
    
    for action in actions:
        path = action.attributes['path'].value
        print "path : " + str(path)
        
        for root, dirs, files in os.walk(dirPath): 
            for fl in files: 
                fl = os.path.join(root, fl) 
                with open(fl) as f:
                    for contents in f:
                        try:
                            if path in contents: 
                                print "\t " + str(file)
                        
                        except :
                            pass
