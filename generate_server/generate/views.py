from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.decorators import api_view, APIView, permission_classes
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Original
from .serializers import OriginalSerializer,ResultSerializer
from .permissions import CreaterOrReadOnly
from accounts.serializers import CurrentUserPicSerializer

# 获取当前用户信息
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_user_for_current(request: Request):
    user = request.user

    serializer = CurrentUserPicSerializer(instance=user,
                                            context={"request": request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)

# 查看全部历史记录、上传并处理单个原图
class OriginListCreateView(APIView):

    serializer_class = OriginalSerializer
    permission_classes = [CreaterOrReadOnly]


    def get(self,request,*args,**kwargs):
        original_pic = Original.objects.all()
        serializer = self.serializer_class(instance=original_pic,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data = request.data
        data['created_by'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
              
            response = {
              "message":"图片已成功上传！",
              "data":serializer.data,
            }

            return Response(data=response,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_201_CREATED)


# 查看、更新、删除单个上传记录
class OriginalRetrieveUpdateDeleteView(APIView):
    serializer_class = OriginalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request:Request,pic_id:str):
        detail = get_object_or_404(Original,pk=pic_id)

        serializer = self.serializer_class(instance=detail)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request:Request,pic_id:str):
        detail = get_object_or_404(Original,pk=pic_id)

        data = request.data
        data['created_by'] = request.user.id

        serializer = self.serializer_class(instance=detail,data=data)
 
        if serializer.is_valid():
            serializer.save()
            response = {
              "message":"Original_pic Updated",
              "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request:Request,pic_id:str):
        detail = get_object_or_404(Original,pk=pic_id)

        detail.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
