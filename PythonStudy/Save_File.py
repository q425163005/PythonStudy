import pickle

game_data={"position":"N2 E3","POCKET":["key","knife"],"money":60}
save_file=open("save.dat","wb")
pickle.dump(game_data,save_file)
save_file.close()