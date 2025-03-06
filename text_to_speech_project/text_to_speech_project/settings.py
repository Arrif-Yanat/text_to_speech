import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # หาตำแหน่งของโปรเจกต์

MEDIA_URL = '/media/'  # URL สำหรับเข้าถึงไฟล์มีเดีย เช่น mp3
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # โฟลเดอร์เก็บไฟล์เสียงจริง ๆ

SECRET_KEY = 'django-insecure-...'  # กุญแจลับ (ห้ามใช้ key นี้จริง)

DEBUG = True  # เปิดโหมด debug ระหว่างพัฒนา

ALLOWED_HOSTS = []  # โฮสต์ที่อนุญาตให้เข้าถึง

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tts',  # ลงทะเบียนแอป tts ที่สร้างขึ้น
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # ป้องกัน CSRF attack
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'text_to_speech_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'tts' / 'templates'],  # ตั้งค่าที่อยู่ของไฟล์ template
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'text_to_speech_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ตั้งค่าการเก็บไฟล์ static
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

