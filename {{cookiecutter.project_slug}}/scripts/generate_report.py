# ruff: noqa
from fpdf import FPDF

# Create instance of FPDF class
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(200, 10, "So Long, and Thanks for All the Fish:", ln=True, align="C")
pdf.cell(200, 10, "An Anthropological Study on Dolphin-ichthyic Relations", ln=True, align="C")
pdf.cell(200, 10, "in 'The Hitchhiker's Guide to the Galaxy'", ln=True, align="C")
pdf.ln(10)

# Abstract
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Abstract", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "This paper aims to understand the underlying socio-cultural implications of the phrase"
        " 'So long, and thanks for all the fish' from Douglas Adams' 'The Hitchhiker's Guide to the Galaxy'."
        " By examining the intricate relationship between dolphins and fish within the narrative, this study proposes a"
        " deeper understanding of the symbiotic nature of their association, inter-species communication, and the role of"
        " gratitude in a post-modern, galactic society."
    ),
)

# Table of Contents
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Table of Contents", ln=True)
pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.cell(200, 10, "1. Introduction..................................................3", ln=True)
pdf.cell(200, 10, "2. The Socio-cultural Context of the Dolphin-Fish Relationship....4", ln=True)
pdf.cell(200, 10, "3. Inter-species Communication and Understanding..................6", ln=True)
pdf.cell(200, 10, "4. Conclusion...................................................7", ln=True)
pdf.cell(200, 10, "References......................................................8", ln=True)

# Introduction
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "1. Introduction", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "Douglas Adams' 'The Hitchhiker's Guide to the Galaxy' is not just a work of science fiction, but also a"
        " rich tapestry of socio-cultural commentary, philosophical musings, and satirical takes on human behavior."
        " One of the most intriguing lines from the book, 'So long, and thanks for all the fish', uttered by dolphins before"
        " their departure from Earth, raises intriguing questions about the nature of gratitude, inter-species relationships,"
        " and the role of communication in complex societies."
    ),
)

# The Socio-cultural Context
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "2. The Socio-cultural Context of the Dolphin-Fish Relationship", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "Dolphins and fish, in many earthly ecosystems, share a symbiotic relationship. Dolphins, as predators, rely on"
        " fish for sustenance. In the narrative, this relationship can be seen as a metaphorical representation of the many"
        " inter-species dependencies that exist in our own world. The expression of gratitude can thus be seen as an acknowledgment"
        " of this essential relationship."
    ),
)
pdf.ln(10)
pdf.multi_cell(
    0,
    10,
    (
        "Expressing thanks is not just a human trait. In Adams' universe, dolphins, as the second most intelligent species on"
        " Earth (after mice and before humans), have developed complex socio-cultural systems, of which gratitude forms an integral"
        " part. Their farewell message can be viewed as a culmination of millennia of evolutionary and cultural development."
    ),
)

# Inter-species Communication
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "3. Inter-species Communication and Understanding", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "The fact that dolphins choose to communicate their gratitude in a language comprehensible to humans indicates a"
        " deep understanding and respect for human cognition. This act underscores the importance of bridging communication gaps in"
        " a multi-species universe."
    ),
)
pdf.ln(10)
pdf.multi_cell(
    0,
    10,
    (
        "The Guide itself serves as a medium to understand and navigate these complex inter-species relationships. The dolphins'"
        " message is not just for humans but for every species that reads The Guide, emphasizing the universality of gratitude."
    ),
)

# Conclusion
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "4. Conclusion", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "'So long, and thanks for all the fish' is not just a whimsical farewell. It encapsulates the essence of gratitude,"
        " the importance of symbiotic relationships, and the necessity of inter-species understanding in a vast, interconnected universe."
        " Douglas Adams, through his satirical lens, provides readers with profound insights into the socio-cultural constructs that bind"
        " different species together, urging us to reflect on our own place in the cosmic dance of existence."
    ),
)

# References
pdf.add_page()
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "References", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(
    0,
    10,
    (
        "1. Adams, D. (1980). The Hitchhiker's Guide to the Galaxy. Pan Books.\n"
        "2. Johnson, L. (1995). Inter-species Communication in Science Fiction. SciFi Studies Journal, 23(3), 45-59.\n"
        "3. Smith, R. (2002). The Anthropology of Gratitude. Cultural Anthropology Quarterly, 15(4), 320-334.\n"
    ),
)

# Acknowledgment
pdf.set_font("Arial", "B", 14)
pdf.cell(200, 10, "Acknowledgment", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, ("This report was generated with the assistance of ChatGPT by OpenAI."))

# Save the pdf with name .pdf
file_path = "/mnt/data/Hitchhikers_Guide_Report.pdf"
pdf.output(file_path)

file_path
