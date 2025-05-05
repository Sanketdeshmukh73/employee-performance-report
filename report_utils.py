# utils/report_utils.py

from fpdf import FPDF
import matplotlib.pyplot as plt


class PDFReport(FPDF):
    def __init__(self):
        super().__init__()
        self.primary_color = (0, 51, 102)       # Dark blue
        self.secondary_color = (230, 230, 230)  # Light gray

    def header(self):
        self.set_font("Arial", "B", 16)
        self.set_text_color(*self.primary_color)
        self.cell(0, 10, "Employee Performance Report", ln=True, align="C")
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(*self.primary_color)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_table(self, data):
        self.set_font("Arial", size=12)
        col_widths = [60, 60, 60]  # Adjust to fit A4 width

        # Header row
        self.set_fill_color(*self.primary_color)
        self.set_text_color(255, 255, 255)
        for i, item in enumerate(data[0]):
            self.cell(col_widths[i], 10, str(item),
                      border=1, fill=True, align='C')
        self.ln()

        # Data rows
        for i, row in enumerate(data[1:]):
            fill_color = self.secondary_color if i % 2 else (255, 255, 255)
            self.set_fill_color(*fill_color)
            self.set_text_color(0, 0, 0)
            for j, item in enumerate(row):
                self.cell(col_widths[j], 10, str(item),
                          border=1, fill=True, align='C')
            self.ln()


def generate_chart(df):
    avg_scores = df.groupby('Department')['Score'].mean()
    plt.figure(figsize=(6, 4))
    avg_scores.plot(kind='bar', color='skyblue')
    plt.title('Average Score by Department')
    plt.ylabel('Score')
    plt.tight_layout()
    plt.savefig("chart.png")
    plt.close()
