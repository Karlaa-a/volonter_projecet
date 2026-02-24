from django.db import transaction
from django.core.management.base import BaseCommand

from volonteri.models import Kategorija, Aktivnost, Prijava
from volonteri.factory import (
    KategorijaFactory,
    AktivnostFactory,
    PrijavaFactory,
)

NUM_KATEGORIJA = 10
NUM_AKTIVNOSTI = 5
NUM_PRIJAVA = 12


class Command(BaseCommand):
    help = "Generira testne podatke"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Brišem stare podatke...")
        models = [Prijava, Aktivnost, Kategorija]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Stvaram nove podatke...")

        KategorijaFactory.create_batch(NUM_KATEGORIJA)
        AktivnostFactory.create_batch(NUM_AKTIVNOSTI)
        PrijavaFactory.create_batch(NUM_PRIJAVA)

        self.stdout.write(self.style.SUCCESS("Gotovo!"))
