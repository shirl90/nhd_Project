'''
----------------------------------------------------------------------------------
 Source Name:   Well_WKT.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  
 FeatureCode :  48700 - Wells
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
fc_Point = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\LakePond_WKT.txt", "w")


where_clause = "GNIS_ID <> ' ' AND FCode = 48700"

query = arcpy.SearchCursor (fc_Point, where_clause, "", "", "")
for row in query:
  GNIS_ID = row.getValue("GNIS_ID")
  the_geom=row.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')
  #print wkt
outFile.close()

print "Data succesfully written in File!"
