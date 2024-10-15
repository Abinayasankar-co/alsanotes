import json
import matplotlib.pyplot as plt
from pptx import Presentation
from pptx.util import Inches

class PowerPointGenerator:
    def __init__(self, json_data):
        self.data = json.loads(json_data)
        self.prs = Presentation()

    def create_presentation(self):
        # Create title slide
        self._add_title_slide(self.data["title"])

        # Create content slides
        for slide_data in self.data["slides"]:
            self._add_content_slide(slide_data)

        # Save the presentation
        self.prs.save('business_performance_presentation.pptx')
        print("PowerPoint with table, bar graph, and pie chart generated successfully!")

    def _add_title_slide(self, title_text):
        title_slide_layout = self.prs.slide_layouts[0]
        slide = self.prs.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = title_text
        subtitle.text = "Generated using Python"

    def _add_content_slide(self, slide_data):
        slide_layout = self.prs.slide_layouts[1]
        slide = self.prs.slides.add_slide(slide_layout)
        title = slide.shapes.title
        title.text = slide_data["title"]

        # Add content or table
        if "content" in slide_data:
            content_box = slide.shapes.placeholders[1].text_frame
            content_box.text = slide_data["content"]

        if "table_data" in slide_data:
            self._add_table(slide, slide_data["table_data"]["headers"], slide_data["table_data"]["rows"])

        if "bar_chart_data" in slide_data:
            # Create bar chart with dynamic title based on slide title
            image_path = "bar_chart.png"
            self._create_bar_chart(
                slide_data["bar_chart_data"]["categories"],
                slide_data["bar_chart_data"]["revenue"],
                slide_data["title"],
                image_path
            )
            slide.shapes.add_picture(image_path, Inches(2), Inches(3), Inches(6), Inches(3))

        if "pie_chart_data" in slide_data:
            # Create pie chart with dynamic title based on slide title
            image_path = "pie_chart.png"
            self._create_pie_chart(
                slide_data["pie_chart_data"]["categories"],
                slide_data["pie_chart_data"]["values"],
                slide_data["title"],
                image_path
            )
            slide.shapes.add_picture(image_path, Inches(2), Inches(3), Inches(6), Inches(3))

    def _add_table(self, slide, headers, rows):
        x, y, cx, cy = Inches(2), Inches(2), Inches(6), Inches(2)
        table = slide.shapes.add_table(len(rows) + 1, len(headers), x, y, cx, cy).table

        # Add headers
        for i, header in enumerate(headers):
            table.cell(0, i).text = header

        # Add rows
        for row_idx, row in enumerate(rows, start=1):
            for col_idx, cell_value in enumerate(row):
                table.cell(row_idx, col_idx).text = str(cell_value)

    def _create_bar_chart(self, categories, values, title, image_path):
        plt.figure(figsize=(5, 4))
        plt.bar(categories, values, color='blue')
        plt.xlabel('Quarter')
        plt.ylabel('Revenue ($)')
        plt.title(title)  # Title dynamically set based on slide title
        plt.savefig(image_path)
        plt.close()

    def _create_pie_chart(self, categories, values, title, image_path):
        plt.figure(figsize=(5, 4))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(title)  # Title dynamically set based on slide title
        plt.savefig(image_path)
        plt.close()

# Sample JSON Data (unchanged)
json_data = '''{
    "title": "Business Performance Report",
    "slides": [
        {
            "title": "Introduction",
            "content": "This report presents an overview of our business performance, focusing on revenue, expenses, and market share distribution."
        },
        {
            "title": "Revenue and Expenses Overview",
            "table_data": {
                "headers": ["Quarter", "Revenue ($)", "Expenses ($)", "Profit ($)"],
                "rows": [
                    ["Q1", 50000, 30000, 20000],
                    ["Q2", 60000, 35000, 25000],
                    ["Q3", 70000, 40000, 30000],
                    ["Q4", 80000, 45000, 35000]
                ]
            }
        },
        {
            "title": "Revenue Comparison - Bar Chart",
            "bar_chart_data": {
                "categories": ["Q1", "Q2", "Q3", "Q4"],
                "revenue": [50000, 60000, 70000, 80000]
            }
        },
        {
            "title": "Market Share - Pie Chart",
            "pie_chart_data": {
                "categories": ["Product A", "Product B", "Product C"],
                "values": [45, 30, 25]
            }
        }
    ]
}'''

# Usage
ppt_generator = PowerPointGenerator(json_data)
ppt_generator.create_presentation()
