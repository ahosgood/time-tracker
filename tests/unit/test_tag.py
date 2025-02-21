from datetime import datetime

from app.models import Tag


def test_new_tag(client, new_user):
    new_tag = Tag(user_id=new_user.id, name="New Tag")
    assert new_tag.user_id == new_user.id
    assert new_tag.name == "New Tag"
    assert type(new_tag.created_at) == datetime
    assert new_tag.updated_at is None
