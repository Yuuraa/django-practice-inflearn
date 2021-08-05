from django.contrib.auth.forms import UserCreationForm

class PasswordUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True # 비밀번호를 변경하므로 사용자 이름은 고정시킴