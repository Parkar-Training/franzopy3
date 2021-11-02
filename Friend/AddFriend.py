from AllImports import *
from Friend.AddFriendSerialization import *
from Friend.models import *

class AddFriend(APIView):
    def get(self,request):
        print("inside get of caht ")
        serializer= AddFriendSerializerClass(friendModel.objects.all(), many=True)
        return Response(serializer.data)

    def post(self,request):
        print("inside post of new chat")
        getQstring= self.request.data
        print("get q sting data ",getQstring)
       # print("get q sting type ",type(getQstring),"\n to id ",getQstring['to_id'])

        #-------------check id is integer or not
        try:
            int(self.request.data['FriendId'])
            int(self.request.data['FuserId'])

            # -------check if users exists or not
            checkId = {}

            checkId['userId'] = self.request.data['FriendId']
            print("type search data1: ", type(checkId), "value 1 ", checkId)
            checkQstring = users_new.objects.all().filter(**checkId)
            print("check q string ", checkQstring)

            if checkQstring.exists():

                checkId['userId'] = self.request.data['FuserId']
                sender = list(checkQstring.values_list()[0])

                print("type search data 2: ", type(checkId), "value 2 ", checkId,"\nsender",sender)
                checkQstring = users_new.objects.all().filter(**checkId)
                print("2nd checkqstring", checkQstring)
                if checkQstring.exists():
                    receiver = list(checkQstring.values_list()[0])

                    #------check if they are friends or not---------
                    #checkId['FriendId'] = self.request.data['FuserId']
                    getQstring = self.request.data
                    print("getq String: ", getQstring)
                    print("type search data 3: ", type(getQstring), "value 3 ", getQstring)
                    checkQstring = friendModel.objects.all().filter(**getQstring)
                    print("check q string: ", checkQstring)
                    #tmp= request.data['FriendId']

                    #getQstring['FriendId'] = self.request.data['FuserId']
                    #getQstring['FuserId']= self.request.data[tmp]
                    #checkQstring2 = friendModel.objects.all().filter(**getQstring)
                    #print("check 2 string: ", checkQstring2)
                    if checkQstring.exists():# and checkQstring2.exists()):
                        return Response("Already friends or Pending Request!!!!!!", status=status.HTTP_404_NOT_FOUND)

                    serializer= AddFriendSerializerClass(data=self.request.data)

                    if serializer.is_valid():
                        serializer.save()
                        serializer.validated_data['sender name']=sender[1]
                        serializer.validated_data['sender userId']=sender[0]
                        serializer.validated_data['receiver userId']=receiver[1]
                        serializer.validated_data['receiver name']=receiver[0]
                        serializer.validated_data['status code']=status.HTTP_200_OK
                        serializer.validated_data['timestamp']=datetime.now()
                        return Response(serializer.validated_data,status=status.HTTP_200_OK)

                    return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

            return Response("FriendId doesnt exists", status=status.HTTP_404_NOT_FOUND)


        except ValueError:
            return Response("ID value is not integer",status=status.HTTP_400_BAD_REQUEST)

