from abc import ABC,abstractmethod

class Browser_Manager(ABC):

    @abstractmethod
    def start(self):
        pass

    def stop(self):
        print("Stopping the browser")


class ChromeBrowser(Browser_Manager):

    def start(self):
        print("Starting the chrome browser")

obj_ref=ChromeBrowser()
obj_ref.start()
obj_ref.stop()