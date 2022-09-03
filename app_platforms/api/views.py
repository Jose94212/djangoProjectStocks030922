from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from app_platforms.models import ModelPlatforms
from rest_framework import status
from rest_framework.decorators import api_view
from  app_platforms.api.serializers import PlatformSerializer


# @api_view(['GET'])
# def details(request,pk): 
#     try:
#         platforms = ModelPlatforms.objects.get(pk=pk)
    
#     except ModelPlatforms.DoesNotExist:
#         return Response('hey@@@@',status=status.HTTP_404_NOT_FOUND)
    
#     serializers=PlatformSerializer(platforms)
#     return Response(serializers.data)

# @api_view(['GET'])
# def list_platforms(request):

#     all_platforms = ModelPlatforms.objects.all()
#     serializers=PlatformSerializer(all_platforms)
#     return Response(serializers.data)

# @api_view(['POST'])
# def create_platform(request):
#     serializer = PlatformSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['PUT'])
# def update_platform(request, pk):
#     try:
#         platforms = ModelPlatforms.objects.get(pk=pk)
#     except ModelPlatforms.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         serializers = PlatformSerializer(platforms,data=request.data)
#         if serializers.is_valid():
#             data={}
#             serializers.save()
#             data["succcess"]= "updated successfully"
#             return Response(data=data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def delete_platform(request,pk):
#     try:
#         platforms = ModelPlatforms.objects.get(pk=pk)
#     except ModelPlatforms.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'DELETE':
#         operation = platforms.delete()
#         data={}
#         if operation:
#             data["success"]= "delete success"
#             return Response(data=data, status=status.HTTP_204_NO_CONTENT)
#         else:
#             data["failure"]= "delete failure"
#             return Response(data=data, status=status.HTTP_400_BAD_REQUEST)  


# @api_view(['PATCH'])
# def patch_platform(request):
#     pass

@api_view(['GET','POST'])
def list_post_platforms(request):
    if request.method == 'GET':
        all_platforms = ModelPlatforms.objects.all()
        serializer=PlatformSerializer(all_platforms,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def get_update_delete(request,pk):
    try:
        platform=ModelPlatforms.objects.get(pk=pk)
    except ModelPlatforms.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation=platform.delete()
        if operation:
            return Response("Platform: "+str(pk)+" deleted successfully",status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer= PlatformSerializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'GET':
        serializer= PlatformSerializer(platform)
        return Response(serializer.data,status=status.HTTP_200_OK)