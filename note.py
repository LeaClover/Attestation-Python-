class note(object):
    def __init__(self, id, title, body, date, time) -> None:
        self.id = id
        self.title = title
        self.body = body
        self.date = date
        self.time = time
        
    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
        
    def get_body(self):
        return self.body
    
    def set_body(self, body):
        self.body = body
        
    def get_date(self):
        return self.date
    
    def set_date(self, date):
        self.date = date
        
    def get_time(self):
        return self.time
    
    def set_time(self, time):
        self.time = time
    