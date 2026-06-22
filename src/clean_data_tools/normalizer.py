"""
توابع نرمال‌سازی داده‌ها
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Union

class Normalizer:
    """
    کلاس نرمال‌سازی داده‌ها
    
    Examples:
        >>> normalizer = Normalizer(df)
        >>> df_scaled = normalizer.min_max_scale()
        >>> df_standard = normalizer.standardize()
    """
    
    def __init__(self, data: pd.DataFrame):
        self.df = data.copy()
        self._params = {}
    
    def min_max_scale(self, columns: Optional[List[str]] = None,
                       feature_range: tuple = (0, 1)) -> pd.DataFrame:
        """
        نرمال‌سازی Min-Max (مقیاس‌سازی به بازه مشخص)
        
        Args:
            columns: لیست ستون‌ها (اگر None باشد، همه ستون‌های عددی)
            feature_range: بازه مورد نظر (min, max)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        result = self.df.copy()
        for col in columns:
            if col not in self.df.columns:
                continue
            
            min_val = self.df[col].min()
            max_val = self.df[col].max()
            
            if max_val - min_val == 0:
                result[col] = 0
            else:
                result[col] = (self.df[col] - min_val) / (max_val - min_val) * (feature_range[1] - feature_range[0]) + feature_range[0]
            
            self._params[col] = {'min': min_val, 'max': max_val}
        
        return result
    
    def standardize(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        استانداردسازی (میانگین صفر، انحراف معیار یک)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        result = self.df.copy()
        for col in columns:
            if col not in self.df.columns:
                continue
            
            mean = self.df[col].mean()
            std = self.df[col].std()
            
            if std == 0:
                result[col] = 0
            else:
                result[col] = (self.df[col] - mean) / std
            
            self._params[col] = {'mean': mean, 'std': std}
        
        return result
    
    def robust_scale(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        مقیاس‌سازی مقاوم به داده‌های پرت (با استفاده از میانه و IQR)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        result = self.df.copy()
        for col in columns:
            if col not in self.df.columns:
                continue
            
            median = self.df[col].median()
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            
            if iqr == 0:
                result[col] = 0
            else:
                result[col] = (self.df[col] - median) / iqr
            
            self._params[col] = {'median': median, 'iqr': iqr}
        
        return result
    
    def log_transform(self, columns: Optional[List[str]] = None) -> pd.DataFrame:
        """
        تبدیل لگاریتمی (برای داده‌های با توزیع چوله)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        result = self.df.copy()
        for col in columns:
            if col not in self.df.columns:
                continue
            
            # اطمینان از مثبت بودن داده‌ها
            if (self.df[col] <= 0).any():
                shift = abs(self.df[col].min()) + 1
                result[col] = np.log1p(self.df[col] + shift)
            else:
                result[col] = np.log(self.df[col])
        
        return result
