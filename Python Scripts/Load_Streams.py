'''
----------------------------------------------------------------------------------
 Source Name:   Load_Streams.py
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
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Data-MidAtlantic\List_Streams.txt", "w")
print "Workspace Space Set"
fc_NHDFlowLine = "Z:\Documents\Shirly\Ontology Research\Data-To Work\Data-MidAtlantic\NHDPlusMA.gdb\Hydrography\FlowLine_Dissolve"
fields = ["GNIS_Name", "GNIS_ID"]

# Create a search cursor

#where_clause = "GNIS_ID <> ' ' AND (FCode = 46000 OR FCode = 46003 OR FCode = 46006)"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
where_clause = "GNIS_ID <> ' '"
Stream_Table = arcpy.SearchCursor (fc_NHDFlowLine, where_clause, "", "", "")
#Stream_Table = arcpy.da.SearchCursor (fc_NHDFlowLine,fields , where_clause, "", "", "DISTINCT")

           

for rows in Stream_Table:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    rows = Stream_Table.next()
outFile.close()

 
