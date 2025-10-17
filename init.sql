CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT NOT NULL,
        note TEXT NOT NULL,
        embedding TEXT NOT NULL  -- JSON encoded list of floats
    )
