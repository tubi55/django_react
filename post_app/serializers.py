from rest_framework import serializers
from .models import Posts

# 순서4 - 클라이언트와 서버쪽의 데이터 구조가 다르기 때문에 중간에서 데이터를 변환처리
# 직렬화 - 서버쪽데이터를 클라이언트에서 읽을수 있도록 변환
# 역직렬화 - 클라이언트쪽 데이터를 서버쪽에서 읽을수 있도록 변환
class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields = ['id','title','body','slug','category','created','updated']