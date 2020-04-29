from .forms import UserRegistrationForm, ProfileRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import NumericPasswordValidator

class UserServices:
    def postRegisterUser(self, request):
        """method for register user and his profile in db, where data - inputed data from user"""

        userForm = UserRegistrationForm(request.POST)
        profileForm = ProfileRegistrationForm(request.POST)
        newUser = None
        if userForm.is_valid() and profileForm.is_valid():
            newUser = userForm.save(commit=False)
            newUser.set_password(userForm.cleaned_data['password'])
            newUser.save()
            
            newProfile = profileForm.save(commit=False)
            newProfile.user = newUser
            if newProfile.isLecturer:
                newProfile.group = None
            else:
                newProfile.faculty = None
                newProfile.cathedra = None
            newProfile.save()
            
        return (newUser, userForm, profileForm,)


    def getRegisterUser(self):
        return (UserRegistrationForm(), ProfileRegistrationForm())


    def getEditUser(self, request):
        """method for rendering user profile page"""

        userForm = UserEditForm(instance=request.user)
        profileForm = ProfileEditForm(instance=request.user.profile)
        return (userForm, profileForm)


    def postEditUser(self, request):
        """method for edit user profile, which based on inputed data from user."""

        userForm = UserEditForm(instance=request.user, data=request.POST)
        profileForm = ProfileEditForm(instance=request.user.profile, data=request.POST)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
        else:
            with open('file.txt', 'w', encoding='utf-8') as file:
                print(f'not valid', file=file)

    
    def getUserByUsername(self, username):
        """method that return user object, if user with username exists in database"""
        try:
            return User.objects.get(username=username)
        except:
            return None


    def checkIsUsernameAvailable(self, username):
        """checked is transferable username in database"""

        return User.objects.filter(username__iexact=username).exists()


    def checkIsEmailAvailable(self, email):
        """checked is transferable email in database"""

        return User.objects.filter(email=email).exists()


    def checkIsEmailAvailableForExistUser(self, email, user):
        exist = User.objects.filter(email=email).exists()
        if exist:
            return email != user.email
        else:
            return exist
