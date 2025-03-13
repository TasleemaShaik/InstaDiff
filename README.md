# InstaDiff
**Diff Checker for Followers vs Following**  

## Overview
**InstaDiff** is a **Python-based tool** that helps Instagram users analyze their **followers and following lists** by comparing them to detect:
- **Users who don’t follow you back**  
- **Ghost followers** (people who follow you, but you don’t follow back)  
- **Complete following audit** for Instagram accounts  

**This tool works for both private and public accounts** and does not require **API access, Selenium, or automation login**—making it a **safe and reliable** way to track your Instagram network.  

---

## Why I Chose the Instagram Data Download Method

Initially, I considered two main approaches:  

### **Rejected Methods**
1. **Instagram Graph API**  
   - **Problem**: Works only for **business/creator accounts** linked to a Facebook page.  
   - **Limitation**: Cannot fetch followers for personal/private accounts.  

2. **Web Scraping (Selenium)**  
   - **Problem**: Instagram detects automation, often leading to login issues or account bans.  
   - **Limitation**: High maintenance, as Instagram frequently updates its website.  

### **Final Solution: Instagram Data Download**  
I chose the **Instagram data download method** because:  
- **Works for all account types** (private, public, business, creator).  
- **No risk of detection or account suspension** (no automation needed).  
- **More reliable than APIs or web scraping**.  
- **Direct JSON data from Instagram** provides **accurate** results.  

---

## How to Download Your Instagram Data  
Follow these steps to download your followers & following list:

1️⃣ **Go to** [Instagram Settings](https://www.instagram.com/accounts/privacy_and_security/)  
2️⃣ Scroll down to **"Download Your Information"**  
3️⃣ Click **"Request a Download"** → Choose **"JSON" format**  
4️⃣ **Instagram will email you a download link** (may take a few minutes)  
5️⃣ Download and **extract the ZIP file**  
6️⃣ Locate:
   - `followers_and_following/followers.json` → Followers list  
   - `followers_and_following/following.json` → Following list  

---

## How to Use InstaDiff  

### **Step 1: Install Requirements**  
Ensure you have Python installed.

###  **Step 2: Run Extract Followers and Following Lists**
```bash
export DATA_FOLDER=<FOLDER-THAT-CONTAINS-FOLLOWERS-AND-FOLLOWING-JSON>
python extract.py
```
Also, Please find the same working code with minute changes compared to the local script from my google colab
https://colab.research.google.com/drive/13ahPYiKsUycAQbm760ojqDdbQf9P3p-M?usp=sharing

### **Step 3: Have fun finding out who exactly unfollowed you after some days of sending you request and unfollow them too!**

