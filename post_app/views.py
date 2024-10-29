from django.shortcuts import render
from post_app.models import Posts
from post_app.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def posts(request):

  # 들어온 요청이 GET 방식일때는 기존의 모델데이터를 JSON형태로 직렬화해서 프론트로 전달
  if request.method == 'GET':
    posts = Posts.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

  # 들어온 요청이 POST 방식일때는 클라이언트로부터 받은 데이터를 역질렬화해서 모델저장
  elif request.method == 'POST':
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)    

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def posts_detail(request, slug): 
  try:
    post = Posts.objects.get(slug=slug)  
  except Posts.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method=='GET':
    serializer = PostSerializer(post)
    return Response(serializer.data)

  elif request.method =='PUT':   
    serializer = PostSerializer(post, data= request.data)

    if serializer.is_valid():    
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
  elif request.method =='DELETE':
    post.delete()
    return  Response(status=status.HTTP_204_NO_CONTENT)
