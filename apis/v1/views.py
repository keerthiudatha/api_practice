import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from app1.models import books
from apis.v1.serializer import herosSerializer
@csrf_exempt
def all_books(request):
    if request.method == "GET":
        result=books.objects.all()
        SerializerResult=herosSerializer(result,many=True)
        if SerializerResult.is_valid:
            return JsonResponse(SerializerResult.data,safe=False)
        return HttpResponse("some error occured")
    else:
        return HttpResponse("invalid request type")
@csrf_exempt
def add_books(request):
    if request.method == "POST":
      incoming_data=JSONParser().parse(request)
      serializedata=herosSerializer(data=incoming_data)
      if serializedata.is_valid():
          serializedata.save()
          return JsonResponse(serializedata.data,status=201)
      return JsonResponse(serializedata.errors,status=400)
    return HttpResponse("invalid request method")

@csrf_exempt
def edit_books(request):
    if request.method == "PATCH":
      incoming_data=JSONParser().parse(request)
      pk=incoming_data.get("id")
      obj=books.objects.get(id=pk)
      serializedata=herosSerializer(obj,data=incoming_data,partial=True)
      if serializedata.is_valid():
          serializedata.save()
          return JsonResponse(serializedata.data,status=201)
      return JsonResponse(serializedata.errors,status=400)
    return HttpResponse("invalid request method") 


@csrf_exempt
def put_books(request):
    if request.method == "PUT":
      incoming_data=JSONParser().parse(request)
      pk=incoming_data.get("id")
      obj=books.objects.get(id=pk)
      serializedata=herosSerializer(obj,data=incoming_data)
      if serializedata.is_valid():
          serializedata.save()
          return JsonResponse(serializedata.data,status=201)
      return JsonResponse(serializedata.errors,status=400)
    return HttpResponse("invalid request method") 

@csrf_exempt
def delete_books(request):
    if request.method=="DELETE":
        incoming_data=JSONParser().parse(request)
        pk=incoming_data.get("id")
        obj=books.objects.get(id=pk)
        obj.delete()
        return HttpResponse("delete sucessfully")

def one_books(request,auth):
    if request.method == "GET":
        result=books.objects.get(id=auth)
        obj= herosSerializer(result) 
        if obj.is_valid:
            return JsonResponse(obj.data,status=201)
        else:
            return JsonResponse(obj.error,status=400)
    return HttpResponse("invalid request")         