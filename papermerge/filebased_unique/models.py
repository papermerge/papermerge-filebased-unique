from django.core.exceptions import ValidationError
from papermerge.core.models import Document, AbstractDocument


class DocumentPart(AbstractDocument):
    """
    Extend papermerge document model with extra validation.

    self.clean() validation method is called whenever document instance
    is saved.
    """

    def clean(self):
        """
        Check for file_name duplicates.

        Raise an error in if > 1 documents have same file_name
        """
        file_name = self.get_file_name()
        if Document.objects.filter(file_name=file_name).count() > 1:
            raise ValidationError(
                "Documents file_name duplicates detected"
            )
