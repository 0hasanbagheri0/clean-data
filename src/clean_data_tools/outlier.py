"""
تشخیص و حذف داده‌های پرت (Outlier)
"""

import pandas as pd
import numpy as np
from typing import List, Optional, Union
from scipy import stats

class OutlierDetector:
    """
    کلاس تشخیص و مدیریت داده‌های پرت
    
    Examples:
        >>> detector = OutlierDetector(df)
        >>> outliers = detector.detect_iqr()
        >>> df_clean = detector.remove_outliers()
    """
    
    def __init__(self, data: pd.DataFrame):
        self.df = data.copy()
        self.outliers_info = {}
    
    def detect_iqr(self, columns: Optional[List[str]] = None,
                   multiplier: float = 1.5) -> dict:
        """
        تشخیص داده‌های پرت با روش IQR
        
        Args:
            columns: لیست ستون‌ها
            multiplier: ضریب (پیش‌فرض 1.5)
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        outliers = {}
        for col in columns:
            if col not in self.df.columns:
                continue
            
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            
            lower_bound = q1 - multiplier * iqr
            upper_bound = q3 + multiplier * iqr
            
            mask = (self.df[col] < lower_bound) | (self.df[col] > upper_bound)
            outliers[col] = {
                'count': mask.sum(),
                'indices': self.df.index[mask].tolist(),
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }
        
        self.outliers_info = outliers
        return outliers
    
    def detect_zscore(self, columns: Optional[List[str]] = None,
                      threshold: float = 3) -> dict:
        """
        تشخیص داده‌های پرت با روش Z-Score
        """
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        outliers = {}
        for col in columns:
            if col not in self.df.columns:
                continue
            
            z_scores = np.abs(stats.zscore(self.df[col].dropna()))
            mask = z_scores > threshold
            
            outliers[col] = {
                'count': mask.sum(),
                'indices': self.df.index[mask].tolist() if not mask.empty else []
            }
        
        self.outliers_info = outliers
        return outliers
    
    def remove_outliers(self, columns: Optional[List[str]] = None,
                        method: str = 'iqr',
                        threshold: float = 1.5) -> pd.DataFrame:
        """
        حذف رکوردهای حاوی داده‌های پرت
        """
        result = self.df.copy()
        
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        mask = pd.Series([False] * len(result), index=result.index)
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            if method == 'iqr':
                q1 = self.df[col].quantile(0.25)
                q3 = self.df[col].quantile(0.75)
                iqr = q3 - q1
                lower = q1 - threshold * iqr
                upper = q3 + threshold * iqr
                mask |= (self.df[col] < lower) | (self.df[col] > upper)
            
            elif method == 'zscore':
                z_scores = np.abs(stats.zscore(self.df[col].dropna()))
                mask |= pd.Series(z_scores > threshold, index=self.df.index).fillna(False)
        
        result = result[~mask]
        return result
    
    def replace_outliers(self, columns: Optional[List[str]] = None,
                         method: str = 'median',
                         multiplier: float = 1.5) -> pd.DataFrame:
        """
        جایگزینی داده‌های پرت با میانگین، میانه یا مقدار دلخواه
        """
        result = self.df.copy()
        
        if columns is None:
            columns = self.df.select_dtypes(include=[np.number]).columns
        
        for col in columns:
            if col not in self.df.columns:
                continue
            
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - multiplier * iqr
            upper = q3 + multiplier * iqr
            
            mask = (self.df[col] < lower) | (self.df[col] > upper)
            
            if method == 'mean':
                replacement = self.df[col].mean()
            elif method == 'median':
                replacement = self.df[col].median()
            else:
                replacement = method
            
            result.loc[mask, col] = replacement
        
        return result
