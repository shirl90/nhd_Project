'''
----------------------------------------------------------------------------------
 Source Name:   Load_SwampMarsh.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  33400 - Connector
                33600 - Canal/Ditch
                42801 - Pipeline
                42803 - Underground Pipeline
                46000 - Stream/River
                46003 - Stream/River (Intermittent)
                46006 - Stream/River (Perrenial)
                55800 - Artificial Path
                56600 - Coastline
                46600 - SwampMarsh
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
arcpy.env.workspace = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDWaterbody"
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_SwampMarsh.txt", "w")
print "Workspace Space Set"
fc_NHDWaterbody = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDWaterbody"

# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 46600"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
Swamp_Table = arcpy.SearchCursor (fc_NHDWaterbody, where_clause, "", "", "")

for rows in Swamp_Table:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' - ' +GNISName)+'\n')
    #print GNISName
    rows = Swamp_Table.next()
outFile.close()

