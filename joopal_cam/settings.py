from os.path import join, dirname
import dotenv


dotenv_path = join(dirname(__file__), '../.env')
dotenv.load_dotenv(dotenv_path)

def write_config(key, val):
    return dotenv.set_key(dotenv_path, key, val)

