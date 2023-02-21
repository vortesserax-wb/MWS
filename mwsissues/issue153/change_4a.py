# coding=utf-8
""" 
change_4a.py   
"""
from __future__ import print_function
import sys, re,codecs
import digentry
import langgroup

def select(entries):
 nfound = 0
 for entry in entries:
  langgroup = entry.langgroup
  if langgroup == None:
   continue
  langgroup.iline = None
  lnumg = int(langgroup.lnum)
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1 + iline + 1
   if lnum == lnumg:
    langgroup.iline = iline

def select_2(entries):
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   if '<ns>Prākṛt</ns>' in line:
    old = line
    new = old.replace('<ns>Prākṛt</ns>','<lang>Prākṛt</lang>')
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_3(entries):
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   new = line.replace('<s1 slp1="pAli">Pāli</s1>','<lang>Pāli</lang>')
   if new != line:
    old = line
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_4(entries):
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   new = line.replace('Persian <lang script="Arabic" n="Persian">',
                      '<lang>Persian</lang> <lang script="Arabic" n="Persian">')
   if new != line:
    old = line
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_5(entries):
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   new = line.replace('English',
                      '<lang>English</lang>')
   if new != line:
    old = line
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_6(entries):
 nfound = 0
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   new = line.replace('<ab>Eng.</ab> <etym>',
                      '<lang>Eng.</lang> <etym>')
   if new != line:
    old = line
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_7(entries):
 nfound = 0
 changes = [
  ('<ab>Lat.</ab>', '<lang>Lat.</lang>'),
  ('<ab>Gk.</ab>', '<lang>Gk.</lang>'),
  ('<ab>Old Germ.</ab>', '<lang>Old Germ.</lang>'),
  ('<ab>Mod.</ab> <ab>Germ.</ab>', '<lang>Mod. Germ.</lang>'),
  ('<ab>Lith.</ab>', '<lang>Lith.</lang>'),
  ('<ab>Lit.</ab>', '<lang>Lit.</lang>'),
  ('Irish anal', '<lang>Irish</lang> <etym>anal</etym>'),
  ('Irish <etym>Erin</etym>', '<lang>Irish</lang> <etym>Erin</etym>'),
  ('<ab>Goth.</ab>', '<lang>Goth.</lang>'),
  ('<s1 slp1="jEna">Jaina</s1> <lang>Prākṛt</lang>',
   '<lang>Jaina Prākṛit</lang>'),
  ('Arabic <lang script="Arabic"',
   '<lang>Arabic</lang> <lang script="Arabic"'),
  ('<ab>Cambro-Brit.</ab>', '<lang>Cambro-Brit.</lang>'),
  ('<ab>Angl.Sax.</ab>', '<lang>Angl.Sax.</lang>'),
  ('<ab>Russ.</ab>', '<lang>Russ.</lang>'),
  ('<ab>Zend</ab>', '<lang>Zend</lang>'),
  ('<ab>Zd.</ab>', '<lang>Zd.</lang>'),
  ('<ab>Germ.</ab>', '<lang>Germ.</lang>'),
  ('<ab>Old Slav.</ab>', '<lang>Old Slav.</lang>'),
  ('<ab>Slav.</ab>', '<lang>Slav.</lang>'),
  ('<ab>Hib.</ab>', '<lang>Hib.</lang>'),
  ('<ab>Armen.</ab>', '<lang>Armen.</lang>'),
  ('<ab>Old High Germ.</ab>', '<lang>Old High Germ.</lang>'),
  ('<ab>Mod. Eng.</ab>', '<lang>Mod. Eng.</lang>'),
  ('<ab>Gaël.</ab>', '<lang>Gaël.</lang>'),
  ('<ab>Old</ab> <ab>Pers.</ab>', '<lang>Old Pers.</lang>'),
  ('<ab>O.</ab> <ab>Pers.</ab>', '<lang>O. Pers.</lang>'),
  ('<ab>Pers.</ab>', '<lang>Pers.</lang>'),
  ('<ab>Old High Germ.</ab>', '<lang>Old High Germ.</lang>'),
  ('<ab>Old Pruss.</ab>', '<lang>Old Pruss.</lang>'),
  ('<ab>O. Pruss.</ab>', '<lang>O. Pruss.</lang>'),
  ('<ab>Engl.</ab>', '<lang>Engl.</lang>'),
  ('<ab>O. E.</ab>', '<lang>O. E.</lang>'),
  ('<ab>O. H. G.</ab>', '<lang>O. H. G.</lang>'),
  ('<ab>Sl.</ab>', '<lang>Sl.</lang>'),
  ('<ab>Sk.</ab>', '<lang>Sk.</lang>'),
  ('<ab>O. N.</ab>', '<lang>O. N.</lang>'),
  ('<ab></ab>', '<lang></lang>'),
  ('<ab></ab>', '<lang></lang>'),
  ('<ab></ab>', '<lang></lang>'),
  ]
 for entry in entries:
  entry.changes = []
  for iline,line in enumerate(entry.datalines):
   new = line
   for oldtxt,newtxt in changes:
    new = new.replace(oldtxt,newtxt)
   if new != line:
    old = line
    lnum = entry.linenum1 + iline + 1
    entry.changes.append((lnum,old,new))

def select_8(entries):
 nfound = 0
 for entry in entries:
  langgroup = entry.langgroup
  if langgroup == None:
   continue
  langgroup.iline = None
  lnumg = int(langgroup.lnum)
  for iline,line in enumerate(entry.datalines):
   lnum = entry.linenum1 + iline + 1
   if lnum == lnumg:
    langgroup.iline = iline

