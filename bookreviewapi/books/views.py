from django.contrib.auth.models import User

from rest_framework import generics, permissions

from rest_framework.response import Response

from rest_framework.views import APIView

from .models import Book, Review

from .serializers import RegisterSerializer, BookSerializer, ReviewSerializer

from .permissions import IsOwnerOrReadOnly

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

class ChangePasswordView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):

        user = request.user

        old_password = request.data.get("old_password")

        new_password = request.data.get("new_password")

        if not user.check_password(old_password):

            return Response({"error": "Wrong password"})

        user.set_password(new_password)

        user.save()

        return Response({"message": "Password changed"})

class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    def get_permissions(self):

        if self.request.method == 'POST':

            return [permissions.IsAdminUser()]

        return [permissions.AllowAny()]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()

    serializer_class = BookSerializer

    def get_permissions(self):

        if self.request.method in ['PUT', 'DELETE']:

            return [permissions.IsAdminUser()]

        return [permissions.AllowAny()]

class ReviewListCreateView(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer

    def get_queryset(self):

        book_id = self.kwargs['book_id']

        return Review.objects.filter(book_id=book_id)

    def perform_create(self, serializer):

        serializer.save(

            user=self.request.user,

            book_id=self.kwargs['book_id']

        )

    permission_classes = [permissions.IsAuthenticated]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    permission_classes = [IsOwnerOrReadOnly]