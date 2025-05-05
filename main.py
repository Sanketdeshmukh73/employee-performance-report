# main.py
import pandas as pd
from utils.report_utils import PDFReport, generate_chart

# Read CSV
df = pd.read_csv("data.csv")

# Generate chart
generate_chart(df)

# Create PDF with enhanced design
pdf = PDFReport()
pdf.add_page()

# --- Summary Section ---
pdf.set_font("Arial", "B", 14)
pdf.set_text_color(0, 0, 0)  # Black text
pdf.cell(0, 10, "Key Performance Metrics", ln=True, align="C")
pdf.ln(8)  # Vertical spacing

# Metric details
pdf.set_font("Arial", size=12)
pdf.set_fill_color(240, 240, 240)  # Light gray background
pdf.cell(
    0, 10, f"   Average Score: {df['Score'].mean():.2f}", ln=True, fill=True)
pdf.cell(
    0, 10, f"   Top Performer: {df.loc[df['Score'].idxmax(), 'Name']}", ln=True, fill=True)
pdf.ln(15)

# --- Table Section ---
# Explicitly select columns to avoid extra data
table_data = [["Name", "Department", "Score"]] + \
    df[["Name", "Department", "Score"]].values.tolist()
pdf.add_table(table_data)
pdf.ln(10)  # Space after table

# --- Chart Section ---
# Calculate available space
remaining_space = 297 - pdf.get_y()  # A4 height = 297mm
chart_height = 80  # Fixed height for chart container

# Add new page if insufficient space
if remaining_space < chart_height + 20:
    pdf.add_page()

# Chart container styling
pdf.set_draw_color(200, 200, 200)  # Light gray border
pdf.rect(x=10, y=pdf.get_y() + 5, w=190, h=chart_height)
pdf.set_font("Arial", "I", 10)
pdf.cell(0, 5, "Department Performance Analysis", ln=True)

# Embed chart image
pdf.image("chart.png",
          x=15,  # Indent from left
          y=pdf.get_y() + 5,
          w=180,  # Match container width
          h=chart_height - 15)  # Leave space for title

# Save PDF
pdf.output("report.pdf")
print("Report generated successfully!")
