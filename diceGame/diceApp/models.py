from django.db import models

# Create your models here.
class Client(models.Model):

    client_rB = models.IntegerField(default=0)
    client_dice = models.IntegerField(default=0)
    
    def __str__(self) :
        return self.client_rB
    
    def __str__(self) :
        return self.client_dice
    
class Server(models.Model):

    server_rA = models.IntegerField(default=0)
    server_winner = models.IntegerField(default=0)
    server_dice = models.IntegerField(default=0)
    server_string = models.IntegerField(default=0)  

    def __str__(self) :
        return self.server_rA
    
    def __str__(self) :
        return self.server_dice 
    
    def __str__(self) :
        return self.server_winner
    

    def __str__(self) :
        return self.server_string
    
 