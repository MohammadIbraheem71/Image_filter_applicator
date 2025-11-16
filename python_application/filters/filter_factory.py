#import filters here

#this class maintains a list (or dictionary) of the filters
#takes in an input name and returns a filter object
#wowowow hello this is ibraheem

#need to make this a singelton

class filter_factory:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(filter_factory, cls).__new__(cls)
            cls._instance.filter_dict = {}
        
        return cls._instance
    
    def add_filter(self, filter_name : str, filter_obj):
        self.filter_dict[filter_name] = filter_obj
        
    def del_filter(self, filter_name : str):
        if filter_name not in self.filter_dict:
            raise Exception(f"trying to delete {filter_name}, it does not exist in the filter_factory")
            return
        
        del self.filter_dict[filter_name]

    def get_filter(self, filter_name : str):
        if filter_name not in self.filter_dict:
            raise Exception(f"unknown filter: {filter_name}")
            return
        
        return self.filter_dict[filter_name]