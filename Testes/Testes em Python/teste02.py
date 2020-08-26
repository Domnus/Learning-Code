lista = []
list1 = []
list2 = []
list3 = []
while True:

  h = int(input('Insira o numero enquanto quiser adicionar,para break digite 0'))
  if h == 0:
      break
  else:
        lista.append(h)
maiorl = 0
def maior(a,b):
    if a > b:
        return a
    return b
def mmci(maiorl):
  list1 = []
  list2 = []
  list3 = []
  for i in lista:

      if i>maiorl:
            maiorl = i
  for j in lista:
      for i in range(1,maiorl+1):
        list1.append(j*i)
        if list2 == []:
            list3 = list1
        else:
            for x in list1:
                if x in list2:
                    list3.append(x)
        mmc=list3[0]
        list1.clear()
        list2 = list3
        list3.clear()
  return mmc
print(mmci(0))