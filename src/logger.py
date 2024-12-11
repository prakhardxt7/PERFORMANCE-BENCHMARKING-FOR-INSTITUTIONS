import logging  # Import the logging module to enable logging functionality
import os  # Import the os module to interact with the operating system (for file and directory operations)
from datetime import datetime  # Import the datetime module to get the current date and time

# Create a log file name using the current date and time (format: month_day_year_hour_minute_second)
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create the log directory path by joining the current working directory with the "logs" folder
log_path = os.path.join(os.getcwd(), "logs")

# Create the "logs" directory if it doesn't already exist. `makedirs` ensures the directory is created, and any parent directories are also created if missing.
os.makedirs(log_path, exist_ok=True)

# Combine the log directory path with the log file name to create the full path for the log file
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure the logging system to log messages to the log file with a specific format
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the file where the logs should be saved
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',  # Define the log message format: timestamp, line number, logger name, log level, and the message
    level=logging.INFO,  # Set the log level to INFO, meaning it will log messages of INFO level and higher (INFO, WARNING, ERROR, CRITICAL)
)

# Main block where the logging is triggered
# if __name__ == '__main__':
#     logging.info('logging is sorted')  # Log an INFO level message: 'logging is sorted'




# 1. **`import logging`**: Sabse pehle, hum logging module ko import karte hain. Isse hume apne program mein log messages create karne ka option milta hai, jo baad mein files ya console mein save ho sakte hain.
# 
# 2. **`import os`**: Yeh module file aur directory management ke liye hota hai. Isse hum apne system pe directories create kar sakte hain ya file paths handle kar sakte hain.
# 
# 3. **`from datetime import datetime`**: Yeh line current date aur time ko fetch karne ke liye hai, taaki hum apne log file ka naam dynamic bana sakein. Jaise `12_11_2024_12_30_25.log`.
# 
# 4. **`LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"`**: Yeh line current date aur time ko format karke ek log file ka naam bana rahi hai. Jaise aapko ek file milegi `12_11_2024_12_30_25.log` naam se, jo har baar alag hoga.
# 
# 5. **`log_path = os.path.join(os.getcwd(), "logs")`**: Yeh line current working directory aur "logs" folder ko join karke ek path banati hai jahan log file store hogi.
# 
# 6. **`os.makedirs(log_path, exist_ok=True)`**: Yeh line ensure karti hai ki agar "logs" directory exist nahi karti, toh wo create ho jaye. Agar already exist karti hai, toh koi error nahi aayega.
# 
# 7. **`LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)`**: Ab hum jo log file ka path bana rahe hain, usme hum "logs" folder aur dynamic file name ko combine karte hain, jisse ek complete file path milta hai.
# 
# 8. **`logging.basicConfig(...)`**: Yeh line logging ka configuration set karti hai. Hum yahan specify kar rahe hain ki log file kis path pe store hoga, log format kya hoga (timestamp, line number, log level, message), aur kis level tak messages ko log kiya jayega (yahan `INFO` set kiya gaya hai, matlab `INFO`, `WARNING`, `ERROR`, aur `CRITICAL` messages log honge).
# 
# 9. **`if __name__ == '__main__':`**: Yeh check karta hai ki script directly run ho rahi hai ya kisi dusre program se import ho rahi hai. Agar script directly run ho rahi hai, tab jo code niche diya gaya hai, woh execute hoga.
# 
# 10. **`logging.info('logging is sorted')`**: Yeh line ek simple log message create karti hai, jo "INFO" level ka hoga. Yeh message log file mein store ho jayega.
# 
# ### Overall Working Summary:
# Yeh program apne log file ko dynamically create karta hai, usme current date aur time ka timestamp use karke. Uske baad, logging configuration set karta hai taaki log messages ek file mein save ho sakein. Jab script run hoti hai, to ek `INFO` level ka message `"logging is sorted"` file mein store ho jata hai.
# 
# Toh basically, yeh code apne application mein logging system ko set up karta hai aur logs ko ek file mein store karta hai, taaki future reference ke liye uska analysis kiya ja sake.
