from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_driver():
    """Создает и возвращает настроенный экземпляр Chrome драйвера"""
    options = Options()
    options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)

async def get_moex_data(symbol):
    driver = None
    try:
        driver = create_driver()
        driver.get(f"https://www.moex.com/ru/issue.aspx?board=TQBR&code={symbol}")
        
        tickerMoex = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div[1]/h1/span'))
        )
        tickerMoex_text = tickerMoex.text
        
        stock_nameMoex = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div/div[1]/h1'))
        )
        stock_nameMoex_text = stock_nameMoex.text

        current_priceMoex = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[1]/div[2]/div/span'))
        )
        current_priceMoex_text = current_priceMoex.text

        result = {
            "ticker": tickerMoex_text,
            "stock": stock_nameMoex_text,
            "price": current_priceMoex_text 
        }
        return result
    
    except (TimeoutError, NoSuchElementException, WebDriverException) as e:
        logger.error(f"Error fetching MOEX data for {symbol}: {str(e)}")
        return None
    finally:
        if driver:
            driver.quit()

async def get_spb_data(symbol):
    driver = None
    try:
        driver = create_driver()
        driver.get(f"https://spbexchange.ru/stocks/indices/{symbol}/")
        
        tickerSpb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/ul/li[3]'))
        )
        tickerSpb_text = tickerSpb.text

        stock_nameSpb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[1]/h1'))
        )
        stock_nameSpb_text = stock_nameSpb.text

        current_priceSpb = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div/div/div/div/div[2]/div[1]/div/div[2]'))
        )
        current_priceSpb_text = current_priceSpb.text

        result = {
            "ticker": tickerSpb_text,
            "stock": stock_nameSpb_text,
            "price": current_priceSpb_text
        }
        return result

    except (TimeoutError, NoSuchElementException, WebDriverException) as e:
        logger.error(f"Error fetching SPB data for {symbol}: {str(e)}")
        return None
    finally:
        if driver:
            driver.quit()