"""
کلاس اصلی برای تمیزکاری داده‌ها
"""

import pandas as pd
import numpy as np
from typing import Union, Optional, List, Any
from pathlib import Path

class DataCleaner:
    """
    کلاس اصلی برای تمیزکاری داده‌ها
    
    Examples:
        >>> cleaner = DataCleaner(df)
        >>> cleaner.remove_duplicates()
        >>> cleaner.fill_missing("mean")
        >>> df_clean = cleaner.get_data()
    """
    
    def __init__(self, data: Union[pd.DataFrame, str, Path]):
        """
        مقداردهی اولیه
        
        Args:
            data: دیتافریم پانداس یا مسیر فایل CSV/Excel
        """
        if isinstance(data, (str, Path)):
            self.df = self._load_data(data)
        elif isinstance(data, pd.DataFrame):
            self.df = data.copy()
        else:
            raise TypeError("ورودی باید دیتافریم پانداس یا مسیر فایل باشد")
        
        self.original_df = self.df.copy()
        self._changes_log = []
    
    def _load_data(self, path: Union[str, Path]) -> pd.DataFrame:
        """بارگذاری داده از فایل"""
        path = Path(path)
        if path.suffix == '.csv':
            return pd.read_csv(path)
        elif path.suffix in ['.xlsx', '.xls']:
            return pd.read_excel(path)
        else:
            raise ValueError("فرمت فایل پشتیبانی نمی‌شود. فقط CSV و Excel")
    
    def get_data(self) -> pd.DataFrame:
        """دریافت دیتافریم تمیز شده"""
        return self.df
    
    def get_original(self) -> pd.DataFrame:
        """دریافت دیتافریم اصلی"""
        return self.original_df
    
    def get_changes_log(self) -> List[str]:
        """دریافت گزارش تغییرات"""
        return self._changes_log
    
    def _log_change(self, message: str):
        """ثبت تغییر در گزارش"""
        self._changes_log.append(message)
    
    def remove_duplicates(self, subset: Optional[List[str]] = None,
                          keep: str = 'first') -> 'DataCleaner':
        """
        حذف رکوردهای تکراری
        
        Args:
            subset: لیست ستون‌ها برای بررسی تکراری بودن
            keep: 'first', 'last', یا False
        """
        before = len(self.df)
        self.df = self.df.drop_duplicates(subset=subset, keep=keep)
        after = len(self.df)
        self._log_change(f"حذف {before - after} رکورد تکراری")
        return self
    
    def fill_missing(self, method: Union[str, dict, int, float],
                     columns: Optional[List[str]] = None) -> 'DataCleaner':
        """
        پر کردن مقادیر خالی
        
        Args:
            method: 'mean', 'median', 'mode', 'zero', یا مقدار دلخواه
            columns: لیست ستون‌ها (اگر None باشد، همه ستون‌ها)
        """
        if columns is None:
            columns = self.df.columns
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            missing_count = self.df[col].isna().sum()
            if missing_count == 0:
                continue
            
            if isinstance(method, dict):
                fill_value = method.get(col, 0)
            elif method == 'mean':
                fill_value = self.df[col].mean()
            elif method == 'median':
                fill_value = self.df[col].median()
            elif method == 'mode':
                fill_value = self.df[col].mode()[0] if not self.df[col].mode().empty else 0
            elif method == 'zero':
                fill_value = 0
            else:
                fill_value = method
            
            self.df[col] = self.df[col].fillna(fill_value)
            self._log_change(f"پر کردن {missing_count} مقدار خالی در ستون '{col}'")
        
        return self
    
    def remove_missing(self, threshold: float = 0.5,
                       axis: int = 0) -> 'DataCleaner':
        """
        حذف سطرها یا ستون‌های با مقدار خالی زیاد
        
        Args:
            threshold: حداقل درصد داده‌های غیر خالی (بین 0 تا 1)
            axis: 0 برای سطر، 1 برای ستون
        """
        before = len(self.df) if axis == 0 else len(self.df.columns)
        self.df = self.df.dropna(thresh=int(threshold * len(self.df)), axis=axis)
        after = len(self.df) if axis == 0 else len(self.df.columns)
        self._log_change(f"حذف {before - after} {'سطر' if axis == 0 else 'ستون'}")
        return self
    
    def convert_types(self, columns: Optional[List[str]] = None) -> 'DataCleaner':
        """
        تبدیل خودکار نوع ستون‌ها (عددی، تاریخ، رشته)
        """
        if columns is None:
            columns = self.df.columns
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            try:
                # تلاش برای تبدیل به عدد
                self.df[col] = pd.to_numeric(self.df[col], errors='ignore')
            except:
                pass
            
            try:
                # تلاش برای تبدیل به تاریخ
                self.df[col] = pd.to_datetime(self.df[col], errors='ignore')
            except:
                pass
        
        self._log_change("تبدیل خودکار انواع داده")
        return self
    
    def strip_strings(self, columns: Optional[List[str]] = None) -> 'DataCleaner':
        """حذف فاصله‌های اضافی از رشته‌ها"""
        if columns is None:
            columns = self.df.select_dtypes(include=['object']).columns
        
        for col in columns:
            if col in self.df.columns and self.df[col].dtype == 'object':
                self.df[col] = self.df[col].str.strip()
        self._log_change("حذف فاصله‌های اضافی از رشته‌ها")
        return self
    
    def rename_columns(self, mapping: dict) -> 'DataCleaner':
        """تغییر نام ستون‌ها"""
        self.df = self.df.rename(columns=mapping)
        self._log_change(f"تغییر نام {len(mapping)} ستون")
        return self
    
    def filter_rows(self, condition: Any) -> 'DataCleaner':
        """فیلتر کردن سطرها بر اساس شرط"""
        before = len(self.df)
        self.df = self.df[condition]
        after = len(self.df)
        self._log_change(f"فیلتر کردن: {before - after} سطر حذف شد")
        return self
    
    def reset(self) -> 'DataCleaner':
        """بازگشت به داده‌های اصلی"""
        self.df = self.original_df.copy()
        self._changes_log = []
        self._log_change("بازگشت به داده‌های اصلی")
        return self
