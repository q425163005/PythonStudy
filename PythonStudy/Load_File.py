import pickle

load_file=open("save.dat","rb")
load_game_data=pickle.load(load_file)
load_file.close()
