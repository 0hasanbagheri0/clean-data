"""
توابع کمکی برای گزارش‌گیری از کیفیت داده
"""

import pandas as pd
import numpy as np
from typing import Dict, Any

def get_data_quality_report(df: pd.DataFrame) -> Dict[str, Any]:
    """
    دریافت گزارش کامل از کیفیت داده‌ها
    
    Returns:
        دیکشنری شامل: تعداد سطرها، ستون‌ها، مقادیر خالی، تکراری‌ها، نوع داده‌ها، و ...
    """
    report = {
        'shape': {
            'rows': len(df),
            'columns': len(df.columns)
        },
        'missing': {},
        'duplicates': {
            'count': df.duplicated().sum(),
            'percentage': (df.duplicated().sum() / len(df)) * 100
        },
        'data_types': df.dtypes.to_dict(),
        'statistics': {},
        'memory_usage': df.memory_usage(deep=True).sum() / 1024  # KB
    }
    
    # بررسی مقادیر خالی
    for col in df.columns:
        missing_count = df[col].isna().sum()
        report['missing'][col] = {
            'count': missing_count,
            'percentage': (missing_count / len(df)) * 100
        }
    
    # آمار توصیفی برای ستون‌های عددی
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        report['statistics'][col] = {
            'min': df[col].min(),
            'max': df[col].max(),
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'unique': df[col].nunique()
        }
    
    return report

def get_column_info(df: pd.DataFrame, column: str) -> Dict[str, Any]:
    """دریافت اطلاعات کامل یک ستون خاص"""
    if column not in df.columns:
        raise ValueError(f"ستون '{column}' در دیتافریم وجود ندارد")
    
    return {
        'name': column,
        'dtype': str(df[column].dtype),
        'missing_count': df[column].isna().sum(),
        'missing_percentage': (df[column].isna().sum() / len(df)) * 100,
        'unique_values': df[column].nunique(),
        'memory_usage': df[column].memory_usage(deep=True) / 1024  # KB
    }
