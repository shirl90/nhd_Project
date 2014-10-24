'''
----------------------------------------------------------------------------------
 Source Name:   Bay_WKT.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  
 FeatureCode :  
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
bayTable = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\ExtraData_GNIS\Bay"


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\Bay_WKT.txt", "w")


where_clause = "STATE_ALPH = 'ME'"

query = arcpy.SearchCursor (bayTable, where_clause, "", "", "")
for row in query:
  GNIS_ID = row.getValue("FEATURE_ID")
  the_geom=row.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(str(GNIS_ID) + ' ; ' +wkt)+'\n')
  #print wkt
outFile.close()

print "Data succesfully written in File!"
