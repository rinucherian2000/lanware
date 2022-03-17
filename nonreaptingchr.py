from collections import Counter
def nonrepeatchar(string):
   strings=Counter(string)
   for i in string:
      if(strings[i]==1):
         print(i)
         break
string="pythondjangostudents"
nonrepeatchar(string)