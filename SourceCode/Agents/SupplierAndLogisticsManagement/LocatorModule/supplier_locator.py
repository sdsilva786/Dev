import pandas as pd
from geopy.distance import geodesic


class SupplierLocator:
    def __init__(self, dataframe):
        """
        Initialize the SupplierLocator with a pandas DataFrame containing suppliers' data.
        The DataFrame should contain columns: supplier_name, latitude, longitude.
        """
        self.suppliers = self.load_suppliers_from_dataframe(dataframe)

    def load_suppliers_from_dataframe(self, dataframe):
        """
        Load suppliers from a pandas DataFrame.
        """
        suppliers = []
        for index, row in dataframe.iterrows():
            suppliers.append((
                             row['supplier_id'], row['supplier_name'], row['rate'], row['defect_rates'], row['country'],
                             row['ahp_score'], row['latitude'], row['longitude'], row['minimum_quantity']))
        return suppliers

    def calculate_distance(self, location1, location2):
        """
        Calculate the distance between two locations.
        Each location should be a tuple containing (latitude, longitude).
        """
        return geodesic(location1, location2).kilometers

    def find_nearest_supplier(self, location):
        """
        Find the nearest supplier to the given location.
        The location should be a tuple containing (latitude, longitude).
        """
        nearest_supplier = None
        shortest_distance = float('inf')

        for supplier in self.suppliers:
            supplier_location = (supplier[2], supplier[3])
            distance = self.calculate_distance(location, supplier_location)
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_supplier = supplier

        return nearest_supplier

    def find_nearest_suppliers(self, location, n):
        """
        Find the given number of nearest suppliers to the specified location.
        The location should be a tuple containing (latitude, longitude).
        n specifies the number of nearest suppliers to return.
        Returns a pandas DataFrame with the nearest suppliers and their distances.
        """
        distances = []

        for supplier in self.suppliers:
            supplier_location = (supplier[6], supplier[7])  # Adjusted indices for latitude and longitude
            distance = self.calculate_distance(location, supplier_location)
            distances.append((supplier, distance))

        # Sort suppliers by distance
        distances.sort(key=lambda x: x[1])

        # Extract the top n nearest suppliers
        nearest_suppliers = distances[:n]

        # Create a DataFrame for the nearest suppliers
        data = [
            {
                "supplier_id": supplier[0],
                "supplier_name": supplier[1],
                "rate": supplier[2],
                "defect_rates": supplier[3],
                "country": supplier[4],
                "ahp_score": supplier[5],
                "latitude": supplier[6],
                "longitude": supplier[7],
                "minimum_quantity": supplier[8],
                "distance_kms": distance
            }
            for supplier, distance in nearest_suppliers
        ]

        return pd.DataFrame(data)
