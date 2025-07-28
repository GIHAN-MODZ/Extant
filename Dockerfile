RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-sin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
