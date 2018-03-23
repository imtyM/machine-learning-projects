"""
Kotze, S.J.
u13026242
steankotze@gmail.com
"""

"*****************************************************************************"

import numpy as np
import math as mt

"*****************************************************************************"

class JUSTDOIT:
    #MY_NODE###################################################################
    class steak:
        def __init__(self):
            self.isRoot = False
            self.valium = None
            self.parentChoice = None
            self.children = []
        
    #INITIALIZE################################################################
    def __init__(self, datArr):
        self.head = self.buildTree(datArr, "head")
        
    #MAIN_TREE_BUILDER#########################################################
    def buildTree(self, arg1, arg2):
        orgArg  = self.organizeData(arg1)
        sizeOrgArg = np.shape(orgArg)
        sizeArg = np.shape(arg1)
        iEntropy = []
        iPos = 0
        
        #determine amount of positive values
        for i in range(1, sizeArg[0]):
            if (arg1[i][sizeArg[1] - 1] == "Yes"):
                iPos = iPos + 1
                
        #get the entropies of the 2D arrays returned from self.organizeData
        for i in range(0, sizeOrgArg[0]):
            iEntropy.append(self.getEntropy(orgArg[i], iPos, sizeOrgArg[0] - 1))
        
        #find out which of the entropies is the largest
        iSmallestVal = iEntropy[0]
        iSmallestInd = 0
        for i in range(0, len(iEntropy)):
            if (iEntropy[i] > iSmallestVal):
                iSmallestVal = iEntropy[i]
                iSmallestInd = i
        
        #make the node that will be returned
        newNode = self.steak()
        newNode.isRoot = False
        newNode.valium = arg1[0][iSmallestInd + 1]
        newNode.parentChoice = arg2
        
        #check if any of the entropies of THE CHOSEN ONE are 0
        temp = self.checkZero(orgArg[iSmallestInd])
        tempAdded = []
        if (temp != None):
            for i in range(0, len(temp)):
                tempNode = self.steak()
                tempNode.isRoot = True
                tempNode.valium = temp[i][0]
                tempNode.parentChoice = temp[i][1]
                tempAdded.append(tempNode.parentChoice)
                newNode.children.append(tempNode)
        
        #get number of children still to add
        tempSize = np.shape(orgArg[iSmallestInd])
        tempToAdd = []
        for i in range(1, tempSize[0]):
            if (orgArg[iSmallestInd][i][0] not in tempAdded):
                tempToAdd.append(i)
        
        #add children that are left
        if (len(tempToAdd) != 0):
            for i in range(0, len(tempToAdd)):
                sTemp = orgArg[iSmallestInd][tempToAdd[i]][0]
                newData = self.getNewData(arg1, iSmallestInd + 1, sTemp)
                newChild = self.buildTree(newData, sTemp)
                newNode.children.append(newChild)
                
        #return new node to parent
        return newNode
        
    #2D_ARRAY_TO_3D_FOR_ENTROPY################################################
    def organizeData(self, arg):
        sizeArg = np.shape(arg)
        xValues = []
        yValues = []
        arrOut = []
        
        #get all the choices made in the last column, works
        for i in range(1, sizeArg[1]):
            if (arg[sizeArg[0] -1][i] not in xValues):
                xValues.append(arg[0][i])
        
        #get the values of all the variables, works
        for i in range(1, sizeArg[1]):
            tempArr = []
            for j in range(1, sizeArg[0]):
                if (arg[j][i] not in tempArr):
                    tempArr.append(arg[j][i])
            yValues.append(tempArr)
        
        #make the new arrays which are to be returned
        for k in range(0, len(xValues) - 1):
            tempArr = []
            
            #add true false range
            tempArr.append([])
            tempY = yValues[len(yValues) - 1]
            for i in range(0, len(tempY) + 1):
                if (i == 0):
                    tempArr[0].append(None)
                else:
                    tempArr[0].append(tempY[i - 1])
            
            #add range of yvalues
            for i in range(1, len(yValues[k]) + 1):
                tempArr.append([])
                for j in range(0, len(tempY) + 1):
                    if (j == 0):
                        tempArr[i].append(yValues[k][i - 1])
                    else:
                        tempArr[i].append(0)
            
            #populate with data
            importX = sizeArg[1] - 1
            for i in range(1, sizeArg[0]):
                yIndex = yValues[k].index(arg[i][k+1]) + 1
                xIndex = tempY.index(arg[i][importX]) + 1
                tempArr[yIndex][xIndex] = tempArr[yIndex][xIndex] + 1
            
            arrOut.append(tempArr)
        
        return arrOut
    
    #MAIN_ENTROPY##############################################################
    def getEntropy(self, arg1, arg2, arg3):
        #returns the remainder of a 2D array of int
        def remainder(arg):
            arrSize = np.shape(arg)
            totalNP = 0
            sumOf = 0
            
            for i in range(arrSize[0]):
                for j in range(0, arrSize[1]):
                    totalNP = totalNP + arg[i][j]
            
            for i in range(0, arrSize[0]):
                tempArr = []
                tempTot = 0
                
                for j in range(0, arrSize[1]):
                    tempArr.append(arg[i][j])
                    tempTot = tempTot + arg[i][j]
                    
                tempArr = B1(tempArr)
                tempTot = float(tempTot)/totalNP
                tempTot = tempTot*tempArr
                sumOf = sumOf + tempTot
                
            return sumOf
        
        #returns the entropy of a 1D array of int
        def B1(arg):
            totalNPk = 0
            sumOf = 0
            
            for i in range(0, len(arg)):
                totalNPk = totalNPk + arg[i]
            
            for i in range(0, len(arg)):
                iTemp1 = float(arg[i])/totalNPk
                iTemp2 = iTemp1*np.log2(iTemp1)
                sumOf = sumOf + iTemp2
                
            if (mt.isnan(sumOf)):
                return 0
            return -1*sumOf   
        
        def B2(arg1, arg2):
            iTemp = -1*((float(arg1)/arg2)*np.log2(float(arg1)/arg2) + (float(arg2 - arg1)/arg2)*np.log2(float(arg2 - arg1)/arg2))
            return iTemp
        
        sizeOfArg = np.shape(arg1)
        newArr = []
        
        #make 2D int array for entropy finding
        for i in range(1, sizeOfArg[0]):
            newArr.append([])
            for j in range(1, sizeOfArg[1]):
                newArr[i - 1].append(arg1[i][j]) 
        
        rem = B2(arg2, arg3) - remainder(newArr)
        return rem
    
    #NEW_ARRAY_FOR_RECURSIVE_BUILD#############################################
    def getNewData(self, arg1, arg2, arg3):
        sizeOfArg = np.shape(arg1)
        newArr = []
        lvl = 0
        
        #add range of x types
        newArr.append([])
        newArr[lvl].append(None)
        for i in range(1, sizeOfArg[1]):
            if (i != arg2):
                newArr[lvl].append(arg1[0][i])
        lvl = lvl + 1
        
        #populate the rest of the 2D array
        for i in range(1, sizeOfArg[0]):
            if (arg1[i][arg2] == arg3):
                newArr.append([])
                
                for j in range(0, sizeOfArg[1]):
                    if (j != arg2):
                        newArr[lvl].append(arg1[i][j])
                lvl = lvl + 1
        
        return newArr
        
    #CHECKS_IF_VALUES_IN_ENTROPY_ARE_0########################################
    def checkZero(self, arg):
        argSize = np.shape(arg)
        tempArr = []
        
        for i in range(1, argSize[0]):
            iTemp = 0
            for j in range(1, argSize[1]):
                if (arg[i][j] != 0):
                    iTemp = iTemp + 1
            
            if (iTemp == 1):
                for j in range(1, argSize[1]):
                    if (arg[i][j] != 0):
                        tupleTemp = (arg[0][j], arg[i][0])
                        tempArr.append(tupleTemp)
        
        return tempArr
    
    #DETERMINES_PATH_TO_RESULT#################################################
    def determinePath(self, arg):
        tempNode = self.head
        sPath = "Path = ( "
        
        while True:
            tempArr = []
            
            #get choices of paths from node
            for i in range(0, len(tempNode.children)):
                tempArr.append(tempNode.children[i].parentChoice)
            
            #see if arg[i] is in choices if so go to node
            for i in range(0, len(arg)):
                if (arg[i] in tempArr):
                    iTemp = tempArr.index(arg[i])
                    """
                    print sPath
                    print len(tempArr)
                    print len(tempNode.children)
                    print iTemp
                    print
                    print"""
                    sPath = sPath + tempNode.valium + " = " + tempNode.children[iTemp].parentChoice + " -> "
                    tempNode = tempNode.children[iTemp]
                    break
            
            if (tempNode.isRoot == True):
                sPath = sPath + "*willWait == " + tempNode.valium + "* )"
                return sPath
        
    #PRINTS_TREE###############################################################
    def printTree(self):
        tempArr = []
        tempArr.append(self.head)
        
        while True:
            holdArr = []
            for i in range(0, len(tempArr)):
                tempNode = tempArr.pop(0)
                
                if (tempNode.isRoot == True):
                    print "[**" + tempNode.parentChoice + " -> " + tempNode.valium + "**]" ,
                else:
                    print "[ " + tempNode.parentChoice + " -> " + tempNode.valium + " - (",
                    for j in range(0, len(tempNode.children)):
                        holdArr.append(tempNode.children[j])
                        print " " + tempNode.children[j].parentChoice + " ",
                    print ")] ",
            
            print
            if (len(holdArr) == 0):
                return
            else:
                tempArr = holdArr  
                
                
