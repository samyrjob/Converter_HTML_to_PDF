"""
Test script for HTML to PDF Converter API

Usage:
    python test_api.py                          # Test localhost
    python test_api.py https://your-app.azurestaticapps.net  # Test deployed app
"""

import requests
import base64
import sys
import os

def test_pdf_conversion(base_url="http://localhost:7071"):
    """Test the PDF conversion API"""
    
    # API endpoint
    api_url = f"{base_url}/api/convert_to_pdf"
    
    # Sample HTML (similar to the CV in the original code)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <style>
            @page {
                size: A4;
                margin: 2cm;
            }
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                color: #333;
            }
            .header {
                text-align: center;
                border-bottom: 3px solid #667eea;
                padding-bottom: 20px;
                margin-bottom: 30px;
            }
            .header h1 {
                color: #667eea;
                font-size: 32pt;
                margin: 0;
            }
            .section {
                margin-bottom: 25px;
            }
            .section-title {
                font-size: 18pt;
                font-weight: bold;
                color: #667eea;
                border-bottom: 2px solid #e0e0e0;
                padding-bottom: 5px;
                margin-bottom: 15px;
            }
            .content {
                margin-left: 20px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Test PDF Document</h1>
            <p>Generated using WeasyPrint on Azure Functions</p>
        </div>

        <div class="section">
            <div class="section-title">About This Test</div>
            <div class="content">
                <p>The conversion uses <strong>WeasyPrint</strong> to render HTML with full CSS support.</p>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Features</div>
            <div class="content">
                <ul>
                    <li>Full CSS3 support including @page rules</li>
                    <li>Custom fonts and styling</li>
                    <li>Proper PDF pagination</li>
                    <li>A4 page size with margins</li>
                    <li>Professional formatting</li>
                </ul>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Technical Stack</div>
            <div class="content">
                <table border="1" cellpadding="10" style="border-collapse: collapse; width: 100%;">
                    <tr>
                        <th style="background: #f0f0f0;">Component</th>
                        <th style="background: #f0f0f0;">Technology</th>
                    </tr>
                    <tr>
                        <td>Frontend</td>
                        <td>HTML + JavaScript + Milligram Framework</td>
                    </tr>
                    <tr>
                        <td>Backend</td>
                        <td>Python + Azure Functions</td>
                    </tr>
                    <tr>
                        <td>PDF Engine</td>
                        <td>WeasyPrint</td>
                    </tr>
                    <tr>
                        <td>Hosting</td>
                        <td>Azure Static Web Apps</td>
                    </tr>
                </table>
            </div>
        </div>

        <div class="section">
            <div class="section-title">Success!</div>
            <div class="content">
                <p style="font-size: 14pt; color: #27ae60;">
                    ✅ If you're reading this as a PDF, the conversion worked perfectly!
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    
    print(f"\n🧪 Testing API at: {api_url}")
    print("=" * 60)
    
    try:
        # Make request
        print("\n📤 Sending HTML content...")
        response = requests.post(
            api_url,
            json={
                "html": html_content,
                "filename": "test_output.pdf"
            },
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        print(f"📥 Response status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            
            if data.get('success'):
                # Decode base64 and save PDF
                pdf_bytes = base64.b64decode(data['pdf_base64'])
                
                output_file = 'test_output.pdf'
                with open(output_file, 'wb') as f:
                    f.write(pdf_bytes)
                
                print(f"\n✅ SUCCESS!")
                print(f"   • PDF size: {data['size_kb']} KB ({data['size_bytes']} bytes)")
                print(f"   • File saved: {os.path.abspath(output_file)}")
                print(f"\n💡 Open the PDF to verify the conversion!")
                
                return True
            else:
                print(f"\n❌ API returned error: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"\n❌ HTTP Error {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Error: {error_data.get('error', 'Unknown error')}")
            except:
                print(f"   Response: {response.text[:200]}")
            return False
            
    except requests.exceptions.ConnectionError:
        print(f"\n❌ Connection Error!")
        print(f"   • Is the server running at {base_url}?")
        print(f"   • For local testing, run: swa start public --api-location api")
        return False
        
    except requests.exceptions.Timeout:
        print(f"\n❌ Request Timeout!")
        print(f"   • The API took too long to respond")
        print(f"   • Try increasing the timeout or check server logs")
        return False
        
    except Exception as e:
        print(f"\n❌ Unexpected Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    # Parse command line argument
    if len(sys.argv) > 1:
        base_url = sys.argv[1].rstrip('/')
        print(f"\n🌐 Testing deployed app at: {base_url}")
    else:
        base_url = "http://localhost:7071"
        print(f"\n🏠 Testing local API at: {base_url}")
        print(f"💡 To test deployed app, run: python {sys.argv[0]} https://your-app.azurestaticapps.net")
    
    success = test_pdf_conversion(base_url)
    sys.exit(0 if success else 1)
