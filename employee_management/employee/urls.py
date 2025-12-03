from django.urls import path
from .views.auth.auth import login
from .views.auth.auth import signup
from .views.admin.dashboard import admin_dasboard
from .views.admin.profile import admin_profile
from .views.admin.task import admin_task
from .views.admin.user import admin_user
from .views.administrator.companies import administrator_companies
from .views.administrator.dashboard import administrator_dashboard
from .views.administrator.profiles import administrator_profile
from .views.administrator.users import administrator_users
from .views.manager.dashboard import manager_dashboard
from .views.manager.task import manager_tasks
from .views.manager.team import manager_team
from .views.users.dashboard import user_dashboard
from .views.users.profile import user_profile
from .views.users.task import user_task


urlpatterns = [
    # Auth
    path('', login, name="login"),
    path('/signup', signup, name='signup'),

    # Admin
    path('admin_dashboard', admin_dasboard, name='admin_dasboard'),
    path('admin_profile', admin_profile, name='admin_profile'),
    path('admin_task', admin_task, name='admin_task'),
    path('admin_user', admin_user, name='admin_user'),

    # Administrator
    path('adminstrator_companies', administrator_companies, name='administrator_companies'),
    path('administrator_dashboard', administrator_dashboard, name='administrator_dashboard'),
    path('administrator_profile', administrator_profile, name='administrator_profile'),
    path('administrator_users', administrator_users, name='administrator_users'),

    # Manager
    path('manager_dashboard', manager_dashboard, name='manager_dashboard'),
    path('manager_tasks', manager_tasks, name='manager_tasks'),
    path('manager_team', manager_team, name='manager_team'),

    # users
    path('user_dashboard', user_dashboard, name='user_dashboard'),
    path('user_profile', user_profile, name='user_profile'),
    path('user_task', user_task, name='user_task')
]
