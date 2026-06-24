import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
student = {'rollno': 1, 'name': 'naresh', 'course': 'Y'}
student_marks = {'rollno': 1, 'sub1': 40, 'sub2': 50}

def display_student(request):
    output = f'''<HTML>
    <BODY>
    <TABLE BORDER="1" WIDTH=50%>
    <TR>
    <TH>ROLLNO</TH>
    <TH>NAME</TH>
    <TH>COURSE</TH>
    </TR>
    <TR>
    <TD>{student['rollno']}</TD>
    <TD>{student['name']}</TD>
    <TD>{student['course']}</TD>
    </TR>
    </TABLE>
    </BODY></HTML>'''
    response = HttpResponse(output)
    return response

def find_result(request):
    # Fixed: Kept the ternary operator on a single line
    result = "PASS" if student_marks['sub1'] >= 40 and student_marks['sub2'] >= 40 else "FAIL"
    
    output = f'''
<HTML>
<BODY>
<P>Rollno:{student_marks['rollno']}<br>
Subject1:{student_marks['sub1']}<br>
Subject2:{student_marks['sub2']}<br>
Result:{result}</P>
</BODY>
</HTML>'''
    response = HttpResponse(output)
    return response

def home(request):
    dt = datetime.datetime.today()
    t = dt.time()
    h = t.hour
    
    if h >= 5 and h < 12:
        msg = "Good Morning"
    elif h >= 12 and h < 17:
        msg = "Good Afternoon"
    else:
        msg = "Good Evening"
  
    output = f'''
<html>
<body>
<h3>{msg}, welcome to my application</h3>
</body>
</html>'''
    response = HttpResponse(output)
    return response