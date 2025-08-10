import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def human_like_delay():
    """Random delay to mimic human behavior"""
    time.sleep(random.uniform(2, 4))


def scroll_randomly(driver):
    """Randomly scroll the page to mimic human behavior"""
    if random.random() > 0.6:
        scroll_amount = random.randint(200, 500)
        driver.execute_script(f"window.scrollBy(0, {scroll_amount});")
        time.sleep(random.uniform(1, 2))


def main():
    print("🤖 Facebook Auto Poke Back Bot - Desktop Version")
    print("=" * 55)
    
    # Chrome options for better stealth
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
    
    # Configuration
    MAX_POKES = 50  # Maximum number of pokes to send back
    BASE_DELAY = 3  # Base delay between pokes (seconds)
    
    try:
        # Initialize Chrome WebDriver
        print("🔄 Starting Chrome WebDriver...")
        driver = webdriver.Chrome(options=chrome_options)
        driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )
        
        # Navigate to Facebook login
        print("🌐 Navigating to Facebook...")
        driver.get("https://www.facebook.com/login")
        
        # Wait for user to login manually
        print("\n" + "="*55)
        print("🔐 PLEASE LOG IN TO FACEBOOK MANUALLY")
        print("👉 You have 60 seconds to complete the login process")
        print("✅ After login, the bot will automatically continue...")
        print("="*55 + "\n")
        
        # Wait for manual login (60 seconds)
        login_wait_time = 60
        for i in range(login_wait_time, 0, -1):
            print(f"⏰ Waiting for login... {i} seconds remaining", end='\r')
            time.sleep(1)
        
        print("\n🔄 Checking login status...")
        
        # Check if user is logged in by looking for typical Facebook elements
        try:
            # Look for elements that appear after successful login
            WebDriverWait(driver, 5).until(
                EC.any_of(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='search']")),
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='Facebook']")),
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='blue_bar']"))
                )
            )
            print("✅ Login successful! Proceeding with poke back...")
        except TimeoutException:
            print("❌ Login not detected. Please make sure you're logged in.")
            return
        
        human_like_delay()
        
        # Navigate to pokes page
        print("📋 Navigating to pokes page...")
        driver.get("https://www.facebook.com/pokes/")
        human_like_delay()
        
        # Wait for pokes page to load
        print("🔍 Loading pokes page...")
        time.sleep(random.uniform(3, 5))
        
        pokes_sent = 0
        poke_attempts = 0
        
        print(f"🚀 Starting auto poke back (max: {MAX_POKES})...")
        print("-" * 40)
        
        while pokes_sent < MAX_POKES and poke_attempts < MAX_POKES * 2:
            try:
                # Look for poke back buttons/links
                poke_selectors = [
                    "a[href*='poke_dialog']",
                    "a[href*='pokeback']",
                    "a[href*='poke.php']",
                    "[role='button']:contains('Poke Back')",
                    "span:contains('Poke Back')",
                    "a:contains('Poke Back')"
                ]
                
                poke_element = None
                for selector in poke_selectors:
                    try:
                        if ':contains' in selector:
                            # Use XPath for text-based selection
                            xpath_selector = f"//a[contains(text(), 'Poke Back')] | //span[contains(text(), 'Poke Back')] | //button[contains(text(), 'Poke Back')]"
                            poke_elements = driver.find_elements(By.XPATH, xpath_selector)
                            if poke_elements:
                                poke_element = poke_elements[0]
                                break
                        else:
                            poke_elements = driver.find_elements(By.CSS_SELECTOR, selector)
                            if poke_elements:
                                poke_element = poke_elements[0]
                                print(f"Found poke element with selector: {selector}")
                                break
                    except Exception as e:
                        continue
                
                if poke_element:
                    try:
                        # Scroll to the element
                        driver.execute_script("arguments[0].scrollIntoView(true);", poke_element)
                        time.sleep(random.uniform(1, 2))
                        
                        # Click the poke back element
                        if poke_element.is_displayed() and poke_element.is_enabled():
                            poke_element.click()
                            pokes_sent += 1
                            print(f"👋 Poke #{pokes_sent} sent successfully!")
                            
                            # Random delay between pokes
                            delay = random.uniform(BASE_DELAY, BASE_DELAY + 3)
                            print(f"⏱️  Waiting {delay:.1f} seconds before next poke...")
                            time.sleep(delay)
                            
                            # Occasionally scroll randomly
                            scroll_randomly(driver)
                            
                        else:
                            print("⚠️  Poke element not clickable, skipping...")
                            
                    except Exception as e:
                        print(f"❌ Error clicking poke element: {e}")
                
                else:
                    print("🔍 No more poke back buttons found, checking for more...")
                    
                    # Try to refresh or scroll to load more pokes
                    scroll_randomly(driver)
                    time.sleep(random.uniform(2, 4))
                    
                    # If no pokes found after several attempts, break
                    if poke_attempts > 10:
                        print("ℹ️  No more pokes available to send back.")
                        break
                
                poke_attempts += 1
                
                # Prevent infinite loops
                if poke_attempts > MAX_POKES * 2:
                    print("⚠️  Maximum attempts reached.")
                    break
                    
            except Exception as e:
                print(f"❌ Error in poke loop: {e}")
                time.sleep(random.uniform(5, 10))
                poke_attempts += 1
                continue
        
        print("\n" + "="*40)
        print(f"🎉 Poke back session completed!")
        print(f"📊 Total pokes sent: {pokes_sent}")
        print(f"📊 Total attempts: {poke_attempts}")
        print("="*40)
        
        # Wait before closing
        print("⏳ Waiting 10 seconds before closing browser...")
        time.sleep(10)
        
    except KeyboardInterrupt:
        print("\n⚠️  Bot stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        try:
            driver.save_screenshot("poke_error_screenshot.png")
            print("📸 Error screenshot saved as 'poke_error_screenshot.png'")
        except:
            pass
    finally:
        try:
            driver.quit()
            print("🔒 Browser closed successfully")
        except:
            pass


if __name__ == "__main__":
    main()
