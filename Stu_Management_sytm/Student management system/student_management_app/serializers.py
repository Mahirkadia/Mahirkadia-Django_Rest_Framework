# student_management_app/serializers.py
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = CustomUser(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'user_type']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            user_type=validated_data.get('user_type', 3)  # Default to Student
        )
        return user

class AdminSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    
    class Meta:
        model = AdminHOD
        fields = ['id', 'admin', 'created_at', 'updated_at']

class StaffSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    
    class Meta:
        model = Staffs
        fields = ['id', 'admin', 'address', 'created_at', 'updated_at']

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials")
        else:
            raise serializers.ValidationError("Both username and password are required")

        attrs['user'] = user
        return attrs
class StudentSerializer(serializers.ModelSerializer):
    admin = UserSerializer(read_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    
    class Meta:
        model = Students
        fields = ['id', 'admin', 'gender', 'profile_pic', 'address', 'course_id', 'session_year_id', 
                 'username', 'email', 'password', 'first_name', 'last_name']
    
    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    
    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
        
    def create(self, validated_data):
        # Extract user data
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        
        try:
            # Create user with student type (3)
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                user_type=3
            )
            
            # Create student with the user as admin
            student = Students.objects.create(admin=user, **validated_data)
            return student
        except Exception as e:
            # If user was created but student creation failed, delete the user to avoid orphaned users
            if 'user' in locals():
                user.delete()
            raise serializers.ValidationError(str(e))

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'course_name', 'created_at', 'updated_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'subject_name', 'course_id', 'staff_id', 'created_at', 'updated_at']

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = ['id', 'student_id', 'subject_id', 'subject_exam_marks', 'subject_assignment_marks']
class SessionYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionYearModel
        fields = ['id', 'session_start_year', 'session_end_year']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'subject_id', 'attendance_date', 'session_year_id']

class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = ['id', 'student_id', 'attendance_id', 'status']  # Include 'status' field

class LeaveReportStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStudent
        fields = ['id', 'student_id', 'leave_date', 'leave_message', 'leave_status']

class LeaveReportStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveReportStaff
        fields = ['id', 'staff_id', 'leave_date', 'leave_message', 'leave_status']

class FeedbackStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStudent
        fields = ['id', 'student_id', 'feedback', 'feedback_reply']
class FeedbackStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackStaffs
        fields = ['id', 'staff_id', 'feedback', 'feedback_reply']

class NotificationStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStudent
        fields = ['id', 'student_id', 'message']

class NotificationStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationStaffs
        fields = ['id', 'stafff_id', 'message']

class StudentResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentResult
        fields = ['id', 'student_id', 'subject_id', 'subject_exam_marks', 'subject_assignment_marks']

