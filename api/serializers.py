from rest_framework import serializers
from .models import Books,Users,MyAccountManager
from rest_framework.authtoken.views import Token
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id','book','Description','Created_on']


