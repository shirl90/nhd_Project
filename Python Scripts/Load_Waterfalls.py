'''
----------------------------------------------------------------------------------
 Source Name:   Load_Waterfalls.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  48700 - Waterfall
                43100 - Rapids
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Waterfalls.txt", "w")
print "Workspace Space Set"
fc_NHDPoint = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"
fc_NHDLine = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDLine"
fc_NHDArea = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDArea"



# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND (FCode = 48700 OR FCode = 43100)"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
Waterfall_Table_Point = arcpy.SearchCursor (fc_NHDPoint, where_clause, "", "", "")

for rows in Waterfall_Table_Point:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Waterfall_Table_Point.next()

Waterfall_Table_Line = arcpy.SearchCursor (fc_NHDLine, where_clause, "", "", "")

for rows in Waterfall_Table_Line:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Waterfall_Table_Line.next()
    
Waterfall_Table_Area = arcpy.SearchCursor (fc_NHDArea, where_clause, "", "", "")

for rows in Waterfall_Table_Area:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Waterfall_Table_Area.next()
    
outFile.close()

