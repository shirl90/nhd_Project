'''
----------------------------------------------------------------------------------
 Source Name:   SwampMarsh_WKT.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 Description :  
 FeatureCode :  
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
nhdWaterbody =  "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\Hydrography\NHDWaterbody"


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\Geometry_Data\Swamp_WKT.txt", "w")


where_clause = "GNIS_ID <> ' ' AND FCODE = 46600"

query = arcpy.SearchCursor (nhdWaterbody, where_clause, "", "", "")
for row in query:
  GNIS_ID = row.getValue("GNIS_ID")
  the_geom=row.getValue('Shape') # Get Geometry field
  #print "Retreinving WKT value"
  wkt = the_geom.WKT # Convert to WKT, can also use WKB, JSON etc
  outFile.write(str(GNIS_ID + ' ; ' +wkt)+'\n')
  #print wkt
outFile.close()

print "Data succesfully written in File!"
