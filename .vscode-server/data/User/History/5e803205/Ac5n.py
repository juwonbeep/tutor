from django.shortcuts import render
from .models import Article
import requests
from bs4 import BeautifulSoup
import time
from user.models import Member

# Create your views here.
def subject(request):
    data_dic={}
    data_dic['user_id'] = request.session.get('user')

    if data_dic['user_id']:
        data_dic['userinfo'] = Member.objects.get(memberID = data_dic['user_id'])
        print(data_dic['userinfo'].subject1)
        data_dic['articles']=Article.objects.filter(subject1 = data_dic['userinfo'].subject1)[::-1][:20]
        return render(request, 'article/subject.html', data_dic)
    
    else:
        data_dic['article']=Article.objects.all()[::-1][:20]
        print(data_dic['articles'])
        return render(request, 'article/subject.html', data_dic)
    

def articlereg(request):
    field_var = 'econ'
    resultSize_var = 1000

    url = f"https://arxiv.org/list/{field_var}/recent?skip=0&show={resultSize_var}"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        chunks = soup.find_all('div', {'class': 'meta'})
        links = [link['href'] for link in soup.find_all('a', attrs = {'title': 'Abstract'})]
        
        for id, paper in enumerate (chunks) :
            index = links[id]
            link = f"https://arxiv.org{index}"
            subjects_tmp = paper.find('div', {'class': 'list-subjects'}).get_text()

            subjects_tmp = subjects_tmp.replace('\n', '')
            subjects_tmp = subjects_tmp.replace('Subjects:', '')
            subjects_tmp = subjects_tmp.strip()
            subjects_tmp = [subjects.split(' (')[0] for subjects in subjects_tmp.split('; ')]

            econ_subjects = ['Econometrics', 'Theoretical Economics', 'General Economics']

            for subject in subjects_tmp:
                if subject in econ_subjects:
                    subject1 = subject
                    subjects_tmp.remove(subject1)
                    break

            if len(subjects_tmp) >0:
                subject2 = subjects_tmp[0]
            else:
                subject2 = ''
            
            #title
            title = paper.find('div', {'class': 'list-title mathjax'}).get_text()
            title = title.replace('\n', '')
            title = title.replace('Title:', '')
            title = title.strip()

            #author
            authors = paper.find('div', {'class': 'list-authors'}).get_text()
            authors = authors.replace('\n', '')
            authors = authors.replace('Authors:', '')
            authors = authors.strip()
            
            #others
            comment = [item.get_text() for item in paper.find_all('div', {'class': 'list-comments mathjax'})]
            reference = [item.get_text() for item in paper.find_all('div', {'class' : 'list-journral-ref'})]
            others = comment + reference
            others = 'i '.join(others)
            others = others.replace('\n', '')
            

            #doi 
            response = requests.get(link)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, 'html.parser')


                doi = soup.find('td', {'class': 'tablecell arxivdoi'})
                doi = doi.find('a').get_text()
                
                abstract = soup.find('blockquote', {'class': 'abstract mathjax'}).get_text()
                abstract = abstract.replace('\n', '')
                abstract = abstract.replace('Abstract', '')
                abstract = abstract.strip()
                
                date = soup.find('div', {'class': 'dateline'}).get_text()
                date = date.replace('\n', '')
        print(id)       
        print(subject1)
        articleregister = Article(
            index = index,
            link = link,
            doi = doi,
            subject1 = subject1,
            # subject2 = subject2,
            title = title,
            author = authors,
            abstract = abstract,
            date = date,
            etc = others,
        )

        articleregister.save()
        time.sleep(0.1)

        return render(request, 'home/index.html')

