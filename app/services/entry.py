from app.models.entry import Title, Entry


class EntryService():
    def __init__(self):
        pass

    @staticmethod
    def _clear_content(value):
        # TODO: Clear Non-Ascii Characters
        return value

    def create_title(self, title, *args, **kwargs):
        title = self._clear_content(title)
        title_object = Title.query.filter_by(name=title).filter_by(is_active=True).first()

        if title_object:
            return title_object

        title_object = Title()
        title_object.name = title
        title_object.save()

        return title_object

    def delete_title(self, title, *args, **kwargs):
        title = self._clear_content(title)
        title_object = Title.query.filter_by(title=title).filter_by(is_active=False).first()

        if title_object:
            title_object.is_active = False
            title_object.save()

        return True

    def get_title(self, title):
        title = self._clear_content(title)
        title_object = Title.query.filter_by(name=title).filter_by(is_active=True).first()

        if title_object:
            return title_object

        return None

    def create_entry(self, title, entry, user, *args, **kwargs):
        title = self._clear_content(title)
        entry = self._clear_content(entry)

        title_object = self.create_title(title)

        entry_object = Entry()
        entry_object.user = user
        entry_object.content = entry
        entry_object.title = title_object
        entry_object.save()

        return entry_object

    def delete_entry(self):
        pass
