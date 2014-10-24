'''
----------------------------------------------------------------------------------
 Source Name:   FlowsWrite.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  
 FeatureCode :  
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
dissolveLayer =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\Simplify_Final"
nhdArea =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDArea"
flowLineLayer =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDFlowLine"


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\FlowLines_Stream_WKT.txt", "w")


where_clause_Line = "GNIS_ID <> ' '"

query_Line = arcpy.SearchCursor (dissolveLayer, where_clause_Line, "", "", "")
for row_Line in query_Line:
  GNIS_ID = row_Line.getValue("GNIS_ID")
##  where_clause = "GNIS_ID = '" + GNIS_ID+"'"
##  query = arcpy.SearchCursor (flowLineLayer, where_clause, "", "", "")
##  for row in query:
##    GNIS_NAME = row.getValue("GNIS_NAME")
  GNIS_NAME = row_Line.getValue("GNIS_NAME")
  the_geom=row_Line.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +GNIS_NAME+ ' ; ' +wkt)+'\n')
  #print wkt

where_clause_Polygon = "GNIS_ID <> ' ' AND FCODE = 46006"

query_Polygon = arcpy.SearchCursor (nhdArea, where_clause_Polygon, "", "", "")
for row_Polygon in query_Polygon:
  GNIS_ID = row_Polygon.getValue("GNIS_ID")
  GNIS_NAME = row_Polygon.getValue("GNIS_NAME")
  the_geom=row_Polygon.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +GNIS_NAME+ ' ; ' +wkt)+'\n')
  #print wkt
outFile.close()

print "Data succesfully written in File!"
