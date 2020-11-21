
print 'Start Script'


Script.ChangeMode("Acro")
Script.Sleep(50)

Script.ChangeMode("Acro")

for chan in range(1,9):
    print 'Arming Channel', chan
    Script.SendRC(chan,1500,False)
    Script.SendRC(3,Script.GetParam('RC3_MIN'),True)

Script.ChangeMode("Acro")


while cs.lat == 0:
    print 'Waiting for GPS'
    Script.Sleep(1000)

print 'Got GPS'
jo = 10 * 13
print jo
Script.SendRC(3,1000,False)
Script.SendRC(4,2000,True)
cs.messages.Clear()
Script.WaitFor('ARMING MOTORS',30000)
Script.SendRC(4,1500,True)
print 'Motors Armed!'
Script.SendRC(3,1700,True)

while cs.alt < 10:
    print "Waiting for Alt to Reach 50"
    Script.Sleep(50)

print 'ACRO'
Script.SendRC(5,2000,True) # acro
#print 'ROLL'
#Script.SendRC(1,2000,False) # roll
print 'Throttle'
Script.SendRC(3,1370,True) # throttle

#while cs.roll > -45: # top half 0 - 180
#    Script.Sleep(5)

#while cs.roll < -45: # -180 - -45
#    Script.Sleep(5)

print 'Stabilize'
Script.SendRC(5,1500,False) # stabilize
print 'Level Roll'
Script.SendRC(1,1500,True) # level roll
print 'Sleep 2 seconds'
Script.Sleep(2000) # 2 sec to stabilize
print 'Throttlee back to land'
Script.SendRC(3,1300,True) # throttle back to land
thro = 1350 # will descend

while cs.alt > 0.1:
    Script.Sleep(300)

Script.SendRC(3,1000,False)
Script.SendRC(4,1000,True)
Script.WaitFor('DISARMING MOTORS',30000)
Script.SendRC(4,1500,True)

print 'Roll complete'
