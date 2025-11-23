#Static Methods

# Static methods belongs to class rather than instance of class

class P:
    @staticmethod
    def sum(a,b):
        return a+b

print(P.sum(2,6))