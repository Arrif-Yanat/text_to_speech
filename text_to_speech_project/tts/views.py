from django.shortcuts import render
from gtts import gTTS  # ใช้ Google Text-to-Speech แปลงข้อความเป็นเสียง
import os
from django.conf import settings
import uuid  # ใช้สร้างชื่อไฟล์ที่ไม่ซ้ำกัน

def index(request):
    audio = None  # ตัวแปรเก็บ URL ไฟล์เสียงที่ถูกสร้าง
    if request.method == "POST":  # เช็คว่าผู้ใช้กดปุ่ม submit หรือไม่
        text = request.POST.get('text')  # ดึงข้อความที่ผู้ใช้ป้อน
        if text:  # ตรวจสอบว่าผู้ใช้ไม่ได้ส่งข้อความว่าง
            unique_filename = f"{uuid.uuid4()}.mp3"  # สร้างชื่อไฟล์ไม่ซ้ำกัน
            filename = os.path.join(settings.MEDIA_ROOT, unique_filename)  # กำหนด path ที่จะเก็บไฟล์เสียง
            
            tts = gTTS(text=text, lang='th')  # แปลงข้อความเป็นเสียง (ภาษาไทย)
            tts.save(filename)  # บันทึกเป็นไฟล์ .mp3
            
            audio = os.path.join(settings.MEDIA_URL, unique_filename)  # สร้าง URL สำหรับไฟล์เสียง

    return render(request, 'tts/index.html', {'audio': audio})  
    # ส่ง URL ไฟล์เสียงกลับไปให้แสดงผลในหน้า HTML




