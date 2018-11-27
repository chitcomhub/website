from django.test import TestCase
from .models import Chiter


class ChitersTest(TestCase):

    def test_uses_chiters_template(self):
        response = self.client.get('/chiters/')
        self.assertTemplateUsed(response, 'chiters/chiters.html')

    def test_uses_register_template(self):
        response = self.client.get('/chiters/register/')
        self.assertTemplateUsed(response, 'chiters/register.html')

    def test_uses_message_template(self):
        response = self.client.get('/chiters/message/')
        self.assertTemplateUsed(response, 'chiters/message.html')

    def test_saving_and_retrieving_chiters(self):
        first_chiter = Chiter(
            name="John", nickname="Doe",
            direction="Dinosaur",technology="Python"
        )
        first_chiter.save()

        second_chiter = Chiter(
            name="Alucard", nickname="SonOfDracula",
            direction="Vampire", technology="Teeth"
        )
        second_chiter.save()

        saved_chiters = Chiter.objects.all()
        self.assertEqual(saved_chiters.count(), 2)

        first_saved_chiter = saved_chiters[0]
        second_saved_chiter = saved_chiters[1]
        self.assertEqual(
            (
                first_saved_chiter.name,
                first_saved_chiter.nickname,
                first_saved_chiter.direction,
                first_saved_chiter.technology
            ),

            ("John", "Doe", "Dinosaur", "Python")
        )
        self.assertEqual(
            (
                second_saved_chiter.name,
                second_saved_chiter.nickname,
                second_saved_chiter.direction,
                second_saved_chiter.technology
            ),

            ("Alucard", "SonOfDracula", "Vampire", "Teeth")
        )


    def test_can_save_a_POST_request(self):
        response = self.client.post('/chiters/register/', data={
            'name':'Lom-Ali', 'nickname':'Leon-Ali', 'direction':'Backend', 'technology':'Python'
        })

        self.assertEqual(Chiter.objects.count(), 1)
        new_chiter = Chiter.objects.first()
        self.assertEqual(new_chiter.name, 'Lom-Ali')

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/chiters/message')
