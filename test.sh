#!/bin/bash

echo "Ensure your FastAPI app is running on http://127.0.0.1:8000"
echo "--------------------------------------------------------------------------------"

# Helper function for POST requests
post_note() {
    local patient_id=$1
    local note_content=$2
    echo "Adding note for $patient_id..."
    curl -X POST "http://127.0.0.1:8000/add_note" \
         -H "Content-Type: application/json" \
         -H "X-API-Token: mysecrettoken123"\
         -d "{\"patient_id\": \"$patient_id\", \"note\": \"$note_content\"}" 
    echo ""
    sleep 0.1
}

echo "--- 1. Testing POST /add_note (Adding 11 Total Notes) ---"

post_note "P001" "Patient reports chest pain and shortness of breath."

# Note 2: General Illness
post_note "P002" "Client presents with a mild fever, persistent headache, and muscle aches for 48 hours."
# Note 3: Acute Pain
post_note "P003" "Emergency visit due to severe, cramping abdominal pain localized in the lower right quadrant."
# Note 4: Respiratory (Distinct from P001)
post_note "P004" "Reports a hacking cough that has lasted for one week and a persistent sore throat."
# Note 5: Injury
post_note "P005" "Diagnosis of a severely sprained ankle from a slip and fall incident yesterday afternoon."
# Note 6: Chronic Care
post_note "P006" "Routine follow-up appointment to review medication for chronic high blood pressure."
# Note 7: General Symptom
post_note "P007" "Patient reports long-term extreme fatigue and general malaise, affecting daily life."
# Note 8: Administrative
post_note "P008" "Request for an urgent prescription refill for their thyroid medication."
# Note 9: Dermatology
post_note "P009" "Developing a raised, red rash on the right arm with significant, intense itching."
# Note 10: Respiratory (Semantically CLOSE to P001 for good search result)
post_note "P010" "Admitted due to acute respiratory distress, presenting with audible wheezing and difficulty breathing."
# Note 11: Preventive Care
post_note "P011" "Routine annual physical examination and blood work completed. All vitals are stable."
echo ""
echo "--- 2. Testing GET /search_notes (Querying for Top 3) ---"
echo "===================================================================================="
curl -H "X-API-Token: mysecrettoken123" \
"http://127.0.0.1:8000/search_notes?q=difficulty%20getting%20enough%20air"
echo "===================================================================================="
curl -H "X-API-Token: mysecrettoken123" \
     "http://127.0.0.1:8000/search_notes?q=prescription%20renewal%20for%20hypertension&top_k=3"
echo "===================================================================================="
curl -H "X-API-Token: mysecrettoken123" \
     "http://127.0.0.1:8000/search_notes?q=accident%20after%20falling%20and%20hurting%20ankle&top_k=3"
echo "===================================================================================="
echo ""
echo ""
echo "--- Test Complete ---"
