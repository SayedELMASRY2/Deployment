# دليل إنجاز التاسك 34: PySpark CI with GitHub Actions

هذا الدليل يشرح لك كل ما يخص التاسك خطوة بخطوة من الصفر التام (من أول تجهيز الملفات حتى تشغيل الـ CI والـ Pull Request على GitHub)، مع توضيح سبب كتابة كل سطر.

---

## 1. ملخص ومطلوب التاسك (Objective)

المطلوب الأساسي في ملف `#34 Task.pdf`:
1. إنشاء دالة معالجة بيانات باسم `clean_data(df)` في ملف `pyspark_job.py`.
2. الدالة تطبق 4 شروط:
   - حذف الصفوف التي فيها قيمة `amount <= 0`.
   - حذف الصفوف التي فيها اسم العميل `name is NULL`.
   - إضافة عمود جديد باسم `amount_with_tax`.
   - حساب قيمة هذا العمود كالتالي: `amount * 1.20`.
3. كتابة اختبارات وحدوية (Unit Tests) باستخدام `pytest` للتأكد من الشروط السابقة في ملف `test_pyspark_job.py`.
4. إعداد مسار عمل تلقائي (GitHub Actions CI) في ملف `.github/workflows/ci.yml` يعمل تلقائياً كلما تم فتح أو تحديث **Pull Request**.

---

## 2. هيكل المشروع (Project Directory Tree)

المشروع يجب أن يكون منظم بالشكل التالي:

```text
spark-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyspark_job.py
├── test_pyspark_job.py
├── requirements.txt
└── TASK_34_GUIDE.md
```

---

## 3. الفحص والمراجعة للملفات الحالية (Files Audit & Fixes)

عند مراجعة مجلد العمل تم رصد وتصحيح الآتي:

1. **`requirements.txt`**:
   - كان موجوداً ويحتوي على الإصدارات المطلوبة بالملف تماماً:
     ```text
     pyspark==3.5.6
     pytest==8.4.2
     ```
2. **`pyspark_job.py`**:
   - كان الملف فارغاً تماماً.
   - **التعديل:** تم كتابة دالة `clean_data` كاملة ومطابقة للشروط.
3. **`test_pyspark_job.py`**:
   - كان يحتوي على كود الاختبار الأساسي.
   - **التعديل/التحسين:** تمت إضافة `.orderBy("id")` قبل `.collect()` لضمان ثبات ترتيب النتائج وتفادي أي عشوائية ناتجة عن الـ Partitions في Spark، مما يضمن نجاح الـ Assertion دائماً بنسبة 100%.
4. **`.github/workflows/ci.yml`**:
   - كان الملف فارغاً تماماً.
   - **التعديل:** تم إعداد الـ Workflow ليعمل عند إنشاء أو تحديث أي `pull_request`، مع إضافة خطوة **مهمة وحرجة جداً** وهي تثبيت **Java JDK 17** (`actions/setup-java@v4`)؛ لأن PySpark لا يمكن أن يعمل بدون وجود بيئة تشغيل Java (JVM) سواء محلياً أو على سيرفرات GitHub Actions.

---

## 4. خطوات التنفيذ خطوة بخطوة من الصفر (Step-by-Step)

### الخطوة 1: تثبيت المتطلبات (`requirements.txt`)
المطلوب في ملف البي دي إف إصدارين محددين:
- افتح ملف `requirements.txt` واكتب بداخله:
  ```text
  pyspark==3.5.6
  pytest==8.4.2
  ```
- لتثبيت المكتبات محلياً في جهازك:
  ```bash
  pip install -r requirements.txt
  ```

---

### الخطوة 2: كتابة دالة المعالجة (`pyspark_job.py`)
افتح ملف `pyspark_job.py` وضع الكود التالي:

```python
from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def clean_data(df: DataFrame) -> DataFrame:
    """
    Cleans the input DataFrame according to the requirements:
    1. Remove rows where amount <= 0.
    2. Remove rows where name is NULL.
    3. Add a column amount_with_tax calculated as amount * 1.20.
    """
    return (
        df.filter((F.col("amount") > 0) & (F.col("name").isNotNull()))
        .withColumn("amount_with_tax", F.col("amount") * 1.20)
    )
```

**شرح الكود:**
- `F.col("amount") > 0`: يفلتر ويلغي أي صف فيه المبلغ أقل من أو يساوي صفر.
- `F.col("name").isNotNull()`: يحذف أي صف لا يحتوي على اسم (NULL).
- `&`: علامة الـ AND المنطقية في PySpark لتطبيق الشرطين معاً.
- `.withColumn("amount_with_tax", F.col("amount") * 1.20)`: ينشئ عموداً جديداً ويضرب قيمة الـ `amount` في `1.20` لحساب الضريبة.

---

### الخطوة 3: كتابة الاختبارات الوحدوية (`test_pyspark_job.py`)
افتح ملف `test_pyspark_job.py` وضع الكود التالي:

