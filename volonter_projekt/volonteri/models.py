from django.db import models

# Create your models here.

class Kategorija(models.Model):
    naziv = models.CharField(max_length=100)

    def __str__(self): 
        return self.naziv

class Aktivnost(models.Model):
    naziv_aktivnosti = models.CharField(max_length=200)
    opis = models.TextField()
    datum = models.DateField()
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)

    def __str__(self): 
        return self.naziv_aktivnosti
    
class Prijava(models.Model):
    ime = models.CharField(max_length=100) 
    prezime = models.CharField(max_length=100) 
    aktivnost = models.ForeignKey(Aktivnost, on_delete=models.CASCADE) 
    datum_prijave = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.ime + " " + self.prezime 
