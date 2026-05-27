from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from DjangoApp.forms import TaskForm, ProfileForm
from .models import Task, UserProfile


def is_admin(user):
    return user.userprofile.role == 'Manager'

def home(request):
    return render(request, 'djApp/Home.html')

@user_passes_test(is_admin)
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.team = request.user.userprofile.team
            form.save()
            return redirect('allTask')
    else:
        form = TaskForm(initial={'team': request.user.userprofile.team})
    return render(request, 'task/task_form.html', {'form': form,'team':request.user.userprofile.team})

@user_passes_test(is_admin)
def delete_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        task.delete()
        return redirect('allTask')
    return render(request, 'task/confirm_delete.html', {'task': task})

@user_passes_test(is_admin)
def update_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('allTask')
    else:
        form = TaskForm(instance=task)
        return render(request, 'task/task_form.html', {'form': form})


@login_required
def allTask(request):
    user_profile = request.user.userprofile
   # if user_profile.role == 'Manager':
     #   tasks = Task.objects.all()
   # else:
    tasks = Task.objects.filter(team=user_profile.team)
    
    # Apply filters
    status_filter = request.GET.get('status', '')
    performer_filter = request.GET.get('performer', '')
    
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    if performer_filter:
        tasks = tasks.filter(performer__username__icontains=performer_filter)
    
    # Get unique statuses and performers for filter options
    all_statuses = Task.objects.filter(team=user_profile.team).values_list('status', flat=True).distinct()
    all_performers = Task.objects.filter(team=user_profile.team).values_list('performer__username', flat=True).distinct()
    
    return render(request, 'task/task_list.html', {
        'tasks': tasks,
        'statuses': all_statuses,
        'performers': sorted([p for p in all_performers if p]),
        'selected_status': status_filter,
        'selected_performer': performer_filter
    })

#REGISTER
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after register
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "auth/Register.html", {"form": form})


@login_required
def profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('allTask')
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'auth/Profile.html', {'form': form})

@login_required
def myTasks(request):
    tasks = Task.objects.filter(performer=request.user)
    return render(request, 'task/MyTasks.html', {'tasks': tasks})

@login_required
def assign_task(request, id):
    task = get_object_or_404(Task, pk=id)
    if not task.performer:
        task.performer = request.user
        task.status = 'In_Progress'
        task.save()
    return redirect('allTask')

@login_required
def update_status(request, id):
    task = get_object_or_404(Task, pk=id)
    if task.performer != request.user:
        return HttpResponse("אינך האחראי על משימה זו", status=403)
    if request.method == "POST":
        new_status = request.POST.get('status')
        if new_status in ['In_Progress', 'Completed']:
            task.status = new_status
            task.save()
            return redirect('allTask')
    return render(request, 'task/update_status.html', {'task': task})




@login_required
def create_profile(request, user_id):
    profile = get_object_or_404(UserProfile, user__id=user_id)

    if request.method == "POST":
        # העברת הנתונים מהטופס יחד עם האובייקט הקיים (instance)
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        # הצגת הטופס כשהוא כבר "מולא" בנתונים הקיימים של האובייקט
        form = ProfileForm(instance=profile)

    return render(request, "auth/Profile.html", {
        "form": form,
        "profile": profile
    })


# LOGIN
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "auth/Login.html", {"form": form})


# LOGOUT

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def setProfile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form = ProfileForm()
    return render(request, "auth/Profile.html", {"form": form})
