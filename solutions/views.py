from django.shortcuts import render

from .models import Computer
from .serializers import ComputerSerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.

class ComputerView(APIView):
    def get(self, request):
        try:
            computers = Computer.objects.all()
            serializer = ComputerSerializer(computers, many=True)

            return Response({
                'data': serializer.data,
                'message': "Computers Data fetched Successfully"
            }, status= status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status= status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            data = request.data
            serializer = ComputerSerializer(data=data)  

            if not serializer.is_valid():
                return Response({
                'data': serializer.errors,
                'message': "Something went wrong"
            }, status= status.HTTP_400_BAD_REQUEST)
 
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "New computer is created"
            }, status= status.HTTP_201_CREATED)

        except:
            return Response({
                'date': {},
                'message': "Something went wrong in creation of Computer"
            }, status= status.HTTP_400_BAD_REQUEST)


    def patch(self, request):
        try:
            data = request.data
            computer1 = Computer.objects.filter(id=data.get('id'))

            if not computer1.exists():
              return Response({
                'data': {},
                'message': "Computer is not Found with this ID"
            }, status= status.HTTP_404_NOT_FOUND)

            serializer = ComputerSerializer(computer1[0], data= data, partial=True)

            if not serializer.is_valid():
                return Response({
                  'data': serializer.errors,
                  'message': "Something went wrong"
                }, status= status.HTTP_500_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Computer is Updated successfully"
             }, status= status.HTTP_200_OK)

        except:     
            return Response({
                'data': {},
                'message': "Something went wrong in creation of Computer"
            }, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data =request.data
            computer1 = Computer.objects.filter(id =data.get('id'))
            
            if not computer1.exists():
               return Response({
                'data': {},
                'message': "Computer is not Found with this ID"
            }, status= status.HTTP_404_NOT_FOUND)

            computer1[0].delete() 
            return Response({
                'data': {},
                'message': "Computer is Deleted"
             }, status= status.HTTP_200_OK)

        except:  
              return Response({
                'data': {},
                'message': "Something went wrong in deleting the Computer"
            }, status= status.HTTP_400_BAD_REQUEST)


      

             






            
