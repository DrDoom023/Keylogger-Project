# Keylogger-Project
Keylogger Project 


To initiate this project, I first needed to develop two Python scripts: one to act as a keylogger to capture keystrokes from the victim machine and another as a listener to receive those keystrokes on the attacker's machine. I created a basic keylogger that imports necessary libraries, including requests and pynput.keyboard. The script is designed to capture each character typed on the victim machine, including special keys like space, shift, and backspace. Once captured, these keystrokes are sent to the attacker's machine and stored in a text file.

To transfer the keystrokes, the keylogger sends the data to a Kali Linux server listening on port 8080. The listener script on the attacker’s machine receives these keystrokes and appends them to a specified text file for later analysis. It is important to note that once the listener script stops running, the server will no longer capture keystrokes, but any previously logged keys will remain saved in the text file.

For network communication, I configured both virtual machines to be on the same network by using Bridge Adapter mode (RZ608 Wi-Fi 6E 80MHz). Before testing the connection, I ensured that the Windows virtual machine could accept incoming traffic by adjusting the firewall settings to allow ICMP traffic. This enabled the Windows 10 machine to respond to pings from external sources. I then used the command ping {Kali Linux IP Address} and successfully received a response, establishing a communication channel between the victim and attacker machines for the transfer and storage of keystroke data. With successful communication established, the next step was to start the server on port 8080 using the command python3 -m http.server 8080. After the server began listening, I connected to it from the Windows machine by typing the IP address of the Kali machine and port in the browser, using the URL http://{Kali Linux IP Address}:8080. This brought up the directory list stored on the Kali machine, which included the keylogger script under key_logger.py. The victim would then click on and download this script.

Now that the script is downloaded, the attacker stopped the HTTP server and started the listener, which waited for a connection from the keylogger script. With the listener active, the victim ran the keylogger on their machine, establishing a connection and beginning to capture keystrokes. As long as the listener remained active, all keys entered on the victim's machine were captured and sent through the listener. As evident from the text file, the victim entered a username "admin" and password "admin1234$$".

The attack I demonstrated was simple and basic, suitable for beginners. However, advanced keyloggers can be even more stealthy, sending malicious scripts to the victim's machine that only start capturing keystrokes when triggered. The attack I performed is relatively minor compared to the more sophisticated threats prevalent in today's technology landscape. Unfortunately, keylogger attacks occur more frequently than people realize, often without the victim's knowledge or consent. A common method of infection is through email phishing, where opening an email from an unknown source. Malicious emails may contain seemingly harmless attachments, such as photos or downloads, or even links, when clicked will allow the attacker to install a keylogger on the victim's machine, capturing all keystrokes and stealing sensitive information.

To prevent this type of attack, it's essential to exercise caution when interacting with emails from unknown sources. Avoid opening suspicious emails or clicking on links, photos, or downloads from unfamiliar senders, as this can inadvertently allow malicious scripts to infiltrate your system. Additionally, maintaining robust security habits is crucial. This includes keeping your software up-to-date with the latest security patches, ensuring your antivirus software is enabled and actively scanning for threats, and activating real-time protection on your firewall. By following these simple yet effective measures, you can significantly reduce the risk of falling victim to this type of attack and protect your sensitive information.

This project was a valuable learning experience, teaching me how to set up an HTTP server and establish connections with other machines. This networking technique has numerous applications in both offensive and defensive security scenarios. By creating the Python scripts, I gained hands-on experience with using a keylogger and setting up a listener to receive data from the compromised machine. Ultimately, the most important lesson I took away was how to protect against this type of attack, which has significantly enhanced my understanding of cybersecurity.

For future projects, I plan to enhance the keylogger to make it more advanced and focus on defensive strategies to demonstrate how users can protect themselves from this type of attack. By keeping the keylogger up-to-date with the latest advancements in Python, I aim to educate users on how to defend against emerging attack strategies, ultimately empowering them to safeguard their sensitive information.
If you have any feedback or suggestions, please feel free to reach out to me on Discord.  

Steps to Follow:

Step 1: Start the HTTP server
python3 -m http.server 8080

Step 2: Download the key_logger.py file.

Step 3: Stop the HTTP server by pressing Ctrl+C in the terminal.

Step 4: Start the listener on the Kali machine.

Step 5: Run the key_logger.py script on the Windows machine.

Step 6: Shut down the listener on the Kali machine.

Step 7: Check the .txt file to view the captured keystrokes. 

