from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)

from .models import UserProfile, HomeDetails, HomeRentDetails
from .serializer import (
    ProfileSerializer, HomeDetailSerializer,
    HomeRentSerializer
)

def index(request):
    return HttpResponse("<h1>Welcome to home rental site</h1>")

class CreateUserProfileView(APIView):
    """ for create user profile of home owner and renter
    """
    def post(self, request, format=None):
        try:
            user_obj = User.objects.create_user(
                first_name=request.data.get('first_name', ''),
                last_name=request.data.get('last_name', ''),
                username=request.data['username'],
                password=request.data['password'],
                email=request.data.get('email', '')
            )
        except Exception as e:
            result = {'status': '0', 'error': str(e)}
            return Response(result)
        if user_obj:
            # it contains user type home owner or renter
            user_type = request.data.get('type')
            g, created = Group.objects.get_or_create(
                name=user_type)
            user_obj.groups.add(g)
        prof_obj = UserProfile.objects.create(
            user=user_obj,
            phone=request.data.get('phone',''),
            address=request.data.get('address','')
        )
        result = {'status': '1', 'msg': 'Created Succesfully'}
        return Response(result)


class UserProfileView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProfileSerializer
    queryset = UserProfile.objects.all()


class HomeViewSerializerView(CreateAPIView):
    serializer_class = HomeDetailSerializer
    queryset = HomeDetails.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class HomeReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = HomeDetailSerializer
    queryset = HomeDetails.objects.all()


class CreateHomeRentAPIView(APIView):
    def post(self, request, format=None):
        try:
            data = request.data
            import pdb ; pdb.set_trace()
            home_id = data.get('home_id')
            home_obj = HomeDetails.objects.get(pk=home_id)
            renter_id = data.get('renter_id')
            print('...', renter_id)
            renter_obj = UserProfile.objects.get(pk=renter_id)
            rental_obj = HomeRentDetails.objects.create(
                home=home_obj,
                renter=renter_obj,
                start_date=data.get('start'),
                end_date=data.get('end'),
                description=data.get('desc')
            )
            return Response({'status': '1', 'msg': 'created successfully'})
        except Exception as e:
            return Response({'status': '0', 'error': str(e)})


class HomeRentReadUpdateDelete(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = HomeRentSerializer
    queryset = HomeRentDetails.objects.all()
