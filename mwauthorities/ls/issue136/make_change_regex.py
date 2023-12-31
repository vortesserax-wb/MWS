#-*- coding:utf-8 -*-
"""make_change_regex.py 
"""
import sys,re,codecs
## https:##stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
## This required by git bash to avoid error
## UnicodeEncodeError: 'charmap' codec cannot encode characters 
## when run in a git bash script.

sys.stdout.reconfigure(encoding='utf-8') 

class Case(object):
 def __init__(self,metaline,iline,line,match,newline):
  self.metaline = metaline
  self.iline = iline
  self.line = line
  self.match = match  
  self.newline = newline
  
def init_cases(lines,regex1,regex2):
 cases = []
 metaline = None
 imetaline1 = None
 page = None
 prevls = None
 for iline,line in enumerate(lines):
  if iline == 0: 
   continue  # 
  line = line.rstrip('\r\n')
  if line == '':
   continue
  elif line.startswith('<L>'):
   metaline = line
   imetaline1 = iline+1
   #continue
  elif line == '<LEND>':
   metaline = None
   imetaline = None
   prevls = None
   continue
  elif line.startswith('[Page'):
   page = line
   #continue
  m = re.search(regex1,line)
  if m == None:
   continue
  match = m.group(0)
  newline = re.sub(regex1,regex2,line)
  if newline != line:
   # generate a case
   cases.append(Case(metaline,iline,line,match,newline))

 print(len(cases),'changes of %s'%regex1)
 return cases

def write_cases_regex(fileout,cases,regex1,regex2):
 n = 0
 nchg = 0
 prevline = None
 previline = None
 outrecs = []
 # section title
 outarr = []
 outarr.append('; ======================================================')
 outarr.append('; %s (%s)' %(fileout,len(cases)))
 outarr.append('; regex1 = /%s/,  regex2 = /%s/' %(regex1,regex2))
 outarr.append('; ======================================================')
 outrecs.append(outarr)
 for case in cases:
  outarr = []
  n = n + 1
  outarr.append(r'; -------------------------------------------------------')
  metaline = re.sub(r'<k2>.*$','',case.metaline)
  outarr.append('; %s' % metaline)
  outarr.append('; %s ' % case.match)
  iline = case.iline
  lnum = iline + 1
  line = case.line
  if previline == iline:
   # in case we change same line more than once
   line = prevline
  outarr.append('%s old %s' %(lnum,line))
  nchg = nchg + 1
  newline = case.newline
  outarr.append(';')
  outarr.append('%s new %s' %(lnum,newline))
  outrecs.append(outarr)
  previline = iline
  prevline = newline

 with codecs.open(fileout,"w","utf-8") as f:
  for outarr in outrecs:
   for out in outarr:
    f.write(out+'\n')
 print(len(cases),'cases written to',fileout)

interpret_option = {
  '1': (r', </ls>', r'</ls>, '),
  '1a': (r' </ls> ', r'</ls> '),
  '1b': (r' </ls><info', r'</ls><info'),
  '1c': (r' </ls>', r'</ls> '),
  '1d': (r',</ls>', r'</ls>,'),
  '1e': (r'</ls>; <ls>Kāś.',r'</ls>, <ls>Kāś.'),
  '2': (r'<ls>([^ <]+) ([xivcl]+), ([xivcl]+\.?)</ls>',
        r'<ls>\1 \2</ls>, <ls n="\1">\3</ls>'),
  '2a': (r'<ls>([^ <]+) ([xivcl]+), ([xivcl]+), ([xivcl]+\.?)</ls>',
        r'<ls>\1 \2</ls>, <ls n="\1">\3</ls>, <ls n="\1">\4</ls>'),
  '2b': (r'<ls>([^ <]+) ([xivcl]+), ([xivcl])',
        r'<ls>\1 \2</ls>, <ls n="\1">\3'),
  '2cnotused': (r'<ls>(IW\.|RTL\.|MWB\.) ([0-9]+), ([0-9]+)',
         r'<ls>\1 \2</ls>, <ls n="\1">\3'),
  '2c': (r'and ([ivxcl]+)\b',
         r'and <ls n="">\1'),
  '2d': (r'([^.]) x',
         r'\1 <ls n="">x'),
  '3a': (r' ([ivxcl]+)[.] ([0-9])',
         r'** \1, \2'),
  '3b': (r'(<ls[^<]+) &',
         r'\1</ls> & <ls n="">'),
  '3c': (r'(<ls[^<]*[0-9])[.] ([0-9])',
         r'**\1, \2'),
  '4a': (r'(<ls[^<]*)<s1',
         r'**\1<s1'),
  '4b': (r'([0-9]) ([0-9])',
         r'\1**\2'),
  '4c': (r'( *- *</ls>)',
         r'</ls>**'),
  '5': (r'(<ls[^<]* [^<]*[cixlv][.]? [0-9])',
        r'**\1'),
  '5a': (r'(<ls[^<]*\b[xivlc]+, [xivlc])',
        r'**\1'),
  '6': (r'(-[0-9].)(<info)',
        r'\1**\2'),
  '7a': (r'  ',' '),
  '7b': (r' ,', r',**'),
  '7c': (r' \.', r'.**'),
  '7d': (r' ;', r';**'),
  '7e': (r' \)', r')**'),
  '7f': (r' >', r' **'),
  '7g': (r'<ls n="Unknown">',
         r'<ls n="">')
 }
if __name__=="__main__":
 # Problem with input of regexes into command line
 # python make_change_regex.py ', </ls>' '</ls>, ' temp_mw_3.txt temp.txt
 # The 2nd paramenter '</ls>, ' is not intepreted properly
 # It prints as "<C:/Program Files/Git/ls>, "
 # Thus, use an option number
 option = sys.argv[1]
 regex1,regex2 = interpret_option[option]

 filein = sys.argv[2] #  xxx.txt (path to digitization of xxx)
 fileout = sys.argv[3] # possible change transactions
 
 with codecs.open(filein,"r","utf-8") as f:
  lines = [x.rstrip('\r\n') for x in f]
 cases = init_cases(lines,regex1,regex2) 
 print(len(cases),'cases')
 write_cases_regex(fileout,cases,regex1,regex2)
  
