
def KDA():
  try:
    k = int(input("Input your Kills: "))
    d = int(input("Input your Deaths: "))
    kdw = int(input("Input your desired KD: "))
    kd = k/d
    if kd < 1:
      k1 = d-k
      print("You need to do",k1,"Kills this match to achieve your KD of",kdw)    
    elif kd >= 1:
      k1 = (kdw*d)
      k2=(k1-k)
      print("You need to do",k2,"Kills this match to achieve your KD of",kdw)   
  except:
    print("Invalid input, try again\n")
    KDA()

KDA()