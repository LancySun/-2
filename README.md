# -*- coding: utf-8 -*-



import os
import shutil
import datetime
from getJiraIssue import MyHTMLParser
from LightMysql import LightMysql
import pymysql
import datetime
from datetime import timedelta
import re
import sys
from atomdatabase import DataToMysql
import paramiko
import threading
import time
from jira import JIRA


class Modelname:
    def Modelname_handle(self,template):
        rule = r'_(.*?)_'
        slotList = re.findall(rule, template)
        if not slotList:
            return slotList
        else:
            s = "("+"'"+slotList[0]+"'"+","+")"
            s1 = eval(s)
            return s1
        
    def models(self,path_root,root_directory_name):
        ite = file_handle()
        path_root_next = os.path.join(path_root,root_directory_name)
        item = ite.file2(path_root_next)
        return item
    def models1(self,path_root,root_directory_name):
        ite = file_handle()
        path_root_next = os.path.join(path_root,root_directory_name)
        item = ite.file1(path_root_next)
        return item
    def model_member(self,item_1,item):
        for model_member in item_1:
            if model_member in item:
                continue
            else:
                item.append(model_member)
        return item

class file_handle:
    def file2(self,path_root):
        item1=[]
        #path_root = r'C:\\Users\\sunlanzi\\Desktop\\all\\daily'
        file_list2 = os.listdir(path_root)
        for i in file_list2:
            path2 = os.path.join(path_root,i)
            for dirpath, dirs, files in os.walk(path2):
            ##print(files)
                for name in files:
                    if os.path.splitext(name)[1] == '.html' and name.find("_email_") >= 0:
                    ##print(i)
                        if i in item1:
                            continue
                        else:
                            item1.append(i)
                    else:
                        continue
        return item1
    def file1(self,path_root):
        item1=[]
        #path_root = r'C:\\Users\\sunlanzi\\Desktop\\all\\daily'
        file_list2 = os.listdir(path_root)
        for i in file_list2:
            #path2 = os.path.join(path_root,i)
            for dirpath, dirs, files in os.walk(path_root):
            ##print(files)
                for name in files:
                    if os.path.splitext(name)[1] == '.html' and name.find("_email_") >= 0:

                        model_name = Modelname()
                        i_i = model_name.Modelname_handle(i)
                        for i_2 in i_i:
                            if i_2 in item1:
                                continue
                            else:
                                item1.append(i_2)
                    else:
                        continue
        return item1


class days_count:
    def week_get2(self,d):
        dayscount = datetime.timedelta(days=d.isoweekday())
        dayfrom = d - dayscount + datetime.timedelta(days=1)
        dayto = d - dayscount + datetime.timedelta(days=7)
        ##print (' ~~ '.join([str(dayfrom), str(dayto)]))
        week7 = []
        i = 0
        while (i <= 6):
            day_oneweek = str(i+1)
            week7.append(str(dayfrom + datetime.timedelta(days=i)))
            i += 1
        return week7
    def week_get1(self,d):
        dayscount = datetime.timedelta(days=d.isoweekday())
        dayto = d - dayscount
        sixdays = datetime.timedelta(days=6)
        dayfrom = dayto - sixdays
        date_from = datetime.datetime(dayfrom.year, dayfrom.month, dayfrom.day, 0, 0, 0)
        date_to = datetime.datetime(dayto.year, dayto.month, dayto.day, 23, 59, 59)
        ##print ('---'.join([str(date_from), str(date_to)]))
        week7 = []
        i = 0
        while (i <= 6):
            week7.append(str(dayfrom + datetime.timedelta(days=i)))
            i += 1
        return week7
    def two_or_one_week(self):
        d = datetime.datetime.now()
        d1 = days_count()
        d1.week_get1(d)
        w = []
        w1 = []
        for week1 in d1.week_get1(d):
            w.append(week1)
        for week2 in d1.week_get2(d):
            w1.append(week2)
            w.append(week2)
        day_twoweeks = []
        for i in w:
            i1= i[2:10]
            day_twoweeks.append(i1)
        day_oneweek = []
        for j in w1:
            j1 = j[2:10]
            day_oneweek.append(j1)
        return day_twoweeks,day_oneweek
class Html_content:
    def content(self,fullname1):
        global p
        print("fullname1:",fullname1)
        file_content=open(fullname1,"r").read()
        parser = MyHTMLParser()
        parser.feed(file_content)
        if '.html' in fullname1:
            #print(MyHTMLParser.items)
            if 'PASS' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('PASS')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('PASS','P')
                #item1.append(MyHTMLParser.items[p])
            if 'FAIL' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('FAIL')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('FAIL','F')
                #item1.append(MyHTMLParser.items[p])
            if 'Conditional PASS' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('Conditional PASS')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Conditional PASS','R')
                #item1.append(MyHTMLParser.items[p])
            if 'Exception Happens' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('Exception Happens')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Exception Happens','E')
            #print(MyHTMLParser.items[p])
            return MyHTMLParser.items[p]
        else:
            return ''
        MyHTMLParser.items = []
    def content1(self,fullname3,i_is_html):
        global p
        #fullname3 =  os.path.join(path__1,i_is_html)                       
        file_content=open(fullname3,"r").read()
        parser = MyHTMLParser()
        parser.feed(file_content)
        m = Modelname()
        modelname1 = m.Modelname_handle(i_is_html)
        #if modelname1[0] in MyHTMLParser.items:
        if 'PASS' in MyHTMLParser.items:
            p = MyHTMLParser.items.index('PASS')
            MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('PASS','P,0')
        if 'FAIL' in MyHTMLParser.items:
            p = MyHTMLParser.items.index('FAIL')
            MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('FAIL','F,0')
        if 'Conditional PASS' in MyHTMLParser.items:
            p = MyHTMLParser.items.index('Conditional PASS')
            MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Conditional PASS','C,0')
        if 'Exception Happens' in MyHTMLParser.items:
            p = MyHTMLParser.items.index('Exception Happens')
            MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Exception Happens','E,0')
        return MyHTMLParser.items[1],MyHTMLParser.items[p],modelname1[0]
        MyHTMLParser.items = []
    def content2(self,fullname3,i_is_html):
        global p
        #fullname3 =  os.path.join(path__1,i_is_html)                       
        file_content=open(fullname3,"r").read()
        parser = MyHTMLParser()
        parser.feed(file_content)
        m = Modelname()
        modelname1 = m.Modelname_handle(i_is_html)
        if modelname1[0] in MyHTMLParser.items:
            if 'PASS' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('PASS')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('PASS','P')
            if 'FAIL' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('FAIL')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('FAIL','F')
            if 'Conditional PASS' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('Conditional PASS')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Conditional PASS','C')
            if 'Exception Happens' in MyHTMLParser.items:
                p = MyHTMLParser.items.index('Exception Happens')
                MyHTMLParser.items[p] = MyHTMLParser.items[p].replace('Exception Happens','E')
        return MyHTMLParser.items[1],MyHTMLParser.items[p],modelname1[0]
        MyHTMLParser.items = []
