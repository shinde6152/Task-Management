from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from ...models.user import user

def administrator_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('/')

    try:
        user_obj = user.objects.get(id=user_id)

    except ObjectDoesNotExist:
        # User deleted from database → logout
        return redirect('/')

    except Exception as e:
        # Other errors (debug)
        print("Profile Error:", e)
        return redirect('/')

    profile_details = {
        'user_id': user_obj.id,
        'name': user_obj.name,
        'email': user_obj.email,
        'phone': user_obj.phone,
        'role': user_obj.role
    }

    return render(request, 'administrator/profile.html', {
        "profile_details": profile_details
    })


def administrator_updateprofile(request):
    
    return redirect("administrator_profile")