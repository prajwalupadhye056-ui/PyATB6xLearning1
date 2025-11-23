class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MySQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading form MySQL")

class TC1:
    def run(self):
        ExcelReader.readExcelFile()
        MySQLDBConnection.readMySQLFile()
        print("Hi")

class TC2:
    def run(self):
        ExcelReader.readExcelFile()
        MySQLDBConnection.readMySQLFile()
        print("Hi")

tc=TC1()
tc1=TC2()
tc.run()
tc1.run()