def lines(nombreArchivo,S):
 try:
  f = open(nombreArchivo,'r')
  l = f.readlines()
  for i in l:
      k=i.split()
      if S==k[2]:
          print i
 except:
  return("error")
  #Si trabaje profesor!!! soy Ximena XD, estábamos hablando por skype de como resolverlo.
