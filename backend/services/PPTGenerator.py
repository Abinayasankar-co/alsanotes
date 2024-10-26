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
        self.prs.save('/pptx/business_performance_presentation.pptx')
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
            for content_item in slide_data["content"]:
                content_box = slide.shapes.placeholders[1].text_frame
                content_box.text = content_item["text"]

        if "table_data" in slide_data:
            self._add_table(slide, slide_data["table_data"]["headers"], slide_data["table_data"]["rows"])

        if "chart" in slide_data:
            chart_type = slide_data["chart_type"]
            if chart_type == "bar":
                self._add_bar_chart(slide, slide_data)
            elif chart_type == "pie":
                self._add_pie_chart(slide, slide_data)

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

    def _add_bar_chart(self, slide, slide_data):
        image_path = "bar_chart.png"
        categories = list(slide_data["data"].keys())
        values = list(slide_data["data"].values())
        self._create_bar_chart(categories, values, slide_data["title"], image_path)
        slide.shapes.add_picture(image_path, Inches(2), Inches(3), Inches(6), Inches(3))

    def _add_pie_chart(self, slide, slide_data):
        image_path = "pie_chart.png"
        categories = list(slide_data["data"].keys())
        values = list(slide_data["data"].values())
        self._create_pie_chart(categories, values, slide_data["title"], image_path)
        slide.shapes.add_picture(image_path, Inches(2), Inches(3), Inches(6), Inches(3))

    def _create_bar_chart(self, categories, values, title, image_path):
        plt.figure(figsize=(5, 4))
        plt.bar(categories, values, color='blue')
        plt.xlabel('Category')
        plt.ylabel('Values')
        plt.title(title)
        plt.savefig(image_path)
        plt.close()

    def _create_pie_chart(self, categories, values, title, image_path):
        plt.figure(figsize=(5, 4))
        plt.pie(values, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(title)
        plt.savefig(image_path)
        plt.close()




#Example Usage
json_data = " "
ppt_generator = PowerPointGenerator(json_data)
ppt_generator.create_presentation()
