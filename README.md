# 🛠 WP Info - أداة لجلب معلومات مستخدمي WordPress عبر REST API

## 🔍 نظرة عامة
**WP Info** هي أداة قوية بلغة **Python** لاختبار الأمان واستخراج بيانات مستخدمي **WordPress** عبر `wp-json/wp/v2/users`.  
تعتمد الأداة على **REST API** وتتيح جمع بيانات المستخدمين المسجلين في الموقع بسهولة.  

## 🚀 المميزات  
✅ التحقق مما إذا كان الموقع يستخدم WordPress.  
✅ استخراج معرفات وأسماء المستخدمين وروابطهم.  
✅ دعم **عدة مواقع دفعة واحدة** باستخدام `ThreadPoolExecutor`.  
✅ حفظ البيانات تلقائيًا في **ملف CSV**.  
✅ **عرض النتائج بطريقة منظمة** مع `tqdm` لمؤشر التقدم.  
✅ تجنب الحظر عبر **اختيار User-Agent عشوائي**.  

## 📌 المتطلبات  
قبل تشغيل الأداة، قم بتثبيت المتطلبات عبر `pip`:
```bash
pip install requests pyfiglet tqdm
# فتح كتلة جديدة
echo "Hello, World!"
