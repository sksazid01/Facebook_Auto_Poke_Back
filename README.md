# Facebook Auto Poke Back Bot

An **automated poke back tool** for Facebook using Python and Selenium! This script uses facebook.com (not the mobile site), and lets you log in manually in your own browser window for security. It then automatically pokes back at everyone who has poked you, with human-like behavior to avoid detection.

---

## Features

- 🖥️ Supports **desktop Facebook** (`facebook.com`)
- 🔐 **Manual login** for maximum security (no need to share your credentials inside the code)
- 👋 **Auto poke back** everyone who has poked you
- 🤖 **Mimics human behavior** via random delays and scrolling
- 📊 Console **progress tracking** and error handling
- 🚦 **Respects Facebook’s limits** to reduce risk of blocks
- ⚠️ **Highly customizable** (max pokes, delay, etc.)

---

## Keywords

`facebook poke back` &nbsp; `auto poke` &nbsp; `poke bot` &nbsp; `selenium facebook` &nbsp; `desktop facebook automation` &nbsp; `facebook poke automation`

---

## Installation & Setup

### 1. Prerequisites

- Python 3.6 or higher
- Google Chrome browser (latest version recommended)
- ChromeDriver (version _matching_ your Chrome, [Download here](https://chromedriver.chromium.org/downloads))

### 2. Install Dependencies

```bash
pip install selenium
```

### 3. Prepare ChromeDriver

- Download the correct version from [here](https://chromedriver.chromium.org/downloads).
- Put the Chromedriver executable somewhere on your system PATH, or in the same folder as `Auto_Poke_Back_at_FB.py`.

---

## Usage

1. **Run the Script**
   ```bash
   python Auto_Poke_Back_at_FB.py
   ```

2. **Manual Facebook Login**
   - The Chrome browser will open and take you to the Facebook login page.
   - **Log in with your credentials manually** (the script will wait for about 60 seconds).
   - After login, do not close the browser—let the script continue!

3. **Automatic Poke Back**
   - The script navigates to `facebook.com/pokes`.
   - It finds and clicks "Poke Back" on available users, inserting random delays and scrolling to simulate human behavior.

4. **Completion**
   - When done (or if there are no pokes left), it displays a summary and closes the browser.

---

## Configuration

You can open the `Auto_Poke_Back_at_FB.py` file and adjust:

```python
MAX_POKES = 50      # Maximum number of people to poke back per run
BASE_DELAY = 3      # Base delay (in seconds) between pokes
```

These defaults are safe, but you may lower/increase them as needed.

---

## Troubleshooting

- **Login not detected:** Make sure you complete the login process within 60 seconds, including two-factor authentication if prompted.
- **No poke back buttons found:** Probably no one has poked you recently. Try again later! If Facebook updates their design, code selectors may need updating.
- **ChromeDriver errors:** Ensure you’ve downloaded the matching version for your installed Chrome browser.
- **Blocked or limited:** Reduce poke frequency/delay, or wait before running again. Don’t overuse automation!

---

## Safety & Disclaimer

- **Manual login only!** Your password is never stored or sent to this script.
- **Use responsibly** and respect Facebook’s [Terms of Service](https://www.facebook.com/terms.php).
- **Don’t spam or harass others.** This script is for fun and automation-experimentation, not abuse.
- Excessive or repeated automated poking _may_ trigger Facebook’s anti-bot protections. Adjust delays and limits accordingly.

---

## FAQ

**Q: Will my password be safe?**  
A: Yes. You log in manually through Chrome. The script does not record, send, or store your credentials.

**Q: Can I run it on Mac/Linux?**  
A: Yes, if you have Chrome + compatible Chromedriver + Python.

**Q: Can Facebook block me?**  
A: Any automated actions risk a temporary block. Use conservative settings and don’t run the script excessively.

---

## Tags

`#FacebookAutomation` `#PokeBack` `#SeleniumBot` `#PythonAutomation`

---

Enjoy, and happy poking back! 👋

For any help, contact me on LinkedIn:
> https://www.linkedin.com/posts/sksazid_auto-pokeback-program-httpslnkdin-activity-7170492870242553856-HXeJ?utm_source=share&utm_medium=member_android
