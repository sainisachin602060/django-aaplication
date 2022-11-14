from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

import psycopg2
try:
    connection=psycopg2.connect(user="postgres",
                            host = "127.0.0.1",
                            port = "5432",
                            database = "CRUD",
                            password="sachin"
                            )
    
    

    cursor=connection.cursor()
    print("DataBase is Connected")
    
except:
    print("query not exceute")    
   





def home(request):
    return render(request,'home.html')

def save(request):
    if(request.method=='POST'):
        date=request.POST['date']
        task1=request.POST['task1']
        task2=request.POST['task2']
        task3=request.POST['task3']
        task4=request.POST['task4']
       
        print(task1)
        
        query1="insert into data1 values(%s,%s,%s,%s,%s)"
        query2=(date,task1,task2,task3,task4) 
        
        try:
            cursor.execute(query1,query2)
            connection.commit() 
            msg="data has been susccessfull save✅"
            return render(request,'home.html',{'ms':msg})
            
        except:
            print("data is not inserted") 
            cursor.close()
            connection.close()
            
            
    else:
        return HttpResponse("wrong code")
    
    
    
    
def show(request):
    data=[]
    query1="select * from data1"
    try:
        cursor.execute(query1)
        data=cursor.fetchall()
        return render(request,'show.html',{'data':data})
        cursor.close()
        connection.close()
    except Exception as e:
        print(e)
        print("query not exceuted")
        
        
        
def delete(request):
    ts=request.GET['date']
    
    query1="delete from data1 where date=%s" 
    query2=(ts,)  
    try:
        cursor.execute(query1,query2)
        connection.commit()  
        return HttpResponseRedirect('/show/')
        cursor.close()
        connection.close()
    
    except:
        print("query not executed")
        cursor.close()
        connection.close()
        
        
def edit(request):
    date=request.GET['date']
    data=[]
  
    
    query1="select * from data1 where date=%s"   
    query2=(date,) 
    
    try:
        cursor.execute(query1,query2)
        data=cursor.fetchmany()
        return render(request,'edit.html',{'ms':data})
        cursor.close()
        connection.close()
    
    except:
        print("query not execute")
        
        
def edited(request):
    if(request.method=='POST'):
        
        datee=request.POST['date']   
        task1=request.POST['task1']     
        task2=request.POST['task2']     
        task3=request.POST['task3']     
        task4=request.POST['task4']     
        query1="insert into data1 values(%s,%s,%s,%s,%s)"
        query2=(datee,task1,task2,task3,task4)
       
        
        try:
            cursor.execute(query1,query2)
            connection.commit()
            return HttpResponseRedirect("/show/")
            cursor.close()
            connection.close()
        
        except:
            print("query not executed")    
            
    else:
        return HttpResponse("<h1>Error 404")

  
          
                  