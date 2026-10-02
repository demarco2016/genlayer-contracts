# GenLayer Intelligent Contract
# Example source; deployment is not verified in this repository.

from genlayer import *

class HelloWorld(gl.Contract):
    storage: str

    def __init__(self):
        self.storage = "Hello from GenLayer!"

    @gl.public.view
    def get_storage(self) -> str:
        return self.storage

    @gl.public.write
    def update_storage(self, new_storage: str) -> None:
        self.storage = new_storage

