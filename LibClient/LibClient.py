import System.Collections.Generic
import random

import clr    
clr.AddReferenceToFileAndPath(r"c:\Users\wszwe\Documents\Visual Studio 2017\Projects\UseCSinIronPython\Library\bin\Debug\Library.dll")
import Library

collector = System.Collections.Generic.Dictionary[int, Library.USUM]()
for i in range(10):
    data = Library.USUM()
    data.id = i+1 
    data.x = random.randint(0,100)/10.0
    data.y = random.randint(0,100)/10.0
    data.z = random.randint(0,100)/10.0
    collector.Add(data.id, data)

tmp = Library.FEM.SaveToFile(collector, "test.txt");

for i in tmp:
    print(i.Key, i.Value.ToString())

