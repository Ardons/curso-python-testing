import unittest

SERVER = "Server b"

class AllAssertsTests(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10,10,"Los valores no son iguales")
        self.assertEqual("Hola","hola","Los valores no son iguales")
        
    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertTrue(False, "El valor es Falso")
        
    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")
    
    def test_assert_in(self):
        self.assertIn(10, [1,2,3,10])
        self.assertNotIn(10, [1,2,3])
    
    def test_assert_dicts(self):
        self.assertDictEqual({
            "first_name": "Luis",
            "last_name": "Martinez"
            }, {
            "first_name": "Luis",
            "last_name": "Martinez"
            })
        self.assertSetEqual({1,2,3}, {1,2,3})
    
    #decoradores de unittest para saltar pruebas
    @unittest.skip("Trabajo en progreso, sera habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")
    
    @unittest.skipIf(SERVER == "Server b", "Saltado porque no estamos en el servidor correcto")
    def test_skip_if(self):
        self.assertEqual(100, 100)
    
    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100,150)