from django.test import TestCase
from myapp.models import histobj

class histobjTestCase(TestCase):
    def setUp(self):
        histobj.objects.create(cmd_action="testingaction", cmd_target="roar")
    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        lion = histobj.objects.get(cmd_action="testingaction")
        self.assertEqual(lion.cmd_target, 'roar')
