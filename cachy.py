import subprocess
import sys
import os
subprocess.check_call([sys.executable, "-m", "pip", "install", "pathlib", "joblib"])
from pathlib import Path
import joblib
class Cachy:
    def __init__(self):
        cache_path = Path(os.getcwd() + "/bin/cache/")
        if not Path(os.getcwd() + "/bin/").exists():
            Path(os.getcwd() + "/bin/").mkdir()
        if not cache_path.exists():
            cache_path.mkdir()
        if not Path(os.getcwd() + "/bin/cache/sessions/").exists():
            Path(os.getcwd() + "/bin/cache/sessions/").mkdir()
        self.cache_container = []
        print("[Alert] Cacher Rutime Initialized!")
        return

    def session_save(self, name="session_default"):
        session_path = Path(os.getcwd() + "/bin/cache/sessions/" + name + ".session")
        session_path.touch()
        joblib.dump(self.cache_container, session_path)
        return

    def session_load(self, name="session_default"):
        session_path = Path(os.getcwd() + "/bin/cache/sessions/" + name + ".session")
        session_path.touch()
        self.cache_container = joblib.load(session_path)
        return
    
    def session_clear(self, name="session_default"):
        session_path = Path(os.getcwd() + "/bin/cache/sessions/" + name + ".session")
        session_path.touch()
        os.remove(session_path)
        return
    
    def session_clear_all(self):
        listed_dir = os.listdir(Path(os.getcwd() + "/bin/cache/sessions/"))
        for x in listed_dir:
            if x[-8:] == ".session":
                session_path = Path(os.getcwd() + "/bin/cache/sessions/" + x)
                session_path.touch()
                os.remove(session_path)
        return
    
    def deposit(self, data, id):
        self.cache_container.append({"id":id, "data":data})
        print("[Log] Cached item - " + id)
        return
    
    def withdraw(self, id, mode=0):
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                if mode ==1:
                    self.cache_container.pop(count)
                    print("[Log] Passed item - " + id + " and removed from cache")
                else:
                    print("[Log] Passed item - " + id)
                break
        return data
    
    def destroy(self, id):
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                self.cache_container.pop(count)
                print("[Log] Destroyed Cached item - " + id)
                break
        return
    
    def clear(self):
        print("[Alert] Clearing All Cached Items!")
        self.cache_container = []
        return
    
    def save(self, data, id):
        self.cache_container.append({"id":id, "data":data})
        print("[Log] Cached item - " + id)
        print("[Log] Making Local Save of Cached item...")
        cache_path = Path(os.getcwd() + "/bin/cache/")
        if not cache_path.exists():
            cache_path.mkdir()
        cache_file_path = Path(os.getcwd() + "/bin/cache/" + id + ".tmp")
        print(cache_path)
        cache_file_path.touch()
        for x in self.cache_container:
            if x["id"] == id:
                data = x["data"]
                break
        if data is list:
            joblib.dump(data, cache_file_path)
        else:
            with open(cache_file_path, 'w') as f:
                f.write(str(data))
        print("[Log] Local Save Made!")
        return
    
    def load(self, id):
        cache_path = Path(os.getcwd() + "/bin/cache/")
        cache_file_path = Path(os.getcwd() + "/bin/cache/" + id + ".tmp")
        try:
            with open(cache_file_path, 'r') as f:
                data = f.read()
        except:
            data = joblib.load(cache_file_path)
        for x in self.cache_container:
            if x["id"] == id:
                x["data"] = data
                break
        return data

    def save_item(self, id):
        cache_path = Path(os.getcwd() + "/bin/cache/")
        cache_path.mkdir()
        cache_file_path = Path(os.getcwd() + "/bin/cache/" + id + ".tmp")
        cache_file_path.touch()
        for x in self.cache_container:
            if x["id"] == id:
                data = x["data"]
                break
        if data is list:
            joblib.dump(data, cache_file_path)
        else:
            with open(cache_file_path, 'w') as f:
                f.write(str(data))
        return

    def destroy_item(self, id):
        cache_path = Path(os.getcwd() + "/bin/cache/")
        cache_file_path = Path(os.getcwd() + "/bin/cache/" + id + ".tmp")
        os.remove(cache_file_path)
        count = -1
        for x in self.cache_container:
            count = count + 1
            if x["id"] == id:
                data = x["data"]
                self.cache_container.pop(count)
                print("[Log] Destroyed Cached item - " + id)
                break
        return

    def unsave(self, id):
        cache_path = Path(os.getcwd() + "/bin/cache/")
        cache_file_path = Path(os.getcwd() + "/bin/cache/" + id + ".tmp")
        os.remove(cache_file_path)
    
    def clear_all(self):
        self.clear()
        files = os.listdir(Path(os.getcwd() + "/bin/cache/"))
        for x in files:
            os.remove(Path(os.getcwd() + "/bin/cache/" + x))
        return

    def edit(self, data, id):
        for x in self.cache_container:
            if x["id"] == id:
                x["data"] == data
        return
Cachy()