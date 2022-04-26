
import arcpy
aWS= r"C:\Khalid\Assignment_02\Assignment_02.gdb"
arcpy.env.workspace= aWS

aFC= arcpy.ListFeatureClasses()
File= open(r"C:\Khalid\Assignment_02\msg.txt", "w")
for x in aFC:
    des= arcpy.Describe(x)
    anitem=x+"_p"

    if des.SpatialReference.type== "Projected":
        aword= "projected"
    else:
        arcpy.Exists(x+"_p")
        arcpy.Delete_management(x+"_p")
        aword= "not projected. It has been projected to {0}".format(anitem.upper())
        arcpy.Project_management(x, x+"_p", arcpy.SpatialReference(26945))

    print "{0} feature class is {1} type and has {2} features.It is {3} \n".format(x.upper(), des.shapeType, arcpy.GetCount_management(x), aword)
    File.write("{0} feature class is {1} type and has {2} features.It is {3} \n".format(x.upper(), des.shapeType, arcpy.GetCount_management(x), aword))
        
    
File.close()
print "done"