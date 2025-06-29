### Instagram Follower Checker

A simple **Streamlit** web app that helps you compare your Instagram followers and following lists — so you can quickly see who you follow that doesn’t follow you back.

Link: https://atharva-rajguru-insta-follower--insta-followers-checker-sahy0t.streamlit.app/


## ✅ What This App Does

- Upload your official Instagram `followers_1.json` and `following.json` files.
- The app compares them and shows you accounts that **don’t follow you back**.
- Runs entirely in your browser — your data stays private!


## 📂 How to Get Your JSON Files

To use this tool, you need to download your data from Instagram:

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
11. Click **“Create File.”** Instagram will email you a download link when it’s ready.


## 🚀 How to Use This App

1. Clone this repo or run it locally with Streamlit.
2. Upload **both**:
   - `followers_1.json`
   - `following.json`
3. Once both files are uploaded, click **“Check”**.
4. The app will list accounts you’re following that **don’t follow you back**.


## ⚙️ Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/) installed:  
  ```bash
  pip install streamlit