"*****************************************************************************"

aa = [[None , "Alternate?", "Bar?", "Friday?", "Hungry?", "Patrons?" , "Price?", "Rain?", "Reservation?" , "Type?"   , "Est?"  , "WillWait"],
      ["x1" , "Yes", "No" , "No" , "Yes", "Some", "$$$"  , "No"  , "Yes" , "French" , "0-10" , "Yes"],
      ["x2" , "Yes", "No" , "No" , "Yes", "Full", "$"    , "No"  , "No"  , "Thai"   , "30-60", "No"],
      ["x3" , "No" , "Yes", "No" , "No" , "Some", "$"    , "No"  , "No"  , "Burger" , "0-10" , "Yes"],
      ["x4" , "Yes", "No" , "Yes", "Yes", "Full", "$"    , "Yes" , "No"  , "Thai"   , "10-30", "Yes"],
      ["x5" , "Yes", "No" , "Yes", "No" , "Full", "$$$"  , "No"  , "Yes" , "French" , ">60"  , "No"],
      ["x6" , "No" , "Yes", "No" , "Yes", "Some", "$$"   , "Yes" , "Yes" , "Italian", "0-10" , "Yes"],
      ["x7" , "No" , "Yes", "No" , "No" , "None", "$"    , "Yes" , "No"  , "Burger" , "0-10" , "No"],
      ["x8" , "No" , "No" , "No" , "Yes", "Some", "$$"   , "Yes" , "Yes" , "Thai"   , "0-10" , "Yes"],
      ["x9" , "No" , "Yes", "Yes", "No" , "Full", "$"    , "Yes" , "No"  , "Burger" , ">60"  , "No"],
      ["x10", "Yes", "Yes", "Yes", "Yes", "Full", "$$$"  , "No"  , "Yes" , "Italian", "10-30", "No"],
      ["x11", "No" , "No" , "No" , "No" , "None", "$"    , "No"  , "No"  , "Thai"   , "0-10" , "No"],
      ["x12", "Yes", "Yes", "Yes", "Yes", "Full", "$"    , "No"  , "No"  , "Burger" , "30-60", "Yes"]]
      

asf = JUSTDOIT(aa)
asf.printTree()
"""
sTemp = asf.determinePath(["Yes", "No","Yes","Yes","Full","$$","Yes","No","Thai","10-30"])
print sTemp
"""