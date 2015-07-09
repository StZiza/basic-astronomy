#!/usr/bin/env python
# -*- coding: utf-8 -*-


from math import *

d=input("gun giriniz: ")
m=input("ay giriniz: ")
y=input("yil giriniz: ")

tg=(y-1)*365
print tg


tg=(y-1)/4+tg
print tg

#print tg 

if m == 1 :
 tg=tg+0
elif m==2:
 tg=tg+31
elif m==3:
 tg=tg+59
elif m==4:
 tg=tg+90
elif m==5:
 tg=tg+121
elif m==6:
 tg=tg+151
elif m==7:
 tg=tg+181
elif m==8:
 tg=tg+212
elif m==9:
 tg=tg+243
elif m==10:
 tg=tg+273
elif m==11:
 tg=tg+304
elif m==12:
 tg=tg+334
 
print tg
 

tg = tg + d
 
print tg

if m > 2 and y % 4 == 0:
    tg=tg+1
    
print tg

if tg%7==0:
    print "cuma"
elif tg%7==1:
    print "cumartesi"
elif tg%7==2:
    print "pazar"
elif tg%7==3:
    print "pazartesi"
elif tg%7==4:
    print "salı"
elif tg%7==5:
    print "çarşamba"     
elif tg%7==6:
    print "perşembe"  
