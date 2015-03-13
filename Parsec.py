#######################################################
#######################################################
#######################################################
# http://www.codeskulptor.org/#user39_EdPuMNXkjm_0.py #
#######################################################
#######################################################
#######################################################	

from math import *
#uzaklık gir milyon km cinsinden parsek hesaplayacak ıy cinsinden

b = input('AU cinsinden uzaklik giriniz:')

a = 1./3600.
#print a
pc = float(b)/tan(radians(a))
print tan(a)
print float(b)
print pc

ly = 3e5*365*24*60*60
print ly
au = 150e6
print au
iy = (pc*au)/ly


print 'Bulundugunuz gezegen icin 1 pc degeri:' 
print pc, 'Astronomi birimi'
print iy, 'Isik yili'


#a - açı saniyesi
#au - astronomi birimi
#ıy - ışık yılı bilmem kaç km
#sonuç - 
################################################
################################################
################################################
################################################
