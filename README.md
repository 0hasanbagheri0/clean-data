# Clean-Data

#ابزارهای قدرتمند برای تمیزکاری و پیش‌پردازش داده‌ها در پایتون.

[![PyPI version](https://badge.fury.io/py/clean-data.svg)](https://badge.fury.io/py/clean-data)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ ویژگی‌ها

- **حذف رکوردهای تکراری**
- **پر کردن مقادیر خالی** (با میانگین، میانه، مد یا مقدار دلخواه)
- **تشخیص و حذف داده‌های پرت** (با روش‌های IQR و Z-Score)
- **نرمال‌سازی داده‌ها** (Min-Max, Standardization, Robust Scaling)
- **تبدیل خودکار نوع داده‌ها**
- **گزارش کیفیت داده** (درصد خالی، تکراری، نوع داده‌ها و ...)

## 📦 نصب

```bash
pip install clean-data

#🚀 شروع سریع
python
import pandas as pd
from cleandata import DataCleaner, OutlierDetector, Normalizer, get_data_quality_report

# بارگذاری داده
df = pd.read_csv("data.csv")

# تمیزکاری
cleaner = DataCleaner(df)
cleaner.remove_duplicates()
cleaner.fill_missing("mean")
cleaner.strip_strings()

# تشخیص داده‌های پرت
detector = OutlierDetector(cleaner.get_data())
outliers = detector.detect_iqr()
df_clean = detector.remove_outliers()

# نرمال‌سازی
normalizer = Normalizer(df_clean)
df_scaled = normalizer.min_max_scale()

# گزارش کیفیت
report = get_data_quality_report(df_clean)
print(report)
#📄 مجوز
#MIT
