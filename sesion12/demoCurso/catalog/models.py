import uuid
from django.db import models
from django.urls import reverse

# Create your models here.

#asocian código de una clase con una base de datos
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del género")

    def __str__(self):
        return self.name #representacion informal del objeto
    
class Book(models.Model):
    title = models.CharField(max_length=32, help_text="Pon el título del libro")
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, blank=True)
    sumary = models.TextField(max_length=100, help_text="Pon el sumario del libro")
    isbn = models.CharField(max_length=13, help_text="Pon el ISBN del libro")
    genre = models.ManyToManyField(Genre, help_text="Pon los géneros del libro")

    def __str__(self):
        return self.title #representacion informal del objeto
    
    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)]) #url de la vista

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro", editable=False)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, blank=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    #django lo va a representar en forma de lista
    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')
    
    class Meta:
        ordering = ['due_back']
    
    def __str__(self):
        return '%s (%s)' % (self.id, self.book.title) #representacion inform
        #return f'{self.id} - {self.book.title}' #representacion informal del objeto

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)]) #url de la vista

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name) #representacion informal del
        #return f'{self.last_name}, {self.first_name}' #representacion informal del objeto
    

    