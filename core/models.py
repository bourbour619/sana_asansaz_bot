import enum
from datetime import datetime
from typing import List, Optional

from sqlalchemy.orm import declarative_base
from sqlalchemy import ForeignKey, String, DateTime, Time
from sqlalchemy.orm import Mapped, mapped_column, relationship


Base = declarative_base()


class Config(Base):
    __tablename__ = 'configs'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    key: Mapped[str] = mapped_column(String(50), unique=True)
    value: Mapped[str] = mapped_column(String(255), nullable=True)
    attachment_value: Mapped['Attachment'] = relationship(
        back_populates='config')
    date: Mapped[datetime] = mapped_column(DateTime)


class PostStatus(enum.Enum):
    Draft = 'پیش نویس'
    Ready = 'آماده'
    Error = 'خطا'


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(nullable=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), unique=True)
    date: Mapped[str] = mapped_column(
        String(16), primary_key=True, nullable=False)
    status: Mapped[PostStatus]
    items: Mapped[List['SanaItem']] = relationship(back_populates='post')
    start_time: Mapped[datetime.time] = mapped_column(Time, nullable=True)
    end_time: Mapped[datetime.time] = mapped_column(Time, nullable=True)

    @property
    def items_count(self):
        return len(self.items)

    @property
    def success_count(self):
        return len([item for item in self.items if item.success])

    @property
    def error_count(self):
        return self.items_count() - self.success_count()


class SanaItemType(enum.Enum):
    Layehe_Defaie = 'لایحه دفاعیه'
    Parvande_Ejrayie = 'پرونده اجرایی'
    TajdidNazarKhahi = 'تجدیدنظرخواهی'


class SanaAudienceType(enum.Enum):
    Saba = 'سابا'
    Sata = 'ساتا'


class SanaItem(Base):
    __tablename__ = 'sana_items'

    id: Mapped[int] = mapped_column(nullable=True, autoincrement=True)
    number: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[Optional[str]] = mapped_column(String(16), nullable=False)
    type: Mapped[SanaItemType]
    owner: Mapped[str] = mapped_column(String(255))
    branch: Mapped[str] = mapped_column(String(25))
    file_number: Mapped[str] = mapped_column(String(18))
    notice_number: Mapped[str] = mapped_column(String(18))
    notice_date: Mapped[str] = mapped_column(String(10))
    set_date: Mapped[str] = mapped_column(String(10))
    sana_audience: Mapped[SanaAudienceType] = mapped_column(nullable=False)
    tracking_code: Mapped[str] = mapped_column(String(16), nullable=True)
    success: Mapped[bool] = mapped_column(default=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    attachments: Mapped[List['Attachment']] = relationship(
        back_populates='sana_item')

    post_date: Mapped[str] = mapped_column(ForeignKey('posts.date'))
    post: Mapped['Post'] = relationship(back_populates='items')

    @property
    def attachments_count(self):
        return len([attachment for attachment in self.attachments if not attachment.merged])


class Attachment(Base):
    __tablename__ = 'attachments'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(225))
    path: Mapped[str] = mapped_column(String(255))
    count: Mapped[int] = mapped_column(default=1)
    sana_item_number: Mapped[int] = mapped_column(
        ForeignKey('sana_items.number', ), nullable=True)
    config_id: Mapped[int] = mapped_column(
        ForeignKey('configs.id', ), nullable=True)

    sana_item: Mapped['SanaItem'] = relationship(back_populates='attachments')
    config: Mapped['Config'] = relationship(back_populates='attachment_value')
