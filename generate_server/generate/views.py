from accounts.serializers import UserSerializer
from django.core.files import File
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import APIView, api_view, permission_classes
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Origin, Result
from .permissions import CreaterOrReadOnly
from .serializers import OriginSerializer, ResultSerializer


# 获取当前用户的上传记录
class UserPictureListView(APIView):
    
    serializer_class = OriginSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,user_id:str):
        user_pic = Origin.objects.filter(created_by=user_id)
        serializer = OriginSerializer(user_pic,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def getUserPic(request):
    user_id = request.GET.get('id')
    user_pic_list = Origin.objects.filter(created_by=user_id)
    serializer = OriginSerializer(user_pic_list,many=True)

    return Response(data=serializer.data,status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllResult(request):
  
  res_list = Result.objects.all()
  serializer = ResultSerializer(res_list,many=True)

  return Response(data=serializer.data,status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggleFavorite(request,res_id):

    cur_res = Result.objects.get(id=res_id)

    if request.user in cur_res.favorited.all():
        cur_res.favorited.remove(request.user)
        cur_res.like_count -= 1
        cur_res.save()

        return Response(data={'is_favorite':False},status=status.HTTP_200_OK)

    else:
        cur_res.favorited.add(request.user)
        cur_res.like_count += 1
        cur_res.save()
        return Response(data={'is_favorite':True},status=status.HTTP_200_OK)
      


# 获取当前用户信息
@api_view(http_method_names=['GET'])
@permission_classes([IsAuthenticated])
def get_user_for_current(request: Request):
    user = request.user

    serializer = UserSerializer(instance=user,
                                            context={"request": request})

    return Response(data=serializer.data, status=status.HTTP_200_OK)


# 查看全部历史记录、上传并处理单个原图
class PictureListCreateView(APIView):

    serializer_class = OriginSerializer
    permission_classes = [CreaterOrReadOnly]


    def get(self,request,*args,**kwargs):
        origin = Origin.objects.all()
        serializer = self.serializer_class(instance=origin,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        image_file = request.FILES['picture']
        
        image_name = image_file.name

        data = request.data
        data['created_by'] = request.user.id

        data['name'] = image_name
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            # request.data.FILE 传进来的文件 放进模型处理
            # /generate_server/
            # 处理图片
            # 处理后的图片 读取这个路径
            handle_img = open(f"media/res/{image_name}","rb")
            image_file = File(handle_img)
            image_file.name = image_name
            serializer.save()
            origin = Origin.objects.filter(id=serializer.data['id']).first()
            result = Result.objects.create(modified_pic=image_file,created_by=request.user,origin=origin)
            # result = Result(modified_pic=image_file,created_by=request.user)
            # result.save()
            
                        
            response = {
              "message":"图片已成功处理和上传！",
              "data":serializer.data,
              "modified_pic":'http://127.0.0.1:8000/media/' + str(result.modified_pic)
            }
            

            return Response(data=response,status=status.HTTP_201_CREATED)
            # return Response('ok',status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_201_CREATED)


# 查看、更新、删除单个上传记录
class RecordRetrieveUpdateDeleteView(APIView):
    serializer_class = OriginSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request:Request,pic_id:str):
        detail = get_object_or_404(Origin,pk=pic_id)

        serializer = self.serializer_class(instance=detail)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request:Request,pic_id:str):
        detail = get_object_or_404(Origin,pk=pic_id)
        data = request.data
        serializer = self.serializer_class(instance=detail,data=data)
 
        if serializer.is_valid():
            serializer.save(created_by=request.user.id)
            response = {
              "message":"Record Updated",
              "data":serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request:Request,pic_id:str):
        detail = get_object_or_404(Origin,pk=pic_id)

        detail.delete()

        return Response({'message':'删除成功'},status=status.HTTP_200_OK)
