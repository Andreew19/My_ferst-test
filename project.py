import sys, getopt

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print ('project.py -i <inputfile>') 
      sys.exit(1)
   for opt, arg in opts:
      if opt == '-h':
         print ('project.py -i <inputfile>') 
         sys.exit()
      elif opt in ("-i", "--ifile"):
       num(arg)
def num(a):

        try:
            a = int(input("Введите число:"))
        except ValueError:
           print("Это не число")
        c = str(a)
        print("Хорошое число:"+c)
if __name__ == "__main__":
   arguments = sys.argv[1:]
   main(arguments)
