from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rating = models.FloatField()
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Ticket(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Ticket for {self.movie_title.title} - {self.price}"

class Customer(models.Model):
    user_name = models.CharField(max_length=50)
    tickets = models.ManyToManyField(Ticket)

    def __str__(self):
        return self.user_name

class Places(models.Model):
    amount = models.IntegerField()
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} places owned by {self.owner}"