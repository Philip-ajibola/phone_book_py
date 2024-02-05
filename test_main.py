from unittest import TestCase
import main


class Test(TestCase):
    def test_add_new_contact(self):
        main.clear_list()
        main.collect_info("philip","09027531222","muri abiola","philip_ajibola")
        result = main.add_new_contact()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()

        expected = "contact saved"
        self.assertEqual(result,expected)



    def test_function_display_all_contact(self):
        main.clear_list()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()

        result1 = main.display_all_contact()
        expected = "philip\nphilip\n"
        self.assertEqual(result1,expected)

    def test_function_delete_contact(self):
        main.clear_list()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()
        main.collect_info("Ajibola", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()

        result1 = main.delete_contact("philip")
        expected = "philip Contact Deleted"
        self.assertEqual(result1,expected)

    def test_that_after_deleting_contact_is_deleted(self):
        main.clear_list()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()
        main.collect_info("Ajibola", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()

        result = main.delete_contact("philip")
        result1 = main.display_all_contact()
        expected = "Ajibola\n"
        self.assertEqual(result1,expected)

    def test_function_edit_contact(self):
        main.clear_list()
        main.collect_info("philip", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()
        main.collect_info("Ajibola", "09027531222", "muri abiola", "philip_ajibola")
        result = main.add_new_contact()

        result = main.edit_contact("philip","bobby")
        self.assertEqual("Contact Edited",result)
        result1 = main.display_all_contact()
        expected = "bobby\nAjibola\n"
        self.assertEqual(result1,expected)


