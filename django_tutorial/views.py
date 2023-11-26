from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, 'base.html')
def Services(request):
    return render(request, 'Services.html')
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'About-Us.html')
def Intro(request):
    return render(request, 'Intro.html')
def Get_Started(request):
    return render(request, 'Get_Started.html')
def Install_Django(request):
    return render(request, 'Install_Django.html')
def Create_Project(request):
    return render(request, 'Create_Project.html')
def Create_App(request):
    return render(request, 'Create_App.html')
def View(request):
    return render(request, 'View.html')
def URLs(request):
    return render(request, 'URLs.html')
def Templates(request):
    return render(request, 'Templates.html')
def Models(request):
    return render(request, 'Models.html')
def Insert_Data(request):
    return render(request, 'Insert_Data.html')
def Update_Data(request):
    return render(request, 'Update_Data.html')
def Delete_Data(request):
    return render(request, 'Delete_Data.html')
def Update_Model(request):
    return render(request, 'Update_Model.html')
def Template_404(request):
    return render(request, '404_Template.html')
def File_Upload(request):
    return render(request, 'File_Upload.html')
def Admin(request):
    return render(request, 'Admin.html')
def Create_Superuser(request):
    return render(request, 'Create_Superuser.html')
def Include_Models(request):
    return render(request, 'Include_Models.html')
def Set_List_Display(request):
    return render(request, 'Set_List_Display.html')
def Update_Members(request):
    return render(request, 'Update_Members.html')
def Add_Members(request):
    return render(request, 'Add_Members.html')
def Delete_Members(request):
    return render(request, 'Delete_Members.html')
def Cookies_Handling(request):
    return render(request, 'Cookies_Handling.html')
def Variables(request):
    return render(request, 'Variables.html')
def Tags(request):
    return render(request,'Tags.html')
def If_Else(request):
    return render(request,'If_Else.html')
def For_Loop(request):
    return render(request,'For_Loop.html')
def Comment(request):
    return render(request,'Comment.html')
def Include(request):
    return render(request,'Include.html')
def Form(request):
    return render(request,'Form.html')
def Add_Static_Files(request):
    return render(request,'Add_Static_Files.html')
def Add_Slug_Field(request):
    return render(request, 'Add_Slug_Field.html')
def Add_Bootstrap_5(request):
    return render(request, 'Add_Bootstrap_5.html')
def Database_Connect(request):
    return render(request, 'Database_Connect.html')