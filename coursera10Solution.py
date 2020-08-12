lst = ['From stephen.marquard@uct.ac.za Sat Jan  5 09',
       'From louis@media.berkeley.edu Fri Jan  4 18',
       'From zqian@umich.edu Fri Jan  4 16',
       'From rjlowe@iupui.edu Fri Jan  4 15',
       'From zqian@umich.edu Fri Jan  4 15',
       'From rjlowe@iupui.edu Fri Jan  4 14',
       'From cwen@iupui.edu Fri Jan  4 11',
       'From cwen@iupui.edu Fri Jan  4 11',
       'From gsilver@umich.edu Fri Jan  4 11',
       'From gsilver@umich.edu Fri Jan  4 11',
       'From zqian@umich.edu Fri Jan  4 11',
       'From gsilver@umich.edu Fri Jan  4 11',
       'From wagnermr@iupui.edu Fri Jan  4 10',
       'From zqian@umich.edu Fri Jan  4 10',
       'From antranig@caret.cam.ac.uk Fri Jan  4 10',
       'From gopal.ramasammycook@gmail.com Fri Jan  4 09',
       'From david.horwitz@uct.ac.za Fri Jan  4 07',
       'From david.horwitz@uct.ac.za Fri Jan  4 06',
       'From david.horwitz@uct.ac.za Fri Jan  4 04',
       'From david.horwitz@uct.ac.za Fri Jan  4 04',
       'From stephen.marquard@uct.ac.za Fri Jan  4 04',
       'From louis@media.berkeley.edu Thu Jan  3 19',
       'From louis@media.berkeley.edu Thu Jan  3 17',
       'From ray@media.berkeley.edu Thu Jan  3 17',
       'From cwen@iupui.edu Thu Jan  3 16',
       'From cwen@iupui.edu Thu Jan  3 16',
       'From cwen@iupui.edu Thu Jan  3 16']

mark = list()

for l in lst:
    mark.append(l[-2] + l[-1])


counts = dict()

for word in mark:
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] = counts[word]+1

llist = list()
for key, val in counts.items():
    newtup = (key, val)
    llist.append(newtup)

llist.sort()

for key, val in llist:
    print(key, val)