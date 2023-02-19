from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from dj.choices import Choice,Choices
from location_field.models.plain import PlainLocationField

# Create your models here.


        
class userman(BaseUserManager):
    def create_user(self, fname, lname,email,location,username, phone_number, password):
        if not phone_number:
            raise ValueError("users must have phone numbers")
        if not fname:
            raise ValueError("users must have a first name")
        if not lname:
            raise ValueError("users must have a last name")
        
        if not password:
            raise ValueError("users must have passwords")
        # if not gender:
        #     raise ValueError("users must have a  gender")
        

        user = self.model(
            email = self. normalize_email(email),
            fname = fname,
            lname = lname,
            phone_number = phone_number,
            username = username,
            location = location
            # gender = gender
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
        

class farmer(AbstractBaseUser):
    fname           = models.CharField(verbose_name="first name", null=False, blank=False, help_text="farmer's first name", max_length=20)
    lname           = models.CharField(verbose_name="last name", null=False, blank=False, help_text="farmer's last name", max_length=20)
    # gender          = models.CharField(verbose_name="gender",null=False, blank=False,help_text="patient's gender", max_length='6', choices=Gender(), default = Gender.male )
    username        = models.CharField(verbose_name="username", null=False, blank=True,unique=False, help_text="farmer's user name",max_length=50 )
    phone_regex     = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number    = models.CharField(verbose_name='phone number', validators=[phone_regex], max_length=17, unique=True, help_text="farmer's phone number")
    email           = models.EmailField(verbose_name="email",unique=True,blank=True,help_text="farmer's email")
    last_login      = models.DateTimeField(verbose_name="last login", auto_now=True)
    password        =models.CharField(verbose_name="password", null="false", max_length=100)
    is_active       =models.BooleanField(default=True)
    location        =PlainLocationField(verbose_name="location", null=False, blank=False, help_text="farmer's country",max_length=25)


    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['fname', 'lname', 'date_of_birth','password']

    objects = userman()