from django.db import models

class Article(models.Model):
    # 각 필드에 대한 정의 및 설명
    index = models.CharField(max_length=100, primary_key=True)  # 고유 인덱스
    link = models.CharField(max_length=200)  # 기사 링크
    doi = models.CharField(max_length=100, null=True)  # DOI (Digital Object Identifier), null 허용
    subject1 = models.CharField(max_length=50)  # 주요 주제 1
    subject2 = models.CharField(max_length=50, null=True)  # 주요 주제 2, null 허용
    title = models.CharField(max_length=200)  # 제목
    author = models.CharField(max_length=200)  # 저자
    abstract = models.TextField()  # 초록 (긴 텍스트)
    date = models.CharField(max_length=200)  # 날짜 (문자열 형태로 저장, DateField로 변경 고려)
    etc = models.TextField(null=True)  # 기타 내용 (null 허용)

    class Meta:
        db_table = 'ARTICLE'  # 데이터베이스 테이블 이름 지정

# Create your models here.
