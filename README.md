# PythonProjects

A collection of Python exercises and small applications built while learning Python, including projects from the 100 Days of Code: The Complete Python Pro Bootcamp.

## Projects

The workspace includes examples covering:

- Python fundamentals, functions, and data structures
- Object-oriented programming
- Tkinter desktop applications, including a flash-card app and Pomodoro timer
- Turtle graphics and games, including Pong, Snake, and Turtle Crossing
- Working with CSV files, APIs, and scheduled tasks
- Small utilities such as a password manager, mail merge, and flight search tools

Most folders are independent exercises. Run an application from its project directory so any relative data or asset paths resolve correctly:

```powershell
cd path\to\project
python main.py
```

Some projects require third-party packages or API credentials. Install dependencies for the specific project as needed, provide credentials through environment variables, and keep any local `.env` files out of version control. `rain_alert` reads `OWM_API_KEY`, `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `ALERT_RECIPIENT_PHONE`, `TWILIO_SENDER_PHONE`, `RAIN_LATITUDE`, and `RAIN_LONGITUDE`. The birthday wisher and `stock-news-normal-start` use `EMAIL_ADDRESS`, `EMAIL_PASSWORD`, and `EMAIL_RECIPIENT`; `stock-news-normal-start` also needs `STOCK_API_KEY` and `NEWS_API_KEY`. `issoverhead-start` uses the email variables plus `MY_LATITUDE` and `MY_LONGITUDE`.