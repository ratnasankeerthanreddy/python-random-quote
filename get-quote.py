import random
def main():
 f = open("quotes.txt")
 quotes = f.readlines()
 quotes=[s.strip() for s in quotes]
 #print("Keep it logically awesome.")
 f.close()
 l=len(quotes)
 r=random.randint(0,l)
 print(quotes[r])

if __name__== "__main__":
  main()
