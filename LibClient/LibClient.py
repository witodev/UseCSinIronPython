import System.Collections.Generic
import clr    
clr.AddReferenceToFileAndPath(r"c:\Users\wszwe\Documents\Visual Studio 2017\Projects\UseCSinIronPython\Library\bin\Debug\Library.dll")
import Library

print('Hello world')

data = Library.USUM()
data.id = 1
data.x = 123.123
data.y = 432.112
data.z = 342.645

d = System.Collections.Generic.Dictionary[int, Library.USUM]()
d.Add(data.id, data)

tmp = Library.FEM.SaveToFile(d, "test.txt");

print("Siema")

