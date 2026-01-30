# HTML to PDF Converter - Azure Static Web App

A serverless HTML to PDF conversion application using **Python + WeasyPrint** deployed on Azure Static Web Apps.

## 🎯 Inspired By Your Code

This application uses the **exact same PDF conversion logic** as in your Streamlit app:

```python
def convert_html_to_pdf(html_string):
    """Convert HTML string to PDF bytes using WeasyPrint"""
    # ✅ WeasyPrint respecte beaucoup mieux le CSS
    pdf_bytes = HTML(string=html_string).write_pdf()
    return pdf_bytes
```

**Source:** `streamlit_app/ui/download_components.py`

## 📁 Project Structure

```
html-to-pdf-azure/
├── public/                          # Static web app frontend
│   ├── index.html                   # Main UI
│   └── staticwebapp.config.json     # Azure SWA configuration
│
├── api/                             # Azure Functions backend (Python)
│   ├── convert_to_pdf/
│   │   ├── __init__.py              # PDF conversion function
│   │   └── function.json            # Function configuration
│   ├── requirements.txt             # Python dependencies (WeasyPrint)
│   └── host.json                    # Functions runtime config
│
└── README.md                        # This file
```

## 🚀 Features

- ✅ **Python-based** PDF conversion using WeasyPrint
- ✅ **Serverless** architecture on Azure Functions
- ✅ **Static frontend** with beautiful UI
- ✅ **Full CSS support** in PDF rendering
- ✅ **No infrastructure management** required
- ✅ **Automatic scaling** with Azure

## 📦 Prerequisites

- **Azure Account** (free tier works)
- **Azure CLI** installed
- **Node.js** (for Static Web Apps CLI)
- **Git** installed

## 🛠️ Local Development

### 1. Install Azure Static Web Apps CLI

```bash
npm install -g @azure/static-web-apps-cli
```

### 2. Install Azure Functions Core Tools

```bash
npm install -g azure-functions-core-tools@4
```

### 3. Install Python dependencies

```bash
cd api
pip install -r requirements.txt
```

### 4. Run locally

From the project root:

```bash
swa start public --api-location api
```

Open **http://localhost:4280** in your browser.

## ☁️ Deploy to Azure

### Method 1: Using Azure Portal (Easiest)

1. **Create GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR-USERNAME/html-to-pdf-azure.git
   git push -u origin main
   ```

2. **Create Azure Static Web App**
   - Go to [Azure Portal](https://portal.azure.com)
   - Search for "Static Web Apps"
   - Click "Create"
   - Select your GitHub repository
   - **Build configuration:**
     - App location: `/public`
     - Api location: `/api`
     - Output location: `` (leave empty)
   - Click "Review + Create"

3. **GitHub Actions will automatically deploy** your app!

### Method 2: Using Azure CLI

```bash
# Login to Azure
az login

# Create resource group
az group create \
  --name html-to-pdf-rg \
  --location "West Europe"

# Create Static Web App
az staticwebapp create \
  --name html-to-pdf-converter \
  --resource-group html-to-pdf-rg \
  --source https://github.com/YOUR-USERNAME/html-to-pdf-azure \
  --location "West Europe" \
  --branch main \
  --app-location "/public" \
  --api-location "/api" \
  --login-with-github
```

## 🧪 Testing the API

### Using curl

```bash
curl -X POST https://YOUR-APP-NAME.azurestaticapps.net/api/convert_to_pdf \
  -H "Content-Type: application/json" \
  -d '{
    "html": "<!DOCTYPE html><html><body><h1>Hello World</h1></body></html>",
    "filename": "test.pdf"
  }'
```

### Using Python

```python
import requests
import base64

url = "https://YOUR-APP-NAME.azurestaticapps.net/api/convert_to_pdf"

html_content = """
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial; }
        h1 { color: #667eea; }
    </style>
</head>
<body>
    <h1>My PDF Document</h1>
    <p>This was generated from HTML!</p>
</body>
</html>
"""

response = requests.post(url, json={
    "html": html_content,
    "filename": "my-document.pdf"
})

data = response.json()

if data['success']:
    # Decode base64 and save PDF
    pdf_bytes = base64.b64decode(data['pdf_base64'])
    with open('output.pdf', 'wb') as f:
        f.write(pdf_bytes)
    print(f"✅ PDF saved! ({data['size_kb']} KB)")
else:
    print(f"❌ Error: {data['error']}")
```

## 📊 API Reference

### POST `/api/convert_to_pdf`

**Request Body:**
```json
{
  "html": "<html>...</html>",
  "filename": "output.pdf"
}
```

**Response (Success):**
```json
{
  "success": true,
  "filename": "output.pdf",
  "size_bytes": 123456,
  "size_kb": 120.56,
  "pdf_base64": "JVBERi0xLjcK..."
}
```

**Response (Error):**
```json
{
  "success": false,
  "error": "Error message here"
}
```

## 🔧 Configuration

### Increase Function Timeout

If you're converting large HTML documents, increase the timeout in `api/host.json`:

```json
{
  "functionTimeout": "00:10:00"
}
```

### Custom CSS

You can include custom CSS directly in your HTML:

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        @page {
            size: A4;
            margin: 2cm;
        }
        body {
            font-family: 'Arial', sans-serif;
            font-size: 12pt;
        }
    </style>
</head>
<body>
    <h1>Your Content</h1>
</body>
</html>
```

## 💰 Pricing

Azure Static Web Apps offers a **free tier** that includes:
- ✅ 100 GB bandwidth/month
- ✅ 0.5 GB storage
- ✅ Custom domains
- ✅ SSL certificates

Azure Functions free tier:
- ✅ 1 million requests/month
- ✅ 400,000 GB-s compute/month

Perfect for personal projects and small-scale use!

## 🐛 Troubleshooting

### Issue: "WeasyPrint not found"

**Solution:** Make sure `requirements.txt` is in the `api/` folder and contains:
```
weasyprint>=60.0
```

### Issue: "CORS Error"

**Solution:** Check `staticwebapp.config.json` has proper CORS headers:
```json
"globalHeaders": {
  "Access-Control-Allow-Origin": "*"
}
```

### Issue: "Function timeout"

**Solution:** Increase timeout in `api/host.json`:
```json
{
  "functionTimeout": "00:10:00"
}
```

## 📚 Resources

- [Azure Static Web Apps Documentation](https://docs.microsoft.com/en-us/azure/static-web-apps/)
- [Azure Functions Python Documentation](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [WeasyPrint Documentation](https://doc.courtbouillon.org/weasyprint/)

## 📝 License

MIT License - Feel free to use this in your projects!

## 🙏 Credits

- **WeasyPrint** for excellent HTML to PDF conversion
- **Azure** for serverless infrastructure
- **Original inspiration** from `streamlit_app/ui/download_components.py`

---

**Made with ❤️ using Python + Azure**
