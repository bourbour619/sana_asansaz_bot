import datetime
import jdatetime
import enum

from pydantic import BaseModel, Field, field_validator, computed_field, ValidationInfo
from typing import Optional, List

JALALI_MONTHS = (
    'فرودین', 'اردیبهشت', 'خرداد',
    'تیر', 'مرداد', 'شهریور',
    'مهر', 'آبان', 'آذر',
    'دی', 'بهمن', 'اسفند',
)

class PostStatus(enum.Enum):
    Draft = 'پیش نویس'
    Ready = 'آماده'
    Error = 'خطا'


class CreatePost(BaseModel):
    date: str = Field(kw_only=True)
    status: PostStatus
    items: Optional[List] = None
    start_time: Optional[datetime.time] = None
    end_time: Optional[datetime.time] = None

    @field_validator('date')
    @classmethod
    def validate_date(cls, v: str) -> str:
        try:
            _ = jdatetime.datetime.strptime(v, '%Y/%m/%d')
        except ValueError:
            raise ValueError('تاریخ شمسی وارد شده معتبر نیست')
        return v.title()

    @computed_field
    @property
    def title(self) -> str:
        y, m, d = self.date.split('/')
        return 'لوایح ارسالی تاریخ {0} {1} {2}'.format(d, JALALI_MONTHS[int(m) - 1], y)


class SanaItemType(str, enum.Enum):
    Layehe_Defaie = 'لایحه دفاعیه'
    Parvande_Ejrayie = 'پرونده اجرایی'
    TajdidNazarKhahi = 'تجدیدنظرخواهی'


class CreateSanaItem(BaseModel):
    number: str = Field(strict=False)
    date: str
    type: SanaItemType
    owner: str
    branch: str
    file_number: str = Field(max_length=18, strict=False)
    notice_number: str = Field(max_length=18, strict=False)
    notice_date: str = Field(max_length=10)
    set_date: str
    tracking_code: Optional[str] = Field(max_length=16, default=None)
    success: Optional[bool] = None
    description: Optional[str] = None
    attachments: Optional[List] = None

    @field_validator('date', 'notice_date', 'set_date')
    @classmethod
    def validate_date(cls, v: str, info: ValidationInfo) -> str:
        try:
            _ = jdatetime.datetime.strptime(v, '%Y/%m/%d')
        except ValueError:
            raise ValueError('تاریخ شمسی وارد شده معتبر نیست')
        return v.title()


class CreateAttachment(BaseModel):
    name: str
    path: str
    count: Optional[int] = None







