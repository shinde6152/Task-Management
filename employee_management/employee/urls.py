from django.urls import path
from .views.auth.auth import login,signup,logout
from .views.admin.dashboard import admin_dashboard
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

    # -------------------- AUTH --------------------
    path("", login, name="login"),
    path("logout/", logout, name="logout"),
    path("signup/", signup, name="signup"),

    # -------------------- ADMINISTRATOR --------------------
    path("administrator/dashboard/", administrator_dashboard, name="administrator_dashboard"),
    path("administrator/profile/", administrator_profile, name="administrator_profile"),
    path("administrator/companies/", administrator_companies, name="administrator_companies"),
    path("administrator/users/", administrator_users, name="administrator_users"),

    # -------------------- ADMIN --------------------
    path("app-admin/dashboard/", admin_dashboard, name="admin_dashboard"),
    path("app-admin/profile/", admin_profile, name="admin_profile"),
    path("app-admin/task/", admin_task, name="admin_task"),
    path("app-admin/users/", admin_user, name="admin_user"),

    # -------------------- MANAGER --------------------
    path("manager/dashboard/", manager_dashboard, name="manager_dashboard"),
    path("manager/tasks/", manager_tasks, name="manager_tasks"),
    path("manager/team/", manager_team, name="manager_team"),

    # -------------------- USER --------------------
    path("user/dashboard/", user_dashboard, name="user_dashboard"),
    path("user/profile/", user_profile, name="user_profile"),
    path("user/task/", user_task, name="user_task"),
]
