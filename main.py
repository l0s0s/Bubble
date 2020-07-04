class bubble:
  
  def __init__(self, arrage):
    
    for i in range(len(arrage)):
      for arr in range(len(arrage) - 1):
        if arrage[arr] > arrage[arr + 1]:
          arrage[arr], arrage[arr + 1] = arrage[arr + 1], arrage[arr]
    self.arrage = arrage
    

  def display_info(self):
    print(self.arrage)  

arrage = [2, 5, 3, 8, 1, 9]

bub = bubble(arrage)
bub.display_info()