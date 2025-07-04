#  Utility Function
import os
base_dir = os.path.dirname(__file__)
def get_path(filename):
    return os.path.join(base_dir, "data", filename)
