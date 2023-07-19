import unittest2 as unittest
from mercado_libre_data import MercadoLibreData

class TestMercadoLibreData(unittest.TestCase):
    def test_retrieve_data(self):
        # Create an instance of the MercadoLibreData class.
        ml_data = MercadoLibreData('El Camino de Santiago', 150)
        
        # Call the retrieve_data method.
        ml_data.retrieve_data()
        
        # Verify that the resulting DataFrame is not empty.
        self.assertGreater(len(ml_data.df), 0)

if __name__ == '__main__':
    unittest.main()