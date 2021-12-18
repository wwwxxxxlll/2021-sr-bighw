#返回一个html页面
from django.shortcuts import render
from django.views.generic import View
from functools import cmp_to_key
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime
import json
headers = {"Authorization": "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"}

# Create your views here.

class Index(View):
    def get(self,request):
        return render(request,'index.html')

class aboutus(View):
    def get(self,request):
        return render(request,'about-us.html')

class Error(View):
    def get(self,request):
        return render(request,'404.html')

class Explain(View):
    def get(self,request):
        return render(request,'说明.html')



def index(request):
    return render(request,'brief_info.html',{})
# 设置主页对应的页面 + 传到主页的数据内容
def home(request):
    # 使用requests模块得到对应api的json内容，然后使用json.loads获取其内容
    api_request = requests.get('https://api.github.com/users?since=0', headers=headers)

    api = json.loads(api_request.content)
    
    print(api)
    # 返回函数render中的参数包含request,''-要跳转的页面,{key:value}-传递到页面的数据
    return render(request, 'home.html', {'api': api})


def commit(request):
    if request.method == 'POST':
        url = request.POST['url']
        u_list = url.strip().split('/')
        api_url = 'https://api.github.com/repos/'+u_list[3]+'/'+u_list[4]+'/commits'
        content_url = 'https://api.github.com/repos/'+u_list[3]+'/'+u_list[4]

        api_request = requests.get(content_url, headers=headers)
        contents = json.loads(api_request.content)
        if contents:
            owner = contents['owner']['login']
            avatar_url = contents['owner']['avatar_url']
            html_url = contents['owner']['html_url']
            description = contents['description']
            topics = contents['topics']
            stargazers_count = contents['stargazers_count']
            created_at =  contents['created_at']
            id = contents['id']
            api_request = requests.get(api_url)
            api_ret = json.loads(api_request.content)
            committer_dict = {}
            date_list = []
            for committer in api_ret:    
                date_it = committer['commit']['author']['date']
                date = list(date_it)
                date.pop(10)
                date.pop(18)
                l = ''
                l = l.join(date)
                dd = datetime.strptime(l, "%Y-%m-%d%H:%M:%S")
                date_list.append(dd)
            sorted_date = sorted(date_list,reverse=True)
            date_newest = sorted_date[0]
            #插入数据库date_newest与u_list[3],u_list[4]
            for committer in api_ret:
                if committer['commit']['author']['name'] not in committer_dict.keys():
                    committer_dict[committer['commit']['author']['name']] = 1
                else:
                    committer_dict[committer['commit']['author']['name']] = committer_dict[committer['commit']['author']['name']] + 1
            sorted_dict = {}
            sorted_dict = sorted(committer_dict.items(), key = lambda kv:(kv[1], kv[0]),reverse = True)
            #print(sorted_dict)
            commit_users = []
            for i in range(0,3):
                if sorted_dict[i]:
                    commit_url = 'https://github.com/'+sorted_dict[i][0]
                    api_request = requests.get('https://api.github.com/users/'+sorted_dict[i][0], headers=headers)
                    user_info = json.loads(api_request.content)
                    avatar_url_1 = user_info['avatar_url']
                    commit_users.append({"user":sorted_dict[i][0],"url":commit_url,"a_url":avatar_url_1})
            
            return render(request,'brief_info.html',{"id":id,"url":url,"owner":owner,"avatar_url":avatar_url,"html_url":html_url,"description":description,"topics":topics,"stargazers_count":stargazers_count,"created_at":created_at,"commit_users":commit_users,"date_newest":date_newest})

def user(request):
    # 获取搜索框中输入的内容，前端搜索框文本的名称为input_content
    user_name = request.POST['input_content']
    if user_name:  # 输入内容不为空
        # 同home函数中获取api接口内容
        user_request = requests.get(url='https://api.github.com/users/' + user_name)
        user_info = json.loads(user_request.content)
        # 返回函数包含两个数据，分别是要搜索的用户名和对应的用户信息
        return render(request, 'user.html', {'input_contents': user_name, 'user_info': user_info})
    else:
        # 若搜索框内没有输入，则进行提示
        notfound = '请在搜索框中输入您需要查询的用户...'
        return render(request, 'user.html', {'notfound': notfound})

#class Contribution(View):
#    def get(self,request):
#        contribute_data = []
#        conact = {}
#        if request.POST:
#            conact = request.POST.get('urn')
#            print(conact)
#            print("1")
#            contribute_data = {'value': 0, 'name': '0'}
#        else:
#            contribute_data = {'value': 0, 'name': ''}
#        return render(request,'contribution.html', {"contribute_data": contribute_data} )