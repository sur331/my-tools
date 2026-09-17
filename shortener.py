import urllib.request
import urllib.parse
import os

def shorten_link(long_url):
    # استخدام خدمة مجانية ومفتوحة لا تحتاج إلى حساب مفاتيح
    base_url = "https://is.gd"
    try:
        full_url = base_url + urllib.parse.quote(long_url.strip())
        with urllib.request.urlopen(full_url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return f"Error: {e}"

# 1. قراءة الروابط الطويلة من الملف النصي
if os.path.exists("links_to_shorten.txt"):
    with open("links_to_shorten.txt", "r") as f:
        urls = f.readlines()
    
    # 2. اختصار الروابط وحفظ النتيجة
    output_content = "--- قائمة الروابط المقتصرة بواسطة بايثون ---\n"
    for url in urls:
        if url.strip():
            print(f"جاري معالجة: {url.strip()}")
            short = shorten_link(url)
            output_content += f"الأصلي: {url.strip()} -> القصير: {short}\n"
            
    # 3. كتابة النتيجة في ملف جديد
    with open("shortened_results.txt", "w", encoding="utf-8") as f:
        f.write(output_content)
    print("تم الانتهاء بنجاح وحفظ النتائج!")
else:
    print("الملف links_to_shorten.txt غير موجود. يرجى إنشاؤه ووضع الروابط بداخله.")
