from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .import HodViews, StaffViews, StudentViews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from . import api_views
from django.views.decorators.csrf import csrf_exempt
# Create a router for API views
router = DefaultRouter()
router.register(r'admins', api_views.AdminViewSet, basename='admin')
router.register(r'staffs', api_views.StaffViewSet, basename='staff')
router.register(r'students', api_views.StudentViewSet, basename='student')
router.register(r'courses', api_views.CourseViewSet, basename='course')
router.register(r'subjects', api_views.SubjectViewSet, basename='subject')
router.register(r'results', api_views.StudentResultViewSet, basename='result')

urlpatterns = [
    path('', csrf_exempt(views.loginPage), name="login"),
    path('doLogin/',csrf_exempt (views.doLogin), name="doLogin"),
    path('get_user_details/', csrf_exempt(views.get_user_details), name="get_user_details"),
    path('logout_user/', csrf_exempt(views.logout_user), name="logout_user"),
    path('admin_home/', csrf_exempt(HodViews.admin_home), name="admin_home"),
    
    path('add_staff/', csrf_exempt(HodViews.add_staff), name="add_staff"),
    path('add_staff_save/', csrf_exempt(HodViews.add_staff_save), name="add_staff_save"),
    path('manage_staff/', csrf_exempt(HodViews.manage_staff), name="manage_staff"),
    path('edit_staff/<staff_id>/',csrf_exempt( HodViews.edit_staff), name="edit_staff"),
    path('edit_staff_save/', csrf_exempt(HodViews.edit_staff_save), name="edit_staff_save"),
    path('delete_staff/<staff_id>/', csrf_exempt(HodViews.delete_staff), name="delete_staff"),
    path('add_course/', csrf_exempt(HodViews.add_course), name="add_course"),
    path('add_course_save/', csrf_exempt(HodViews.add_course_save), name="add_course_save"),
    path('manage_course/', csrf_exempt(HodViews.manage_course), name="manage_course"),
    path('edit_course/<course_id>/', csrf_exempt(HodViews.edit_course), name="edit_course"),
    path('edit_course_save/', csrf_exempt(HodViews.edit_course_save), name="edit_course_save"),
    path('delete_course/<course_id>/',csrf_exempt( HodViews.delete_course), name="delete_course"),
    path('manage_session/', csrf_exempt(HodViews.manage_session), name="manage_session"),
    path('add_session/', csrf_exempt(HodViews.add_session), name="add_session"),
    path('add_session_save/', csrf_exempt(HodViews.add_session_save), name="add_session_save"),
    path('edit_session/<session_id>', csrf_exempt(HodViews.edit_session), name="edit_session"),
    path('edit_session_save/', csrf_exempt(HodViews.edit_session_save), name="edit_session_save"),
    path('delete_session/<session_id>/', csrf_exempt(HodViews.delete_session), name="delete_session"),
    path('add_student/', csrf_exempt(HodViews.add_student), name="add_student"),
    path('add_student_save/', csrf_exempt(HodViews.add_student_save), name="add_student_save"),
    path('edit_student/<student_id>', csrf_exempt(HodViews.edit_student), name="edit_student"),
    path('edit_student_save/', csrf_exempt(HodViews.edit_student_save), name="edit_student_save"),
    path('manage_student/',csrf_exempt(HodViews.manage_student), name="manage_student"),
    path('delete_student/<student_id>/', csrf_exempt(HodViews.delete_student), name="delete_student"),
    path('add_subject/', csrf_exempt(HodViews.add_subject), name="add_subject"),
    path('add_subject_save/', csrf_exempt(HodViews.add_subject_save), name="add_subject_save"),
    path('manage_subject/', csrf_exempt(HodViews.manage_subject), name="manage_subject"),
    path('edit_subject/<subject_id>/',csrf_exempt(HodViews.edit_subject), name="edit_subject"),
    path('edit_subject_save/',csrf_exempt( HodViews.edit_subject_save), name="edit_subject_save"),
    path('delete_subject/<subject_id>/', csrf_exempt(HodViews.delete_subject), name="delete_subject"),
    path('check_email_exist/', csrf_exempt(HodViews.check_email_exist), name="check_email_exist"),
    path('check_username_exist/', csrf_exempt(HodViews.check_username_exist), name="check_username_exist"),
    path('student_feedback_message/', csrf_exempt(HodViews.student_feedback_message), name="student_feedback_message"),
    path('student_feedback_message_reply/',csrf_exempt( HodViews.student_feedback_message_reply), name="student_feedback_message_reply"),
    path('staff_feedback_message/', csrf_exempt(HodViews.staff_feedback_message), name="staff_feedback_message"),
    path('staff_feedback_message_reply/', csrf_exempt(HodViews.staff_feedback_message_reply), name="staff_feedback_message_reply"),
    path('student_leave_view/', csrf_exempt(HodViews.student_leave_view), name="student_leave_view"),
   path('student_leave_approve/<leave_id>/', csrf_exempt(HodViews.student_leave_approve), name="student_leave_approve"),
    path('student_leave_reject/<leave_id>/', csrf_exempt(HodViews.student_leave_reject), name="student_leave_reject"),
    path('staff_leave_view/', csrf_exempt(HodViews.staff_leave_view), name="staff_leave_view"),
    path('staff_leave_approve/<leave_id>/', csrf_exempt(HodViews.staff_leave_approve), name="staff_leave_approve"),
    path('staff_leave_reject/<leave_id>/', csrf_exempt(HodViews.staff_leave_reject), name="staff_leave_reject"),
    path('admin_view_attendance/',csrf_exempt( HodViews.admin_view_attendance), name="admin_view_attendance"),
    path('admin_get_attendance_dates/', csrf_exempt(HodViews.admin_get_attendance_dates), name="admin_get_attendance_dates"),
    path('admin_get_attendance_student/', csrf_exempt(HodViews.admin_get_attendance_student), name="admin_get_attendance_student"),
    path('admin_profile/', csrf_exempt(HodViews.admin_profile), name="admin_profile"),
    path('admin_profile_update/', csrf_exempt(HodViews.admin_profile_update), name="admin_profile_update"),
 


    # URLS for Staff
    path('staff_home/', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance/', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', StaffViews.get_students, name="get_students"),
    path('save_attendance_data/', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('update_attendance_data/', StaffViews.update_attendance_data, name="update_attendance_data"),
    path('staff_apply_leave/', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save/', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback/', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save/', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile/', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_update/', StaffViews.staff_profile_update, name="staff_profile_update"),
    path('staff_add_result/', StaffViews.staff_add_result, name="staff_add_result"),
    path('staff_add_result_save/', StaffViews.staff_add_result_save, name="staff_add_result_save"),

    # URSL for Student
    path('student_home/', StudentViews.student_home, name="student_home"),
    path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave/', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save/', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback/', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile/', StudentViews.student_profile, name="student_profile"),
    path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
    path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),
    
    # API URLs
    path('api/', include(router.urls)),
    path('api/login/', api_views.LoginAPIView.as_view(), name='api_login'),
    path('api/add_staff/',api_views.AddStaffAPIView.as_view(), name='api_add_staff'),
    path('api/add_course/', api_views.AddCourseAPIView.as_view(), name='api_add_course'),
    path('api/add_subject/',api_views.AddSubjectAPIView.as_view(), name='api_add_subject' ),
    path('api/add_session/', api_views.AddSessionAPIView.as_view(), name='api_add_session'),
    path('api/add_student/', api_views.AddStudentAPIView.as_view(), name='api_add_student'),
    path('api/api_attedence/', api_views.AttendenceAPIView.as_view(), name='api_add_attendance'),
    path('api/api_attedence_report/', api_views.AttendenceReportAPIView.as_view(), name='api_add_attendance_report'),
    path('api/api_leave_report_stu/',api_views.LeaveReportStudentAPIView.as_view(),name='leave_report_stu'),
    path('api_leave_report_staff/', api_views.LeaveReportStaffAPIView.as_view(), name='leave_report_staff'),
    path('api_feedback_staff/', api_views.FeedBackStaffAPIView.as_view(), name='api_feedback_staff'),
    path('api_feedback_student/', api_views.FeedBackStudentAPIView.as_view(), name='api_feedback_student'),
    path('api_notification_stu/',api_views.NotificationStuAPIView.as_view(), name='api_notification_stu'),
    path('api_notification_staff/',api_views.NotificationStaffAPIView.as_view(), name='api_notification_staff'),
    path('api_result/', api_views.StudentResultAPIView.as_view(), name='api_result'),
    path('api/user/', api_views.UserAPIView.as_view(), name='api_user_details'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
