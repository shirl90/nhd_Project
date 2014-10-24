'''
----------------------------------------------------------------------------------
 Source Name:   Waterfall_WKT.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen

 FeatureCode :  48700 - Waterfall
                43100 - Rapids
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
nhdPoint =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDPoint"
nhdLine =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDLine"
nhdArea =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDArea"


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\Waterfall_WKT.txt", "w")

where_clause = "GNIS_ID <> ' ' AND (FCode = 48700 OR FCode = 43100)"


query_Point = arcpy.SearchCursor (nhdPoint, where_clause, "", "", "")
query_Line = arcpy.SearchCursor (nhdLine, where_clause, "", "", "")
query_Area = arcpy.SearchCursor (nhdArea, where_clause, "", "", "")


for row_Point in query_Point:
  GNIS_ID = row_Point.getValue("GNIS_ID")
  the_geom=row_Point.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')
  #print wkt

for row_Line in query_Line:
  GNIS_ID = row_Line.getValue("GNIS_ID")
  the_geom=row_Line.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')

for row_Area in query_Area:
  GNIS_ID = row_Area.getValue("GNIS_ID")
  the_geom=row_Area.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')
outFile.close()

print "Data succesfully written in File!"
