'''
----------------------------------------------------------------------------------
 Source Name:   Load_Rapids.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  43100 - Rapids
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
#arcpy.env.workspace = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Waterfalls.txt", "w")
print "Workspace Space Set"
fc_NHDPoint = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"
fc_NHDArea = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDArea"


# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 43100"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
Waterfall_TablePoint = arcpy.SearchCursor (fc_NHDPoint, where_clause, "", "", "")
Waterfall_TableArea = arcpy.SearchCursor (fc_NHDArea, where_clause, "", "", "")


for rows in Waterfall_TablePoint:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' - ' +GNISName)+'\n')
    #print GNISName
    rows = Waterfall_TablePoint.next()

for rows in Waterfall_TableArea:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' - ' +GNISName)+'\n')
    #print GNISName
    rows = Waterfall_TableArea.next()
outFile.close()

