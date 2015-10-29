def lines(nombreArchivo,S):
 try:
  f = open(nombreArchivo,'r')
  l = f.readlines()
  for i in l:
      k=i.split()
      if k[0]=="117,":
          if S==k[3][:-25]:
              print i
      elif S==k[3][:-1]:
          print i
 except:
  return("error")
