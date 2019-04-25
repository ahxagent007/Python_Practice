from sre_compile import isstring

import xlrd
import re

ringNo =str(input("Enter Ring Number: "))


for i in range(0,6):
    fileName = ""+str(i) + ".xlsx"
    # Opening the file as workbook
    workbook = xlrd.open_workbook(fileName)

    # Opening worksheet by its index
    workSheet = workbook.sheet_by_index(0)

    for j in range(1, workSheet.nrows):
        currentRing2 = workSheet.cell(j, 2).value

        if isstring(currentRing2):
            pass
        else:
            currentRing2 = str(int(currentRing2))
        #print(currentRing2)
        currentRing2 = re.sub("C", "", currentRing2)
        currentRing2 = re.sub("H", "", currentRing2)
        currentRing2 = re.sub("\+", "", currentRing2)
        #print(currentRing2)

        if currentRing2 == ringNo:
            print(str(int(workSheet.cell(j, 0).value))+"th from "+str(workSheet.cell(1,2).value)+"  "+str(workSheet.cell(1,5).value)+" Loft: "+str(workSheet.cell(j, 1).value))


#53955