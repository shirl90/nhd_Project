'''
----------------------------------------------------------------------------------
 Source Name:   Load_Waterfalls.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  45800 - SpringSeep
            
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Spring.txt", "w")
print "Workspace Space Set"
fc_NHDPoint = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"

# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 45800"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
Spring_Table_Point = arcpy.SearchCursor (fc_NHDPoint, where_clause, "", "", "")

for rows in Spring_Table_Point:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Waterfall_Table_Point.next()   
outFile.close()

