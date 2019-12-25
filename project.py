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
       return arg
def num(a):
    integer = check_integer(a)
    result(integer)

def result(integer):
   c = str(integer)
   print("Хорошое число:"+c)

def check_integer(arg):
   try:
      a = int(arg)
      return a
   except ValueError:
      print("Это не число")
      a = input("Введите число:")

      check_integer(a)

if __name__ == "__main__":
   arguments = sys.argv[1:]
   arg = main(arguments)
   num(arg)