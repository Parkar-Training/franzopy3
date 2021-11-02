
#----api.py code----
from django.views.decorators.http import require_http_methods
from requests import post
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

import json
from socialmedia import *
from .loginSerialization import *
from .serialization import *
from .user_serialization import *
from .OtpSerialization import *

import random,smtplib


#-----------------signup get post put delete-----------------

@csrf_exempt
def User(request,id=0):
    if request.method=='GET':
        userGet= users_new.objects.all()
        user_serializer= user_Serialization_Class(userGet,many=True)
        return JsonResponse(user_serializer.data,safe=False)

    elif request.method=='POST':
        user_post_data= JSONParser().parse(request)
        user_serializer= user_Serialization_Class(data=user_post_data)

        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("SignUp successfull!!!",safe= False)

        return JsonResponse("SignUp failed!!!",safe=False)

    elif request.method=='PUT':
        user_put_data= JSONParser().parse(request)
        print("user_pput: ",user_put_data)
        userPut= users_new.objects.get(userId=user_put_data['userId'])
        print("user put id data: ",userPut)
        print("type user put ",type(userPut))
        user_serializer= user_Serialization_Class(userPut,data=user_put_data)
        #print("put serial data: ",user_serializer.data)

        if user_serializer.is_valid():
            user_serializer.save()
            print("put serial data: ", user_serializer.data)
            return  JsonResponse("Password changed successfully!!!",safe=False)

        return JsonResponse(user_serializer.errors,safe=False)







#-----------------------signup end------------------------







#--------------------------------------------------------

'''

class UserList(APIView):
    print("class user list started")
    def get(self, request):
        model = users_new.objects.all()
        print("get start function")
        #serializer = serializerClass(model,many=True)
        serializer= serializerClass(model,many=True)

        #----login serializer----
       # ss=serializerLoginClass(model)
       # print("ss.data",ss.data)
        #------------------

        test1=(serializer.data)
        print(type(test1))
        print(type(serializer.data))

        #tuple_list = list(test1.items())
        #print(tuple_list[0])

        #an_iterator = itertools.islice(test1.items(), 0, 1)
        #key_value = next(an_iterator)

        #print(key_value)
        print("json slice: ")
        json_object = json.dumps(test1, indent=4)

        print(json_object)

        #return "done!!"
        print("\nend get function 1")
        #return Response("sample")
        return Response(serializer.data)

    print("\nend get function2")
    def post(self,request):
        # model = Users.objects.all()
        serializer = serializerClass(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ",serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            #return "SignUp successfull!!!"
            return Response("SignUp successfull!!!", status.HTTP_201_CREATED)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


print("Userlist class exited")

class UserDetail(APIView):
    def get_user(self, userId):
        try:
            model = users_new.objects.get(id=userId)
            print("model get user ", model)
            return model

        except users_new.DoesNotExist:
            print("get user id ", userId)
            return Response(f'User with employee id {userId} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)

    def get(self, request, userId):
        if not self.get_user(userId):
            return Response(f'User with emp id {userId} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = serializerClass(self.get_user(userId))
        return Response(serializer.data)

    def put(self, request, employee_id):
        serializer = serializerClass(self.get_user(employee_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

    def delete(self, request, userId):
        model = self.get_user(userId)
        model.delete()
        print("deleted ",userId)
        return Response(status=status.HTTP_204_NO_CONTENT)

'''


#-----api.py end

'''
        Name=input("Enter name: ")
        Mobile=input("Enter mobile number: ")
        Password= input("Enter password: ")
        Confirm_password= input("Enter password again: ")
        if (Password==Confirm_password):
            Emailid = input("Enter emailid: ")
            Acc_created = ""
            FList = ""
            private = input("Enter 0 to make public or 1 to make private: ")
        else:
            print("enter same password again to confirm")
            return post()
'''