import random
import factory
from .models import Kategorija, Aktivnost, Prijava

factory.Faker._DEFAULT_LOCALE = "hr_HR"
KATEGORIJE = [
    "Ekologija",
    "Sport",
    "Humanitarno",
    "Zdravlje",
    "Obrazovanje",
    "Kultura",
    "Zajednica",
    "Pomoć starijima",
    "Rad s djecom",
    "Zaštita životinja"
]

class KategorijaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Kategorija

    naziv = factory.Iterator(KATEGORIJE)

NAZIVI = [
    "Čišćenje gradske plaže.",
    "Prikupljanje hrane za potrebite.",
    "Organizacija radionice za djecu.",
    "Sadnja drveća u parku.",
    "Pomoć starijima u svakodnevnim aktivnostima."
]

class AktivnostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Aktivnost

    naziv_aktivnosti = factory.Iterator(NAZIVI)
    opis = factory.Faker("text")
    datum = factory.Faker("date")
    kategorija = factory.Iterator(Kategorija.objects.all())


class PrijavaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Prijava

    ime = factory.Faker("first_name")
    prezime = factory.Faker("last_name")
    aktivnost = factory.Iterator(Aktivnost.objects.all())
