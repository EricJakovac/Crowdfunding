from django.contrib.auth.models import User
from django.db import models

# One to One - UserProfile je vezan uz točno jednog korisnika.
class UserProfile(models.Model):
    korisnik = models.OneToOneField(User, on_delete=models.CASCADE)
    opis = models.TextField()
    slika_profila = models.ImageField(upload_to='slike_profila/', blank=True)

    def __str__(self):
        return self.korisnik.username
    
# Many to One - Svaki projekt ima točno jednog autora, ali jedan autor može imati više projekata.
class Project(models.Model):
    naziv = models.CharField(max_length=255)
    opis = models.TextField()
    pocetak_kampanje = models.DateTimeField()
    zavrsetak_kampanje = models.DateTimeField()
    ciljani_iznos = models.DecimalField(max_digits=10, decimal_places=2)
    trenutni_iznos = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.naziv

# Many to One - Svaka donacija pripada jednom donatoru i jednom projektu.
class Donation(models.Model):
    iznos = models.DecimalField(max_digits=10, decimal_places=2)
    datum_donacije = models.DateTimeField(auto_now_add=True)
    donator = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.donator.username} - {self.iznos} kn"

# Many to Many - Više korisnika može podržavati više projekata.
class Support(models.Model):
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    projekt = models.ForeignKey(Project, on_delete=models.CASCADE)
    datum_podrske = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.korisnik.username} podržava {self.projekt.naziv}"
