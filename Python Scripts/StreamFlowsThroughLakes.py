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
plusFlow =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\PlusFlow"
#nhdWaterBody = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDWaterbody"
#nhdFlowLine = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDFlowLine"

outFile = open("Z:\Documents\Shirly\Ontology Research\Output\StreamFlowsThroughLakes.txt", "w")
print "Workspace Set"

# Create a search cursor


#where_clause = '"GNIS_ID" IS NOT NULL AND "FCode" = 46006'
#where_clause = "GNIS_ID = '869805'"
where_clause = "From_GNIS_Name <> ' ' AND To_GNIS_Name <> ' ' AND From_GNIS_Name <> To_GNIS_Name AND (From_FCODE = 46006 OR From_FCODE = 46003) AND ( To_FCODE = 55800)"

# Make a feature layer with nhdWaterBody - Target Layer
#arcpy.MakeFeatureLayer_management(nhdWaterBody, "NHDWaterbody")
# Make a feature layer with nhdFlowLine - Source Layer
#arcpy.MakeFeatureLayer_management(nhdFlowLine, "NHDFlowLine")

#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
plusFlow_Results = arcpy.SearchCursor (plusFlow, where_clause, "", "", "")
nameField = "COMID"

for rows in plusFlow_Results:
    From_GNISID = rows.getValue("From_GNIS_ID")
    To_GNISID = rows.getValue("To_GNIS_ID")
    # Make a feature layer containing only the feature of interest
    #arcpy.MakeFeatureLayer_management(nhdFlowLine,"SelectionLineLayer",'"' + str(nameField) + '" =' + str(To_COMID))
    # Apply a selection by location
    #output_Layer = arcpy.SelectLayerByLocation_management("NHDWaterbody","INTERSECT","SelectionLineLayer","","NEW_SELECTION")
    #output_Layer_Results = arcpy.SearchCursor (output_Layer, "", "", "", "")
    where_clause2 = "From_GNIS_ID ='"+To_GNISID+"' AND To_GNIS_ID = '"+From_GNISID+"'"
    print where_clause2
    plusFlow_Results2 = arcpy.SearchCursor (plusFlow, where_clause2, "", "", "")

    for result_rows in plusFlow_Results2:
        outFile.write(str(From_GNISID + ';' +To_GNISID)+'\n')
    #arcpy.Delete_management("SelectionLineLayer")
outFile.close()

