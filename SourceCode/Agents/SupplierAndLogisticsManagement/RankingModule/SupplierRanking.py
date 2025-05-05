import pandas as pd

pd.options.mode.copy_on_write = True


def ranking(part_name, auto_parts_data_path, supplier_data_path):
    # Load the data from CSV files
    auto_parts_data = pd.read_csv(auto_parts_data_path)
    supplier_data = pd.read_csv(supplier_data_path)

    # Filter data for the given part
    part_data = auto_parts_data[auto_parts_data['partName'] == part_name]

    # Merge with supplier data to get defect rates
    merged_data = pd.merge(part_data, supplier_data, left_on='supplierId', right_on='supplier_id')

    # Normalize the defect rates and rates
    merged_data['normalized_defect_rate'] = merged_data['defect_rates'] / merged_data['defect_rates'].max()
    merged_data['normalized_rate'] = merged_data['rate'] / merged_data['rate'].max()

    # Calculate the AHP score (lower is better)
    merged_data['ahp_score'] = merged_data['normalized_defect_rate'] + merged_data['normalized_rate']

    # Sort by AHP score
    ranked_suppliers = merged_data.sort_values(by='ahp_score').head(5)

    return ranked_suppliers[
        ['supplier_id', 'supplier_name', 'rate', 'defect_rates', 'country', 'ahp_score', 'latitude', 'longitude',
         'minimum_quantity']]
