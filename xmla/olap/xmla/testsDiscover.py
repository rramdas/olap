'''
Created on 18.04.2012

SSAS Tests are done against the Adventure Works DW 2008R2, tested against ssas version 10.50.2500.0 (comes with sqlserver 2008 R2)
Mondrian was test with version 3.3.0.14703

@author: norman

n.b.:
  Mondrian is running with a mysql backend. 
  Using the distributed embedded derby backend fails in MDSchemaMembers with an internal error (when
  a subselect is executed in the read-only container where the database lives).
  
'''

import unittest
import olap.xmla.xmla as xmla



mondrian={
"type":"mondrian",
"spn":None,          
"location":"http://localhost:8080/mondrian/xmla",
"ds": "Provider=Mondrian;DataSource=MondrianFoodMart;",
"catalog":"FoodMart",
"restrict_cube":"HR",
"restrict_dim":"Position",
"restrict_unique_dim":"[Gender]",
"cubes_expected":7,
"restrict_funcname":"||",
"restrict_hier":"Time",
"restrict_level_unique_name":"[Employees].[Employee Id]",
"restrict_hierarchy_unique_name":"[Time]",
"cube_measures":5,
"schema_levels":3,
}

ssas={
"type":"ssas",
"spn":"HOST@DWH-BI",
"location":"http://dwh-bi/olap/msmdpump.dll",
"ds":"DWH-BI",
"catalog":"Adventure Works DW 2008R2",
"restrict_cube":"Adventure Works",
"restrict_dim":"Account",
"restrict_unique_dim":"[Account]",
"cubes_expected":7,
"restrict_funcname":"TRIM",
"restrict_hier":"Account Number",
"restrict_level_unique_name":"[Customer].[Customer Geography].[Country]",
"restrict_hierarchy_unique_name":"[Customer].[Customer Geography]",
"cube_measures": 51,
"schema_levels":6,
}

supported = None

