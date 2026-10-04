# دليل توثيق وتسليم التاسك 34 (Submission & Screenshots Guide)
## PySpark CI with GitHub Actions - Samsung Innovation Campus

هذا الدليل مخصص لشرح **كيفية توثيق وتسليم التاسك بأعلى دقة وتفصيل (In Details)**، وتحديد **كل لقطة شاشة (Screenshot)** تحتاج إلى التقاطها، وماذا يجب أن يظهر فيها بالضبط لضمان الحصول على الدرجة الكاملة في التقييم.

---

## 📌 الفهرس العام
1. [خريطة السكرين شوتس المطلوبة (11 لقطة أساسية)](#1-خريطة-السكرين-شوتس-المطلوبة)
2. [الخطوات العملية خطوة بخطوة لالتقاط كل سكرين شوت](#2-الخطوات-العملية-خطوة-بخطوة)
3. [نصائح شكلية واحترافية لجودة الصور والتوثيق](#3-نصائح-احترافية-للتوثيق)
4. [طريقة تسليم التاسك (ملف PDF / Word أو GitHub Link)](#4-طريقة-تسليم-التاسك)

---

## 1. خريطة السكرين شوتس المطلوبة

| رقم السكرين شوت | اسم اللقطة | ماذا يجب أن يظهر فيها؟ | الهدف من الصورة في التقييم |
| :--- | :--- | :--- | :--- |
| **Screenshot 01** | هيكل المشروع الكامل | نافذة VS Code Explorer على اليسار وتظهر كل الملفات والمجلدات | إثبات الالتزام بتوزيع الملفات المطلوب في PDF |
| **Screenshot 02** | متطلبات المشروع `requirements.txt` | فتح الملف وظهور نسختي PySpark و PyTest | إثبات مطابقة الإصدارات المحددة |
| **Screenshot 03** | كود معالجة البيانات `pyspark_job.py` | دالة `clean_data` وشروط الفلترة والضريبة | إثبات استيفاء منطق المعالجة المطلوب |
| **Screenshot 04** | كود الاختبارات `test_pyspark_job.py` | كود دالة `test_clean_data` وحالات الاختبار والـ Assertions | إثبات اختبار كل الحالات (NULLs, <=0, Tax) |
| **Screenshot 05** | ملف مسار العمل `.github/workflows/ci.yml` | كود الـ Workflow كاملاً متضمناً `pull_request` وتثبيت Java | إثبات ضبط الـ CI بالشكل السليم |
| **Screenshot 06** | تشغيل أوامر Git والـ Push في الـ Terminal | تنفيذ أوامر إنشاء الفرع `feature/pyspark-pipeline` والـ Push | إثبات العمل بنظام الـ Feature Branching |
| **Screenshot 07** | إنشاء الـ Pull Request على GitHub | واجهة GitHub أثناء فتح الـ PR من الـ branch إلى `main` | إثبات فهم مسار الـ PR |
| **Screenshot 08** | انطلاق الـ Workflow تلقائياً في صفحة Actions | تبويب **Actions** في ريبو GitHub وتظهر الجوب في حالة التشغيل (أو بدأت فور فتح الـ PR) | إثبات أن الـ Trigger يعمل مع الـ PR أوتوماتيكياً |
| **Screenshot 09** | نجاح مسار الـ CI باللون الأخضر (Passed) | صفحة الـ Workflow خضراء بعلامة صح `Run PySpark Unit Tests` | إثبات خلو الـ Pipeline من الأخطاء |
| **Screenshot 10** | تفاصيل لوج الاختبار (Detailed PyTest Logs) | الضغط على خطوة `Run PySpark tests with pytest` وظهور `1 passed` | إثبات نجاح الاختبار الفعلي بـ PyTest |
| **Screenshot 11** | شارة النجاح داخل صفحة الـ Pull Request | صفحة الـ PR من الأسفل وتظهر: **"All checks have passed"** | إثبات اكتمال دورة الـ CI/CD بنجاح |

---

## 2. الخطوات العملية خطوة بخطوة

اتبع هذه الخطوات بالترتيب، وعند الوصول لكل مرحلة التقط السكرين شوت الخاصة بها:

---

### المرحلة الأولى: توثيق الملفات المحلية (Local Files)

#### 📸 Screenshot 01: هيكل المشروع (Project Structure)
- **كيف تلتقطها؟**
  - افتح المجلد في **VS Code**.
  - افتح القائمة الجانبية اليسرى (File Explorer) وتأكد من فتح مجلد `.github/workflows/`.
  - يجب أن يظهر التالي بوضوح:
    - `.github/workflows/ci.yml`
    - `pyspark_job.py`
    - `test_pyspark_job.py`
    - `requirements.txt`
- **التعليق المقترح تحت الصورة في التقرير:**
  > *"Project structure showing all required files according to Task 34 specifications."*

---

#### 📸 Screenshot 02: ملف الاعتماديات (`requirements.txt`)
- **كيف تلتقطها؟**
  - افتح ملف `requirements.txt` في المحرر.
  - يجب أن يظهر السطرين:
    ```text
    pyspark==3.5.6
    pytest==8.4.2
    ```
- **التعليق المقترح:**
  > *"Exact pinned dependencies: pyspark 3.5.6 and pytest 8.4.2."*

---

#### 📸 Screenshot 03: كود المعالجة (`pyspark_job.py`)
- **كيف تلتقطها؟**
  - افتح ملف `pyspark_job.py`.
  - تأكد من وضوح كود دالة `clean_data` والشروط:
    1. حذف `amount <= 0`
    2. حذف `name is NULL`
    3. إضافة عمود `amount_with_tax` بحساب `amount * 1.20`
- **التعليق المقترح:**
  > *"Implementation of `clean_data(df)` filtering invalid rows and calculating `amount_with_tax`."*

---

#### 📸 Screenshot 04: كود الاختبارات (`test_pyspark_job.py`)
- **كيف تلتقطها؟**
  - افتح ملف `test_pyspark_job.py`.
  - تأكد من ظهور البيانات التجريبية والـ Assertions التي تؤكد الشروط الأربعة:
    - بقاء السجلات الصالحة (Ahmed و Mohamed).
    - حذف السجلات التي بها 0 أو سالب أو NULL.
    - صحة حساب الضريبة (120 و 240).
- **التعليق المقترح:**
  > *"Unit tests implemented using pytest verifying all business requirements."*

---

#### 📸 Screenshot 05: ملف الـ CI Workflow (`.github/workflows/ci.yml`)
- **كيف تلتقطها؟**
  - افتح ملف `.github/workflows/ci.yml`.
  - ركز على:
    - `on: pull_request`
    - خطوة تثبيت Python
    - خطوة تثبيت Java JDK 17 (`actions/setup-java@v4`)
    - خطوة تشغيل `pytest -v`
- **التعليق المقترح:**
  > *"GitHub Actions CI workflow configuration configured to trigger on Pull Requests with Java 17 and Python 3.10."*

---

### المرحلة الثانية: إعداد Git والرفع على GitHub

قم بفتح الـ Terminal في VS Code ونفّذ التالي:

1. إنشاء مستودع Git محلي:
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit with pyspark pipeline and CI"
   git branch -M main
   ```
2. اربط المستودع بريبو جديد على حسابك في GitHub:
   ```bash
   git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO_NAME>.git
   git push -u origin main
   ```
3. الآن قم بإنشاء فرع جديد (Branch) لإنشاء الـ Pull Request منه:
   ```bash
   git checkout -b feature/pyspark-pipeline
   git commit --allow-empty -m "ci: test pull request workflow trigger"
   git push -u origin feature/pyspark-pipeline
   ```

#### 📸 Screenshot 06: أوامر الـ Terminal (Git Branching & Push)
- **كيف تلتقطها؟**
  - التقط سكرين شوت للـ Terminal يظهر فيه أمر إنشاء الفرع `git checkout -b ...` وأمر `git push -u origin feature/pyspark-pipeline` مع رسائل الرفع الناجحة.
- **التعليق المقترح:**
  > *"Creating a feature branch and pushing changes to GitHub to initiate a Pull Request."*

---

### المرحلة الثالثة: فتح الـ Pull Request وتوثيق الـ CI على GitHub

1. اذهب إلى صفحة المستودع الخاص بك على موقع **GitHub**.
2. ستجد زر أصفر/أخضر يظهر تلقائياً: **Compare & pull request** (أو اضغط على تبويب **Pull requests** ثم **New pull request**).
3. حدد الـ base: `main` والـ compare: `feature/pyspark-pipeline`.

#### 📸 Screenshot 07: صفحة إنشاء الـ Pull Request
- **كيف تلتقطها؟**
  - التقط الشاشة وأنت في صفحة **Open a pull request** وتظهر الفروع بوضوح، وعنوان الـ PR والزر الأخضر **Create pull request**.
- **التعليق المقترح:**
  > *"Creating a Pull Request from `feature/pyspark-pipeline` into `main`."*

4. اضغط على **Create pull request**.

---

#### 📸 Screenshot 08: مسار الـ Actions بدأ بالعمل (In Progress)
- **كيف تلتقطها؟**
  - ادخل على تبويب **Actions** في الريبو.
  - ستجد الـ Workflow بعنوان `PySpark CI` قد بدأ العمل تزامناً مع فتح الـ PR وتظهر دائرة صفراء تدور تشير إلى أنه (In Progress).
- **التعليق المقترح:**
  > *"GitHub Actions automatically triggered upon Pull Request creation."*

---

#### 📸 Screenshot 09: اكتمال الـ CI بنجاح (Workflow Success - Passed)
- **كيف تلتقطها؟**
  - بعد حوالي 30 إلى 60 ثانية، ستتحول العلامة إلى **دائرة خضراء بصح ✅**.
  - اضغط على الـ Workflow وخذ لقطة للصفحة وهي تعرض:
    - اسم الـ Workflow: `PySpark CI`
    - الحدث: `pull_request`
    - الجوب: `Run PySpark Unit Tests` بعلامة صح خضراء.
- **التعليق المقترح:**
  > *"CI pipeline successfully executed with all steps passed."*

---

#### 📸 Screenshot 10: تفاصيل الـ PyTest Logs (أهم صورة تقنية)
- **كيف تلتقطها؟**
  - من داخل الجوب الناجحة، اضغط على خطوة **`Run PySpark tests with pytest`** لتفتح التفاصيل (Logs).
  - يجب أن يظهر بوضوح السطر:
    ```text
    test_pyspark_job.py::test_clean_data PASSED
    ========================= 1 passed in ...s =========================
    ```
- **التعليق المقترح:**
  > *"Detailed execution logs confirming that all PySpark unit tests passed successfully."*

---

#### 📸 Screenshot 11: صفحة الـ Pull Request والشارة الخضراء
- **كيف تلتقطها؟**
  - ارجع إلى صفحة الـ **Pull Request** الذي فتحته.
  - انزل لأسفل محادثة الـ PR عند صندوق الـ Checks.
  - ستجد رسالة واضحة:
    - **"All checks have passed"** وبجانبها علامة صح خضراء واسم الفحص `PySpark CI / test`.
- **التعليق المقترح:**
  > *"Pull Request status showing all CI checks passed, ready for merge."*

---

## 3. نصائح احترافية للتوثيق (Best Practices)

1. **الوضوح والدقة:** تأكد أن السكرين شوت واضحة والخط مقروء (استخدم أداة `Snipping Tool` أو اختصار `Windows + Shift + S`).
2. **إظهار عناوين الروابط (URL):** عند أخذ لقطات من موقع GitHub، احرص أن يظهر شريط العنوان أو اسم الريبو في أعلى الصفحة لإثبات أن هذا العمل على حسابك الشخصي.
3. **تحديد الأجزاء المهمة بمستطيل أحمر (Highlighting):** وضع مستطيل أو سهم أحمر حول السطور الهامة (مثل علامة الصح الخضراء، سطر `1 passed`، سطر `actions/setup-java`) يعطي التقرير شكلاً احترافياً للغاية ويسهل على المعيد/المراجع إعطاءك الدرجة فوراً.

---

## 4. نموذج هيكل تقرير التسليم النهائي (Submission Report Template)

إذا كان المطلوب تسليم ملف PDF أو Word، يمكنك تنظيم التقرير بالشكل التالي:

```text
1. Cover Page:
   - Task Title: PySpark CI with GitHub Actions (Task #34)
   - Student Name: [اسمك]
   - Track: Data Engineering - Samsung Innovation Campus
   - GitHub Repository Link: https://github.com/...

2. Project Architecture & Code Implementation:
   - Brief explanation of clean_data function.
   - [Insert Screenshot 01: Project Structure]
   - [Insert Screenshot 02: requirements.txt]
   - [Insert Screenshot 03: pyspark_job.py]
   - [Insert Screenshot 04: test_pyspark_job.py]

3. CI/CD Pipeline Implementation:
   - Explanation of GitHub Actions workflow & Java setup.
   - [Insert Screenshot 05: .github/workflows/ci.yml]

4. Execution, Pull Request & CI Verification:
   - [Insert Screenshot 06: Git Branching & Push Terminal]
   - [Insert Screenshot 07: Pull Request Creation]
   - [Insert Screenshot 08: Actions Triggered]
   - [Insert Screenshot 09: Actions Workflow Passed]
   - [Insert Screenshot 10: PyTest Output Logs]
   - [Insert Screenshot 11: Pull Request "All checks have passed"]

5. Conclusion:
   - Confirmation that the pipeline is fully automated and idempotent.
```
