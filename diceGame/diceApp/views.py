from django.shortcuts import render

import random
import socket
import string
import hashlib

# Create your views here.

from django.http import HttpResponse

from diceApp.models import Client , Server


def home(request):
    # client_dice = random.randrange(1, 7)
    # chars = string.ascii_uppercase + string.ascii_lowercase + string.digits  # rB client calculation
    # rB = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    return render(request, 'home.html')



def test(request):
    if request.method == 'POST':
        #Client.client_rB = request.POST.get('client_rB_hash', '')
        temp_rB = request.POST.get('client_rB_hash', '')
        #print(temp_rB + " client's rB")
        
        #save rB in client's model
        Client.client_rB = temp_rB
        #print("client rb in test = "+Client.client_rB.__str__())

        #rA upologismos
        chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        r_server = ''.join(random.choice(chars) for _ in range(10))

        serverDice = random.randrange(1,7)
        #print("server dice is =  "+str(serverDice))

        #save rA in server's model
        Server.server_rA = r_server
        #print("server rA in test function = "+ Server.server_rA.__str__())

        #save server dice in server's model
        Server.server_dice = serverDice
        #print("server dice in test = "+Server.server_dice.__str__())

        #sha256 (dice number,rA,rB) ypologismos
        string_for_hash = str(serverDice)+r_server + temp_rB
        Server.server_string = string_for_hash
        #print("server string= "+ Server.server_string.__str__())
        h_commit =hashlib.sha256(string_for_hash.encode('utf-8')).hexdigest()
        #print(h_commit)
       
        #stelno h_commit ston client
        return render(request,'home.html',{'h_commit':h_commit})
    
    return render(request,'home.html')

def receive(request):
    if request.method == 'POST':
        #get the client dice from client
        client_dice = request.POST.get('dice2','')
        #print("the client's dice is = "+str(client_dice))

        #xrisi toy model class gia get server_rA,server_dice kai client_rB
        rA = Server.server_rA.__str__()
        rB = Client.client_rB.__str__()
        s_dice = Server.server_dice.__str__()
        #print ("rA = "+ rA + " rB= "+rB + " server_dice= "+ s_dice)
        
        #winner is
        if (client_dice > s_dice):
            result = "YOU are the winner"
        elif (client_dice < s_dice):
            result = "SERVER is the winner"
        else:
            result = "Tie, same dice number"
        server_string = Server.server_string
        #print(server_string+" = server string in receive")

        #send to client server_dice,rA,rB to compute sha256 and check if cheated
        return render(request,'home.html',{'result':result,'rA':rA,
                                           'rB':rB,'s_dice':s_dice})
    
    return render(request,'home.html')

