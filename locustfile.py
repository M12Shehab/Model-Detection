from locust import HttpUser, task

class QuickstartUser(HttpUser):
    body = """
    Every User/HTTP connection from Locust opens a new file (technically a file descriptor). 
    Many operating systems by default set a low limit for the maximum number of files that can be open at the same time.
    Locust will try to adjust this automatically for you, but in a lot of cases your operating system will not allow it (in which case you will get a warning in the log). 
    Instead you will have to do it manually.
    """
    @task
    def hello_world(self):
        self.client.post("/predict", json={"text": f"{self.body}"})