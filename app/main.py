from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from database import get_db_connection
from ai_service import analyze_email

app = FastAPI()

class Inbound(BaseModel):
    customer_email : str
    support_email : str
    subject_line : str
    email_body : str
    email_received_at : datetime
    GAS_fired_at : datetime

@app.post("/api/v1/tickets/inbound")
def read_inbound(inbound_email : Inbound):
    db_conn = get_db_connection()

    cur = db_conn.cursor()
    cur.execute("INSERT INTO Inbound_Emails (customer_email, support_email, subject_line, email_body, email_received_at, GAS_fired_at) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;", (inbound_email.customer_email, inbound_email.support_email, inbound_email.subject_line, inbound_email.email_body, inbound_email.email_received_at, inbound_email.GAS_fired_at))
    returned_id = cur.fetchone()[0]

    ai_json_response = analyze_email(inbound_email.subject_line, inbound_email.email_body)
    
    db_conn.commit()
    cur.close()
    db_conn.close()
    
    return {"status": "Success", "message": "Email ingested", "internal_id": returned_id}