def make_new_1(oldline):
 # check same number of <etym>X</etym> in oldline as in newetyms
 newline = oldline.replace('<ab>Beng.</ab>','<lang>Beng.</lang>')
 newline = newline.replace('<ns>Bengāli</ns>', '<lang>Bengālī</lang>')
 newline = newline.replace('<ns>Bengālī</ns>', '<lang>Bengālī</lang>')
 return newline

def make_outarr_1(entry):
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = entry.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 langgroup = entry.langgroup
 iline = langgroup.iline
 if iline == None:
  outarr.append('; PROBLEM')
  print('problem 1 at %s' % meta)
  return outarr
  
 lnum = entry.linenum1 + iline + 1
 old = entry.datalines[iline]
 new = make_new_1(old)
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 if new == old:
  outarr.append('; PROBLEM')
  print('problem 2 at %s' % meta)
 outarr.append('%s new %s' %(lnum,new))
 return outarr

def make_outarr_8(entry):
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = entry.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 langgroup = entry.langgroup
 iline = langgroup.iline
 if iline == None:
  outarr.append('; PROBLEM')
  print('problem 1 at %s' % meta)
  return outarr
  
 lnum = entry.linenum1 + iline + 1
 
 old = entry.datalines[iline]
 new = old
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 outarr.append('; ms_AB: %s' %langgroup.lines[0])
 abline = langgroup.new
 outarr.append('; mw_AB: %s' % abline)
 outarr.append(';')
 outarr.append('%s new %s' %(lnum,new))
 return outarr


def make_outarr_2(entry):
 outarr = []
 outarr.append('; ------------------------------------------------------')
 meta = entry.metaline
 meta = re.sub(r'<k2>.*$','',meta)
 outarr.append('; %s' % meta)
 changes = entry.changes
 for change in changes:
  lnum,old,new = change
 outarr.append('%s old %s' %(lnum,old))
 outarr.append(';')
 if new == old:
  outarr.append('; PROBLEM')
  print('problem 2 at %s' % meta)
 outarr.append('%s new %s' %(lnum,new))
 return outarr

def make_outarr_3(entry):
 return make_outarr_2(entry)

def make_outarr_4(entry):
 return make_outarr_2(entry)

def write_recs(fileout,outrecs):
 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print('write_recs outputs %s records to %s' % (len(outrecs),fileout))
 
def write(option,fileout,entries):
 outrecs = []
 # title
 outarr = []
 outarr.append('; ***********************************************************')
 outarr.append('; %s' % fileout)
 outarr.append('; ***********************************************************')
 outrecs.append(outarr)
 #
 for entry in entries:
  if option == '1':
   langgroup = entry.langgroup
   if langgroup == None:
    continue
   outarr = make_outarr_1(entry)
  elif option == '8':
   langgroup = entry.langgroup
   if langgroup == None:
    continue
   outarr = make_outarr_8(entry)
  elif option == '2':
   if entry.changes == []:
    continue
   outarr = make_outarr_2(entry)
  elif option == '3':
   if entry.changes == []:
    continue
   outarr = make_outarr_3(entry)
  elif option == '5':
   if entry.changes == []:
    continue
   outarr = make_outarr_2(entry) # reuse
  elif option == '6':
   if entry.changes == []:
    continue
   outarr = make_outarr_2(entry) # reuse
  elif option == '7':
   if entry.changes == []:
    continue
   outarr = make_outarr_2(entry) # reuse
  else:
   print('write option error',option)
   exit(1)
  outrecs.append(outarr)
 write_recs(fileout,outrecs)
    
def entrygroups(langgroups,entries):
 ## initialize langgroup attribute for entries
 for entry in entries:
  entry.langgroup = None
 ## assume langgroups sorted by lnum
 nentries = len(entries)
 ientry0 = 0
 for langgroup in langgroups:
  lnum = int(langgroup.lnum)
  ientry = ientry0
  jentry = None
  while ientry < nentries:
   entry = entries[ientry]
   if entry.linenum1 <= lnum <= entry.linenum2:
    entry.langgroup = langgroup
    jentry = ientry
    break
   else:
    ientry = ientry + 1
  if jentry == None:
   print('entrygroups problem at lnum=',lnum)
  else:
   ientry0 = jentry

   
if __name__=="__main__":
 option = sys.argv[1]
 filein = sys.argv[2] # xxx.txt
 filein1 = sys.argv[3] # e.g., lang.string.changes.txt
 fileout = sys.argv[4] # prototype change transactions
 # read all the entries of the dictionary.
 entries = digentry.init(filein)
 # read the lang file
 langgroups_all = langgroup.init_langgroups(filein1)
 #
 if option == '1':
  # Bengali
  msg0 = '<lang>Beng'
  langgroups = [x for x in langgroups_all if msg0 in x.new]
  print(len(langgroups),"langgroup NEW instances of",msg0)
  entrygroups(langgroups,entries)
  select(entries)  # select
  write(option,fileout,entries)
 elif option == '2':
  langgroups = []
  select_2(entries)  # select
  write(option,fileout,entries)
 elif option == '3':
  langgroups = []
  select_3(entries)  # select
  write(option,fileout,entries)
 elif option == '4':
  langgroups = []
  select_4(entries)  # select
  write(option,fileout,entries)
 elif option == '5':
  langgroups = []
  select_5(entries)  # select
  write(option,fileout,entries)
 elif option == '6':
  langgroups = []
  select_6(entries)  # select
  write(option,fileout,entries)
 elif option == '7':
  langgroups = []
  select_7(entries)  # select
  write(option,fileout,entries)
 elif option == '8':
  langgroups = langgroups_all   # lang.string.changes.7
  print(len(langgroups),"langgroup Misc. Tag instances")
  entrygroups(langgroups,entries)
  select_8(entries)  # select
  write(option,fileout,entries)
 else:
  print('change_4a unknown option',option)

 
