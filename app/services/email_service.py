def send_email(to, subject, body):
    server = "smtp.example.com"
    port = 587
    email = "noreply@example.com"
    password = "emailpassword"
    import smtplib
    try:
        smtp_obj = smtplib.SMTP(server, port)
        smtp_obj.starttls()
        smtp_obj.login(email, password)
        message = f"Subject: {subject}\n\n{body}"
        smtp_obj.sendmail(email, to, message)
        smtp_obj.quit()
        return True
    except Exception as e:
        print("Failed to send email:", e)
        return False
