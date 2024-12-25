
# 🚀 **Event Plan Pro**

This project automates event planning using `crewai`, `crewai_tools`, and `pydantic`. It manages key tasks like venue coordination, logistics, and marketing with agents, providing structured outputs in JSON and Markdown formats.

---

## ✨ **Features**
- 🤖 Automated task handling with AI-powered agents.
- 📋 Outputs structured data in JSON and Markdown formats.
- 🔄 Configurable task flow with support for synchronous and asynchronous execution.
- 🌐 API integrations for extended functionalities.

---

## 🔧 **Technologies Used**
- **Python 3.8+**
- **Libraries**:
  - `crewai`
  - `crewai_tools`
  - `pydantic`
  - `dotenv` (for environment variable management)

---

## 🛠️ **Setup Instructions**

### 1️⃣ **Prerequisites**
- Install Python 3.8 or higher.
- Ensure `pip` and `virtualenv` are installed.

### 2️⃣ **Clone the Repository**
```bash
git clone <repository-url>

```

### 3️⃣ **Create a Virtual Environment**

```
python -m venv venv
source venv/bin/activate  # Mac/Linux
.\venv\Scripts\activate   # Windows

```

### 4️⃣ **Install Dependencies**

```
pip install -r requirements.txt

```

### 5️⃣ **Set API Keys**

-   Create a `.env` file in the project directory with the following content:

```
OPENAI_API_KEY=<your-openai-api-key>
SERPER_API_KEY=<your-serper-api-key>

```

### 6️⃣ **Run the Code**

```
python main.py

```

* * * * *

🧑‍💻 **Usage**
---------------

1.  Define the event details in the script:

    ```
    event_details = {
        'event_topic': "Diljit Dosanjh",
        'event_description': "A gathering of punjabi music lovers who witness their favourite punjabi singer Diljit Dosanjh perform live.",
        'event_city': "Chandigarh",
        'tentative_date': "2024-12-15",
        'expected_participants': 30000,
        'budget': 20000000,
        'venue_type': "Stadium"
    }

    ```

2.  Run the script to generate:

    -   `venue_details.json`: Contains venue-related data.
    -   `marketing_report.md`: Includes marketing updates.
3.  Review the JSON and Markdown files for outputs.

* * * * *

📁 **File Descriptions**
------------------------

-   **`main.py`**: Entry point for the project. Executes agents and tasks.
-   **`tasks.py`**: Defines event planning tasks.
-   **`agents.py`**: Sets up agents for venue coordination, logistics, and marketing.
-   **`utils.py`**: Contains utility functions for API key management.
-   **`.env`**: Stores environment variables for sensitive data like API keys.

* * * * *

📋 **Example Outputs**
----------------------

### 📌 Venue Details (JSON)

```
{
    "name": "Maharaja Yadavindra Singh Cricket Stadium",
    "address": "DLF Mullanpur, New Chandigarh, Tira, Punjab 140901",
    "capacity": 38000,
    "booking_status": "Confirmed"
}

```

### 📌 Marketing Report (Markdown)


## Marketing Activities

- **Social Media Campaign**: Successfully launched targeted ads on Instagram and Twitter.
- **Email Outreach**: Sent personalized invitations to 1,000 potential attendees.
- **Press Releases**: Published in major entertainment blogs and local media outlets.
- **Engagement Statistics**:
  - Click-through rate: 25%
  - Registrations: 45000



* * * * *

🔮 **Future Enhancements**
--------------------------

-   💰 Add agents for budget management and attendee engagement tracking.
-   📊 Integrate tools for advanced data scraping and analytics.
-   🛡️ Enhance error handling and logging for better debugging.

* * * * *

