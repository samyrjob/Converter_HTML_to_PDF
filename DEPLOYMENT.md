# 🚀 Deployment Guide for Azure Static Web Apps

## Quick Deploy (5 minutes)

### Step 1: Prerequisites

- [ ] Azure account (free tier works!)
- [ ] GitHub account
- [ ] Git installed locally

### Step 2: Push to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: HTML to PDF converter"

# Create repository on GitHub (replace YOUR-USERNAME)
# Then push
git remote add origin https://github.com/YOUR-USERNAME/html-to-pdf-azure.git
git branch -M main
git push -u origin main
```

### Step 3: Create Azure Static Web App

1. **Go to Azure Portal:** https://portal.azure.com
2. **Search for** "Static Web Apps"
3. **Click** "Create"

#### Configuration:

| Field | Value |
|-------|-------|
| **Subscription** | Your subscription |
| **Resource Group** | Create new: `html-to-pdf-rg` |
| **Name** | `html-to-pdf-converter` (or your choice) |
| **Plan type** | Free |
| **Region** | West Europe (or nearest) |
| **Source** | GitHub |
| **Organization** | Your GitHub username |
| **Repository** | `html-to-pdf-azure` |
| **Branch** | `main` |
| **Build Presets** | Custom |
| **App location** | `/public` |
| **Api location** | `/api` |
| **Output location** | ` ` (leave empty) |

4. **Click** "Review + Create"
5. **Click** "Create"

### Step 4: Wait for Deployment

GitHub Actions will automatically:
- ✅ Build your application
- ✅ Deploy frontend to Azure CDN
- ✅ Deploy Python function
- ✅ Install WeasyPrint dependencies

**This takes ~5-10 minutes** on first deployment.

### Step 5: Get Your URL

Once deployed, you'll get a URL like:
```
https://html-to-pdf-converter-xxx.azurestaticapps.net
```

Visit it and test the converter!

## 🔧 Troubleshooting

### Build Failed on GitHub Actions

**Check:**
1. Go to your GitHub repository
2. Click "Actions" tab
3. Look at the failed workflow
4. Common issues:
   - Missing `requirements.txt` in `/api` folder
   - Wrong Python version (should be 3.9-3.11)

**Fix:**
```bash
# Ensure requirements.txt is in api/ folder
ls api/requirements.txt

# Ensure it has WeasyPrint
cat api/requirements.txt | grep weasyprint
```

### Function Not Working

**Check Logs:**
1. Go to Azure Portal
2. Find your Static Web App
3. Go to "Functions" → Click on `convert_to_pdf`
4. Check "Monitor" tab for errors

**Common issue:** WeasyPrint dependencies missing
- Azure automatically installs from `requirements.txt`
- Ensure file exists in `/api/requirements.txt`

### CORS Errors

**Check:**
1. File `public/staticwebapp.config.json` exists
2. Contains CORS headers:
```json
{
  "globalHeaders": {
    "Access-Control-Allow-Origin": "*"
  }
}
```

## 🔄 Updating Your App

Simply push to GitHub:

```bash
git add .
git commit -m "Updated feature X"
git push
```

GitHub Actions will **automatically redeploy**!

## 🎯 Custom Domain

### Add Custom Domain:

1. Go to your Static Web App in Azure Portal
2. Click "Custom domains"
3. Click "Add"
4. Enter your domain (e.g., `pdf.yourdomain.com`)
5. Follow DNS configuration instructions
6. Azure provides **free SSL certificate**!

## 💰 Monitoring Costs

Azure Static Web Apps **Free Tier** includes:
- ✅ 100 GB bandwidth/month
- ✅ 0.5 GB storage
- ✅ Free SSL
- ✅ Custom domains

Azure Functions **Free Tier** includes:
- ✅ 1 million requests/month
- ✅ 400,000 GB-s compute/month

**You'll stay in free tier** for personal/small projects!

To monitor usage:
1. Go to Azure Portal
2. Click "Cost Management + Billing"
3. Check "Cost Analysis"

## 🔐 Security

### Enable Authentication (Optional)

If you want to restrict access:

1. Go to your Static Web App
2. Click "Authentication"
3. Add identity provider (GitHub, Google, etc.)
4. Update `staticwebapp.config.json`:

```json
{
  "routes": [
    {
      "route": "/*",
      "allowedRoles": ["authenticated"]
    },
    {
      "route": "/api/*",
      "allowedRoles": ["authenticated"]
    }
  ]
}
```

## 📊 Analytics

Enable Application Insights:

1. Go to your Static Web App
2. Click "Application Insights"
3. Click "Enable"
4. You'll get:
   - Request rates
   - Response times
   - Error rates
   - Geographic distribution

## 🆘 Getting Help

If you encounter issues:

1. **Check GitHub Actions logs:**
   - GitHub repo → Actions tab
   - Look at failed step

2. **Check Azure Function logs:**
   - Azure Portal → Your Static Web App
   - Functions → Monitor

3. **Common errors:**
   - `Module not found: weasyprint` → Check `requirements.txt`
   - `CORS error` → Check `staticwebapp.config.json`
   - `Function timeout` → Increase timeout in `host.json`

## 🎉 Success!

Your HTML to PDF converter is now live and serverless!

Test it at:
```
https://YOUR-APP-NAME.azurestaticapps.net
```

---

**Questions?** Open an issue on GitHub or check Azure docs:
- https://docs.microsoft.com/azure/static-web-apps/
