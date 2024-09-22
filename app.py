from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

@app.route('/')
def home():
    return render_template('portfolio.html')  # Replace with your actual template name

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Create the email content
    subject = f"New contact form submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    
    # Send the email (replace with your actual email configuration)
    try:
        send_email(subject, body)
        flash("Your message has been sent successfully!", "success")
    except Exception as e:
        flash(f"An error occurred: {e}", "error")

    return redirect(url_for('home'))

def send_email(subject, body):
    sender_email = 'baig82880@outlook.com'
    receiver_email = 'baig82880@outlook.com'  # Use your email that forwards to mobile
    password = 'Farhan@13'

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Update SMTP settings for Outlook
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
