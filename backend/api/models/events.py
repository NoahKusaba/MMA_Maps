class Events():
    __table__ ='events'
    columns = ["event", "headline", "venue","date", "latitude", "longitude", "color", "url", "org"] 
    def __init__(self,**kwargs) -> None:

        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f"{key} not in columns")

        self.__dict__= dict(zip(self.columns,kwargs.values()))