from flask import Flask, render_template, request, send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_certificate', methods=['POST'])
def generate_certificate():
    name = request.form.get('name')
    
    # Create PDF in memory
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Title
    title = Paragraph("Certificate of Participation", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Body
    body = f"This certifies that <b>{name}</b> has successfully participated in the event."
    body_paragraph = Paragraph(body, styles['BodyText'])
    elements.append(body_paragraph)
    elements.append(Spacer(1, 12))

    # Add more elements if needed

    # Build PDF
    doc.build(elements)
    
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name='certificate.pdf', mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
