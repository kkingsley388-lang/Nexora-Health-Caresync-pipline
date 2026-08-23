
Dataset = {
  "Encounter" : {
     "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\encounters.csv", #r The r makes this a raw string, so Python treats the backslashes (\) in the Windows file path as normal characters. 
       "column_mappings" : {
       "Id" : "ENCOUNTER_ID",
       "START" : "APPOINTMENT_START_DATE_TIME",
       "STOP"  : "APPOINTMENT_END_DATE_TIME",
       "PATIENT": "PATIENT_ID",
       "ORGANIZATION" : "ORGANIZATION_ID",
       "PROVIDER"  : "PROVIDER_ID",
       "PAYER" : "PAYER_ID",
       "ENCOUNTERCLASS" : "ENCOUNTER_CLASS",
       "CODE" : "STANDARIZED_ENCOUNTER_CODE",
       "DESCRIPTION" : "ENCOUNTER_DESCRIPTION",
       "BASE_ENCOUNTER_COST" : "BASE_ENCOUNTER_COST",
       "TOTAL_CLAIM_COST"  : "TOTAL_CLAIM_COST",
       "PAYER_COVERAGE" : "PAYER_COVERAGE"
     }
  },

  "Condition/Diagnosis" :{
    "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\conditions.csv",
      "column_mappings" : {
       "START" : "DIAGNOSIS_START_DATE_TIME",
       "STOP" : "CONDITION_END_DATE_TIME",
       "PATIENT": "PATIENT_ID",
       "ENCOUNTER" : "ENCOUNTER_ID",
       "SYSTEM" : "CONDITION_C0DE_SYSTEM",
       "CODE" : "STANDARIZED_CONDITION_CODE",
       "DESCRIPTION" : "CONDITION_DESCRIPTION"
      }
  },


  "patient":{
    "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\patients.csv",
      "column_mappings" : {
        "Id" : "PATIENT_ID",
        "BIRTHDATE" : "DATE_OF_BIRTH",
        "DEATHDATE" : "DATE_OF_DEATH",
        "MARITAL"   : "MARITAL_STATUS",
        "RACE"      : "RACE",
        "ETHNICITY" : "ETHNICITY",
        "GENDER"    : "GENDER",
        "BIRTHPLACE": "PLACE_OF_BIRTH",
        "ADDRESS"   : "PATIENT_ADDRESS",
        "CITY"      : "PATIENT_CITY",
        "STATE"     : "PATIENT_STATE",
        "COUNTY"    : "PATIENT_COUNTY"
      }     
  },

  "Organization" : {
    "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\organizations.csv",
       "column_mappings": {
       "Id"      : "ORGANIZATION_ID",
       "NAME"    : "ORGANIZATION_NAME",
       "ADDRESS" : "ORGANIZATION_ADDRESS",
       "CITY"    : "ORGANIZATION_CITY",
       "STATE"   : "ORGANIZATION_STATE",
       "ZIP"     : "ORGANIZATION_ZIP_CODE"
      }
  },

  "Provider" : {
    "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\providers.csv",
         "column_mappings": {
           "Id"           : "PROVIDER_ID",
           "ORGANIZATION" : "ORGANIZATION_ID",
           "NAME"         : "PROVIDER_NAME",
           "GENDER"       : "PROVIDER_GENDER",
           "SPECIALITY"   : "PROVIDER_SPECIALITY",
           "CITY"         : "PROVIDER_PRACTICE_CITY",
           "STATE"        : "PROVIDER_PRACTICE_STATE"
         }
  },

  "Payer" : {
     "file_name" : r"C:\Users\resu\Desktop\Nexora-Health-Caresync-pipline\data\payers.csv",
          "column_mappings" : {
            "Id" : "PAYER_ID",
            "NAME" : "PAYER_NAME",
            "OWNERSHIP" : "PAYER_OWNERSHIP_TYPE",
            "ADDRESS"   : "PAYER_ADDRESS",
            "CITY"      : "PAYER_CITY",
            "STATE_HEADQUARTERED": "PAYER_HEADQUARTERS_STATE"
          }
  }
  
}

#rules = Dataset["Encounter"] # rules = { "file_name" : "patients.csv",
 #     "column_mappings" : {
 #       "ID" : "PATIENT_ID",
 #       "BIRTHDATE" : "DATE_OF_BIRTH",
 #       "DEATHDATE" : "DATE_OF_DEATH",}}
#file_path = rules["file_name"] # save_as = "patients.csv"
#mapping = rules["column_mappings"] #mapping = {
 #       "ID" : "PATIENT_ID",
 #       "BIRTHDATE" : "DATE_OF_BIRTH",
 #       "DEATHDATE" : "DATE_OF_DEATH",}
#print(Save_as + "=" + str(mapping))

#print(list(mapping.keys())) 

#print(Dataset["Encounter"]["file_name"])


#print(Dataset["Encounter"].get("file_name"))

#print(Dataset["Encounter"]["file_name"])




print(Dataset["Payer"]["file_name"])
#print(Dataset["Payer"]["column_mappings"])
#print(Dataset)