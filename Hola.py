def lines(nombreArchivo,N):
 try:
  f = open(nombreArchivo,'r')
  l = f.readlines()
  for i in l:
      k=i.split()
      return l[:N]
 except:
  return("error")

def dictionary(R):
    dic={}
    for i in R:
        E={}
        k=i.split()
        E={'nombre':k[3][:-1]}

        E={'resto':k[3:]}
        print E['nombre'],E['resto']
        dic={k[1]:E}
    return dic

def imprimir():
    dic=dictionary(lines('pt-data1.csv',118))
    print len(dic)
    for i in dic:
        print i
