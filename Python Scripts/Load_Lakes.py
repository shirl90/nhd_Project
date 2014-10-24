'''
----------------------------------------------------------------------------------
 Source Name:   Load_Lakes.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  39004 - LakePond
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
arcpy.env.workspace = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDFlowLine_Dissolve_GNIS_ID"
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Lakes.txt", "w")
print "Workspace Space Set"
fc_WaterBody = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDWaterbody"

# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 39004"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
lake_Table = arcpy.SearchCursor (fc_WaterBody, where_clause, "", "", "")

for rows in lake_Table:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Stream_Table.next()
outFile.close()

