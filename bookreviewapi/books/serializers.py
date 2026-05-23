from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Book, Review

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['username', 'email', 'password']

        extra_kwargs = {

            'password': {'write_only': True}

        }

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data['username'],

            email=validated_data['email'],

            password=validated_data['password']

        )

        return user

class BookSerializer(serializers.ModelSerializer):

    class Meta:

        model = Book

        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:

        model = Review

        fields = '__all__'