from dataset_specs import Dataset

#def dataset(dataset_key):
#  file = Dataset[dataset_key]
#  mappings = file["column_mappings"]
#  return mappings

#whatever = dataset("Payer")
#print(whatever)

whatever = Dataset["Payer"].get("file_name")
print(whatever)