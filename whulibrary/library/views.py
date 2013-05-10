# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
import sys
import datetime
import os,time
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


def home(request):
    # reload( sys )
    # sys.setdefaultencoding('utf-8')
    return HttpResponse('aa') 
    #render_to_response('index.html',locals())
@csrf_exempt
def robot(request):
    print 'hello word'
    print request.method
    if request.method=='GET':
        return HttpResponse(request.GET.get('echostr'))
    if request.method=='POST':
        from BeautifulSoup import BeautifulSoup
        soup = BeautifulSoup(request.raw_post_data)
        s="""<xml>
             <ToUserName>"""+soup.fromusername.text+"""</ToUserName>
             <FromUserName>"""+soup.tousername.text+"""</FromUserName>
             <CreateTime>12345678</CreateTime> <MsgType>text</MsgType>
             <Content>nihao</Content>
             <FuncFlag>0</FuncFlag> </xml>"""
    return HttpResponse(s)
       


