from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Admin_Registration,User_Registration,News_Feed,Saved_Feed

def feed(  ):
                
                  

                        
                            all_feeds = News_Feed.objects.all()
                            data = []
                            for ins in all_feeds:
                                print(ins)  
                                feed_data = {
                                   'username': ins.username,
                                     'content': ins.content,
                                     'feed_id':ins,
                                     }
                                data.append(feed_data)
                            return data






def home(request):
    
    return render(request, 'Home.html' )


def RegisterAs(request):
    return render(request, 'RegisterAs.html')

def About(request):
    return render(request, 'About.html')

def Contact(request):
    return render(request, 'Contact.html')

def Login(request):
    return render(request, 'Login.html')

#Login Verification
def Login_Submmission(request):
    if request.method == 'POST':
        getusername=request.POST['username']
        getpassword=request.POST['password']
        getuser_type=request.POST['user_type']
       # print("Done")

        if(getuser_type=='Admin'):  
             user = Admin_Registration.objects.get(username=getusername)
        #     print(user.username)
        #     print(getusername)
        #     print(user.password)
        #     print(getpassword)
             if(getusername == user.username and getpassword == user.password):
         #           print("Done")
                    request.session['username'] = getusername 
                    sesssion_username = request.session.get('username')
                    val=feed()
                    user = Admin_Registration.objects.get(username=sesssion_username)
        #            print(user.name)
                    return render(request, 'admin_index.html',{'data': val,'name':user.name})
        if(getuser_type=='User'):
             user = User_Registration.objects.get(username=getusername)
        #     print(user)
             if(getusername == user.username and getpassword == user.password):
        #            print("Done")
                    request.session['username'] = getusername 
                    sesssion_username = request.session.get('username')
                    val=feed()
        #            print(val)
                    user = User_Registration.objects.get(username=sesssion_username)
        #            print(user.name)
                    return render(request, 'user_index.html',{'data': val,'name':user.name})

def User_Register(request):
    return render(request, 'User_Register.html')

def Admin_Register(request):
    return render(request, 'Admin_Register.html')

def admin_register_submit(request):
    if request.method == 'POST':
            name=request.POST['name']
            mobile=request.POST['mobile']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            adm_obj=Admin_Registration(name=name,mobile=mobile,email=email,username=username,password=password)
            adm_obj.save()
            return render( request,"After_Registration.html")



def user_register_submit(request):
    if request.method == 'POST':
            name=request.POST['name']
            mobile=request.POST['mobile']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            adm_obj=User_Registration(name=name,mobile=mobile,email=email,username=username,password=password)
            adm_obj.save()
            return render( request,"After_Registration.html")


def feed_post(request):
     if request.method =='POST':
        print("Hello")
        sesssion_username = request.session.get('username')
        st_register_username = Admin_Registration.objects.get(username=sesssion_username)     
        feed_content =request.POST['feed_content']
        ques_obj=News_Feed(username= st_register_username, content=feed_content)
        ques_obj.save()        
        print("Done")
        val=feed()  
        print(val)
        user = Admin_Registration.objects.get(username=sesssion_username)
        return render(request, 'admin_index.html',{'data':val,'name':user.name})
        



def Already_Saved(request):
     return render(request,'Already_Saved.html')


def Save_Item(request,feed_id):
     
     if request.method=='POST':
          sesssion_username = request.session.get('username')
          log_obj=User_Registration.objects.get(username=sesssion_username)
          print(feed_id)    

          split_string = feed_id.split()
          number = split_string[-1].strip('()')
          #print(number)
          feed_obj=News_Feed.objects.get(Feed_Id=number)
          
          #print(log_obj)
          #print(feed_obj.Feed_Id)
          #print(log_obj.username)


          sa_feed_obj=Saved_Feed.objects.filter(username=log_obj)
          
          #print(sa_feed_obj)
          for ins in sa_feed_obj:
             if ins.username == log_obj and ins.Feed_Id == feed_obj:
                  print("Matched")
                  return render(request,'Already_Saved.html')
             
             
          save_obj=Saved_Feed(username=log_obj,Feed_Id=feed_obj)
          save_obj.save()

          
          
          val=feed()
          #print(val)
          user = User_Registration.objects.get(username=sesssion_username)
          #print(user.name)
          return render(request, 'user_index.html',{'data': val,'name':user.name})
          











def Saved_Items_List(request):
    #print("Hello")
    sesssion_username = request.session.get('username')
    print(sesssion_username)
    log_obj=User_Registration.objects.get(username=sesssion_username)
    sa_feed_obj=Saved_Feed.objects.filter(username=log_obj)
    #print("Hello")
    print(sa_feed_obj)

    fee=[]
    for ins in sa_feed_obj:
         print(ins.Feed_Id)
         fee.append(ins.Feed_Id)
    print(fee)
      
    def feed():
                        allfeed = News_Feed.objects.all()
                        data = []
                        for val in allfeed :
                            #print(val)
                            if val in fee:
                              print("it's Here")
                              #print(val)

                              #print(ins.id)
                              feed_data = {
                                   'username': val.username,
                                     'content':val.content,
                                     'feed_id':val}
                              
                              data.append(feed_data)
                        return data
    val=feed()
    print(val)







    return render(request, 'user_index.html', {'data': val}) 


