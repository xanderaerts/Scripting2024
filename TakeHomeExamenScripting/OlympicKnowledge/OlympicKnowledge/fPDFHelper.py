from fpdf import FPDF

class PDF(FPDF):
    def title(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'OlympicKnowledge', 0, 1, 'C')
        self.ln(10)

    def add_image(self, image_path, x, y, w, h):
        self.image(image_path, x, y, w, h)

    def add_text(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)
        self.ln()
    
    def add_bulleted_list(self, items, x, y, w):
        self.set_xy(x, y)
        for item in items:
            parts = item.split(' ', 1)
            first_word = parts[0]
            rest_of_text = parts[1] if len(parts) > 1 else ''
            self.set_font('Arial', 'B', 12)
            self.cell(10, 10, u'\u2022', 0, 0, 'L')
            self.cell(0, 10, first_word, 0, 0, 'L')
            self.set_font('Arial', '', 12)
            self.cell(0, 10, ' ' + rest_of_text, 0, 1, 'L')
        self.ln()

def create_pdf(title,filename, image_path, text):
    pdf = PDF()
    pdf.add_page()

    pdf.set_title(title) 

    pdf.add_image(image_path, 10, 40, 100, 100)

    pdf.add_text(text)

    pdf.output(filename)
