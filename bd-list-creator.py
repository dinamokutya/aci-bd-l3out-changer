import json

VRF = 'VRF-ANDRISKA-IAC'

f = open('fvBD.json')
f2 = open("bd-list.txt", "w")
data = json.load(f)
length = len(data)

#print (data[0]['fvBD']['children'][3]['fvRsCtx']['attributes']['tnFvCtxName'])

for i in range(length):
    print (data[i]['fvBD']['attributes']['name'] + "," + data[i]['fvBD']['children'][3]['fvRsCtx']['attributes']['tnFvCtxName'])
    
    if data[i]['fvBD']['children'][3]['fvRsCtx']['attributes']['tnFvCtxName'] == VRF :
        f2.write (data[i]['fvBD']['attributes']['name'] + "," + data[i]['fvBD']['children'][3]['fvRsCtx']['attributes']['tnFvCtxName'] )
        f2.write("\n")
f.close()
f2.close()