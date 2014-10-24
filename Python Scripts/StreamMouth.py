'''
----------------------------------------------------------------------------------
 Source Name:   FlowsWrite.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  Mouth of Streams
                From GNIS  -  To GNIS
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
plusFlow =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\PlusFlow"
NHDFlowLine_Dissolve_ForPoints =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDFlowLine_Dissolve_ForPoints.shp"


outFileStreamSource = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\StreamMouth.txt", "w")

print "Workspace Set"

# Create a search cursor


#where_clause = '"GNIS_ID" IS NOT NULL AND "FCode" = 46006'
#where_clause = "GNIS_ID = '869805'"
where_clause = "From_GNIS_Name <> ' ' AND To_GNIS_Name <> ' ' AND From_GNIS_Name <> To_GNIS_Name AND (From_FCODE = 46006 OR From_FCODE = 46003) AND ( To_FCODE = 46003 OR To_FCODE = 46006 )"
print where_clause
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
stream_Table = arcpy.SearchCursor (plusFlow, where_clause, "", "", "")

for rows in stream_Table:
    From_GNISID = rows.getValue("From_GNIS_ID")
    To_GNISID = rows.getValue("To_GNIS_ID")
    Start_X = rows.getValue("Start_X")
    Start_Y = rows.getValue("Start_Y")
##    where_clauseGNIS = "GNIS_ID ='"+To_GNISID+"'"
##    streamFeatureTable = arcpy.SearchCursor (NHDFlowLine_Dissolve_ForPoints, where_clauseGNIS, "", "", "")
##    for row in streamFeatureTable:
##        Start_X = row.getValue("Start_X")
##        Start_Y = row.getValue("Start_Y")
    outFileStreamSource.write(str(To_GNISID + ';' +str(Start_X)+ ';' +str(Start_Y))+'\n')
   # print str(From_GNISName + ' - ' +To_GNISName)
outFileStreamSource.close()

