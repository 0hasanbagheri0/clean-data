markdown
# Clean-Data

ابزارهای قدرتمند برای تمیزکاری و پیش‌پردازش داده‌ها در پایتون

[![PyPI version](https://badge.fury.io/py/clean-data.svg)](https://badge.fury.io/py/clean-data)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🌐 English | [فارسی](#فارسی)

---

# English Documentation

## 📁 Clean-Data

**Clean-Data** is a powerful library for data cleaning and preprocessing in Python. It simplifies repetitive tasks like handling missing values, removing duplicates, detecting outliers, and normalizing data.
---
### ✨ Key Features

- **Remove Duplicates**: Eliminate duplicate records easily
- **Handle Missing Values**: Fill with mean, median, mode, or custom values
- **Outlier Detection**: Using IQR and Z-Score methods
- **Data Normalization**: Min-Max, Standardization, and Robust Scaling
- **Auto Type Conversion**: Convert columns to appropriate types
- **Quality Report**: Get detailed statistics about your data

---

### 📦 Installation

```bash
pip install clean-data
```
---

### 🚀 Quick Start
```python
import pandas as pd
from cleandata import DataCleaner, OutlierDetector, Normalizer, get_data_quality_report
```
# Load data
```bash
df = pd.read_csv("data.csv")
```
# Clean data
```bash
cleaner = DataCleaner(df)
```
```bash
cleaner.remove_duplicates()
```
```bash
cleaner.fill_missing("mean")
```
```bash
cleaner.strip_strings()
```
# Detect and remove outliers
```bash
detector = OutlierDetector(cleaner.get_data())
```
```bash
outliers = detector.detect_iqr()
```
```bash
df_clean = detector.remove_outliers()
```
# Normalize
```bash
normalizer = Normalizer(df_clean)
```
```bash
df_scaled = normalizer.min_max_scale()
```
# Quality report
```bash
report = get_data_quality_report(df_clean)
```
```bash
print(report)
```
---

### 📚 API Reference
# DataCleaner Class
|Method|	Description|
| :--- | :--- |
|remove_duplicates(subset, keep)	|Remove duplicate rows|
|fill_missing(method, columns)	|Fill missing values with mean, median, mode, or custom|
|remove_missing(threshold, axis)	|Remove rows/columns with too many missing values|
|convert_types(columns)	|Auto-convert column data types|
|strip_strings(columns)	|Remove extra whitespace from strings|
|rename_columns(mapping)	|Rename columns|
|filter_rows(condition)	|Filter rows based on condition|
|reset()	|Revert to original data|

# OutlierDetector Class

|Method	|Description|
| :--- | :--- |
|detect_iqr(columns, multiplier)	|Detect outliers using IQR method|
|detect_zscore(columns, threshold)	|Detect outliers using Z-Score method|
|remove_outliers(columns, method, threshold)	|Remove rows with outliers|
|replace_outliers(columns, method, multiplier)	|Replace outliers with mean/median/custom|

# Normalizer Class

|Method	|Description|
| :--- | :--- |
|min_max_scale(columns, feature_range)	|Scale to a range (default 0-1)|
|standardize(columns)	|Standardize to mean=0, std=1|
|robust_scale(columns)	|Scale using median and IQR (robust to outliers)|
|log_transform(columns)	|Apply log transformation|
# Utility Functions
|Function	|Description|
| :--- | :--- |
|get_data_quality_report(df)|	Get comprehensive data quality report|
|get_column_info(df, column)|	Get detailed info about a specific column|

---

### 🛠️ Requirements
Python 3.7 or higher

pandas>=1.0.0

numpy>=1.18.0

scipy>=1.4.0

---

### 🤝 Contributing
We welcome contributions! Please:

1.Fork the repository

2.Create a new branch (git checkout -b feature/amazing-feature)

3.Commit your changes (git commit -m 'Add amazing feature')

4.Push to the branch (git push origin feature/amazing-feature)

5.Open a Pull Request

---

### 📄 License
This project is licensed under the MIT License.

---

### 📧 Contact
Email: hasan111bagher@gmail.com

GitHub: 0hasanbagheri0

---
---

فارسی

---

### 📁 Clean-Data
Clean-Data یک کتابخانه قدرتمند برای تمیزکاری و پیش‌پردازش داده‌ها در پایتون است. این کتابخانه کارهای تکراری مانند مدیریت مقادیر خالی، حذف رکوردهای تکراری، تشخیص داده‌های پرت و نرمال‌سازی داده‌ها را ساده می‌کند.

---

### ✨ ویژگی‌های کلیدی

حذف رکوردهای تکراری: حذف آسان رکوردهای تکراری

مدیریت مقادیر خالی: پر کردن با میانگین، میانه، مد یا مقدار دلخواه

تشخیص داده‌های پرت: با روش‌های IQR و Z-Score

نرمال‌سازی داده‌ها: Min-Max، Standardization و Robust Scaling

تبدیل خودکار نوع داده‌ها: تبدیل ستون‌ها به نوع مناسب

گزارش کیفیت: دریافت آمار دقیق از داده‌ها

---

### 📦 نصب
```bash
pip install clean-data

```

---

### 🚀 شروع سریع

```python

import pandas as pd
from cleandata import DataCleaner, OutlierDetector, Normalizer, get_data_quality_report
```
# بارگذاری داده
```bash
df = pd.read_csv("data.csv")
```
# تمیزکاری
```bash
cleaner = DataCleaner(df)
```
```bash
cleaner.remove_duplicates()
```
```bash
cleaner.fill_missing("mean")
```
```bash
cleaner.strip_strings()
```
# تشخیص و حذف داده‌های پرت
```bash
detector = OutlierDetector(cleaner.get_data())
```
```bash
outliers = detector.detect_iqr()
```
```bash
df_clean = detector.remove_outliers()
```


# نرمال‌سازی
```bash
normalizer = Normalizer(df_clean)
```
df_scaled = normalizer.min_max_scale()
```
# گزارش کیفیت
```bash
report = get_data_quality_report(df_clean)
print(report)
```
---

### 📚 راهنمای توابع
# کلاس DataCleaner
|تابع	|توضیح|
| :--- | :--- |
|remove_duplicates(subset, keep)|	حذف سطرهای تکراری|
|fill_missing(method, columns)	|پر کردن مقادیر خالی با میانگین، میانه، مد یا مقدار دلخواه|
|remove_missing(threshold, axis)|	حذف سطرها/ستون‌هایی که مقادیر خالی زیادی دارند|
|convert_types(columns)|	تبدیل خودکار نوع ستون‌ها|
|strip_strings(columns)|	حذف فاصله‌های اضافی از رشته‌ها|
|rename_columns(mapping)|	تغییر نام ستون‌ها|
|filter_rows(condition)|	فیلتر کردن سطرها بر اساس شرط|
|reset()|	بازگشت به داده‌های اصلی|
# کلاس OutlierDetector
|تابع	|توضیح|
| :--- | :--- |
|detect_iqr(columns, multiplier)	|تشخیص داده‌های پرت با روش IQR|
|detect_zscore(columns, threshold)	|تشخیص داده‌های پرت با روش Z-Score|
|remove_outliers(columns, method, threshold)	|حذف سطرهای حاوی داده‌های پرت|
|replace_outliers(columns, method, multiplier)	|جایگزینی داده‌های پرت با میانگین/میانه/مقدار دلخواه|
# کلاس Normalizer
|تابع	|توضیح|
| :--- | :--- |
|min_max_scale(columns, feature_range)	|مقیاس‌سازی به بازه مشخص (پیش‌فرض ۰ تا ۱)|
|standardize(columns)	|استانداردسازی (میانگین صفر، انحراف معیار یک)|
|robust_scale(columns)	|مقیاس‌سازی مقاوم به داده‌های پرت (با میانه و IQR)|
|log_transform(columns)|	اعمال تبدیل لگاریتمی|
# توابع کمکی
|تابع	|توضیح|
| :--- | :--- |
|get_data_quality_report(df)	|دریافت گزارش کامل کیفیت داده|
|get_column_info(df, column)	|دریافت اطلاعات دقیق یک ستون خاص|

### 🛠️ نیازمندی‌ها

Python 3.7 یا بالاتر

pandas>=1.0.0

numpy>=1.18.0

scipy>=1.4.0

### 🤝 مشارکت
از مشارکت شما استقبال می‌کنیم! لطفاً:

1.مخزن را Fork کنید

2.یک شاخه جدید بسازید (git checkout -b feature/amazing-feature)

3.تغییرات را Commit کنید (git commit -m 'Add amazing feature')

4.به شاخه خود Push کنید (git push origin feature/amazing-feature)

5.یک Pull Request باز کنید

### 📄 مجوز
این پروژه تحت مجوز MIT منتشر شده است.

### 📧 ارتباط با من
ایمیل: hasan111bagher@gmail.com

گیت‌هاب: 0hasanbagheri0

✨ اگر این کتابخانه برای شما مفید بود، به آن یک ⭐ در گیت‌هاب بدهید!
