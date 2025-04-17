import numpy as np
pad_arr = np.array(["SAYANORA","KOMAL","9553935633","0","JAKKAKOMALSAI"])
for string in pad_arr  : 
    if len(string) < 15 : 
       sub = 15 - len(string)
       left_pad = sub//2
       right_pad = sub-left_pad
       centered_string = "_"*left_pad + string + "_"*right_pad
       left_string = string + "_"*sub
       right_string = "_"*sub+string
       print("CENTERED : "+centered_string)
       print("LEFTED : "+left_string)
       print("RIGTHED : "+right_string+"\n")
    else : 
        cut_string = string[:15]
        print("SLICED : "+cut_string+"\n")
    