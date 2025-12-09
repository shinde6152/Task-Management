from django.shortcuts import redirect

class RoleAccessMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        path = request.path
        role = request.session.get("user_role")

        # ============================
        # 1️⃣ PUBLIC PAGES (NO LOGIN REQUIRED)
        # ============================
        PUBLIC_PATHS = ["/", "/signup/"]
        if path in PUBLIC_PATHS:
            return self.get_response(request)

        # ============================
        # 2️⃣ NOT LOGGED IN → SEND TO LOGIN
        # ============================
        if not role:
            return redirect("/")

        # ============================
        # 3️⃣ ROLE → URL PREFIX MAPPING
        # ============================
        ROLE_PREFIX = {
            "administrator": "/administrator/",
            "admin": "/app-admin/",
            "manager": "/manager/",
            "user": "/user/",
        }

        # ============================
        # 4️⃣ ROLE → DASHBOARD REDIRECT
        # ============================
        ROLE_DASHBOARD = {
            "administrator": "administrator_dashboard",
            "admin": "admin_dashboard",
            "manager": "manager_dashboard",
            "user": "user_dashboard",
        }

        # ============================
        # 5️⃣ CHECK IF USER TRYING TO ACCESS OTHER ROLE PAGE
        # ============================
        for required_role, prefix in ROLE_PREFIX.items():

            if path.startswith(prefix):   # example: "/app-admin/users/"
                if role != required_role: # wrong role trying to access
                    return redirect(ROLE_DASHBOARD[role])

        # Allow the request
        return self.get_response(request)
