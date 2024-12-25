import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Function to generate the certificate PDF
def generate_certificate(name, duration, project):
    # Ensure directory for certificates exists
    output_dir = "certificates"
    os.makedirs(output_dir, exist_ok=True)
    
    # Format filename and create PDF canvas
    file_name = os.path.join(output_dir, f"Certificate_{name.replace(' ', '_')}.pdf")
    c = canvas.Canvas(file_name, pagesize=A4)

    # Design the certificate layout
    c.setFont("Helvetica-Bold", 24)
    c.drawString(150, 700, "Certificate of Internship")

    c.setFont("Helvetica", 14)
    c.drawString(100, 650, f"This is to certify that {name} has successfully completed their internship.")
    c.drawString(100, 630, f"Internship Duration: {duration}")
    c.drawString(100, 610, f"Project Title: {project}")

    # Save the PDF file
    c.save()
    print(f"Certificate generated and saved as {file_name}")

# Function to get details from GUI and generate the certificate
def generate_certificate_gui():
    name = name_entry.get()
    duration = duration_entry.get()
    project = project_entry.get()
    
    if not name or not duration or not project:
        messagebox.showwarning("Input Error", "All fields are required")
    else:
        generate_certificate(name, duration, project)
        messagebox.showinfo("Success", f"Certificate for {name} has been generated.")

# Set up GUI
root = tk.Tk()
root.title("Certificate Generator")

# Labels and entry fields
tk.Label(root, text="Intern's Name").grid(row=0)
tk.Label(root, text="Duration").grid(row=1)
tk.Label(root, text="Project Title").grid(row=2)

name_entry = tk.Entry(root)
duration_entry = tk.Entry(root)
project_entry = tk.Entry(root)

name_entry.grid(row=0, column=1)
duration_entry.grid(row=1, column=1)
project_entry.grid(row=2, column=1)

# Generate button
tk.Button(root, text="Generate Certificate", command=generate_certificate_gui).grid(row=3, columnspan=2)

# Run the application
root.mainloop()