# """
# Azure Function: HTML to PDF Converter
# Inspired by the WeasyPrint implementation in streamlit_app/ui/download_components.py

# This function receives HTML content and converts it to PDF using WeasyPrint
# """

# import azure.functions as func
# import logging
# import json
# from io import BytesIO
# import base64

# # Import WeasyPrint (same as in the original code)
# from weasyprint import HTML, CSS


# def convert_html_to_pdf(html_string):
#     """
#     Convert HTML string to PDF bytes using WeasyPrint
    
#     This is the EXACT same function from the original code:
#     streamlit_app/ui/download_components.py
    
#     Args:
#         html_string (str): HTML content to convert
        
#     Returns:
#         bytes: PDF file as bytes
#     """
#     # ✅ WeasyPrint respecte beaucoup mieux le CSS
#     pdf_bytes = HTML(string=html_string).write_pdf()
    
#     return pdf_bytes


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     """
#     Azure Function entry point
    
#     Expected request body:
#     {
#         "html": "<html>...</html>",
#         "filename": "output.pdf" (optional)
#     }
    
#     Returns:
#         PDF file as base64-encoded string in JSON response
#     """
#     logging.info('HTML to PDF conversion function triggered')

#     try:
#         # Parse request body
#         req_body = req.get_json()
        
#         if not req_body:
#             return func.HttpResponse(
#                 json.dumps({"error": "Request body is required"}),
#                 status_code=400,
#                 mimetype="application/json"
#             )
        
#         html_content = req_body.get('html')
#         filename = req_body.get('filename', 'converted.pdf')
        
#         if not html_content:
#             return func.HttpResponse(
#                 json.dumps({"error": "HTML content is required"}),
#                 status_code=400,
#                 mimetype="application/json"
#             )
        
#         logging.info(f'Converting HTML ({len(html_content)} chars) to PDF...')
        
#         # ✅ Use the SAME function as in the original code
#         pdf_bytes = convert_html_to_pdf(html_content)
        
#         logging.info(f'✅ PDF generated successfully ({len(pdf_bytes)} bytes)')
        
#         # Encode PDF as base64 for JSON response
#         pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        
#         # Return response
#         response_data = {
#             "success": True,
#             "filename": filename,
#             "size_bytes": len(pdf_bytes),
#             "size_kb": round(len(pdf_bytes) / 1024, 2),
#             "pdf_base64": pdf_base64
#         }
        
#         return func.HttpResponse(
#             json.dumps(response_data),
#             status_code=200,
#             mimetype="application/json",
#             headers={
#                 "Access-Control-Allow-Origin": "*",  # Allow CORS for static web app
#                 "Access-Control-Allow-Methods": "POST, OPTIONS",
#                 "Access-Control-Allow-Headers": "Content-Type"
#             }
#         )
        
#     except json.JSONDecodeError:
#         logging.error('Invalid JSON in request body')
#         return func.HttpResponse(
#             json.dumps({"error": "Invalid JSON format"}),
#             status_code=400,
#             mimetype="application/json"
#         )
        
#     except Exception as e:
#         logging.error(f'Error during PDF conversion: {str(e)}')
#         return func.HttpResponse(
#             json.dumps({
#                 "error": f"PDF conversion failed: {str(e)}",
#                 "success": False
#             }),
#             status_code=500,
#             mimetype="application/json"
#         )
"""
Azure Function: HTML to PDF Converter
"""

import azure.functions as func
import logging
import json
import base64

from weasyprint import HTML, CSS


# Page size dimensions
PAGE_SIZES = {
    'A4': {'width': '210mm', 'height': '297mm'},
    'Letter': {'width': '8.5in', 'height': '11in'},
    'Legal': {'width': '8.5in', 'height': '14in'},
}


def convert_html_to_pdf(html_string, page_size='A4', orientation='portrait'):
    """
    Convert HTML string to PDF bytes using WeasyPrint
    
    Args:
        html_string (str): HTML content to convert
        page_size (str): 'A4', 'Letter', or 'Legal'
        orientation (str): 'portrait' or 'landscape'
        
    Returns:
        bytes: PDF file as bytes
    """
    # Get page dimensions
    size = PAGE_SIZES.get(page_size, PAGE_SIZES['A4'])
    
    # Swap width/height for landscape
    if orientation == 'landscape':
        width, height = size['height'], size['width']
    else:
        width, height = size['width'], size['height']
    
    # Create CSS for page size
    page_css = CSS(string=f'''
        @page {{
            size: {width} {height};
            margin: 1cm;
        }}
    ''')
    
    # Generate PDF with page settings
    pdf_bytes = HTML(string=html_string).write_pdf(stylesheets=[page_css])
    
    return pdf_bytes


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function entry point
    """
    logging.info('HTML to PDF conversion function triggered')

    try:
        req_body = req.get_json()
        
        if not req_body:
            return func.HttpResponse(
                json.dumps({"error": "Request body is required"}),
                status_code=400,
                mimetype="application/json"
            )
        
        html_content = req_body.get('html')
        filename = req_body.get('filename', 'converted.pdf')
        page_size = req_body.get('page_size', 'A4')
        orientation = req_body.get('orientation', 'portrait')
        
        if not html_content:
            return func.HttpResponse(
                json.dumps({"error": "HTML content is required"}),
                status_code=400,
                mimetype="application/json"
            )
        
        logging.info(f'Converting HTML ({len(html_content)} chars) to PDF - {page_size} {orientation}')
        
        # Convert with page settings
        pdf_bytes = convert_html_to_pdf(html_content, page_size, orientation)
        
        logging.info(f'PDF generated successfully ({len(pdf_bytes)} bytes)')
        
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')
        
        response_data = {
            "success": True,
            "filename": filename,
            "size_bytes": len(pdf_bytes),
            "size_kb": round(len(pdf_bytes) / 1024, 2),
            "pdf_base64": pdf_base64
        }
        
        return func.HttpResponse(
            json.dumps(response_data),
            status_code=200,
            mimetype="application/json",
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
        
    except json.JSONDecodeError:
        logging.error('Invalid JSON in request body')
        return func.HttpResponse(
            json.dumps({"error": "Invalid JSON format"}),
            status_code=400,
            mimetype="application/json"
        )
        
    except Exception as e:
        logging.error(f'Error during PDF conversion: {str(e)}')
        return func.HttpResponse(
            json.dumps({
                "error": f"PDF conversion failed: {str(e)}",
                "success": False
            }),
            status_code=500,
            mimetype="application/json"
        )