class ST_table:
    def __init__(self,st_chart,cat_daily_chart,cat_weekly_chart,cat_aging_chart,host,user,pswd,database):
        self.st_chart = st_chart
        self.cat_daily_chart = cat_daily_chart
        self.cat_weekly_chart = cat_weekly_chart
        self.cat_aging_chart = cat_aging_chart
        self.db_st = DataToMysql(host,user,pswd,database)
        self.st_m = Modelname()
        self.st_h = Html_content()
    def id_statistics(self,table_name):
        num = self.db_st.select1(table_name)
        for im in num:
            print()
            for tm in im:
                print()
        return tm
    def not_daily_st(self,day_twoweeks,all_filename,path_root,):
        column_name = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun','Mon1','Tue1','Wed1','Thu1','Fri1','Sat1','Sun1']
        column_count = 0
        #处理weekly数据需要
        weekly_set = {}
        
        self.db_st.truncate(self.cat_daily_chart)  
        self.db_st.truncate(self.cat_weekly_chart)  
        self.db_st.truncate(self.cat_aging_chart) 
        self.db_st.truncate(self.st_chart)   
        #向st表中插入model名
        for i_day3 in day_twoweeks:
            item = []
            #文件目录中有这一天
            if i_day3 in all_filename:
                #获取model名称
                item_1 = self.st_m.models1(path_root,i_day3)
                item = self.st_m.model_member(item_1,item)
                #向表中插入model
                self.db_st.model_column(self.st_chart,item)
                self.db_st.model_column(self.cat_daily_chart,item)
                self.db_st.model_column(self.cat_weekly_chart,item)
                self.db_st.model_column(self.cat_aging_chart,item)
            else:
                continue
        #st表模块
        for i_day in day_twoweeks:
            item = []
            item_modelname = []
            
            #文件目录中有这一天
            if i_day in all_filename:
                print('1',i_day)
                #获取model名称
                item_1 = self.st_m.models1(path_root,i_day)
                item = self.st_m.model_member(item_1,item)
                #获取该天路径下的所有文件名称
                path__1 = os.path.join(path_root,i_day)
                filelist = os.listdir(path__1)
                item1_st = []
                item2_st = []
                item3_st = []
                item1_st_daily = {}
                item2_st_weekly = {}
                item2_st_weekly_1 = {}
                item3_st_aging = {}
                same_daily_modelname = []
                same_weekly_modelname = []
                same_aging_modelname = []
               
                #遍历html文件名称及内容
                for i_is_html in filelist:
                    print(i_is_html)
                    date_weekly = ''
                    date_aging = ''
                    #判断符合要求的文件名称，并访问所需信息
                    if '.html' in i_is_html:
                        if 'unit' in i_is_html:
                            continue
                            
                        else:
                            model_name = Modelname()
                            model = model_name.Modelname_handle(i_is_html)
                            #查询weekly内容
                            if 'weekly' in i_is_html:
                                if model in same_weekly_modelname:
                                    print("该model出现过")
                                    fullname2 =  os.path.join(path__1,i_is_html)
                                    a = self.st_h.content1(fullname2,i_is_html)
                                    a2 = a[0]
                                    date_weekly = a2[40:48]
                                    if 'F' in a[1]:
                                        item2_st_weekly[model] = a[1]
                                else:
                                    same_weekly_modelname.append(model)
                                    fullname2 =  os.path.join(path__1,i_is_html)
                                    a = self.st_h.content1(fullname2,i_is_html)
                                    a2 = a[0]
                                    date_weekly = a2[40:48]
                                    item2_st_weekly[model] = a[1]                                      
                                print("item2_st_weekly:",item2_st_weekly)
                            else:
                                if 'pilot' in i_is_html:
                                    print("不管")    
                                else:
                                    if 'daily' in i_is_html:
                                        
                                        if model in same_daily_modelname:
                                            print("该model出现过")
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.st_h.content1(fullname2,i_is_html)
                                            a2 = a[0]
                                            date_weekly1 = a2[10:18]
                                            if 'F' in a[1]:
                                                item1_st_daily[model] = a[1]
                                        else:
                                            same_daily_modelname.append(model)
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.st_h.content1(fullname2,i_is_html)
                                            a2 = a[0]
                                            date_weekly1 = a2[10:18]
                                            item1_st_daily[model] = a[1] 
                                            #modelname = a[2]
                                            #item_modelname.append(modelname)                                     
                                        print("item1_st_daily:",item1_st_daily)
                                    else:
                                        #处理aging内容
                                        if 'aging' in i_is_html:
                                            if model in same_aging_modelname:
                                                print("该model出现过")
                                                fullname2 =  os.path.join(path__1,i_is_html)
                                                a = self.st_h.content1(fullname2,i_is_html)
                                                a2 = a[0]
                                                date_weekly1 = a2[40:48]
                                                if 'F' in a[1]:
                                                    item3_st_aging[model] = a[1]
                                            else:
                                                same_aging_modelname.append(model)
                                                fullname2 =  os.path.join(path__1,i_is_html)
                                                a = self.st_h.content1(fullname2,i_is_html)
                                                a2 = a[0]
                                                date_weekly1 = a2[10:18]
                                                item3_st_aging[model] = a[1]
                                            print("item3_st_aging:",item3_st_aging)


                        item1_st = list(item1_st_daily.values())
                        item2_st = list(item2_st_weekly.values())
                        item3_st = list(item3_st_aging.values())
                        #每次获取完网页所需内容之后需要清空 MyHTMLParser.items 中的内容
                        MyHTMLParser.items = []
                        #处理weekly，取平均值
                        if not item2_st:
                            pass
                        else:
                            #如果weekly是在当天执行当天结束
                            if date_weekly == date_weekly1:
                                pass
                            else:
                                if date_weekly == '':
                                    print("没有weekly数据")
                                else:
                                    l = len(item2_st)
                                    weekly_set[model,date_weekly,l] = item2_st[l-1]
               
                for col in item1_st_daily.keys():
                    item_modelname.append(col[0])                                 
                for col1 in item2_st_weekly.keys():
                    if col1[0] in item_modelname:
                        continue
                    else:
                        item_modelname.append(col1[0])
                
                print(item_modelname)
                #insert daily,weekly,aging data directly
                print("------------------------------------------")
                #print("item1_st_daily:",item1_st_daily)
                #print("item1_st:",item1_st)
                for e,t in zip(item1_st,item_modelname):
                    self.db_st.update1(self.cat_daily_chart,column_name[column_count],repr(e[0]),repr(t))
                #print("item2_st_weekly:",item2_st_weekly)
                if not item2_st_weekly:
                    for e in weekly_set.keys():                
                        if '/' in e[1]:
                            today = '/'+i_day[3:5]+'/'+i_day[6:8]
                        else:
                            if '-' in e[1]:
                                    today = '-'+i_day[3:5]+'-'+i_day[6:8]
                        if today in e[1]:
                            item2_st_weekly[e[0]] = weekly_set[e]
                            for e in item2_st_weekly.keys():
                                self.db_st.update1(self.cat_weekly_chart,column_name[column_count],repr(item2_st_weekly[e]),repr(e[0]))    
                            
                        else:
                            item = ''
                            for t in item_modelname:
                                self.db_st.update1(self.cat_weekly_chart,column_name[column_count],repr(item),repr(t))    
                    
                else:
                    #print('weekly_set:',weekly_set)
                    for e in weekly_set.keys():
                        if '/' in e[1]:
                            today = '/'+i_day[3:5]+'/'+i_day[6:8]
                        else:
                            if '-' in e[1]:
                                    today = '-'+i_day[3:5]+'-'+i_day[6:8]
                        if today in e[1]:
                            #print(e[0])
                            item2_st_weekly_1[e[0]] = weekly_set[e]
                        else:
                            pass
                    #print(item2_st_weekly_1)
                    item2_st = list(item2_st_weekly_1.values())
                    #print(item2_st)
                    for e,t in zip(item2_st,item2_st_weekly_1.keys()):
                        t1 = t[0]
                        self.db_st.update1(self.cat_weekly_chart,column_name[column_count],repr(e[0]),repr(t1))
                #print("item3_st_aging:",item3_st_aging)
                if not item3_st_aging:
                    item = ''
                    for t in item_modelname:
                        self.db_st.update1(self.cat_aging_chart,column_name[column_count],repr(item),repr(t))
                else:
                    for t in item3_st_aging.keys():
                        t1 = item3_st_aging[t]
                        self.db_st.update1(self.cat_aging_chart,column_name[column_count],repr(t1[0]),repr(t[0]))
                #print("weekly_set:",weekly_set)
                print("item1_st:",item1_st)
                print(weekly_set)
                for e in weekly_set.keys():
                    i_day_part = i_day[6:8]
                    if i_day[3:5] in e[1]:
                        if i_day_part in e[1]:  
                            print(i_day)
                            print(e[0])
                            print(item2_st_weekly[e[0]])
                            print('!!!!')                 
                            if item2_st_weekly[e[0]] == 'F,0':
                                item1_st_daily[e[0]] ='F,0'
                                print(item2_st_weekly[e[0]])
                                print(item1_st_daily[e[0]])  
                            else:
                                continue
                print("item1_st_daily:",item1_st_daily)
                #print("item3_st_aging:",item3_st_aging)
                for s in item3_st_aging.keys():
                    if s in item1_st_daily.keys():
                        str_item1_st_daily = item1_st_daily[s]
                        str_item3_st_aging = item3_st_aging[s]
                        item1_st_daily[s] = str_item1_st_daily[0:2]+str_item3_st_aging[0]
                        print(item1_st_daily[s])
                #print("item1_st_daily:",item1_st_daily)
                item1_st = list(item1_st_daily.values())
                #插入含有'daily'数据
                '''
                num = self.db_st.select1(st_chart)
                for im in num:
                    print()
                    for tm in im:
                        print()
                if len(item1_st) <tm:
                    l = tm - len(item1_st)
                    for i in range(0,l):
                        item1_st.append('0,0')
                print("item1_st:",item1_st)
                '''
                print(item_modelname)
                #print("#########################################")
                
                for t in item_modelname:
                    print(t)
                    t1 ="("+"'"+t+"'"+","+")"
                    t2 = eval(t1)
                    if t2 in item1_st_daily.keys():
                        self.db_st.update1(self.st_chart,column_name[column_count],repr(item1_st_daily[t2]),repr(t))
                    else:
                        item = '0,0'
                        self.db_st.update1(self.st_chart,column_name[column_count],repr(item),repr(t))
                r = self.db_st.select5(column_name[column_count],self.st_chart)
                #print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                print(r)
                Num = 0
                for rr in r:
                    Num = Num +1
                    if rr == (None,):
                        rr = '0,0'
                        self.db_st.update(self.st_chart,column_name[column_count],repr(rr),Num)

                column_count=column_count+1
                
            #文件目录没有这一天
            else:
                item2_st_weekly_2 = {}
                item2_st_1 = []
                tm_daily = self.id_statistics(self.cat_daily_chart)
                tm_aging = self.id_statistics(self.cat_aging_chart)
                item = ''
                for i in range(1,tm_daily+1):
                    self.db_st.update(self.cat_daily_chart,column_name[column_count],repr(item),i)
                for i in range(1,tm_aging+1):
                    self.db_st.update(self.cat_aging_chart,column_name[column_count],repr(item),i)
                item1_st_1 = {}
                item1_st_1_weekly=[]
                item1_st_1_copy = ['']
                i_m1 = []
                #目录中没有出现含有weekly的html文件
                if not weekly_set:
                    tm_weekly = self.id_statistics(self.cat_weekly_chart)
                    for i in range(1,tm_weekly+1):
                        self.db_st.update(self.cat_weekly_chart,column_name[column_count],repr(item),i)
                    #判断周天是否已经插入值
                    result = self.db_st.select(column_name[column_count],self.st_chart)
                    result1 = list(result)
                    tm= self.id_statistics(self.st_chart)                    
                    for im1 in range(0,tm):
                        i_m1.append((None,))
                    #如果没有插入值指直接填空
                    if result1 == i_m1:
                        item2 = '0,0'
                        for i in range(1,tm+1):
                            self.db_st.update(self.st_chart,column_name[column_count],repr(item2),i)
                    else:
                        #否则跳出循环
                        k = []
                        for j in result1:
                            #print(j)
                            if j ==('P',):
                                k.append(('P,0',))
                            else:
                                if j ==('F',):
                                   k.append(('F,0',)) 
                                else:
                                    if j==('E',):
                                       k.append(('E,0',))
                                    else:
                                       k.append(('0,0',))
                        print(k)
                        for t,i in zip(k,range(1,tm+1)):
                            num = self.db_st.select1(self.st_chart)
                            for im in num:
                                print(im)
                                for tm in im:
                                    print(tm)
                            for t1 in t:
                                print(t1)
                                self.db_st.update(self.st_chart,column_name[column_count],repr(t1),i)
                    column_count=column_count+1

                else:
                    print(weekly_set)
                    print(item2_st_weekly_2)
                    for e in weekly_set.keys():
                        print(e[1])
                        if '/' in e[1]:
                            today = '/'+i_day[3:5]+'/'+i_day[6:8]
                        else:
                            if '-' in e[1]:
                                today = '-'+i_day[3:5]+'-'+i_day[6:8]
                        #i_day_part = i_day[6:8]
                        if today in e[1]:
                            item2_st_weekly_2[e[0]] = weekly_set[e]
                            
                        else:
                            continue
                    print(item2_st_weekly_2)
                    item2_st_1 = list(item2_st_weekly_2.values())
                    print(item2_st_1)
                    if not item2_st_1:
                        tm1= self.id_statistics(self.cat_weekly_chart)
                        e = ''
                        for t in range(1,tm1+1):
                            self.db_st.update(self.cat_weekly_chart,column_name[column_count],repr(e),t)
                    else:
                        for e,t in zip(item2_st_1,item2_st_weekly_2.keys()):
                            t1 = t[0]
                            self.db_st.update1(self.cat_weekly_chart,column_name[column_count],repr(e[0]),repr(t1))
                    tm2= self.id_statistics(self.st_chart)
                    modelname = self.db_st.select3(self.st_chart)
                    print("modelname:",modelname)
                    for element,m_2 in zip(range(0,tm2),modelname):
                        item1_st_1[m_2] = '0,0'
                    print(item1_st_1)
                    print("item2_st_weekly:",item2_st_weekly)
                    print(weekly_set)
                    for e in weekly_set.keys():
                        print("i_day",i_day)
                        i_day_part = i_day[3:8]
                        print(i_day_part)
                        print(e[1])
                        if i_day_part in e[1]:
                            print('i_day_part:',i_day_part)
                            for e_1 in weekly_set.keys():
                                if e[0] in e_1:
                                    print(e[0])
                                    print(weekly_set[e_1])
                                    print(item1_st_1[e[0]])
                                    item1_st_1[e[0]] = weekly_set[e_1]
                                    print(item1_st_1[e[0]])
                        else:
                            continue

                    print(item1_st_1)
                    item1_st_1_weekly = list(item1_st_1.values())
                            
                if item1_st_1_weekly == item1_st_1_copy:
                    result = self.db_st.select(column_name[column_count],self.st_chart)
                    result1 = list(result)
                    tm3= self.id_statistics(self.st_chart)
                    for im1 in range(0,tm3):
                        i_m1.append((None,))
                    #如果没有插入值指直接填空
                    if result1 == i_m1:
                        item2 = '0,0'
                        for i in range(1,12): 
                            self.db_st.update(self.st_chart,column_name[column_count],repr(item2),i)
                                
                    else:
                        print("该天已经有数据")
                    column_count=column_count+1
                    #print("没有这一天")
                else:
                    if not item1_st_1_weekly:
                        continue
                    else:
                        for element1,i in zip(item1_st_1_weekly,range(1,12)):
                            self.db_st.update(self.st_chart,column_name[column_count],repr(element1),i)
                        column_count=column_count+1
    def daily_st(self,item_1,path_root_next,day_twoweeks):
        for i_st in item_1:
            print("模块名称")
            print(i_st)
            path = os.path.join(path_root_next,i_st)
            file_list=os.listdir(path) #进入指定的目录
            item4_st = []
            for k_st in day_twoweeks:
                print(k_st)
                if k_st in file_list:
    
                    print("文件夹中有这一天的数据")
                    for filename in os.listdir(path):
    
                        if filename==k_st:
                                #细化地址
                            fullname = os.path.join(path,filename)
                            print(fullname)
                            #获取具体某一天目录下的文件列表
                            file_list1 = os.listdir(fullname)
                            print(file_list1)
                            if not file_list1:
                                #item1.append('')
                                item4_st.append('')
                            ##print(file_list1)
                            else:
                                s_st = 0
                                item2 = []
                                item1_st = []
                                #根据文件名不同想不通的表中插入数据
                                for k1_st in file_list1:                                
                                    if 'unit' not in k1_st:
                                        s_st = s_st+1
                                        fullname1 = os.path.join(fullname,k1_st)  
                                        #获取网页源码                         
                                        file_content=open(fullname1,"r").read()
                                        parser = MyHTMLParser()
                                        parser.feed(file_content)
                                        cn = Html_content()
                                        print(item1_st)
                                        item1_st.append(cn.content(fullname1))
                                        print("hhahahahahahahahah",item1_st)
                                        
                                        if s_st>1:
                                            if len(item1_st)>1:
                                                for i_2_st in item1_st:
                                                    if i_2_st == 'F':
                                                        item1_st = ['F']
                                                        item4_st.pop()
                                                        item4_st.append(item1_st[0])
                                        else:
                                            item4_st.append(item1_st[0])
                                        print(item4_st)
                                    else:
                                        continue
                else:
                    print("文件夹中没有这一天的数据")
                    item4_st.append('')
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(item4_st)

            result4 = self.db_st.select3(self.st_chart)
            print(result4)
            item5_st = []
            i_st_1 = "("+"'"+i_st+"'"+","+")"
            print(i_st_1)
            i_st_2 = eval(i_st_1)
            #for ii in result4:
            if i_st_2 in result4:
                print("该model已经有值")
                r = self.db_st.select4(self.st_chart,repr(i_st))
                print("SSSSSSSSSSSSSSS")
                print(r)
                b = list(r)
                print(list(b[0]))
                new = []
                #ii = ['', 'F', '', '', '', '', '', '', '', '', '', '', '', '']
                for i,i1 in zip(range(2,len(list(b[0]))),item4_st):
                    c=list(b[0])
                    #print(c[i])
                    if i1 =='':
                        new.append(c[i])
                    else:
                        if i1 == 'F':
                            d = c[i]
                            d = i1+d[1:3]
                            new.append(d)
                        else:
                            if i1 =='C':
                                d = c[i]
                                d = i1+d[1:3]
                                new.append(d) 
                            else:
                                new.append(c[i])
                print(new)
                if len(new) <15:
                    count =  15 - len(new)
                    for i_1_st in range(0,count):
                        new.append('0,0')
                print(new)
                new[7]=''
                print(new)
                i1 = new[0]
                i2 = new[1]
                i3 = new[2]
                i4 = new[3]
                i5 = new[4]
                i6 = new[5]
                i7 = new[6]
                i8 = new[7]
                i9 = new[8]
                i10 = new[9]
                i11 = new[10]
                i12 = new[11]
                i13 = new[12]
                i14 = new[13]
                i15 = new[14]
                self.db_st.update_not_daily(self.st_chart,repr(i1),repr(i2),repr(i3),repr(i4),repr(i5),repr(i6),repr(i7),repr(i8),repr(i9),repr(i10),repr(i11),repr(i12),repr(i13),repr(i14),repr(i15),repr(i_st))
            else:
                self.db_st.insert(self.st_chart,'model',repr(i_st))
                for ii1 in item4_st:
                    if ii1 == '':
                        item5_st.append("0,0")
                    else:
                        item5_st.append(ii1+',0')
                if len(item5_st) <14:
                    count =  14 - len(item5_st)
                    for i_1_st in range(0,count):
                        item5_st.append('0,0')
                print(item5_st)
                item5_st.insert(7,'')
                print(item5_st)
                i1 = item5_st[0]
                i2 = item5_st[1]
                i3 = item5_st[2]
                i4 = item5_st[3]
                i5 = item5_st[4]
                i6 = item5_st[5]
                i7 = item5_st[6]
                i8 = item5_st[7]
                i9 = item5_st[8]
                i10 = item5_st[9]
                i11 = item5_st[10]
                i12 = item5_st[11]
                i13 = item5_st[12]
                i14 = item5_st[13]
                i15 = item5_st[14]
                self.db_st.update_not_daily(self.st_chart,repr(i1),repr(i2),repr(i3),repr(i4),repr(i5),repr(i6),repr(i7),repr(i8),repr(i9),repr(i10),repr(i11),repr(i12),repr(i13),repr(i14),repr(i15),repr(i_st))
            result_st = self.db_st.select4(self.st_chart,repr(i_st))
            print(result_st)
            result_st1 = result_st[0]
            result_st2 = list(result_st1)
            print(result_st2)
            n = 0
            for r in result_st2:
                if r =='0,0':
                    n = n+1
                else:
                    continue
            print(n)
            if n == 14:
                self.db_st.delete(self.st_chart,repr(i_st))
            print("?????????????????")
        #result_st = self.db_st.select4(st_chart,repr(i_st))

            #result3 = self.db_st.select4(st_chart,i_st)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #def average_value(self,table_name,i_st,item4_st):
        
