'''
----------------------------------------------------------------------------------
 Source Name:   StreamFlowsIntoLake.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  Feature Code for Sea/Ocean - 31200
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
nhdWaterBody = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDWaterbody"

outFile = open("Z:\Documents\Shirly\Ontology Research\Output\SwampPartOfLakePonds.txt", "w")
print "Workspace Set"

# Create a search cursor


#where_clause = '"GNIS_ID" IS NOT NULL AND "FCode" = 46006'
#where_clause = "GNIS_ID = '869805'"
where_clause = "GNIS_ID <> ' ' AND FCODE = 46600"
where_clause_Lake = "GNIS_ID <> ' ' AND FCODE = 39004"
# Make a feature layer with nhdWaterBody - Target Layer
arcpy.MakeFeatureLayer_management(nhdWaterBody, "LakesPonds",where_clause_Lake,"","")

#stream_Polygon_Features = arcpy.SearchCursor (nhdWaterBody_Stream, where_clause_Stream_Polygons, "", "", "")
#arcpy.MakeFeatureLayer_management(nhdArea, "StreamPolygons",where_clause_Stream,"","")

#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
swampFeatures = arcpy.SearchCursor (nhdWaterBody, where_clause, "", "", "")
nameField = "GNIS_ID"

for rows in swampFeatures:
    GNIS_ID = rows.getValue("GNIS_ID")
    print GNIS_ID
    # Make a feature layer containing only the feature of interest
    arcpy.MakeFeatureLayer_management(nhdWaterBody,"SelectionSourceLayer","GNIS_ID ='" + str(GNIS_ID)+"'")
    # Apply a selection by location - For Lakes
    output_Layer = arcpy.SelectLayerByLocation_management("LakesPonds","INTERSECT","SelectionSourceLayer","","NEW_SELECTION")
    output_Layer_Results = arcpy.SearchCursor (output_Layer, "", "", "", "")
    for result_rows in output_Layer_Results:
        GNIS_ID_Lake = result_rows.getValue("GNIS_ID")
        if GNIS_ID_Lake.strip():
            #print str(From_GNISName + ' - ' +To_GNISName)
            outFile.write(str(GNIS_ID + ' ; ' + GNIS_ID_Lake)+'\n')
    arcpy.Delete_management("SelectionSourceLayer")
outFile.close()

