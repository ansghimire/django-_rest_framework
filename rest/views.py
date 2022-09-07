

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from .serializers import PersonDetailSerializer, funcSerializer, TestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Person, PersonDetail
from .serializers import PersonSerializer


def add(a, b):
    return a + b

# @api_view(['GET','POST'])
@api_view(http_method_names=('GET','POST'))
def func(request):
    if(request.method == "GET"):

        serializer = funcSerializer(instance=request.query_params)
        return Response({"message":request.query_params, "output":serializer.data})

    if(request.method == "POST"):
        data = request.data 
        serializer = TestSerializer(data=data)

        if serializer.is_valid():
            return Response(serializer.data, status=201)


        return Response({"message":serializer.errors})




class PersonView(APIView):

    def get(self,*args, **kwargs):
        qs = Person.objects.all()

        # output = []
        # for data in qs :
        #     print(data)
        #     output.append({"name": data.name, "age": data.age})
        # return Response(output, status=200)

        ser = PersonSerializer(qs, many=True)
        data = ser.data 
        # for i in data:
        #     print(i)
        #     i['message'] = f'Hello my age is { i["age"] }'        
        return Response(data, status=200)
        

    def post(self, *args, **kwargs):
        data = self.request.data
        ser = PersonSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(data, status=201)



class PersonDetailView(APIView):
    def get(self, *args, **kwargs):
       qs = PersonDetail.objects.all()
       ser = PersonDetailSerializer(instance=qs, many=True, context={"request": self.request})
       return Response(ser.data, status=200)


    def post(self, *args, **kwargs):
        data = self.request.data
        ser = PersonDetailSerializer(data=data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)

         










# @csrf_exempt
# def func(request):
#     if request.method.lower() == "get":
#         print(request.GET)

#         return JsonResponse({"message":"ok"})

    
#     if request.method.lower() == "post":   

#         data = json.loads(request.body)
      
#         serializer = funcSerializer(data=data)
#         if serializer.is_valid():
#         #     print(serializer.data)
#             num1 = serializer.validated_data['num1']
#             num2 = serializer.validated_data['num2']
#             output = num1 + num2 
#             return JsonResponse({"message":output, "providedValue":serializer.data})
    
#     return JsonResponse({"message":serializer.errors}, status = 400)





