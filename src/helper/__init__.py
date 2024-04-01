import yaml

#def init():
 #   """Function printing python version."""
#
  #  config = read_config()
   # print(config)
#
def read_config():
    """Function printing python version."""   
    with open("../.config/dev.yml", "r") as f:
        return yaml.load(f, Loader=yaml.FullLoader)
#init()
config = read_config()
