'''
----------------------------------------------------------------------------------
 Source Name:   Load_Lakes.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  48700 - Wells
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Well.txt", "w")
print "Workspace Space Set"
fc_Point = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\NHDPoint"

# Create a search cursor

where_clause = "GNIS_ID <> ' ' AND FCode = 48700"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
well_Table = arcpy.SearchCursor (fc_Point, where_clause, "", "", "")

for rows in well_Table:
    GNISName = rows.getValue("GNIS_Name")
    GNISID = rows.getValue("GNIS_ID")
    outFile.write(str(GNISID + ' ; ' +GNISName)+'\n')
    #print GNISName
    #rows = Stream_Table.next()
outFile.close()

