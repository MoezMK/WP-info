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
⚙️ كيفية الاستخدام
1️⃣ جلب بيانات موقع واحد
bash
نسخ
تحرير
python tool.py -u https://example.com
2️⃣ جلب بيانات عدة مواقع من ملف
bash
نسخ
تحرير
python tool.py -f urls.txt
📌 يجب أن يحتوي urls.txt على قائمة بالمواقع (كل موقع في سطر منفصل).

3️⃣ حفظ البيانات في ملف CSV
bash
نسخ
تحرير
python tool.py -u https://example.com -o output.csv
📜 مثال للإخراج
bash
نسخ
تحرير
Fetching data: 50% |██████████          | 2/4 
+----+----------------+----------------------------------+
| ID | Name          | Link                             |
+----+----------------+----------------------------------+
| 1  | Admin         | https://example.com/author/admin |
| 2  | Editor        | https://example.com/author/editor|
+----+----------------+----------------------------------+
📊 نظام البيانات
📌 البيانات التي تجمعها الأداة:
🔹 ID - معرف المستخدم الفريد في WordPress.
🔹 Name - اسم المستخدم الظاهر على الموقع.
🔹 Link - رابط صفحة المستخدم الشخصية.

📌 كيفية حفظ البيانات؟

يتم عرض البيانات مباشرة في سطر الأوامر (CLI).
يتم حفظها تلقائيًا في ملف CSV عند تحديد خيار -o.
📌 الأمان والخصوصية

تعتمد الأداة على بيانات REST API المتاحة للعامة ولا تستغل أي ثغرات.
يجب الحصول على إذن قبل استخدامها على مواقع لا تملكها.
⚠️ ملاحظات هامة
الأداة مخصصة للاختبار الأمني والأغراض التعليمية فقط.
قد تمنع بعض مواقع WordPress الوصول إلى wp-json/wp/v2/users لأسباب أمنية.
👨‍💻 المطور
📌 المطور: MoezMK
📌 المستودع: WP Info
📌 الرخصة: MIT License

✨ إذا أعجبتك الأداة، لا تنسَ ترك ⭐ في المستودع! 🚀
