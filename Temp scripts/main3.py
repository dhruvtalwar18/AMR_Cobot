#!/usr/bin/env python
from math import sqrt
import operator
goaldic_flange = {0 : [200, 0.0, 0.0], 1 : [6, 0.0, 0.0],
 2 : [45, 0.0, 0.0]}
goaldic_flange_temp = goaldic_flange.copy()
#print goaldic_flange.values()
for i in range(len(goaldic_flange)):
 #print goaldic_flange[i]
 #temp = sqrt((goaldic_flange[i][0] -odom_val.pose.pose.position.x]) ** 2 + (goaldic_flange[i][1] - odom_val.pose.pose.position.y]) ** 2)
 temp = sqrt((goaldic_flange[i][0] -25) ** 2 + (goaldic_flange[i][1] - 0) ** 2)
 #print i,temp
 goaldic_flange_temp[i] = int(temp)


 sorted_dict = (sorted(goaldic_flange_temp.items(),key=lambda item: item[1],reverse=False))

 print sorted_dict