class UT_table(object):
    def __init__(self, ut_chart, cat_ut_chart,host,user,pswd,database):
        self.ut_chart = ut_chart
        self.cat_ut_chart = cat_ut_chart
        self.db_ut   = DataToMysql(host,user,pswd,database)
        self.ut_m = Modelname()
        self.ut_h = Html_content()

    def id_statistics_1(self,table_name):
        num = self.db_ut .select1(table_name) 
        for im in num:
            print()
            for tm in im:
                print()
        return tm
    def not_daily_ut(self,day_oneweek,all_filename,path_root):
        self.db_ut .truncate(self.ut_chart)
        weekly_set = {}  
        column_name_ = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        column_count_ = 0
        print("diyi")
        for i_day3 in day_oneweek:
            item = []
            print(i_day3)
            print("1")
            #文件目录中有这一天
            if i_day3 in all_filename:
                #获取model名称
                print("2")
                item_1 = self.ut_m.models1(path_root,i_day3)
                item = self.ut_m.model_member(item_1,item)
                #向表中插入model
                print("3")
                self.db_ut .model_column(self.ut_chart,item)
            else:
                continue
        for i_day1 in day_oneweek:
            item1_unit = []
            item = []
            item_modelname = []
            #文件目录中有这一天
            if i_day1 in all_filename:
                print(i_day1)
                #获取model名称
                
                item_1 = self.ut_m.models1(path_root,i_day1)
                item = self.ut_m.model_member(item_1,item)
                print(item)
                #向表中插入model
                self.db_ut .model_column(self.ut_chart,item)
                #获取该天路径下的所有文件名称
                path__1 = os.path.join(path_root,i_day1)
                filelist = os.listdir(path__1)
                item1_unit = []
                item2_unit = []
                date_weekly_st1 = []
                item1_ut_daily = {}
                item2_ut_weekly = {}
                item3_ut_aging = {}
                same_daily_modelname = []
                same_weekly_modelname = []
                same_aging_modelname = []
                #遍历文件名称集合
                for i_is_html in filelist:
                    
                    date_weekly_ = ''
                    #判断符合要求的文件名称
                    if '.html' in i_is_html:
                        ##print("是html文件")
                        if 'unit' in i_is_html:
                            print(i_is_html)
                            model_name = Modelname()
                            model = model_name.Modelname_handle(i_is_html)
                            ##print("需要插入到ut表中")
                            if 'weekly' in i_is_html:
                                if model in same_weekly_modelname:
                                    print("该model出现过")
                                    fullname2 =  os.path.join(path__1,i_is_html)
                                    a = self.ut_h.content2(fullname2,i_is_html)
                                    a2 = a[0]
                                    date_weekly = a2[40:48]
                                    if 'F' in a[1]:
                                        item2_ut_weekly[model] = a[1]
                                else:
                                    same_weekly_modelname.append(model)
                                    fullname2 =  os.path.join(path__1,i_is_html)
                                    a = self.ut_h.content2(fullname2,i_is_html)
                                    a2 = a[0]
                                    date_weekly = a2[40:48]
                                    item2_ut_weekly[model] = a[1]                                      
                                print("3",item2_ut_weekly)
                                #fullname3 =  os.path.join(path__1,i_is_html)
                                #a = h.content2(fullname3,i_is_html)
                                #a1 = a[0]
                                #date_weekly = a1[40:48]
                                #item2_unit.append(a[1])                        
                            else:
                                if 'pilot' in i_is_html:
                                    print("不管")
                                else:
                                    if 'aging' in i_is_html:
                                        if model in same_aging_modelname:
                                            print("该model出现过")
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.ut_h.content2(fullname2,i_is_html)
                                            a2 = a[0]
                                            #date_weekly1 = a2[40:48]
                                            if 'F' in a[1]:
                                                item3_ut_aging[model] = a[1]
                                        else:
                                            same_aging_modelname.append(model)
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.ut_h.content2(fullname2,i_is_html)
                                            a2 = a[0]
                                            #date_weekly1 = a2[10:18]
                                            item3_ut_aging[model] = a[1]
                                    else:
                                        if 'daily' in i_is_html:
                                            if model in same_daily_modelname:
                                                print("该model出现过")
                                                fullname2 =  os.path.join(path__1,i_is_html)
                                                a = self.ut_h.content2(fullname2,i_is_html)
                                                a2 = a[0]
                                                date_weekly1 = a2[10:18]
                                                if 'F' in a[1]:
                                                    item1_ut_daily[model] = a[1]
                                            else:
                                                same_daily_modelname.append(model)
                                                fullname2 =  os.path.join(path__1,i_is_html)
                                                a = self.ut_h.content2(fullname2,i_is_html)
                                                a2 = a[0]
                                                date_weekly1 = a2[10:18]
                                                item1_ut_daily[model] = a[1]
                                                #print(a[2]) 
                                                #modelname = a[2]
                                                #item_modelname.append(modelname)                                     
                                        print("4",item1_ut_daily)
                                        #fullname3 =  os.path.join(path__1,i_is_html)
                                        #a = h.content2(fullname3,i_is_html)
                                        #a1 = a[0]
                                        #date_weekly_1 = a1[10:18]
                                        #item1_unit.append(a[1])
                                        
                            item1_unit = list(item1_ut_daily.values())
                            item2_unit = list(item2_ut_weekly.values()) 
                            #每次获取完网页所需内容之后需要清空 MyHTMLParser.items 中的内容
                            MyHTMLParser.items = []
                            #处理weekly，取平均值
                            if not item2_unit:
                                pass
                            else:
                                #如果weekly是在当天执行当天结束
                                if date_weekly == date_weekly1:
                                    pass
                                else:
                                    if date_weekly == '':
                                        print("没有weekly数据")
                                    else:
                                        l = len(item2_unit)
                                        weekly_set[model,date_weekly,l] = item2_unit[l-1]                                      
                            #if date_weekly_ == date_weekly_1:
                            #    if item2_unit[-1] =='F':
                            #        item1_unit[-1] = item2_unit[-1]
                            #else:
                            #    if date_weekly_ == '':
                            #        print("没有weekly数据")
                            #    else:
                            #        
                            #        l = len(item2_unit)
                            #        weekly_set[date_weekly,l] = item2_unit[l-1]
                        else:
                            #item1_unit.append('')
                            pass
                            
                            
    
                #插入含有'weekly'的数据
                for e in weekly_set.keys():
                    #e1 = str(e)
                    #print("i_day",i_day)
                    i_day_part = i_day1[6:8]
                    #print(i_day_part)
                    #print(e[1])
                    if i_day_part in e[1]:
                        #print(e[0])
                        if item2_ut_weekly[e[0]] == 'F':
                            item1_ut_daily[e[0]] ='F'
                        else:
                            pass
                print("item1_ut_daily:",item1_ut_daily)
                print("item2_ut_weekly:",item2_ut_weekly)
                for s in item3_ut_aging.keys():
                    if s in item1_ut_daily.keys():
                        str_item1_ut_daily = item1_ut_daily[s]
                        str_item3_ut_aging = item3_ut_aging[s]
                        item1_ut_daily[s] = str_item1_ut_daily[0:2]+str_item3_ut_aging[0]
                        print(item1_st_daily[s])
                print("item1_ut_daily:",item1_ut_daily)
                item1_unit = list(item1_ut_daily.values())
                print(item1_unit)
                for col in item1_ut_daily.keys():
                    item_modelname.append(col[0])
                print(item_modelname)
                #result2 = db.select(column_name_[column_count_],ut_chart)
                #print(result2)
                for e,t in zip(item1_unit,item_modelname):
                    self.db_ut .update1(self.ut_chart,column_name_[column_count_],repr(e),repr(t))
                column_count_=column_count_+1         
            
            #文件目录没有这一天
            else:
                item1_unit_1 = []
                item1_unit_1_copy = ['']
                print(weekly_set)
                if not weekly_set:
                    result = self.db_ut .select(column_name_[column_count_],self.ut_chart)
                    print(result)
                    if not result:
                        item2 = ''
                        tm= self.id_statistics_1(self.ut_chart)
                        for i in range(1,tm+1):
                            self.db_ut .update(self.ut_chart,column_name_[column_count_],repr(item2),i)
                            
                    else:
                        print("该天已经有数据")
                    column_count_=column_count_+1
                else:
                    tm1= self.id_statistics_1(self.ut_chart)
                    for element in range(0,tm1):
                        item1_unit_1.append('')
                    for e in weekly_set.keys():
                        e1 = str(e)
                        if i_day1 in e1:
                            number = int(e1[13])
                            value = weekly_set[i_day1,number]
                            if value == 'F':
                                item1_unit_1[number-1] = value
                            else:
                                continue
                if item1_unit_1 == item1_unit_1_copy:
                    result = self.db_ut .select(column_name_[column_count_],self.ut_chart)
                    if not result:
                        item2 = ''
                        tm2= self.id_statistics_1(self.ut_chart)
                        for i in range(1,tm2+1): 
                            self.db_ut .update(self.ut_chart,column_name_[column_count_],repr(item2),i)   
                    else:
                        print("该天已经有数据")
                    column_count_=column_count_+1
                    #print("没有这一天")
                else:
                    if not item1_unit_1:
                        continue
                    else:
                        tm3= self.id_statistics_1(self.ut_chart)
                        for element1,i in zip(item1_unit_1,range(1,tm3+1)):
                            self.db_ut .update(self.ut_chart,column_name_[column_count_],repr(element1),i)
                        column_count_=column_count_+1
        
    def daily_ut_twoweeks(self,day_twoweeks,all_filename,path_root):
        self.db_ut .truncate(self.cat_ut_chart)
        column_name = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun','Mon1','Tue1','Wed1','Thu1','Fri1','Sat1','Sun1']
        column_count = 0
        #向st表中插入model名
        for i_day3 in day_twoweeks:
            item = []
            #文件目录中有这一天
            if i_day3 in all_filename:
                #获取model名称
                item_1 = self.ut_m.models1(path_root,i_day3)
                item = self.ut_m.model_member(item_1,item)
                #向表中插入model
                self.db_ut .model_column(self.cat_ut_chart,item)
            else:
                continue
        #st表模块
        for i_day in day_twoweeks:
            item = []
            item_modelname = []
            
            #文件目录中有这一天
            if i_day in all_filename:
                print('1',i_day)
                #获取model名称
                item_1 = self.ut_m.models1(path_root,i_day)
                item = self.ut_m.model_member(item_1,item)
                #获取该天路径下的所有文件名称
                path__1 = os.path.join(path_root,i_day)
                filelist = os.listdir(path__1)
                item1_ut = []
                item1_st_daily = {}
                same_daily_modelname = []
               
                #遍历html文件名称及内容
                for i_is_html in filelist:
                    print(i_is_html)
                    #判断符合要求的文件名称，并访问所需信息
                    if '.html' in i_is_html:
                        if 'unit' in i_is_html:
                            model_name = Modelname()
                            model = model_name.Modelname_handle(i_is_html)
                            #查询weekly内容
                            if 'weekly' in i_is_html:
                                pass
                            else:
                                if 'pilot' in i_is_html:
                                    print("不管")    
                                else:
                                    if 'daily' in i_is_html:
                                        
                                        if model in same_daily_modelname:
                                            print("该model出现过")
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.ut_h.content1(fullname2,i_is_html)
                                            a2 = a[0]
                                            date_weekly1 = a2[10:18]
                                            if 'F' in a[1]:
                                                item1_st_daily[model] = a[1]
                                        else:
                                            same_daily_modelname.append(model)
                                            fullname2 =  os.path.join(path__1,i_is_html)
                                            a = self.ut_h.content1(fullname2,i_is_html)
                                            a2 = a[0]
                                            date_weekly1 = a2[10:18]
                                            item1_st_daily[model] = a[1]                              
                                        print("item1_st_daily:",item1_st_daily)
                                    else:
                                        #处理aging内容
                                        if 'aging' in i_is_html:
                                            pass

                            
                        else:
                            pass

                        item1_ut = list(item1_st_daily.values())
                        #每次获取完网页所需内容之后需要清空 MyHTMLParser.items 中的内容
                        MyHTMLParser.items = []
                for col in item1_st_daily.keys():
                    item_modelname.append(col[0])
                for e,t in zip(item1_ut,item_modelname):
                    self.db_ut .update1(self.cat_ut_chart,column_name[column_count],repr(e[0]),repr(t))
               
                column_count=column_count+1
                
            #文件目录没有这一天
            else:
                tm1 = self.id_statistics_1(self.cat_ut_chart)
                item = ''
                for i in range(1,tm1+1):
                    self.db_ut.update(self.cat_ut_chart,column_name[column_count],repr(item),i)
                column_count = column_count+1    
    def daily_ut(self,item_1,path_root_next,day_oneweek):
        for i_unit in item_1:
            print("模块名称")
            print(i_unit)
    
            path = os.path.join(path_root_next,i_unit)
            #print(path)
            file_list=os.listdir(path) #进入指定的目录
            ##print(file_list)
            item4_unit = []
            for k_unit in day_oneweek:
                print(k_unit)
                if k_unit in file_list:
    
                    print("文件夹中有这一天的数据")
                    for filename in os.listdir(path):
    
                        if filename==k_unit:
                                #细化地址
                            fullname = os.path.join(path,filename)
                            ##print(fullname)
                            #获取具体某一天目录下的文件列表
                            file_list1 = os.listdir(fullname)
    
                            if not file_list1:
                                #item1.append('')
                                item4_unit.append('')
                            ##print(file_list1)
                            else:
                                s_unit = 0
                                item2 = []
                                item1_unit = []
                                #根据文件名不同想不通的表中插入数据
                                for k1_unit in file_list1:                                
                                    if 'unit' in k1_unit:
                                        s_unit = s_unit+1
                                        ##print("应该插入到ci_ut中")
                                        fullname1 = os.path.join(fullname,k1_unit)  
                                        #获取网页源码  
                                        cn = Html_content()
                                        item1_unit.append(cn.content(fullname1))
                                        print(item1_unit)                                    
                                        if s_unit>1:
                                            if len(item1_unit)>1:
                                                for i_2_unit in item1_unit:
                                                    if i_2_unit == 'F':
                                                        item1_unit = ['F']
                                                        item4_unit.pop()
                                                        item4_unit.append(item1_unit[0])
                                        else:
                                            item4_unit.append(item1_unit[0])
                                    else:
                                        continue
                else:
                    print("文件夹中没有这一天的数据")
                    item4_unit.append('')
            result4 = self.db_ut .select3(self.ut_chart)
            print(result4)
            item5_ut = []
            i_ut_1 = "("+"'"+i_unit+"'"+","+")"
            print(i_ut_1)
            i_ut_2 = eval(i_ut_1)
            #for ii in result4:
            if i_ut_2 in result4:
                print("该model已经有值")
                r = self.db_ut .select4(self.ut_chart,repr(i_unit))
                print("SSSSSSSSSSSSSSS")
                print(r)
                r1= []
                b = list(r)
                print(list(b[0]))
                for i in list(b[0]):
                    if i is None:
                        r1.append("")
                    else:
                        r1.append(i)
                print(r1)
                new = []
                #ii = ['', 'F', '', '', '', '', '', '', '', '', '', '', '', '']
                for i,i1 in zip(range(2,len(list(r1))),item4_unit):
                    c=list(r1)
                    #print(c[i])
                    if i1 =='':
                        new.append(c[i])
                    else:
                        if i1 == 'F':
                            d = c[i]
                            d = i1+d[1:3]
                            new.append(d)
                        else:
                            if i1 =='C':
                                d = c[i]
                                d = i1+d[1:3]
                                new.append(d) 
                            else:
                                new.append(c[i])
                print(new)
                if len(new) <7:
                    count =  7 - len(new)
                    for i_1_ut in range(0,count):
                        new.append('')
                print(new)
                i1 = new[0]
                i2 = new[1]
                i3 = new[2]
                i4 = new[3]
                i5 = new[4]
                i6 = new[5]
                i7 = new[6]
                self.db_ut .update_daily(self.ut_chart,repr(i1),repr(i2),repr(i3),repr(i4),repr(i5),repr(i6),repr(i7),repr(i_unit))
                #print("插入成功")
            else:
                self.db_ut .insert(self.ut_chart,'model',repr(i_unit))
                for ii1 in item4_unit:
                    if ii1 == '':
                        item5_ut.append("")
                    else:
                        item5_ut.append(ii1)
                if len(item5_ut) <7:
                    count =  7 - len(item5_ut)
                    for i_1_ut in range(0,count):
                        item5_ut.append('')
                print(item5_ut)
                
                i1 = item5_ut[0]
                i2 = item5_ut[1]
                i3 = item5_ut[2]
                i4 = item5_ut[3]
                i5 = item5_ut[4]
                i6 = item5_ut[5]
                i7 = item5_ut[6]
                self.db_ut .update_daily(self.ut_chart,repr(i1),repr(i2),repr(i3),repr(i4),repr(i5),repr(i6),repr(i7),repr(i_unit))
        tm_1= self.id_statistics_1(self.ut_chart) 
        for i in range(1,tm_1+1):
            r = self.db_ut .select6(self.ut_chart,i)
            n = 0
            r1 = r[0]
            r2 = list(r1)
            print(r2)
            for iii in r2:
                if iii == None:
                    n = n+1
                    print(r2,n)
                    if n == 7:
                        self.db_ut .delete1(self.ut_chart,i)
                else:
                    if iii == '':
                        n = n +1
                        print(r2,n)
                        if n == 7:
                            self.db_ut .delete1(self.ut_chart,i)
                            
        self.db_ut .alter(self.ut_chart)
        

