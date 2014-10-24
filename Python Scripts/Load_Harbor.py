'''
----------------------------------------------------------------------------------
 Source Name:   Load_Harbor.py
 Version:       ArcGIS 10.1
 Author:        Shirly Stephen
 FeatureCode :  
            
--------------------------------------------------------------------------------    '''
# Import system modules
import arcpy

### Set the workspace


outFile = open("Z:\Documents\Shirly\Ontology Research\Output\List_Harbor.txt", "w")
print "Workspace Space Set"
harborData = "Z:\Documents\Shirly\Ontology Research\Data-To Work\NHDPlusNE.gdb\ExtraData_GNIS\Harbor"

# Create a search cursor

where_clause = "FEATURE_NA <> ' '"
#where_clause = "[" + fieldname + "] = " + value # for Personal Geodatabase
harbor_Table = arcpy.SearchCursor (harborData, where_clause, "", "", "")

for rows in harbor_Table:
    GNISName = rows.getValue("FEATURE_NA")
    GNISID = rows.getValue("FEATURE_ID")
    outFile.write(str(str(GNISID) + ' ; ' +GNISName)+'\n')
    #print GNISName
outFile.close()

