def do_count(dbstr):
    res_list = {}
    temp_dict = dbstr.split("\n")
    temp_dict.sort()
    for s in temp_dict:
        if s !='':
            if res_list.get(s):
                res_list[s] += 1
            else:
                res_list[s] = 1
    return res_list