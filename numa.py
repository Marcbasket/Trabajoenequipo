def lines(nombreArchivo,N):
 try:
  f = open(nombreArchivo,'r')
  l = f.readlines()
  return l[N-1]
 except:
  return("error")
