from AllImports import *
from chat.NewChatSerialization import NewChatSerializerClass
from chat.models import *

class NewChat(APIView):
    def get(self,request):
        print("inside get of caht ")
        serializer= NewChatSerializerClass(ChatModel.objects.all(), many=True)
        return Response(serializer.data)

    def post(self,request):
        print("inside post of new chat")
        getQstring= self.request.data
        print("get q sting data ",getQstring)
       # print("get q sting type ",type(getQstring),"\n to id ",getQstring['to_id'])

        #-------------check id is integer or not
        try:
            int(self.request.data['to_id'])
            int(self.request.data['from_id'])

            # -------ceck sender id if present
            checkUserId = {}

            checkUserId['userId'] = self.request.data['to_id']
            print("type search data: ", type(checkUserId), "value ", checkUserId)
            checkQstring = users_new.objects.all().filter(**checkUserId)  # 'userId'=='2'
            print("check q string ", checkQstring)

            if checkQstring.exists():

                #print("sample:----->>>s ", sample)
                checkUserId['userId'] = self.request.data['from_id']
                print("type search data: ", type(checkUserId), "value ", checkUserId)
                checkQstring = users_new.objects.all().filter(**checkUserId)  # 'userId'=='2'

                if checkQstring.exists():
                    sample = list(checkQstring.values_list()[0])
                    serializer = NewChatSerializerClass(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        #serializer.validated_data['msg'] = "Conversation Started"
                        serializer.validated_data['status'] = status.HTTP_200_OK
                        serializer.validated_data['timestamp'] = datetime.now()
                        serializer.validated_data['sender name'] = sample[1]

                    return Response(serializer.validated_data, status=status.HTTP_200_OK)
                return Response("sender doesnt exists", status=status.HTTP_404_NOT_FOUND)

            return Response("receiver doesnt exists", status=status.HTTP_404_NOT_FOUND)


        except ValueError:
            return Response("ID value is not integer",status=status.HTTP_400_BAD_REQUEST)




        #serializer= NewChatSerializerClass(data= request.data)
