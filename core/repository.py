from sqlalchemy.orm import Session
from sqlalchemy import text

if __package__ == 'core':
    from . import models
else:
    import models


class PostRepository:

    @staticmethod
    def delete(db: Session, post_date: str):
        post = db.get(models.Post, post_date)
        sana_items_result = db.execute(text(
            "SELECT number FROM sana_items WHERE post_date = :post_date"), {"post_date": post.date})
        sana_item_numbers = [row[0]
                             for row in sana_items_result.fetchall()]
        if sana_item_numbers:
            for item_number in sana_item_numbers:
                db.execute(text("DELETE FROM attachments WHERE sana_item_number = :item_number"), {
                    "item_number": item_number})
            db.execute(text("DELETE FROM sana_items WHERE post_date = :post_date"), {
                "post_date": post.date})
        db.delete(post)
        db.commit()
        return post


class SanaItemRepository:
    pass


class AttachmentRepository:
    pass


class ConfgiRepository:
    pass
