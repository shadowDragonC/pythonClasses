V = int(input())    #obem na baseina
P1 = int(input())   #debit na purva truba
P2 = int(input())   #debit na vtora truba
H = float(input())  #chasove

pipe1 = P1 * H
pipe2 = P2 * H

waterTotal = pipe1 + pipe2

if waterTotal > V:
    print('For %.1f hours the pool overflows with %d liters'%(H, waterTotal - V))
else:
    percent = (waterTotal/V)*100
    prP1 = (pipe1/waterTotal)*100
    prP2 =  100 - prP1
    print('The pool is %d %. Pipe 1: %d %. Pipe 2: %d %'%(percent, prP1, prP2))