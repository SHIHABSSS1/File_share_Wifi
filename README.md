Run server : python file_share.py


Wifi file share ...
multiple upload & download 
You Can Also Download as zip



                                                Manual
📘 WiFi File Sharing App - User Manual
1. Setup and Run
Make sure you have Python installed.

Open your command prompt or terminal and activate your virtual environment (if using):

venv\Scripts\activate
Run the server:


python file_share.py
You should see output like:


* Running on http://0.0.0.0:8000
Find your computer’s local IP address (for example, 192.168.0.102) by running:


ipconfig
2. Accessing the App
On your phone or any device connected to the same WiFi, open a web browser.

Enter the URL:

http://<your-computer-ip>:8000
Example:

http://192.168.0.102:8000
3. Uploading Files
On the webpage, you'll see a file upload form.

Click Choose Files (or Browse) to select one or more files from your device.

Click the Upload button.

The page will reload, and your uploaded files will appear in the Uploaded Files list.

4. Downloading Files
Download Single Files
Each file in the list has a Download button on the right.

Click it to download that individual file.

Download Multiple Files as ZIP
Check the boxes next to the files you want to download.

Click the ⬇ Download Selected as ZIP button.

The selected files will be packaged into a ZIP archive and downloaded.

Download All Files as ZIP
Click the 📦 Download All Files button below the list.

All files in the uploads folder will be zipped and downloaded in one go.

5. Notes and Tips
File names with spaces or special characters are fully supported.

Uploaded files are stored in the uploads folder on your computer running the server.

To stop the server, press Ctrl + C in your terminal.

Make sure your computer and phone are connected to the same WiFi network for access.

6. Troubleshooting
Can't access server from phone?

Check your firewall settings to allow Python or port 8000.

Verify both devices are on the same WiFi.

File doesn't download correctly?

Try refreshing the page and re-uploading the file.

Check for special characters or very long file names.

Server error or crashes?

Look at the terminal output for error messages.

Restart the server if needed.