class TestXMLA(unittest.TestCase):
    
    def setUp(self):
        self.be = mondrian
        self.p = xmla.XMLAProvider()
        self.c = self.p.connect(location=self.be["location"], doKerberos = (self.be == ssas), spn=self.be["spn"])
        self.proprietary, self.conform, self.unsupported, self.supported = self.getSchemaRowsetSupport()
         
    def getSchemaRowsetSupport(self):
        global supported
        if supported is None:
            supported=self.c.getSchemaRowsets().keys()
        proprietary = filter(lambda x: not(x in xmla.xmla1_1_rowsets), supported)
        conform = filter(lambda x: (x in xmla.xmla1_1_rowsets), supported)
        unsupported = filter(lambda x: not (x in supported), xmla.xmla1_1_rowsets)
        return proprietary, conform, unsupported, supported
    
    def tearDown(self):
        pass
    
    def testGetDatasources(self):
        erg=self.c.getDatasources()
        print erg
        self.assertTrue(len(erg) == 1, "One Datasource is expected")
        self.assertEqual(self.be["ds"], erg[0]["DataSourceName"])
        
    def testGetProperties(self):
        erg=self.c.getProperties()
        # check fpr required xmla properties
        req = "AxisFormat,BeginRange,Catalog,Content,Cube,DataSourceInfo,EndRange,Format,LocaleIdentifier,MDXSupport,Password,ProviderName,ProviderVersion,StateSupport,Timeout,UserName"
        for p in req.split(","):
            self.assertIn(p, erg)

    def testGetDBSchemaCatalogs(self):
        erg=self.c.getDBSchemaCatalogs()
        #print self.c.getSchemaRowsets()["DBSCHEMA_CATALOGS"]
        self.assertTrue(len(erg.keys()) > 0, "One Catalog is expected - at least")
        self.assertIn(self.be["catalog"], erg)
        
    
    def testGetDBSchemaColumns(self):
        erg=self.c.getDBSchemaColumns()
        self.assertTrue(len(erg) > 0, "There must be at least one column, really!")
        
    def testGetDBSchemaTables(self):
        erg=self.c.getDBSchemaTables()
        self.assertTrue(len(erg) > 0, "There must be at least one table")

    def testGetDBSchemaProviderTypes(self):
        erg=self.c.getDBSchemaProviderTypes()
        self.assertTrue(len(erg) > 0, "There should be at least one type like INTEGER for example")
        
    def testGetDBSchemaTablesInfo(self):
        if "DBSCHEMA_TABLES_INFO" in self.unsupported: return
        erg=self.c.getDBSchemaTablesInfo()
        self.assertTrue(len(erg) > 0, "There must be at least one tablesinfo")

    def testGetMDSchemaActions(self):
        erg=self.c.getMDSchemaActions(restrictions={"CUBE_NAME":self.be["restrict_cube"]})
        self.assertTrue(len(erg)==0, "no actions expected")

    def testGetMDSchemaCubes(self):
        #print self.c.getSchemaRowsets()["MDSCHEMA_CUBES"]
        # oh my, mondrian doesn't know what do do with Catalog in the Proplist ... but only
        # when requesting cubes, other rowset requests are going through just fine (are probably ignored
        # on the server side)
        if self.be["type"] == "ssas": props = {"CATALOG":self.be["catalog"]}
        else: props=None
        erg=self.c.getMDSchemaCubes(properties=props)
        self.assertEquals(len(erg), self.be["cubes_expected"])
        erg=self.c.getMDSchemaCubes(restrictions={"CUBE_NAME":self.be["restrict_cube"]}, properties=props)
        self.assertEquals(len(erg), 1)

    def testGetSchemaRowsets(self):
        erg=self.c.getSchemaRowsets()
        self.assertTrue(len(erg)>0, "at least one schema is expected")
        
    def testGetMDSchemaFunctions(self):
        erg=self.c.getMDSchemaFunctions()
        self.assertTrue(len(erg)> 1, "There should be more than one function description.")
        erg=self.c.getMDSchemaFunctions(restrictions={"FUNCTION_NAME":self.be["restrict_funcname"]})
        self.assertEquals(len(erg), 1)
        
    def testGetMDSchemaMembers(self):
        erg=self.c.getMDSchemaMembers({'DIMENSION_UNIQUE_NAME':self.be["restrict_unique_dim"]}, properties={"Catalog":self.be["catalog"]})
        self.assertTrue(len(erg)> 1, "There should be more than one dimension member.")

    def testGetMDSchemaProperties(self):
        erg=self.c.getMDSchemaProperties({"CUBE_NAME":self.be["restrict_cube"], 'LEVEL_UNIQUE_NAME': self.be["restrict_level_unique_name"]}, properties={"Catalog":self.be["catalog"]})
        self.assertTrue(len(erg)> 1, "There should be more than one schema property.")

    def testGetMDSchemaSets(self):
        erg=self.c.getMDSchemaSets()
        
        self.assertTrue(len(erg)> 0, "There should be a schema set.")

    def testGetEnumerators(self):
        erg = self.c.getEnumerators()
        self.assertTrue(len(erg)> 0, "There should be at least one enumerator (AuthenticationMode for instance).")
        
    def testGetLiterals(self):
        erg = self.c.getLiterals()
        self.assertTrue(len(erg)> 0, "There should be at least one literal.")
        
    def testGetKeywords(self):
        erg = self.c.getKeywords()
        self.assertTrue(len(erg)> 0, "There should be at least one keyword.")
        
        #print self.c.getSchemaRowsets().keys()

    def testGetMDSchemaDimensions(self):
        #print self.c.getSchemaRowsets()["MDSCHEMA_DIMENSIONS"]
        erg=self.c.getMDSchemaDimensions(restrictions={"CUBE_NAME":self.be["restrict_cube"], "DIMENSION_NAME":self.be["restrict_dim"]},
                                         properties={"Catalog":self.be["catalog"]})
        self.assertEquals(len(erg), 1)
        
    def testGetMDSchemaHierarchies(self):
        erg=self.c.getMDSchemaHierarchies(properties={"Catalog":self.be["catalog"]})
        self.assertTrue(len(erg)> 1, "There should be more than one hierarchy.")
        erg=self.c.getMDSchemaHierarchies(restrictions={"HIERARCHY_NAME":self.be["restrict_hier"], 
                                                        "CUBE_NAME":self.be["restrict_cube"]}, properties={"Catalog":self.be["catalog"]})
        self.assertEquals(len(erg), 1)

    def testGetMDSchemaMeasures(self):
        erg=self.c.getMDSchemaMeasures(properties={"Catalog":self.be["catalog"]})
        self.assertTrue(len(erg)> 1, "There should be more than one measure.")
        erg=self.c.getMDSchemaMeasures({"CUBE_NAME":self.be["restrict_cube"]}, properties={"Catalog":self.be["catalog"]})
        self.assertEquals(len(erg), self.be["cube_measures"])

    def testGetSchemaLevels(self):
        erg = self.c.getMDSchemaLevels({"CUBE_NAME":self.be["restrict_cube"], 'HIERARCHY_UNIQUE_NAME': self.be["restrict_hierarchy_unique_name"]}, properties={"Catalog":self.be["catalog"]})
        self.assertEquals(len(erg), self.be["schema_levels"])
    
    def testGetDBSchemaSchemata(self):
        if "DBSCHEMA_SCHEMATA" in self.supported:
            erg = self.c.Discover("DBSCHEMA_SCHEMATA")


        
def test_suite():
    #import s4u2p
    #s4u2p.authGSSKeytab("/home/norman/workspace/olap/host.keytab")
    return unittest.makeSuite(TestXMLA)
