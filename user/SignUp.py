from AllImports import *


class SignUp(APIView):

    print("class user list started")

    def get(self, request):
        model = users_new.objects.all()
        print("get start function")

        serializer  = serializerClass(model,many=True)
        return Response(serializer.data)

    def post(self,request):
        # -----email setup and login---------------------
        number = random.randint(1111, 9999)  # otp generration
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.ehlo()
        s.starttls()
        s.login('franzosocialmedia@gmail.com', 'apurva87654321')
        print(s.login('franzosocialmedia@gmail.com', 'apurva87654321'))

        print("otp generate: ", number)

        serializer = PasswdserializerClass(data=request.data)

        password=request.data['password']
        request.data['otp'] = number
        hash_password = hashlib.md5(password.encode()).hexdigest()
        print(hash_password)
        print(request.data)
        #request.data['password'] = hash_password
        print(type(request.data))

        #requestDataDict = request.data.dict()
        print("req data type dict: ", request.data['password'])
        request.data['password'] = hash_password
        #request.data['msg'] = "signup  Done!!"

        #print(requestDataDict)
        requestDataQueryDict = QueryDict('', mutable=True)
        requestDataQueryDict.update(request.data)
        #requestDataQueryDict.update(requestDataDict)
        print(requestDataQueryDict)
        print(type(requestDataQueryDict))

        serializer = PasswdserializerClass(data=requestDataQueryDict)
        print("type of sign up serializer: ", type(serializer))

        if serializer.is_valid():
            print("valid----", serializer.validated_data)
            serializer.save()
            s.sendmail('franzosocialmedia@gmail.com', request.data['emailid'], str(number))
            print("valid and save")
            serializer.validated_data['msg']='sign up success!!!'
            print("---->>", serializer.validated_data['emailid'])
            serializer.validated_data['timestamp']=datetime.now()
            serializer.validated_data['status']= status.HTTP_201_CREATED
            serializer.validated_data['otp']= request.data['otp']
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)