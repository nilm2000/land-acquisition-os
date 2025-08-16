"""
Generates PDF reports for parcels/projects.
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def generate_parcel_pdf(parcel_data: dict) -> bytes:
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)

    c.drawString(72, 750, f"Parcel Report: {parcel_data.get('apn', 'Unknown')}")
    c.drawString(72, 730, f"Address: {parcel_data.get('address', '')}")
    c.drawString(72, 710, f"Acreage: {parcel_data.get('acreage', '')}")
    c.drawString(72, 690, f"Owner: {parcel_data.get('owner', '')}")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer.getvalue()
