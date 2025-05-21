# student_management_app/api_views.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import (CustomUser, AdminHOD, Staffs, Students, Courses, Subjects, 
                    Attendance, AttendanceReport, LeaveReportStudent, LeaveReportStaff,
                    FeedBackStudent, FeedBackStaffs, StudentResult)
from .serializers import *

# Custom permissions
class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == '1'

class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == '2'

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == '3'

# Login API View
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self,request):
        user = CustomUser.objects.all()
        serializers = LoginSerializer(user,many=True)
        return Response(serializers.data)
    
    def post(self, request):
        print("Login request received:", request.data)
        email = request.data.get('email')
        password = request.data.get('password')
        if not password:
            return Response({'error': 'Password is required'}, status=status.HTTP_400_BAD_REQUEST)
        if not email :
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            if email:
                user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user_type': user.user_type,
                    'user_id': user.id
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
# ADD Staff API VIew
class AddStaffAPIView(APIView):
    def get(self, request):
        staffs = Staffs.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Add Course API View
class AddCourseAPIView(APIView):
    def get(self, request):
        courses = Courses.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    def put(self,request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Add Stubject APIview 
class AddSubjectAPIView(APIView):
    def get(self, request):
        subjects = Subjects.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# Add Session APIView
class AddSessionAPIView(APIView):
    def get(self, request):
        sesstions = SessionYearModel.objects.all()
        serializer = SessionYearSerializer(sesstions, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SessionYearSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# Add Student APIView
class AddStudentAPIView(APIView):
    def get(self, request):
        stu = Students.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# Attendence API View
class AttendenceAPIView(APIView):
    def get(self, request):
        attendances = Attendance.objects.all()
        serializer = AttendanceSerializer(attendances, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
    
# Attedence Report API
class AttendenceReportAPIView(APIView):
    def get(self, request):
        attend_report = AttendanceReport.objects.all()
        serializer = AttendanceReportSerializer(attend_report, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = AttendanceReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )

# Leave Report Student API
class LeaveReportStudentAPIView(APIView):
    def get(self, request):
        leave_report = LeaveReportStudent.objects.all()
        serializer = LeaveReportStudentSerializer(leave_report, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LeaveReportStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# Leave Report Staff APIView
class LeaveReportStaffAPIView(APIView):
    def get(self, request):
        leave_repo_staff = LeaveReportStaff.objects.all()
        serializer = LeaveReportStaffSerializer(leave_repo_staff, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = LeaveReportStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# Feedback Student API View
class FeedBackStudentAPIView(APIView):
    def get(self, request):
        feedbackstu = FeedBackStudent.objects.all()
        serializer = FeedbackStudentSerializer(feedbackstu, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FeedbackStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# FeedBack Staff API View
class FeedBackStaffAPIView(APIView):
    def get(self, request):
        feedbackstaff = FeedBackStaffs.objects.all()
        serializer = FeedbackStaffSerializer(feedbackstaff, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = FeedbackStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )

# Notification Student APIVIew
class NotificationStuAPIView(APIView):
    def get(self, request):
        noti_stu = NotificationStudent.objects.all()
        serializer = NotificationStudentSerializer(noti_stu,many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = NotificationStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
    
# Notification Staff APIView
class NotificationStaffAPIView(APIView):
    def get(self, request):
        noti_staff = NotificationStaffs.objects.all()
        serializer = NotificationStaffSerializer(noti_staff, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = NotificationStaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )

# Student Result APIVIEW
class StudentResultAPIView(APIView):
    def get(self, request):
        students = StudentResult.objects.all()
        serializer = StudentResultSerializer(students, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = StudentResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request):
        user = request.user
        serializer = StudentResultSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
# User API View
class UserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Admin viewset
class AdminViewSet(viewsets.ModelViewSet):
    serializer_class = AdminSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def get_queryset(self):
        return AdminHOD.objects.all()

# Staff viewset
class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == '1':  # Admin/HOD
            return Staffs.objects.all()
        elif user.user_type == '2':  # Staff
            return Staffs.objects.filter(admin=user)
        return Staffs.objects.none()

# Student viewset
class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == '1':  # Admin/HOD
            return Students.objects.all()
        elif user.user_type == '2':  # Staff
            # Staff can see all students
            return Students.objects.all()
        elif user.user_type == '3':  # Student
            return Students.objects.filter(admin=user)
        return Students.objects.none()

# Course viewset
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

# Subject viewset
class SubjectViewSet(viewsets.ModelViewSet):
    serializer_class = SubjectSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == '1':  # Admin/HOD
            return Subjects.objects.all()
        elif user.user_type == '2':  # Staff
            return Subjects.objects.filter(staff_id=user)
        elif user.user_type == '3':  # Student
            try:
                student = Students.objects.get(admin=user)
                return Subjects.objects.filter(course_id=student.course_id)
            except Students.DoesNotExist:
                return Subjects.objects.none()
        return Subjects.objects.none()

# Student Result viewset
class StudentResultViewSet(viewsets.ModelViewSet):
    serializer_class = StudentResultSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated, IsAdmin | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == '1':  # Admin/HOD
            return StudentResult.objects.all()
        elif user.user_type == '2':  # Staff
            # Staff can see results for subjects they teach
            return StudentResult.objects.filter(subject_id__staff_id=user)
        elif user.user_type == '3':  # Student
            try:
                student = Students.objects.get(admin=user)
                return StudentResult.objects.filter(student_id=student)
            except Students.DoesNotExist:
                return StudentResult.objects.none()
        return StudentResult.objects.none()


