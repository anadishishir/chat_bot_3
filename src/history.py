import json 
import os 

class HistoryManager : 
    def __init__(self, storage_dir="chat_session") : 
        if not os.path.exists(storage_dir) : 
            os.makedirs(storage_dir) 
    
    def _get_path(self, user_id) : 
        return os.path.join(self.stirage_dir,f"{user_id}.json") 
    
    def get_history(self, user_id) : 
        path = self._get_path(user_id) 
        if not os.path.exists(path) : 
            return [] 
        with open(path,"r") as f : 
            return json.load(f) 
    
    def add_to_history(self, user_id, role, content) : 
        history = self.get_history(user_id) 
        history.append({"role" : role, "content" : content}) 
        with open(self._get_path(user_id), "w") as f : 
            json.dump(history[-10:], f) 