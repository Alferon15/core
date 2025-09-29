def do_count(dbstr):
    res_list = {}
    dbstr.sort()
    for s in dbstr:
        if s != '':
            if res_list.get(s):
                res_list[s]['count'] += 1
            else:
                o = {'number':s, 'count':1}
                res_list[s] = o
    return res_list