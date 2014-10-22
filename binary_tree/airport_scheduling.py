#!/usr/bin/env python
# encoding: utf-8

#Problem: airport_scheduling
#1.Airport with single (very busy) runway
#2.“Reservations” for future landings
#3.When plane lands, it is removed from set of pending events
#4.Reserve req specify “requested landing time” t
#5.Add t to the set of no other landings are scheduled within < 3 minutes either way.
#– else error, don’t schedule

#denote the reserved langing times like : R =(41,46,49,56)
#Request for time:44 not allowed (46 in R)
#                 53 OK
#                 20 not allowed (already past)
#                 |R| = n
#Goal: run this system effciently in O(lgn)

#本算法未包含请求时间在now和R[0]之间的,R[len(R)-1]之后的这两种情况
#为考虑R为空的情况
def scheduler(R, now, request_time) :
    if request_time < now :
        return "error"
    for i in xrange(len(R)-1) :
        if abs(request_time-R[i]) >= 3 and \
            abs(request_time-R[i+1]) >=3 :
            break
    else :
        return "error"
    R.append(request_time)
    R.sort()

    land_time = R[0]
    if land_time == now :
        R = R[1:]
    return "success"

R=[]
now = 1
request_time = 10

print scheduler(R,now,request_time)
print R





