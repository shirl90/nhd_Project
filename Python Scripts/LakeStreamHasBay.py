'''
----------------------------------------------------------------------------------
 Source Name:   LakeStreamHasBay.py
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
NHDArea =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDWaterbody"
NHDWaterbody = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDWaterbody"
Bay = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\ExtraData_GNIS\Bay"

outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Data-NorthEast\LakeRiver_HasBays.txt", "w")
print "Workspace Set"

# Create a search cursor

where_clause = "STATE_ALPH = 'ME'"
where_clause_Polygons = "FTYPE = 'StreamRiver' OR FTYPE = 'LakePond'"

# Make a feature layer with nhdWaterBody - Target Layer
arcpy.MakeFeatureLayer_management(NHDWaterbody, "NHDWaterbody",where_clause_Polygons)
# Make a feature layer with nhdFlowLine - Source Layer
arcpy.MakeFeatureLayer_management(NHDArea, "NHDArea",where_clause_Polygons)

#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
bay_Results = arcpy.SearchCursor (Bay, where_clause, "", "", "")
nameField = "FEATURE_ID"

for rows in bay_Results:
    GNISID = rows.getValue("FEATURE_ID")
   
    # Make a feature layer containing only the feature of interest
    arcpy.MakeFeatureLayer_management(Bay,"SelectionBayLayer",'"' + str(nameField) + '" =' + str(GNISID))
    # Apply a selection by location
    output_Layer = arcpy.SelectLayerByLocation_management("NHDWaterbody","INTERSECT","SelectionBayLayer","0.5 Kilometers","NEW_SELECTION")
    output_Layer_Results = arcpy.SearchCursor (output_Layer, "", "", "", "")
    for result_rows in output_Layer_Results:
        Source_GNISID = result_rows.getValue("GNIS_ID")
        if Source_GNISID.strip():
            #print str(From_GNISName + ' - ' +To_GNISName)
            outFile.write(str(str(Source_GNISID) + ';' +str(GNISID))+'\n')

    output_Layer1 = arcpy.SelectLayerByLocation_management("NHDArea","INTERSECT","SelectionBayLayer","0.5 Kilometers","NEW_SELECTION")
    output_Layer_Results1 = arcpy.SearchCursor (output_Layer1, "", "", "", "")
    for result_rows1 in output_Layer_Results1:
        Source_GNISID = result_rows1.getValue("GNIS_ID")
        if Source_GNISID.strip():
            #print str(From_GNISName + ' - ' +To_GNISName)
            outFile.write(str(str(Source_GNISID) + ';' +str(GNISID))+'\n')
            
    arcpy.Delete_management("SelectionBayLayer")
outFile.close()

