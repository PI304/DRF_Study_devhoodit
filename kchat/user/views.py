from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class UserListCreateAPIView(APIView):
    def get(self, request):
        pass
    
    def post(self, request):
        pass
    
    def pust(self, request, pk):
        pass
    
    def delete(self, request, pk):
        pass
    
class UserDetailAPIView(APIView):
    pass