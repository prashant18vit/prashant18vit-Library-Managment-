from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import  AuthenticationForm
from multiprocessing import context
from .models import Books,Users
from django.shortcuts import render,redirect
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import LoginForm,RegesForm
from rest_framework import status


# To list all the data and add the book and add book
@api_view(['GET','POST'])
def books_list(request):
    if request.method == "GET": # if the request is GET
        books = Books.objects.all() # for database Retrieving 
        serializer = BooksSerializer(books,many = True) # we call the serializer class here
        return Response(serializer.data)    # and retrn the serialized data as response

    elif request.method == "POST": # if the request is POST
        serializer = BooksSerializer(data = request.data) # get all the data from the request and pass it to the serializer call we have create the crete method in the serializer class
        if serializer.is_valid(): # it will validate the data if it is valid
            serializer.save()   # then it will save
            return Response(serializer.data, status = status.HTTP_201_CREATED) # and return the response
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) # if not then it returns a error


@api_view(['GET','POST','DELETE'])
def books_details(request,pk):  # for getting the indiviual book , updating and delting
    try:                                    #first we have the try block 
        books = Books.objects.get(pk = pk)  # if the table exist then it will retrive the data

    except Books.DoesNotExist:              # if it does not exist then 
        return Response(status = status.HTTP_404_NOT_FOUND) # it will return the response of 404 not found

    if request.method == "GET":             # if the request is get 
        serializer = BooksSerializer(books) # then the data that we have retrived will be passed to the serializer
        return Response(serializer.data)    # and it will return the response of the serialized data

    elif request.method == "POST":           # if the request is POST
        serializer = BooksSerializer( books, data = request.data) # then the data will be fetched and stored in the data variable
        if serializer.is_valid():           # serializer will check if the data is valid or not
            serializer.save()               # if it is valid then it will save the data
            return Response(serializer.data)# and return a response
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) #else it will respond with 400 Bad request

    elif request.method == "DELETE": # if the request is DELETE
        books.delete()               # the delete function will be called 
        return Response(status = status.HTTP_204_NO_CONTENT) # and because the data is deleted it will return with 204 No content

def Index(request):
    return render(request,'main.html')

def login1(request):
    form = AuthenticationForm()
    if request.POST:
        form = AuthenticationForm(data = request.POST)
        print("YES",request.POST)
        if form.is_valid():
            print("YES")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username,password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('booklist')
            else:
                context = {
                    "form":form
                    }
            
    context = {
        "form":form
    }
    return render(request, 'login.html',context=context)

def Registration(request):
    form = RegesForm()
    if request.POST:
        form = RegesForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(
                form.cleaned_data["password"]
            )
            user.save
            form.save()
            return redirect('login')

    context = {
        "form":form
    }
    return render(request, 'Regis.html',context=context)