import google.generativeai as genai
import json

# Configure your Gemini API key
genai.configure(api_key="AIzaSyCmsmNqErhSOBBBX4w9E1cJ-QEA2kDGTxc")

# Load patient data
with open(r"C:\Users\nphal\fsda-genai_agenticai_project\Projects\Usecases\Claimsprocessing\patients_data.json", "r") as f:
    patients = json.load(f)

# Build a prompt for Gemini
def build_prompt(patients):
    return f"""
You are an insurance claim processing assistant. 
For each patient in the following data, analyze their CPT codes and check if they are covered under their insurance plan.
If a CPT code is not covered, mark it as 'Not Covered'.
Summarize patient details with a recommendation (Approve/Reject).

Patient Data (JSON):
{json.dumps(patients, indent=2)}

Return the summary in the following format:
[
  {{
    "patient_id": "...",
    "name": "...",
    "covered_codes": [...],
    "not_covered_codes": [...],
    "recommendation": "Approve/Reject",
    "reason": "..."
  }},
  ...
]
"""

prompt = build_prompt(patients)

# Generate content with Gemini
model = genai.GenerativeModel("gemini-1.5-pro")  # or latest available
response = model.generate_content(prompt)

# Print summary
print(response.text)
