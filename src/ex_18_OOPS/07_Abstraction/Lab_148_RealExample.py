from abc import ABC,abstractmethod

class GearBox(ABC):

     @abstractmethod
     def setGear(self):
         pass

class Engine:
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Engine,GearBox):

  def setGear(self):
      print("Gearbox is ready")

  def start(self):
      print("start")

  def stop(self):
      print("stop")

  def drive(self):
      self.start()
      self.setGear()
      self.stop()
      


obj_ref=Car()
obj_ref.drive()