#coding: utf-8
#1. Skriv funktionen value_exists2(value, d) som tar in ett dictionary och returnerar True om värdet value finns bland dictionaryts värden. Returnera False om det inte finns.
#Dictionaryts värden ska kunna vara siffror, strängar eller icke-nästlade listor. Funktionen ska även leta efter värdet value i eventuella listor. Om vi letar efter värdet 'hejsan' i dictionaryt
#{ "a": "bokstäver", "b": ['h', 'hejsan'] }
#så ska funktionen returnera True

import os
import os.path

PATH='./a.txt'

if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
    print "File exists and is readable"
else:
    print "Either file is missing or is not readable"