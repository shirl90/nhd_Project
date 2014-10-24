'''
----------------------------------------------------------------------------------
 Source Name:   Load_Waterfalls.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  45800 - SpringSeep
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\\Spring_WKT.txt", "w")
print "Workspace Space Set"
fc_NHDPoint = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"



# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 45800"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
query_Point = arcpy.SearchCursor (fc_NHDPoint, where_clause, "", "", "")


for row_Point in query_Point:
  GNIS_ID = row_Point.getValue("GNIS_ID")
  the_geom=row_Point.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')
  #print wkt
    
outFile.close()

