# 📸 Insta Followback Checker

A simple **Streamlit** web app that helps you compare your Instagram followers and following lists - so you can easily see who you follow that doesn’t follow you back.

**Live app:** https://atharva-rajguru-insta-follower--insta-followers-checker-sahy0t.streamlit.app/

---

## ✅ What This App Does

- Upload your official Instagram `followers_1.json` and `following.json` files **OR a single ZIP file** containing them.
- The app compares your followers and following lists.
- It shows you exactly which accounts you follow that **don’t follow you back**.
- Runs **entirely in your browser** - your data stays private!

---

## 📂 How to Get Your Data from Instagram

To use this tool, you need to download your data directly from Instagram:

1. **Log in** to Instagram on a web browser.
2. Go to your **Profile → Settings**.
3. Click **“See more in Account Center.”**
4. Under **Account Settings**, go to **“Your information and permissions.”**
5. Click **“Download your information.”**
6. Choose your Instagram account under **Download or transfer information**.
7. Go to **“Some of your information.”**
8. Select **“Followers and following”** under **Connections**, then click **Next**.
9. Click **“Download to this Device.”**
10. Set the format to **JSON** and the date range to **All time**.
11. Click **“Create File.”** Instagram will email you a download link with your ZIP file.

---

## 🚀 How to Use This App

1. Clone this repo or open the **live Streamlit link**.
2. Upload **either**:
   - Both files: `followers_1.json` and `following.json`
   - **OR** the single ZIP file that contains them
3. Click **“Check”**.
4. The app will show:
   - ✅ Total followers and following counts
   - ⚠️ A list of accounts you follow that **don’t follow you back**
   - ✅ A friendly message if everyone follows you back!

---

## 🔒 Privacy & Security

- This app runs completely **in your browser session** using Streamlit Community Cloud.
- **Your data stays local** - it is never stored or sent to any server.
- You can inspect the source code yourself.

---

## ⚙️ Requirements (for local use)

- Python 3.8+
- Install Streamlit:
  ```bash
  pip install streamlit
