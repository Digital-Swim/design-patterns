class Database:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        print(args)
        print(kwargs)
        if not(cls._instance):
            print("creating new instance")
            cls._instance = super().__new__(cls)
        
        print("returning new instance")
        return cls._instance
    
    
    def __init__(self, x):
        self.connection = "connection created"
        self.x = x
        print(self.connection)
    
     
db1 = Database(1)
print(db1.x)
db2 = Database("a")
print(db1.x, db2.x)
