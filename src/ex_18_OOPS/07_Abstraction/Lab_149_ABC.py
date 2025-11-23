from abc import ABC ,abstractmethod

class ExcelReader(ABC):

    @abstractmethod
    def readfromExcel(self):
        pass

class Browser(ExcelReader):
    @abstractmethod
    def startBrowser(self):
        pass

    @abstractmethod
    def stopBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Starting the browser")

    def readfromExcel(self):
        print("Reading from Excel")

    def stopBrowser(self):
        print("Stopping the browser")

    def runTc(self):
        self.startBrowser()
        self.readfromExcel()
        self.stopBrowser()

tc =TC1()
tc.runTc()


