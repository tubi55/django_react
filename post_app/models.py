from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

# 순서1 - DB에 저장하고 싶은 데이터 구조에 맞게 모델 구조 설정
# 포스트 모델 생성 클래스
class Posts(models.Model):
  # 포스트 카테고리
  CATEGORY = (('BUSINESS', 'Business'), ('PERSONAL','Personal'),('IMPORTANT','Important'))

  # 포스트 모델 스키마 (제목, 본문, 슬러그, 카테고리, 포스트날짜, 수정날짜)
  title= models.CharField(max_length=100)
  body= models.TextField() 
  slug= models.SlugField(unique=True, blank=True, null=True)
  category = models.CharField(max_length=15, choices=CATEGORY, default='PERSONAL')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  # 포스트 제목 문자열 반환 메서드
  def __str__(self):
    return self.title

  # 슬러그 없을시 고유 슬러그 추가해서 포스트 모델 생성 메서드
  def save(self, *args, ** kwargs):
    if not self.slug:
      
      #추후 게시글 필터링할 때 필요한 기본 슬러그 생성
      slug_base = slugify(self.title)
      slug = slug_base

      #슬러그가 고유값인지 확인후 필요시 슬러그명 수정
      if Posts.objects.filter(slug=slug).exists():
        slug= f'{slug_base}-{get_random_string(5)}'
      self.slug = slug
    super(Posts, self).save(*args, **kwargs)