```python
from pyspark.sql import SparkSession
from pyspark_job import clean_data


def test_clean_data():
    # 1. إنشاء جلسة Spark محلية للاختبار
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("test")
        .getOrCreate()
    )

    # 2. إنشاء بيانات تجريبية تغطي الحالات الإيجابية والسلبية
    data = [
        (1, "Ahmed", 100),    # صالح: يجب أن يبقى (الضريبة = 120)
        (2, "Mohamed", 200),  # صالح: يجب أن يبقى (الضريبة = 240)
        (3, "Omar", 0),       # مرفوض: amount = 0
        (4, "Ali", -50),      # مرفوض: amount < 0
        (5, None, 300),       # مرفوض: name is NULL
    ]

    df = spark.createDataFrame(
        data,
        ["id", "name", "amount"]
    )

    # 3. تشغيل دالة المعالجة
    result = clean_data(df)

    # جمع النتائج مرتبة بالـ id
    rows = result.orderBy("id").collect()

    # 4. التحقق من النتائج (Assertions)
    # التأكد من بقاء صفين فقط
    assert len(rows) == 2

    # التأكد من بقاء الأسماء الصحيحة فقط
    assert rows[0]["name"] == "Ahmed"
    assert rows[1]["name"] == "Mohamed"

    # التأكد من الحساب الصحيح للضريبة
    assert rows[0]["amount_with_tax"] == 120
    assert rows[1]["amount_with_tax"] == 240

    # 5. إغلاق جلسة الـ Spark
    spark.stop()
```

---

### الخطوة 4: تشغيل الاختبارات محلياً والتأكد من نجاحها

لتشغيل الاختبارات في جهازك:
```bash
pytest -v
```

> **ملاحظة فنية هامة جداً (Java JDK):**
> محرك **Apache Spark** مبني على لغة Scala/Java؛ لذلك يحتاج إلى بيئة تشغيل **Java (JDK 8 أو 11 أو 17)** على جهازك ومتغير بيئي `JAVA_HOME`.
> إذا ظهر لك خطأ `[JAVA_GATEWAY_EXITED] Java not found and JAVA_HOME environment variable is not set`:
> هذا يعني أن الـ Java غير مثبتة محلياً على جهازك. يكفي تحميل وتثبيت **JDK 17** (مثلاً Eclipse Temurin)، وستعمل فوراً.

---

### الخطوة 5: إعداد الـ CI عبر GitHub Actions (`.github/workflows/ci.yml`)

أنشئ المجلدات `.github/workflows/` وضع بداخلها الملف `ci.yml`:

```yaml
name: PySpark CI

on:
  pull_request:
    types: [opened, synchronize, reopened]
  push:
    branches: [main, master]

jobs:
  test:
    name: Run PySpark Unit Tests
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Set up Java (JDK 17)
        uses: actions/setup-java@v4
        with:
          distribution: 'temurin'
          java-version: '17'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run PySpark tests with pytest
        run: |
          pytest -v
```

**لماذا قمنا بضبط الـ Workflow بهذا الشكل؟**
1. **`on.pull_request`**: ينفذ المطلوب في البي دي إف: تفعيل الاختبار التلقائي عند فتح PR أو تحديثه بأي تعديلات جديدة (`synchronize`).
2. **`actions/setup-java@v4`**: تجهيز بيئة Java 17 حتى لا يفشل PySpark على سيرفر الـ GitHub Runner.
3. **`pip install -r requirements.txt`**: تثبيت النسخ المطلوبة بالضبط.
4. **`pytest -v`**: تشغيل الاختبارات وإظهار النتيجة بالتفصيل.

---

### الخطوة 6: الرفع على GitHub وإنشاء الـ Pull Request

لإكمال التاسك وتسليمها:

1. **تهيئة Git في المشروع:**
   ```bash
   git init
   git add .
   git commit -m "feat: implement clean_data, tests, and CI workflow"
   ```

2. **ربط المستودع بـ GitHub:**
   - قم بإنشاء Repo جديد على حسابك في GitHub (مثلاً `pyspark-ci-task`).
   - اربط المجلد المحلي بالـ Repo:
     ```bash
     git remote add origin https://github.com/<your-username>/<your-repo-name>.git
     git branch -M main
     git push -u origin main
     ```

3. **إنشاء Branch لعمل الـ Pull Request:**
   ```bash
   git checkout -b feature/pyspark-pipeline
   # قم بعمل أي تعديل طفيف أو مسافة إذا لزم
   git commit --allow-empty -m "trigger: test CI on pull request"
   git push -u origin feature/pyspark-pipeline
   ```

4. **فتح الـ Pull Request على GitHub:**
   - افتح الـ Repo على موقع GitHub.
   - ستظهر لك رسالة `Compare & pull request`. اضغط عليها.
   - اضغط `Create pull request`.
   - توجه لتبويب **Actions** أو أسفل صفحة الـ Pull Request؛ ستلاحظ أن الـ Workflow اشتغل فوراً، وقام بتشغيل الـ pytest وأعطاك علامة صح خضراء `Passed ✅`.
