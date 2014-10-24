'''
----------------------------------------------------------------------------------
 Source Name:   Load_Bays.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  
                
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace
outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Bays.txt", "w")
print "Workspace Space Set"
bayTable = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\ExtraData_GNIS\Bay"

# Create a search cursor

where_clause = "STATE_ALPH = 'ME'"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
bay_Table = arcpy.SearchCursor (bayTable, where_clause, "", "", "")

for rows in bay_Table:
    GNISName = rows.getValue("FEATURE_NA")
    GNISID = rows.getValue("FEATURE_ID")
    outFile.write(str(str(GNISID) + ' ; ' +str(GNISName))+'\n')
    #print GNISName
    #rows = Stream_Table.next()
outFile.close()

