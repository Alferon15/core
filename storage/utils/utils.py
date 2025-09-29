def do_count(dbstr):
    res_list = {}
    dbstr.sort()
    for s in dbstr:
        if s !='':
            if res_list[s]:
                res_list[s].count += 1
            else:
                res_list[s].count = 1
    return res_list