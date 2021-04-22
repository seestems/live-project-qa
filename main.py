import textract
import re
import pandas as pd

PAR_MIN_LEN = 200


def extract_text(file_path):
    text = textract.parsers.process(file_path).decode('utf-8')
    paragraphs_re = re.findall('(.+?(\n|\r\n){2,}|.+?$)', text, re.DOTALL)

    paragraphs = [p[0] for p in paragraphs_re if len(p[0]) >= PAR_MIN_LEN]
    paragraphs_data = pd.DataFrame(paragraphs, columns=["Paragraph"])

    return paragraphs_data


if __name__ == '__main__':
    paragraphs_data = extract_text("data/200309-sustainable-finance-teg-final-report-taxonomy-annexes_en.pdf")
    paragraphs_data.to_parquet("data/paragraphs.parquet")
