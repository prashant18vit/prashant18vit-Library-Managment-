# prashant18vit-Library-Managment-
# Library Management Project


## Apps Used
### api/models.py

`The model have two class for two Databsae table`
#### 1 class Books
This class is used to store the `Books` it has the following fields book description and created on(which is added automatically)
```python

class Books(models.Model):
    book = models.CharField(max_length=255)
    Description = models.TextField(null=True,blank=True)
    Created_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.book}"
```


#### 2 class Users

>I have created custom user model documentation can be found here https://docs.djangoproject.com/en/4.1/topics/auth/customizing/

1) I have all the fields that i think the user should have 
2) Then i have assigned the USERNAME_FIELD to the email field 
```python
USERNAME_FIELD = 'email'
```
This changes the default field that is username to email

 
#### Code

```python
class Users(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30,unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField (verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models. BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects= MyAccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm,obj = None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
```

#### 2 class MyAccountManager
We have to specify the create method for the users model as we have changed the fields
In here we specify the create method for the model


## api/forms.py

##  RegesForm
it inherits from the ModelForm 

## oginForm
* inherits from django's AuthenticationForm 
* sets username as EmailField 


## api/Views.py

### function books_list
    This function has all the required method for GET and POST
    
## books_details
    This function has the implementation for PUT and Delete

## Index
    used to render the main.html
    
## Login 
    implemented the login Functionality
## Registration 
    implemented the registration login
    
## api/serilizers.py
### Serializer
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON
I have used ModelSerializer which provides a useful shortcut for creating serializers that deal with model instances and querysets

### class BookSerializer
The book serializer is used to serialize the Book model data
 