class Copy_file:
    def Host_environment(self,hostname,port,username,password,local_dir,remote_dir):
        t=paramiko.Transport((hostname,port))
        t.connect(username=username,password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        files_remote = sftp.listdir(remote_dir) #这里需要注意，列出远程文件必须使用sftp，而不能用os
        
        count = 0
        for n in files_remote:
            count = count + 1
        
        files_local =  os.listdir(local_dir)
       
        count1 = 0
        for d_name in files_remote:
            local1_dir = os.path.join(local_dir,d_name)+'/'
            #判断该目录是否存在
            result = os.path.exists(local1_dir)
            if result == False:
                
                os.mkdir(local1_dir)
            else:
                #continue
                pass
            #目录结构必须为/home/sunlanzi/all2/类似才会进行操作
            remote1_dir = os.path.join(remote_dir,d_name)+'/' 
            
            if '-' in d_name:
                print(d_name)
                if d_name in files_local:
                    continue
                else:
                    files_remote1 = sftp.listdir(remote1_dir)
                    for file in files_remote1:
                        
                        p = os.path.join(remote1_dir,file)
                        print(p)
                        result = os.path.isdir(p)
                        print(result)
                        try:
                            if result == False:
                                print(file)
                                sftp.get(os.path.join(remote1_dir,file),os.path.join(local1_dir,file)) #注意，此处只能拷贝的是某个具体的文件，而不能是目录
                        except:
                            print("hahah")
                
            else:
                if d_name == 'daily':
                    files_remote2 = sftp.listdir(remote1_dir)
                
                    for file in files_remote2:
                        remote2_dir = os.path.join(remote1_dir,file)+'/'
                    
                        if '.sh' in file:
                            continue
                        else:
                            files_remote3 = sftp.listdir(os.path.join(remote1_dir,file))
                            for i in files_remote3:
                                count1 = count1+1
                        
                    
                        local2_dir = os.path.join(local1_dir,file)+'/'
                        files_local1 = os.listdir(local2_dir)
                        print("@@",file)
                        for item in files_remote3:
                        
                            if item in files_local1:
                                continue
                            else:
                                if '18' in item:
                                    local3_dir = os.path.join(local2_dir,item)+'/'
                                    os.mkdir(local3_dir)
                                    remote3_dir = os.path.join(remote2_dir,item)+'/'
                                    print(remote3_dir)
                                    files_remote4 = sftp.listdir(remote3_dir)
                                    for file1 in files_remote4:
                                        sftp.get(os.path.join(remote3_dir,file1),os.path.join(local3_dir,file1))
                                else:
                                    print("##",item)
                                    print("软链接$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                                    print(os.path.islink(os.path.join(remote2_dir,item)))
                                    sftp.get(os.path.join(remote2_dir,item),os.path.join(local2_dir,item))
        return count,count1   
class Main_process:
    def execute(self): 
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        '''
        print(datetime.datetime.now())
        hostname = '105.128.30.59'
        username = 'root'
        password = 'auto!@#'
        port = 22
        local_dir = r'/home/artik/software/dashboard/DataCollection/all2/'
        
        remote_dir = r'/var/www/artik-release/images/Fileshare/CI/'
        c = Copy_file()
        count=c.Host_environment(hostname,port,username,password,local_dir,remote_dir)
        count1 = count[0]
        count2 = count[1]
        print(count1,count2)
        '''
         
        #获取所有model名
        root_directory_name = 'daily' 
        m = Modelname()
        item_1 = m.models(path_root,root_directory_name)
        ##获取两个星期日期或者一个星期日期
        Day = days_count()
        Day1 = Day.two_or_one_week()
        day_twoweeks = Day1[0]
        #print(day_twoweeks)
        day_oneweek = Day1[1]


        path_root_next = os.path.join(path_root,root_directory_name)
        #item1_unit = []
        #item1_st = []
        insert_data_st = ST_table('dashboard_ci_st_chart1','dashboard_cat_ci_daily_chart','dashboard_cat_ci_weekly_chart','dashboard_cat_ci_aging_chart',host,user,pswd,database)
        insert_data_ut = UT_table('dashboard_ci_ut_chart1','dashboard_cat_ci_ut_chart',host,user,pswd,database)
        #
        insert_data_st.not_daily_st(day_twoweeks,all_filename,path_root)
        insert_data_st.daily_st(item_1,path_root_next,day_twoweeks)
       #
        #
        insert_data_ut.not_daily_ut(day_oneweek,all_filename,path_root)
        insert_data_ut.daily_ut_twoweeks(day_twoweeks,all_filename,path_root)
        insert_data_ut.daily_ut(item_1,path_root_next,day_oneweek)

        
        ji = JiraIssue(host,user,pswd,database,'dashboard_defact_statistics')
        prjlist = ["ARTIK E2E", "ARTIK IoT", "ARTIK E2E IDE"]
        ji.insert_issue("http://105.128.30.62:8080", "chao.wee", "13647408", prjlist)
        
        global timer
        timer = threading.Timer(1.0, Process.execute)
        timer.start()
class JiraIssue(object):
    def __init__(self,host,user,pswd,database,table_name3):
        self.db_Jira = DataToMysql(host,user,pswd,database)
        self.Jira_table = table_name3
    #print issue summary
    def get_issue(self, url, user, pswd, prjname):
        issue_priority = {}
        print(url,user,pswd)
        jira = JIRA(url, basic_auth=(user, pswd))
        issues = jira.search_issues('project = "'+prjname+'" and issuetype="Bug" and status!="Closed"', maxResults=0, fields='summary,priority,status')
        for issue in issues:
            if issue_priority.has_key(issue.fields.priority.name):
                issue_priority[issue.fields.priority.name] = issue_priority[issue.fields.priority.name] + 1
            else:   # add new 
                issue_priority[issue.fields.priority.name] = 1
        return issue_priority
    def insert_issue(self,host,user,pswd,prjlist):
        self.db_Jira.truncate(self.Jira_table)
        for prj in prjlist:
            issue_data = self.get_issue(host, user, pswd, prj)
            keys = "project"
            values = '"' + prj + '"'
            for issue in issue_data:
                keys = keys + "," + issue
                values = values + "," + str(issue_data[issue])
            result = self.db_Jira.insert(self.Jira_table,keys,values)
        
if __name__ == '__main__':
    path_root = r'/home/artik/software/dashboard/DataCollection/all2/'
    #path_root = r'C:\Users\sunlanzi\Desktop\all2-1'
    all_filename = os.listdir(path_root)
    

    host = '109.105.120.34'
    user = 'root'
    pswd = 'auto!@#'
    database = 'dashboard'
    
    Process = Main_process()
    timer = threading.Timer(1.0, Process.execute)
    timer.start()
