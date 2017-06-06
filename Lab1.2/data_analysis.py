from matplotlib import pyplot
from openpyxl import load_workbook
wb=load_workbook('data_analysis_lab.xlsx')
sheet=wb['Data']
def getvalue(x): return x.value
x=sheet['A'][1:]
y1=sheet['B'][1:]
y2=sheet['C'][1:]
X=list(map(getvalue,sheet['A'][1:]))
Y1=list(map(getvalue,sheet['B'][1:]))
Y2=list(map(getvalue,sheet['C'][1:]))
pyplot.plot(X, Y1, label="Метка1")
pyplot.plot(X, Y2, label="Метка")
pyplot.show()
