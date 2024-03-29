# 贪婪算法

# 传入一个数组，他将被转换为集合。
# 集合类似于列表，只是同样的元素只能出现一次，即集合不包含重复的元素
states_needed = set(['mt','wa','or','id','nv','ut','ca','az'])    

stations = {}
stations['kone'] = set(['id','nv','ut'])
stations['ktwo'] = set(['wa','id','mt'])
stations['kthree'] = set(['or','nv','ca'])
stations['kfour'] = set(['nv','ut'])
stations['kfive'] = set(['ca','az'])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station  # & --->计算两个集合的交集   | --->并集    - --->差集
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
