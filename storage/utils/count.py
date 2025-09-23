import json
from ..models import Cartridge

cartridges_db = {}
dbfile = open("list.csv")
dbstr = dbfile.read()
dbfile.close()
temp_dict = dbstr.split("\n")
temp_dict.sort()
for s in temp_dict:
    tmp_str = s.split(";")
    c = Cartridge()
    c.number = tmp_str[0]
    c.article = tmp_str[1]
    c.caption = tmp_str[2]
    c.save()