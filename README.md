📌 المتطلبات

قبل تشغيل الأداة، تأكد من تثبيت الحزم المطلوبة عبر pip:

✅ التثبيت اليدوي

pip install requests pyfiglet tqdm

📂 التثبيت باستخدام requirements.txt

إذا كنت تريد تثبيت جميع المتطلبات دفعة واحدة، استخدم الأمر التالي:

pip install -r requirements.txt

🐍 إنشاء بيئة افتراضية (اختياري)

لمنع تعارض الحزم مع بيئات Python الأخرى، يمكنك إنشاء بيئة افتراضية ثم تثبيت المتطلبات داخلها:

python -m venv env
source env/bin/activate  # على أنظمة Linux/macOS
env\Scripts\activate     # على نظام Windows
pip install -r requirements.txt

