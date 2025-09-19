import threading
import time
import requests


urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2",
    "https://jsonplaceholder.typicode.com/todos/3",
    "https://jsonplaceholder.typicode.com/todos/4",
    "https://jsonplaceholder.typicode.com/todos/5",
]

class ThreadingBeh:
    
    def __init__(self, urls):
        self.urls = urls
        self.threads = [] 
        
    def fetch(self, url):
        response = requests.get(url)
        return response.json()
    
    def process(self):
        for url in self.urls:
            t = threading.Thread(target=self.fetch, args=(url,))
            self.threads.append(t)
            t.start()
        
    
class MultiProcessing:
    def __init__(self):
        pass

class AsyncBeh:
    def __init__(self):
        pass

