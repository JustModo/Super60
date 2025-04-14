import pandas as pd
import re

# Load your Excel file
df = pd.read_excel("D:\\Super60\\PythonBootcamp\\Kritharth\\Knime\\test.xlsx", sheet_name="Consolidated Chennai Data")

# Function to validate Gmail IDs
def is_valid_gmail(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
    return bool(re.match(pattern, email))

# Generalized function to correct Gmail domain
def correct_gmail(email):
    if "@" in email:
        username, _ = email.split("@", 1)
        return f"{username}@gmail.com"
    return email  # Return as-is if the format is invalid

# Check validity and apply corrections
df['Valid Gmail'] = df['Email'].apply(is_valid_gmail)
df['Corrected Email'] = df['Email'].apply(lambda x: correct_gmail(x) if not is_valid_gmail(x) else x)

# Display invalid emails for manual review if needed
invalid_emails = df[~df['Valid Gmail']]
print("Invalid Emails for Review:")
print(invalid_emails[['Email', 'Corrected Email']])

# Save the corrected file
df.to_excel("corrected_emails.xlsx", index=False)
print("Corrected emails saved to 'corrected_emails.xlsx'")
