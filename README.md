# Resume.io to PDF

Download your resume from [resume.io](https://resume.io) as a PDF file. 

<div align="center"><img width="1430" height="636" alt="image" src="https://github.com/user-attachments/assets/941b9485-62f6-4e77-b9f2-722d644e4926" width="700" /></a></div>

Open the application, enter your resume `renderingToken` and click the download button. 
It will automatically download your resume as image files, merge them, inject the hyperlinks,
convert to a PDF file and run OCR to extract the text.

### How to find your renderingToken

Resumes: https://resume.io/api/app/resumes

Cover Letters: https://resume.io/api/app/cover-letters/

You will see a list of your resumes. Find the one you want to download and get the `renderingToken` from 
the payload.

### How to run the application

Clone the repository
```bash
git clone https://github.com/pablomorillas02/resumeio-to-pdf.git
```
    
Go to the project's root folder
```bash
cd resumeio-to-pdf
```

Build the image
```bash
docker build -t resumeio-to-pdf .
```

Run the container
```bash
docker run -p 8000:8000 resumeio-to-pdf
```

Open your browser and access http://localhost:8000

### Disclaimer

Please be advised that this application is designed for preview purposes only. 

By utilizing this tool, you explicitly agree to adhere to all applicable laws and regulations governing the use of such services. 
The creators of this application absolve themselves of any responsibility for potential damages or harm resulting from its utilization.

It is essential to visit the pricing page on Resume.io to explore fair and affordable options for accessing the resume downloading service directly through the official channels provided by Resume.io. 
The creators emphasize the importance of supporting the platform by subscribing to their services and discourage the use of this application as a substitute for legitimate and paid access.
